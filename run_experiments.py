"""Сравнение токенизации одних и тех же текстов разными токенайзерами.

Три семейства:
  1. OpenAI  - кодировки tiktoken (локально, без ключа)
  2. Open    - токенайзеры открытых моделей с Hugging Face (Qwen3, DeepSeek-V3, Llama 3.2, ...)
  3. Claude  - точный подсчёт через Anthropic API `messages.count_tokens` (нужен ANTHROPIC_API_KEY)

Результаты: results/results.json и results/results.md, а также блок в README.md
между маркерами <!-- RESULTS:START --> и <!-- RESULTS:END -->.

Запуск:  python run_experiments.py
"""
import json
import os
import sys
import time
from collections import OrderedDict
from pathlib import Path

from tests_data import LANGS, TESTS

sys.stdout.reconfigure(encoding="utf-8")
os.environ.setdefault("HF_HUB_DISABLE_SYMLINKS_WARNING", "1")

ROOT = Path(__file__).parent
RESULTS = ROOT / "results"
RESULTS.mkdir(exist_ok=True)


def load_dotenv():
    """Читает KEY=VALUE из .env рядом со скриптом (файл в .gitignore, в репозиторий не попадает)."""
    p = ROOT / ".env"
    if not p.exists():
        return
    for line in p.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if line and not line.startswith("#") and "=" in line:
            k, v = line.split("=", 1)
            os.environ.setdefault(k.strip(), v.strip().strip('"').strip("'"))


load_dotenv()

# ---------------------------------------------------------------- бэкенды

TIKTOKEN_ENCODINGS = OrderedDict([
    ("cl100k_base", "OpenAI GPT-4 / GPT-3.5"),
    ("o200k_base", "OpenAI GPT-4o / GPT-4.1"),
    ("o200k_harmony", "OpenAI gpt-oss"),
])

HF_TOKENIZERS = OrderedDict([
    ("Qwen/Qwen3-8B", "Qwen3"),
    ("deepseek-ai/DeepSeek-V3", "DeepSeek-V3"),
    ("unsloth/Llama-3.2-1B", "Llama 3.2 (зеркало unsloth)"),
    ("mistralai/Mistral-Nemo-Instruct-2407", "Mistral Nemo (Tekken)"),
    ("unsloth/gemma-3-1b-it", "Gemma 3 (зеркало unsloth)"),
])

# Модели Claude. Старые (4.6 и 4.5) нужны, чтобы увидеть смену токенайзера.
CLAUDE_MODELS = [
    "claude-opus-5-5",
    "claude-sonnet-5-5",
    "claude-haiku-5-5",
    "claude-fable-5-2",
    "claude-opus-4-6",
    "claude-haiku-4-5",
]


def build_backends():
    """Возвращает (list of (id, family, description, count_fn), list of skipped)."""
    backends, skipped = [], []

    import tiktoken
    for name, desc in TIKTOKEN_ENCODINGS.items():
        try:
            enc = tiktoken.get_encoding(name)
            backends.append((name, "OpenAI", desc, lambda t, e=enc: len(e.encode(t, disallowed_special=()))))
        except Exception as ex:  # noqa: BLE001
            skipped.append((name, f"{type(ex).__name__}: {ex}"))

    try:
        from tokenizers import Tokenizer
    except ImportError:
        Tokenizer = None
        skipped.append(("huggingface tokenizers", "пакет tokenizers не установлен"))
    if Tokenizer:
        for repo, desc in HF_TOKENIZERS.items():
            try:
                tok = Tokenizer.from_pretrained(repo)
                backends.append((repo, "Open", desc,
                                 lambda t, k=tok: len(k.encode(t, add_special_tokens=False).ids)))
            except Exception as ex:  # noqa: BLE001
                skipped.append((repo, f"{type(ex).__name__}: {str(ex)[:120]}"))

    if os.environ.get("ANTHROPIC_API_KEY") or os.environ.get("ANTHROPIC_AUTH_TOKEN"):
        import anthropic
        client = anthropic.Anthropic()
        for model in CLAUDE_MODELS:
            def count(text, m=model):
                r = client.messages.count_tokens(model=m, messages=[{"role": "user", "content": text}])
                return r.input_tokens
            try:
                count("a")  # проверка доступности модели
                backends.append((model, "Claude", "Anthropic count_tokens", count))
            except Exception as ex:  # noqa: BLE001
                skipped.append((model, f"{type(ex).__name__}: {str(ex)[:120]}"))
    else:
        skipped.append(("Claude (все модели)", "нет ANTHROPIC_API_KEY — подсчёт через API пропущен"))

    return backends, skipped


# ---------------------------------------------------------------- прогон

def run():
    backends, skipped = build_backends()
    rows = []  # по одному на (бэкенд, тест, язык)
    for bid, family, desc, fn in backends:
        for tid, test in TESTS.items():
            for lang, text in test["texts"].items():
                for attempt in range(3):
                    try:
                        n = fn(text)
                        break
                    except Exception as ex:  # noqa: BLE001
                        if attempt == 2:
                            n = None
                            skipped.append((f"{bid}/{tid}/{lang}", f"{type(ex).__name__}: {str(ex)[:100]}"))
                        time.sleep(1.5)
                rows.append({
                    "tokenizer": bid, "family": family, "test": tid, "lang": lang,
                    "chars": len(text), "bytes": len(text.encode("utf-8")), "tokens": n,
                })
    data = {
        "backends": [{"id": b[0], "family": b[1], "description": b[2]} for b in backends],
        "skipped": skipped,
        "rows": rows,
    }
    (RESULTS / "results.json").write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    return data


# ---------------------------------------------------------------- отчёт

def cell(rows, tok, test, lang):
    for r in rows:
        if r["tokenizer"] == tok and r["test"] == test and r["lang"] == lang:
            return r["tokens"]
    return None


def render(data):
    rows, backends = data["rows"], data["backends"]
    parallel = [t for t, v in TESTS.items() if v["category"] == "параллельный текст"]
    universal = [t for t, v in TESTS.items() if v["category"] == "универсальный"]
    out = []

    # 1. Суммарно по параллельным тестам: токены по языкам
    out.append("### Сводка: всего токенов на 5 параллельных текстах\n")
    out.append("В скобках — отношение к английскому (во сколько раз больше токенов на тот же смысл).\n")
    head = "| Токенайзер | Семейство | " + " | ".join(LANGS) + " |"
    out += [head, "|" + "---|" * (len(LANGS) + 2)]
    for b in backends:
        totals = {}
        for lang in LANGS:
            vals = [cell(rows, b["id"], t, lang) for t in parallel]
            totals[lang] = None if any(v is None for v in vals) else sum(vals)
        en = totals["en"]
        parts = []
        for lang in LANGS:
            v = totals[lang]
            if v is None:
                parts.append("—")
            elif lang == "en" or not en:
                parts.append(str(v))
            else:
                parts.append(f"{v} ({v / en:.2f}×)")
        out.append(f"| `{b['id']}` | {b['family']} | " + " | ".join(parts) + " |")

    # 2. Подробно по каждому параллельному тесту (отношение к en)
    for t in parallel:
        out.append(f"\n### Тест `{t}`\n")
        out.append("Токенов (отношение к английскому):\n")
        out += [head, "|" + "---|" * (len(LANGS) + 2)]
        for b in backends:
            en = cell(rows, b["id"], t, "en")
            parts = []
            for lang in LANGS:
                v = cell(rows, b["id"], t, lang)
                if v is None:
                    parts.append("—")
                elif lang == "en" or not en:
                    parts.append(str(v))
                else:
                    parts.append(f"{v} ({v / en:.2f}×)")
            out.append(f"| `{b['id']}` | {b['family']} | " + " | ".join(parts) + " |")

    # 3. Универсальные тесты
    out.append("\n### Универсальные тесты (не зависят от языка)\n")
    out.append("| Токенайзер | " + " | ".join(f"`{t}`" for t in universal) + " |")
    out.append("|" + "---|" * (len(universal) + 1))
    for b in backends:
        vals = [cell(rows, b["id"], t, "any") for t in universal]
        out.append(f"| `{b['id']}` | " + " | ".join("—" if v is None else str(v) for v in vals) + " |")

    # 4. Тексты
    out.append("\n### Тексты, которые подавались на вход\n")
    out.append("| Тест | Язык | Символов | Текст |")
    out.append("|---|---|---|---|")
    for tid, test in TESTS.items():
        for lang, text in test["texts"].items():
            shown = text.replace("\n", "\\n").replace("|", "\\|")
            out.append(f"| `{tid}` | {lang} | {len(text)} | {shown} |")

    if data["skipped"]:
        out.append("\n### Пропущено\n")
        for name, why in data["skipped"]:
            out.append(f"- `{name}`: {why}")
    return "\n".join(out) + "\n"


def write_outputs(data):
    md = render(data)
    (RESULTS / "results.md").write_text("# Результаты опытов с токенизацией\n\n" + md, encoding="utf-8")
    readme = ROOT / "README.md"
    if readme.exists():
        text = readme.read_text(encoding="utf-8")
        a, b = "<!-- RESULTS:START -->", "<!-- RESULTS:END -->"
        if a in text and b in text:
            head, rest = text.split(a, 1)
            _, tail = rest.split(b, 1)
            readme.write_text(head + a + "\n" + md + b + tail, encoding="utf-8")


if __name__ == "__main__":
    d = run()
    write_outputs(d)
    print(f"Токенайзеров: {len(d['backends'])}, строк: {len(d['rows'])}, пропущено: {len(d['skipped'])}")
    for n, why in d["skipped"]:
        print(f"  пропущено {n}: {why}")
