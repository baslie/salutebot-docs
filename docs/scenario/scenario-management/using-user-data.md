---
title: "Используем имя, телефон и email"
source_url: "https://github.com/baslie/salutebot-docs/blob/main/docs/scenario/scenario-management/using-user-data.md"
description: "Документация для разработчиков | Разработка чат-ботов"
reading_time: 1
badges: ["SaluteBot", "Graph", "Code"]
breadcrumbs: ["SaluteBot", "Работаем с данными пользователей", "", "SaluteBot", "Работаем с данными пользователей", "Используем имя, телефон и email"]
---

<!-- Бейджи: SaluteBot | Graph | Code -->

# Используем имя, телефон и email

Обновлено 19 сентября 2024

[![](/assets/scenario/scenario-management/using-user-data/salutebot-new.png)
SaluteBot](../../overview.md)[![](/assets/scenario/scenario-management/using-user-data/Graph.png)
Graph](https://developers.sber.ru/docs/ru/va/graph/overview)[![](/assets/scenario/scenario-management/using-user-data/Code.png)
Code](https://developers.sber.ru/docs/ru/va/code/overview)

Если у вас есть проект SaluteBot, подключенный к каналам Jivo, вы можете использовать в сценарии данные пользователя – имя, телефон и электронный адрес.

Graph
Code

В Graph вы можете воспользоваться системной переменной [`$clientProfile`](https://developers.sber.ru/docs/ru/va/graph/variables/system_variables):

* `$clientProfile.name` — ФИО.
* `$clientProfile.email` — электронный адрес.
* `$clientProfile.phone` — номер телефона.

Например, чтобы поприветствовать пользователя, используя имя:

1. Добавьте в сценарий [блок Текст](../blocks/text.md) с приветствием.
2. Добавьте в блок вывод имени пользователя через переменную `$clientProfile.name`.
3. Соберите сценарий и протестируйте чат-бот в подключенном канале Jivo.

При запуске чат-ботов с `$clientProfile.name` в тестовом виджете будет возникать ошибка, так как чат-бот не может получить данные канала Jivo.

В Code вы можете воспользоваться системной переменной [`$rawRequest`](https://developers.sber.ru/docs/ru/va/code/js-api/variables/request):

* `$request.rawrequest.sender.name` — ФИО.
* `$request.rawrequest.sender.email` — электронный адрес.
* `$request.rawrequest.sender.phone` — номер телефона.

Например, вы можете поприветствовать пользователя, используя имя:

```
state: Start
    q!: $regex</start>
    a: Привет {{ $request.rawrequest.sender.name }}! Чем могу помочь?
```

Заметили ошибку?

Выделите текст и нажмите `Ctrl` + `Enter`, чтобы сообщить нам о ней
