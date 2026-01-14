---
description: Створити новий слайд з правильною структурою
argument-hint: [title] [layout: default|two-cols|center|cover]
---

Створи новий слайд у `slidev/slides.md` з заголовком "$1".

## Параметри

- **Title:** $1
- **Layout:** $2 (за замовчуванням: default)

## Структура слайда

Додай в кінець `slidev/slides.md`:

```markdown
---
transition: slide-left
layout: [layout]
---

# [Title]

- Пункт 1
- Пункт 2
- Пункт 3

<!--
Presenter notes:
- Ключові моменти
- Час: ~1 хв
-->
```

## Правила

1. Frontmatter з transition та layout
2. Заголовок H1
3. Контент (максимум 5 пунктів)
4. Presenter notes в HTML коментарі

Дотримуйся правил з @.claude/rules/content-guidelines.md
