# Результаты опытов с токенизацией

### Сводка: всего токенов на 5 параллельных текстах

В скобках — отношение к английскому (во сколько раз больше токенов на тот же смысл).

| Токенайзер | Семейство | en | ru | kk | de | zh |
|---|---|---|---|---|---|---|
| `cl100k_base` | OpenAI | 105 | 206 (1.96×) | 315 (3.00×) | 146 (1.39×) | 163 (1.55×) |
| `o200k_base` | OpenAI | 105 | 125 (1.19×) | 147 (1.40×) | 124 (1.18×) | 114 (1.09×) |
| `o200k_harmony` | OpenAI | 105 | 125 (1.19×) | 147 (1.40×) | 124 (1.18×) | 114 (1.09×) |
| `Qwen/Qwen3-8B` | Open | 115 | 170 (1.48×) | 266 (2.31×) | 156 (1.36×) | 111 (0.97×) |
| `deepseek-ai/DeepSeek-V3` | Open | 105 | 137 (1.30×) | 226 (2.15×) | 143 (1.36×) | 88 (0.84×) |
| `unsloth/Llama-3.2-1B` | Open | 105 | 150 (1.43×) | 253 (2.41×) | 146 (1.39×) | 124 (1.18×) |
| `mistralai/Mistral-Nemo-Instruct-2407` | Open | 116 | 151 (1.30×) | 202 (1.74×) | 147 (1.27×) | 150 (1.29×) |
| `unsloth/gemma-3-1b-it` | Open | 115 | 130 (1.13×) | 192 (1.67×) | 132 (1.15×) | 113 (0.98×) |

### Тест `greeting`

Токенов (отношение к английскому):

| Токенайзер | Семейство | en | ru | kk | de | zh |
|---|---|---|---|---|---|---|
| `cl100k_base` | OpenAI | 17 | 35 (2.06×) | 46 (2.71×) | 28 (1.65×) | 23 (1.35×) |
| `o200k_base` | OpenAI | 17 | 19 (1.12×) | 22 (1.29×) | 23 (1.35×) | 15 (0.88×) |
| `o200k_harmony` | OpenAI | 17 | 19 (1.12×) | 22 (1.29×) | 23 (1.35×) | 15 (0.88×) |
| `Qwen/Qwen3-8B` | Open | 17 | 25 (1.47×) | 38 (2.24×) | 28 (1.65×) | 13 (0.76×) |
| `deepseek-ai/DeepSeek-V3` | Open | 17 | 21 (1.24×) | 34 (2.00×) | 27 (1.59×) | 12 (0.71×) |
| `unsloth/Llama-3.2-1B` | Open | 17 | 26 (1.53×) | 35 (2.06×) | 28 (1.65×) | 17 (1.00×) |
| `mistralai/Mistral-Nemo-Instruct-2407` | Open | 17 | 22 (1.29×) | 28 (1.65×) | 27 (1.59×) | 18 (1.06×) |
| `unsloth/gemma-3-1b-it` | Open | 17 | 18 (1.06×) | 27 (1.59×) | 23 (1.35×) | 13 (0.76×) |

### Тест `short`

Токенов (отношение к английскому):

| Токенайзер | Семейство | en | ru | kk | de | zh |
|---|---|---|---|---|---|---|
| `cl100k_base` | OpenAI | 5 | 10 (2.00×) | 11 (2.20×) | 4 (0.80×) | 6 (1.20×) |
| `o200k_base` | OpenAI | 5 | 4 (0.80×) | 6 (1.20×) | 3 (0.60×) | 3 (0.60×) |
| `o200k_harmony` | OpenAI | 5 | 4 (0.80×) | 6 (1.20×) | 3 (0.60×) | 3 (0.60×) |
| `Qwen/Qwen3-8B` | Open | 5 | 9 (1.80×) | 8 (1.60×) | 4 (0.80×) | 3 (0.60×) |
| `deepseek-ai/DeepSeek-V3` | Open | 5 | 7 (1.40×) | 9 (1.80×) | 4 (0.80×) | 2 (0.40×) |
| `unsloth/Llama-3.2-1B` | Open | 5 | 7 (1.40×) | 8 (1.60×) | 4 (0.80×) | 4 (0.80×) |
| `mistralai/Mistral-Nemo-Instruct-2407` | Open | 5 | 6 (1.20×) | 8 (1.60×) | 4 (0.80×) | 4 (0.80×) |
| `unsloth/gemma-3-1b-it` | Open | 5 | 4 (0.80×) | 7 (1.40×) | 4 (0.80×) | 3 (0.60×) |

### Тест `science`

Токенов (отношение к английскому):

| Токенайзер | Семейство | en | ru | kk | de | zh |
|---|---|---|---|---|---|---|
| `cl100k_base` | OpenAI | 11 | 27 (2.45×) | 39 (3.55×) | 16 (1.45×) | 23 (2.09×) |
| `o200k_base` | OpenAI | 11 | 16 (1.45×) | 17 (1.55×) | 14 (1.27×) | 18 (1.64×) |
| `o200k_harmony` | OpenAI | 11 | 16 (1.45×) | 17 (1.55×) | 14 (1.27×) | 18 (1.64×) |
| `Qwen/Qwen3-8B` | Open | 11 | 22 (2.00×) | 30 (2.73×) | 16 (1.45×) | 14 (1.27×) |
| `deepseek-ai/DeepSeek-V3` | Open | 11 | 17 (1.55×) | 26 (2.36×) | 15 (1.36×) | 10 (0.91×) |
| `unsloth/Llama-3.2-1B` | Open | 11 | 17 (1.55×) | 31 (2.82×) | 16 (1.45×) | 18 (1.64×) |
| `mistralai/Mistral-Nemo-Instruct-2407` | Open | 12 | 17 (1.42×) | 21 (1.75×) | 14 (1.17×) | 20 (1.67×) |
| `unsloth/gemma-3-1b-it` | Open | 11 | 15 (1.36×) | 23 (2.09×) | 12 (1.09×) | 15 (1.36×) |

### Тест `numbers_dates`

Токенов (отношение к английскому):

| Токенайзер | Семейство | en | ru | kk | de | zh |
|---|---|---|---|---|---|---|
| `cl100k_base` | OpenAI | 28 | 40 (1.43×) | 50 (1.79×) | 34 (1.21×) | 31 (1.11×) |
| `o200k_base` | OpenAI | 28 | 29 (1.04×) | 32 (1.14×) | 31 (1.11×) | 26 (0.93×) |
| `o200k_harmony` | OpenAI | 28 | 29 (1.04×) | 32 (1.14×) | 31 (1.11×) | 26 (0.93×) |
| `Qwen/Qwen3-8B` | Open | 38 | 39 (1.03×) | 52 (1.37×) | 44 (1.16×) | 36 (0.95×) |
| `deepseek-ai/DeepSeek-V3` | Open | 28 | 30 (1.07×) | 37 (1.32×) | 33 (1.18×) | 25 (0.89×) |
| `unsloth/Llama-3.2-1B` | Open | 28 | 31 (1.11×) | 42 (1.50×) | 34 (1.21×) | 28 (1.00×) |
| `mistralai/Mistral-Nemo-Instruct-2407` | Open | 38 | 42 (1.11×) | 47 (1.24×) | 42 (1.11×) | 41 (1.08×) |
| `unsloth/gemma-3-1b-it` | Open | 38 | 38 (1.00×) | 44 (1.16×) | 42 (1.11×) | 36 (0.95×) |

### Тест `paragraph`

Токенов (отношение к английскому):

| Токенайзер | Семейство | en | ru | kk | de | zh |
|---|---|---|---|---|---|---|
| `cl100k_base` | OpenAI | 44 | 94 (2.14×) | 169 (3.84×) | 64 (1.45×) | 80 (1.82×) |
| `o200k_base` | OpenAI | 44 | 57 (1.30×) | 70 (1.59×) | 53 (1.20×) | 52 (1.18×) |
| `o200k_harmony` | OpenAI | 44 | 57 (1.30×) | 70 (1.59×) | 53 (1.20×) | 52 (1.18×) |
| `Qwen/Qwen3-8B` | Open | 44 | 75 (1.70×) | 138 (3.14×) | 64 (1.45×) | 45 (1.02×) |
| `deepseek-ai/DeepSeek-V3` | Open | 44 | 62 (1.41×) | 120 (2.73×) | 64 (1.45×) | 39 (0.89×) |
| `unsloth/Llama-3.2-1B` | Open | 44 | 69 (1.57×) | 137 (3.11×) | 64 (1.45×) | 57 (1.30×) |
| `mistralai/Mistral-Nemo-Instruct-2407` | Open | 44 | 64 (1.45×) | 98 (2.23×) | 60 (1.36×) | 67 (1.52×) |
| `unsloth/gemma-3-1b-it` | Open | 44 | 55 (1.25×) | 91 (2.07×) | 51 (1.16×) | 46 (1.05×) |

### Универсальные тесты (не зависят от языка)

| Токенайзер | `python_code` | `json` | `url` | `emoji` | `long_number` |
|---|---|---|---|---|---|
| `cl100k_base` | 37 | 34 | 25 | 17 | 19 |
| `o200k_base` | 37 | 34 | 25 | 10 | 19 |
| `o200k_harmony` | 37 | 34 | 25 | 10 | 19 |
| `Qwen/Qwen3-8B` | 37 | 37 | 25 | 6 | 52 |
| `deepseek-ai/DeepSeek-V3` | 37 | 34 | 28 | 11 | 19 |
| `unsloth/Llama-3.2-1B` | 37 | 34 | 25 | 17 | 19 |
| `mistralai/Mistral-Nemo-Instruct-2407` | 37 | 37 | 28 | 24 | 52 |
| `unsloth/gemma-3-1b-it` | 41 | 37 | 31 | 6 | 52 |

### Тексты, которые подавались на вход

| Тест | Язык | Символов | Текст |
|---|---|---|---|
| `greeting` | en | 80 | Hello, how are you? Today is a wonderful day for learning about language models. |
| `greeting` | ru | 78 | Привет, как дела? Сегодня замечательный день, чтобы узнать о языковых моделях. |
| `greeting` | kk | 63 | Сәлем, қалайсың? Бүгін тіл модельдері туралы білуге тамаша күн. |
| `greeting` | de | 93 | Hallo, wie geht es dir? Heute ist ein wunderbarer Tag, um etwas über Sprachmodelle zu lernen. |
| `greeting` | zh | 22 | 你好，你好吗？今天是了解语言模型的美好日子。 |
| `short` | en | 20 | Thank you very much! |
| `short` | ru | 16 | Большое спасибо! |
| `short` | kk | 13 | Үлкен рахмет! |
| `short` | de | 12 | Vielen Dank! |
| `short` | zh | 5 | 非常感谢！ |
| `science` | en | 56 | Water boils at one hundred degrees Celsius at sea level. |
| `science` | ru | 51 | Вода кипит при ста градусах Цельсия на уровне моря. |
| `science` | kk | 50 | Теңіз деңгейінде су жүз градус Цельсийде қайнайды. |
| `science` | de | 53 | Wasser kocht auf Meereshöhe bei hundert Grad Celsius. |
| `science` | zh | 17 | 在海平面上，水在一百摄氏度时沸腾。 |
| `numbers_dates` | en | 73 | The meeting is on 15 November 2026 at 14:30, the budget is $1,250,000.50. |
| `numbers_dates` | ru | 71 | Встреча состоится 15 ноября 2026 года в 14:30, бюджет — 1 250 000,50 $. |
| `numbers_dates` | kk | 71 | Кездесу 2026 жылғы 15 қарашада сағат 14:30-да, бюджет — 1 250 000,50 $. |
| `numbers_dates` | de | 94 | Das Treffen findet am 15. November 2026 um 14:30 Uhr statt, das Budget beträgt 1.250.000,50 $. |
| `numbers_dates` | zh | 41 | 会议将于2026年11月15日14:30举行，预算为1,250,000.50美元。 |
| `paragraph` | en | 247 | Large language models read text as a sequence of tokens rather than letters. The number of tokens determines the cost of a request and how much text fits into the context window. Different languages are split into tokens with different efficiency. |
| `paragraph` | ru | 239 | Большие языковые модели читают текст как последовательность токенов, а не букв. Количество токенов определяет стоимость запроса и то, сколько текста помещается в контекстное окно. Разные языки разбиваются на токены с разной эффективностью. |
| `paragraph` | kk | 219 | Үлкен тіл модельдері мәтінді әріптер емес, токендер тізбегі ретінде оқиды. Токендер саны сұраныстың құнын және контекст терезесіне қанша мәтін сыятынын анықтайды. Әртүрлі тілдер токендерге әртүрлі тиімділікпен бөлінеді. |
| `paragraph` | de | 260 | Große Sprachmodelle lesen Text als Folge von Tokens und nicht als Buchstaben. Die Anzahl der Tokens bestimmt die Kosten einer Anfrage und wie viel Text in das Kontextfenster passt. Verschiedene Sprachen werden mit unterschiedlicher Effizienz in Tokens zerlegt. |
| `paragraph` | zh | 71 | 大型语言模型把文本当作一串词元来读取，而不是字母。词元的数量决定了请求的成本以及上下文窗口能容纳多少文本。不同语言被切分成词元的效率各不相同。 |
| `python_code` | any | 88 | def fib(n):\n    a, b = 0, 1\n    for _ in range(n):\n        a, b = b, a + b\n    return a\n |
| `json` | any | 78 | {"id": 42, "name": "test", "tags": ["a", "b"], "price": 19.99, "active": true} |
| `url` | any | 88 | https://github.com/saukum/llmexperiment/blob/main/results/results.md?ref=main&tab=readme |
| `emoji` | any | 6 | 👍🚀🇰🇿😀🎉 |
| `long_number` | any | 52 | 3.14159265358979323846264338327950288419716939937510 |

### Пропущено

- `Claude (все модели)`: нет ANTHROPIC_API_KEY — подсчёт через API пропущен
