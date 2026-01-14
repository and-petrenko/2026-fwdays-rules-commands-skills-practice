---
description: Створити Mermaid діаграму
argument-hint: [type: flowchart|sequence|mindmap|graph]
---

Створи **$1** діаграму в Mermaid синтаксисі.

## Типи діаграм

### flowchart - Блок-схема процесу
```mermaid {scale: 0.8}
flowchart TD
    A[Початок] --> B{Умова}
    B -->|Так| C[Дія 1]
    B -->|Ні| D[Дія 2]
    C --> E[Кінець]
    D --> E
```

### sequence - Діаграма послідовності
```mermaid {scale: 0.8}
sequenceDiagram
    User->>+Agent: Запит
    Agent->>+Tool: Виклик
    Tool-->>-Agent: Результат
    Agent-->>-User: Відповідь
```

### mindmap - Карта думок
```mermaid
mindmap
    root((Тема))
        Гілка 1
            Підгілка 1.1
            Підгілка 1.2
        Гілка 2
            Підгілка 2.1
```

### graph - Архітектура
```mermaid {scale: 0.8}
graph LR
    A[Компонент 1] --> B[Компонент 2]
    B --> C[Компонент 3]
    A --> C
```

## Правила

1. Додай `{scale: 0.8}` якщо діаграма велика
2. Використовуй українські підписи де можливо
3. Тримай діаграму простою (5-10 елементів)
