---
description: Запустити Slidev development server
allowed-tools: Bash(pnpm:*), Bash(cd:*)
---

Запусти Slidev dev server для попереднього перегляду презентації.

## Кроки

1. Перейди в директорію `slidev/`
2. Виконай команду `pnpm dev`
3. Сервер буде доступний на http://localhost:3030

## Примітки

- Якщо порт 3030 зайнятий, Slidev автоматично використає інший
- Зміни в `slides.md` автоматично оновлюються (hot reload)
- Для presenter mode додай `?presenter` до URL

## Корисні URL

- http://localhost:3030 - Слайди
- http://localhost:3030/presenter - Presenter mode
- http://localhost:3030/overview - Огляд всіх слайдів
