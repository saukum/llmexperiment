"""Опыт 1: одна и та же фраза на английском и русском через токенайзеры tiktoken.

Запуск: python tokenize_experiment.py > results/experiment1_tokenization.md
"""
import sys

import tiktoken

sys.stdout.reconfigure(encoding="utf-8")  # чтобы вывод был UTF-8 на любой ОС

PHRASES = {
    "en": "Hello, how are you? Today is a wonderful day for learning about language models.",
    "ru": "Привет, как дела? Сегодня замечательный день, чтобы узнать о языковых моделях.",
}
ENCODINGS = ["cl100k_base", "o200k_base"]


def show(enc, text):
    ids = enc.encode(text)
    pieces = []
    for i in ids:
        b = enc.decode_single_token_bytes(i)
        try:
            pieces.append(b.decode("utf-8"))
        except UnicodeDecodeError:
            # токен режет символ посередине: показываем сырые байты
            pieces.append("<" + " ".join(f"0x{x:02X}" for x in b) + ">")
    return ids, pieces


print("# Опыт 1. Токенизация одной фразы: английский vs русский\n")
print("Токенайзеры: tiktoken (OpenAI). Это не токенайзер Claude, числа для Claude будут другими.\n")

summary = []
for name in ENCODINGS:
    enc = tiktoken.get_encoding(name)
    print(f"## {name}\n")
    for lang, text in PHRASES.items():
        ids, pieces = show(enc, text)
        print(f"**{lang}**: {text}\n")
        print(f"- символов: {len(text)}, байт UTF-8: {len(text.encode('utf-8'))}, токенов: {len(ids)}")
        print(f"- символов на токен: {len(text) / len(ids):.2f}")
        print("- токены: " + " ".join(f"[{p!r}]" for p in pieces) + "\n")
        summary.append((name, lang, len(text), len(ids)))

print("## Сводка\n")
print("| Кодировка | Язык | Символов | Токенов | Симв./токен |")
print("|---|---|---|---|---|")
for name, lang, chars, toks in summary:
    print(f"| {name} | {lang} | {chars} | {toks} | {chars / toks:.2f} |")

print("\n## Отношение ru/en по числу токенов\n")
for name in ENCODINGS:
    en = next(t for n, l, c, t in summary if n == name and l == "en")
    ru = next(t for n, l, c, t in summary if n == name and l == "ru")
    print(f"- {name}: {ru}/{en} = {ru / en:.2f}x")
