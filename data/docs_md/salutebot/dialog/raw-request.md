---
title: "Обрабатываем запросы пользователя"
source_url: "https://github.com/baslie/salutebot-docs/blob/main/data/docs_md/salutebot/dialog/raw-request.md"
description: "Документация для разработчиков | Разработка чат-ботов"
reading_time: 1
badges: ["SaluteBot", "Graph"]
toc:
  - title: "Переменная rawRequest"
    level: 2
    id: "peremennaya-raw-request"
  - title: "Подробнее о переменных"
    level: 2
    id: "podrobnee-o-peremennyh"
---

<!-- Бейджи: SaluteBot | Graph -->

# Обрабатываем запросы пользователя

Содержание раздела

* [Переменная rawRequest](#переменная-rawrequest)
* [Подробнее о переменных](#подробнее-о-переменных)

# Обрабатываем запросы пользователя

Обновлено 26 июня 2024

[![](/assets/salutebot/dialog/raw-request/salutebot-new.png)
SaluteBot](../overview.md)[![](/assets/salutebot/dialog/raw-request/Graph.png)
Graph](https://developers.sber.ru/docs/ru/va/graph/overview)

Для обработки данных запроса используется системная переменная [`$rawRequest`](https://developers.sber.ru/docs/ru/va/graph/variables/system_variables).

## Переменная rawRequest

Переменная содержит запрос пользователя в формате [SmartApp API](https://developers.sber.ru/docs/ru/va/api/overview).

Для доступа к полям переменной используется точечная нотация JavaScript:

```
$rawRequest.payload.message;
```

При запуске чат-ботов с `$rawRequest` в тестовом виджете будет возникать ошибка.

## Подробнее о переменных

* [Что такое переменные](https://developers.sber.ru/docs/ru/va/graph/variables/create-variables)
* [Системные переменные](https://developers.sber.ru/docs/ru/va/graph/variables/system_variables)

Заметили ошибку?

Выделите текст и нажмите `Ctrl` + `Enter`, чтобы сообщить нам о ней
