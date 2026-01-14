---
description: Додати приклад коду до слайда
argument-hint: [language: ts|js|json|md] [type: monaco|monaco-run|static]
---

Створи приклад коду мовою **$1** з типом блоку **$2**.

## Параметри

- **Мова:** $1 (ts, js, json, md, vue, bash)
- **Тип:** $2
  - `static` - Звичайний блок коду
  - `monaco` - Редагований код
  - `monaco-run` - Виконуваний код

## Шаблон

### Static (за замовчуванням)
```markdown
```$1 {1|2-3|all}
// Коментар пояснення
const example = "code"
```
```

### Monaco (редагований)
```markdown
```$1 {monaco}
// Спробуй відредагувати!
const example = "code"
```
```

### Monaco-run (виконуваний)
```markdown
```$1 {monaco-run}
// Натисни Run!
console.log("Hello!")
```
```

## Правила

1. **5-15 рядків** коду максимум
2. Додати **підсвічування** `{1|2|3|all}` для static
3. **Коментарі** українською або англійською
4. Для monaco-run код має бути **виконуваним**

Дотримуйся @.claude/rules/code-examples.md
