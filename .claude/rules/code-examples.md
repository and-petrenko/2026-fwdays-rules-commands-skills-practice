---
paths:
  - "slidev/snippets/**/*"
  - "slidev/**/*.md"
---

# Правила для прикладів коду

## Загальні принципи

- Використовувати TypeScript де можливо
- Додавати коментарі для пояснень (українською або англійською)
- Тримати приклади короткими: **5-15 рядків**
- Показувати реальні use cases, не абстрактні приклади

## Формат коду в слайдах

### Підсвічування рядків
```markdown
```ts {1|2-3|all}
// Крок 1: ініціалізація
const config = loadConfig()
// Крок 2-3: обробка
const result = process(config)
```
```

### Покрокова демонстрація
```markdown
```ts {all|1|2|3|all} twoslash
import { ref } from 'vue'
const count = ref(0)
count.value++
```
```

## Monaco Editor

### Коли використовувати {monaco}
- Демонстрація редагування коду
- Показ autocomplete
- Інтерактивні приклади

### Коли використовувати {monaco-run}
- Виконуваний код з результатом
- Демонстрація console.log
- Інтерактивні експерименти

### Приклад
```markdown
```ts {monaco-run}
// Спробуй змінити значення!
const greeting = "Hello fwdays!"
console.log(greeting)
```
```

## Зовнішні сніпети

### Структура файлів
```
slidev/snippets/
├── rules-example.ts      # Приклади правил
├── commands-example.ts   # Приклади команд
├── skills-example.ts     # Приклади навичок
└── mcp-example.ts        # Приклади MCP
```

### Використання маркерів
```typescript
// snippets/rules-example.ts

// #region basic-rule
export const rule = {
  name: "TypeScript style",
  pattern: "*.ts"
}
// #endregion

// #region advanced-rule
export const advancedRule = {
  // ...більше коду
}
// #endregion
```

### Імпорт у слайди
```markdown
<<< @/snippets/rules-example.ts#basic-rule
```

## Приклади для кожної секції

### Секція 2: Rules
```json
// .cursorrules або CLAUDE.md приклади
{
  "rules": [
    "Use TypeScript strict mode",
    "Follow ESLint configuration"
  ]
}
```

### Секція 3: Commands
```markdown
// Slash команди
/review - Code review поточного файлу
/test - Згенерувати тести
/docs - Створити документацію
```

### Секція 4: Skills
```json
// MCP конфігурація
{
  "mcpServers": {
    "context7": {
      "command": "npx",
      "args": ["@anthropic/context7-mcp"]
    }
  }
}
```

## Стиль коментарів

### В коді
```typescript
// Коротко: що робить цей рядок
const result = await fetch(url)

// Детальніше для складної логіки:
// Цей блок обробляє помилки мережі
// та повертає fallback значення
try {
  // ...
} catch (e) {
  // ...
}
```

### В Markdown
```markdown
<!-- Пояснення для складних слайдів -->
```

## Валідація

Перед додаванням коду перевір:
- [ ] Код синтаксично правильний
- [ ] Підсвічування працює (`{1|2|3}`)
- [ ] Monaco блоки запускаються
- [ ] Зовнішні сніпети імпортуються
