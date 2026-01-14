# CLAUDE.md

Цей файл надає інструкції для Claude Code при роботі з цим репозиторієм.

## Огляд проєкту

- **Подія:** fwdays 2026
- **Тема:** "Правила, команди та навички для Agentic IDE"
- **Тривалість:** 35 хвилин
- **Технології:** Slidev v52.11.3+, Vue 3, UnoCSS

## Швидкий старт

```bash
cd slidev && pnpm install && pnpm dev
```

## CLI команди

Виконувати з директорії `slidev/`:

| Команда | Опис |
|---------|------|
| `pnpm dev` | Сервер розробки (localhost:3030) |
| `pnpm build` | Продакшн збірка |
| `pnpm export` | Експорт у PDF |

## Slash-команди

Доступні команди для роботи з презентацією:

| Команда | Опис |
|---------|------|
| `/new-slide [title] [layout]` | Створити новий слайд |
| `/preview` | Запустити dev server |
| `/export [format]` | Експортувати в PDF/PNG |
| `/add-code [lang] [type]` | Додати приклад коду |
| `/add-diagram [type]` | Створити Mermaid діаграму |
| `/check-timing` | Перевірити тайминг презентації |
| `/check-guidelines` | Валідувати контент |
| `/sync-prd` | Порівняти з PRD структурою |

## Навички (Skills)

Автоматично активуються при відповідних запитах:

| Навичка | Опис | Передумови |
|---------|------|------------|
| `generate-slide-image` | Генерація зображень через DALL-E | `OPENAI_API_KEY` |

### generate-slide-image

Генерує AI-зображення та створює слайди з ними.

**Використання:**
```bash
python .claude/skills/generate-slide-image/scripts/generate_image.py "опис зображення"
```

**Встановлення:**
```bash
pip install openai pillow
export OPENAI_API_KEY=sk-...
```

## Архітектура

```
slidev/
├── slides.md          # Головний файл презентації
├── pages/             # Імпортовані слайди (src: директива)
├── components/        # Vue компоненти
├── snippets/          # Сніпети коду для вставки
└── public/            # Статичні ресурси
```

### Ключові файли
- `PRD.md` - Документ вимог з детальною структурою презентації
- `slidev/slides.md` - Всі слайди в одному файлі

## Робочий процес

1. Запусти `pnpm dev` з директорії `slidev/`
2. Відкрий http://localhost:3030
3. Редагуй `slides.md` - зміни автоматично оновлюються
4. Використовуй presenter mode для нотаток

## Конвенції

Детальні правила знаходяться у `.claude/rules/`:
- `slidev-syntax.md` - Синтаксис Slidev
- `content-guidelines.md` - Правила контенту
- `code-examples.md` - Формат прикладів коду

## Deployment

### GitHub Pages (рекомендовано)

Автоматичний деплой через GitHub Actions:

1. Увімкни GitHub Pages в налаштуваннях репозиторію:
   - Settings → Pages → Source: **GitHub Actions**
2. Push в `main` branch запускає автоматичний деплой
3. Презентація доступна за адресою:
   `https://<username>.github.io/2026-fwdays-rules-commands-skills-practice-right/`

Workflow файл: `.github/workflows/deploy.yml`

### Інші платформи

- **Netlify:** Налаштовано в `netlify.toml`
- **Vercel:** Налаштовано в `vercel.json`
- **Output:** `dist/`
