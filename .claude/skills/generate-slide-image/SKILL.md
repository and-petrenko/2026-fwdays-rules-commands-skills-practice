---
name: generate-slide-image
description: Генерація зображень за допомогою OpenAI DALL-E API та створення слайдів з цими зображеннями. Використовуй коли потрібно створити візуальний контент, згенерувати ілюстрацію або додати AI-згенероване зображення до презентації.
allowed-tools: Bash(python:*), Bash(pip:*), Read(**/*), Write(slidev/**/*), Edit(slidev/**/*), Bash(cd:*)
---

# Генерація зображень для слайдів

Створює AI-зображення через OpenAI DALL-E та автоматично додає їх до Slidev презентації.

## Передумови

1. Встановлений Python 3.8+
2. API ключ OpenAI в `.env` файлі в корені проєкту

```bash
# Встановлення залежностей
pip install openai

# Створи .env файл в корені проєкту
echo "OPENAI_API_KEY=sk-your-key-here" > .env
```

## Використання

### Крок 1: Згенерувати зображення

```bash
python .claude/skills/generate-slide-image/scripts/generate_image.py "опис зображення"
```

**Параметри:**
- `prompt` - Текстовий опис зображення (обов'язковий)
- `--size` - Розмір: 1024x1024 (за замовчуванням), 1792x1024, 1024x1792
- `--quality` - Якість: standard (за замовчуванням), hd

**Приклад:**
```bash
python .claude/skills/generate-slide-image/scripts/generate_image.py "Футуристичний робот-асистент що допомагає програмісту писати код" --size 1792x1024
```

### Крок 2: Створити слайд

Після генерації зображення, додай слайд до `slidev/slides.md`:

```markdown
---
layout: image-right
image: /images/[назва_файлу].png
---

# Заголовок слайда

- Пункт 1
- Пункт 2
```

## Layouts для зображень

### image-right - Зображення справа
```yaml
layout: image-right
image: /images/example.png
```

### image-left - Зображення зліва
```yaml
layout: image-left
image: /images/example.png
```

### image - Повноекранне зображення
```yaml
layout: image
image: /images/example.png
class: text-white
```

### cover - Фонове зображення
```yaml
layout: cover
background: /images/example.png
```

## Розміри зображень

| Розмір | Опис | Рекомендація |
|--------|------|--------------|
| 1024x1024 | Квадратне | Для image-right/left |
| 1792x1024 | Широке | Для cover, повноекранних |
| 1024x1792 | Вертикальне | Для портретів |

## Приклади промптів

### Для технічної презентації
- "Мінімалістична ілюстрація AI асистента в IDE, синьо-фіолетова колірна схема, flat design"
- "Абстрактна візуалізація нейронної мережі, темний фон, неонові лінії"
- "Робот що читає код на моніторі, кіберпанк стиль"

### Для концептів
- "Діаграма взаємодії людини та AI, сучасний корпоративний стиль"
- "Візуалізація workflow автоматизації, ізометричний стиль"

## Структура файлів

```
slidev/
└── public/
    └── images/
        └── [згенеровані зображення].png
```

## Troubleshooting

### OPENAI_API_KEY not set

Скрипт автоматично читає `.env` файл з кореня проєкту:

```bash
# .env файл в корені проєкту
OPENAI_API_KEY=sk-your-actual-key-here
```

Або встанови змінну середовища напряму:
```bash
# Windows
set OPENAI_API_KEY=sk-...

# Linux/Mac
export OPENAI_API_KEY=sk-...
```

### Помилка генерації
- Перевір баланс OpenAI акаунту
- Спробуй простіший промпт
- Перевір інтернет з'єднання

## Вартість

DALL-E 3 pricing (приблизно):
- Standard 1024x1024: ~$0.04
- Standard 1792x1024: ~$0.08
- HD 1024x1024: ~$0.08
