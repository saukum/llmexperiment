"""Тестовые тексты. Параллельные тексты: одна и та же мысль на разных языках.

LANGS: en, ru, kk (казахский), de, zh. Универсальные тесты (код, JSON, URL, эмодзи, числа)
не зависят от языка и хранятся под ключом "any".
"""

LANGS = ["en", "ru", "kk", "de", "zh"]

TESTS = {
    "greeting": {
        "category": "параллельный текст",
        "texts": {
            "en": "Hello, how are you? Today is a wonderful day for learning about language models.",
            "ru": "Привет, как дела? Сегодня замечательный день, чтобы узнать о языковых моделях.",
            "kk": "Сәлем, қалайсың? Бүгін тіл модельдері туралы білуге тамаша күн.",
            "de": "Hallo, wie geht es dir? Heute ist ein wunderbarer Tag, um etwas über Sprachmodelle zu lernen.",
            "zh": "你好，你好吗？今天是了解语言模型的美好日子。",
        },
    },
    "short": {
        "category": "параллельный текст",
        "texts": {
            "en": "Thank you very much!",
            "ru": "Большое спасибо!",
            "kk": "Үлкен рахмет!",
            "de": "Vielen Dank!",
            "zh": "非常感谢！",
        },
    },
    "science": {
        "category": "параллельный текст",
        "texts": {
            "en": "Water boils at one hundred degrees Celsius at sea level.",
            "ru": "Вода кипит при ста градусах Цельсия на уровне моря.",
            "kk": "Теңіз деңгейінде су жүз градус Цельсийде қайнайды.",
            "de": "Wasser kocht auf Meereshöhe bei hundert Grad Celsius.",
            "zh": "在海平面上，水在一百摄氏度时沸腾。",
        },
    },
    "numbers_dates": {
        "category": "параллельный текст",
        "texts": {
            "en": "The meeting is on 15 November 2026 at 14:30, the budget is $1,250,000.50.",
            "ru": "Встреча состоится 15 ноября 2026 года в 14:30, бюджет — 1 250 000,50 $.",
            "kk": "Кездесу 2026 жылғы 15 қарашада сағат 14:30-да, бюджет — 1 250 000,50 $.",
            "de": "Das Treffen findet am 15. November 2026 um 14:30 Uhr statt, das Budget beträgt 1.250.000,50 $.",
            "zh": "会议将于2026年11月15日14:30举行，预算为1,250,000.50美元。",
        },
    },
    "paragraph": {
        "category": "параллельный текст",
        "texts": {
            "en": (
                "Large language models read text as a sequence of tokens rather than letters. "
                "The number of tokens determines the cost of a request and how much text fits into "
                "the context window. Different languages are split into tokens with different efficiency."
            ),
            "ru": (
                "Большие языковые модели читают текст как последовательность токенов, а не букв. "
                "Количество токенов определяет стоимость запроса и то, сколько текста помещается "
                "в контекстное окно. Разные языки разбиваются на токены с разной эффективностью."
            ),
            "kk": (
                "Үлкен тіл модельдері мәтінді әріптер емес, токендер тізбегі ретінде оқиды. "
                "Токендер саны сұраныстың құнын және контекст терезесіне қанша мәтін сыятынын анықтайды. "
                "Әртүрлі тілдер токендерге әртүрлі тиімділікпен бөлінеді."
            ),
            "de": (
                "Große Sprachmodelle lesen Text als Folge von Tokens und nicht als Buchstaben. "
                "Die Anzahl der Tokens bestimmt die Kosten einer Anfrage und wie viel Text in das "
                "Kontextfenster passt. Verschiedene Sprachen werden mit unterschiedlicher Effizienz "
                "in Tokens zerlegt."
            ),
            "zh": (
                "大型语言模型把文本当作一串词元来读取，而不是字母。"
                "词元的数量决定了请求的成本以及上下文窗口能容纳多少文本。"
                "不同语言被切分成词元的效率各不相同。"
            ),
        },
    },
    "python_code": {
        "category": "универсальный",
        "texts": {
            "any": "def fib(n):\n    a, b = 0, 1\n    for _ in range(n):\n        a, b = b, a + b\n    return a\n",
        },
    },
    "json": {
        "category": "универсальный",
        "texts": {
            "any": '{"id": 42, "name": "test", "tags": ["a", "b"], "price": 19.99, "active": true}',
        },
    },
    "url": {
        "category": "универсальный",
        "texts": {
            "any": "https://github.com/saukum/llmexperiment/blob/main/results/results.md?ref=main&tab=readme",
        },
    },
    "emoji": {
        "category": "универсальный",
        "texts": {
            "any": "👍🚀🇰🇿😀🎉",
        },
    },
    "long_number": {
        "category": "универсальный",
        "texts": {
            "any": "3.14159265358979323846264338327950288419716939937510",
        },
    },
}
