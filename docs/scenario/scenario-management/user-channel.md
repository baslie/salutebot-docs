---
title: "Определяем откуда пришел пользователь"
source_url: "https://github.com/baslie/salutebot-docs/blob/main/docs/scenario/scenario-management/user-channel.md"
description: "Определяем откуда пришел пользователь | Разработка чат-ботов"
reading_time: 1
badges: ["SaluteBot", "Code", "Graph"]
breadcrumbs: ["SaluteBot", "Работаем с данными пользователей", "", "SaluteBot", "Работаем с данными пользователей", "Определяем откуда пришел пользователь"]
---

<!-- Бейджи: SaluteBot | Code | Graph -->

# Определяем откуда пришел пользователь

Обновлено 22 декабря 2023

[![](/assets/scenario/scenario-management/user-channel/salutebot-new.png)
SaluteBot](../../overview.md)[![](/assets/scenario/scenario-management/user-channel/Code.png)
Code](https://developers.sber.ru/docs/ru/va/code/overview)[![](/assets/scenario/scenario-management/user-channel/Graph.png)
Graph](https://developers.sber.ru/docs/ru/va/graph/overview)

При работе с чат-ботом может быть полезно различать пользователей в зависимости от канала, из которого они пришли. Такое разделение пользователей поможет сделать диалог с ними более предметным, например, предлагать особые условия определенной категории пользователей или при общении давать ссылки на те социальные сети, которые наиболее удобны пользователю (ссылку на Telegram, если пользователь пришел из Telegram и т.п.).

Для получения канала пользователя в сценарии:

Graph
Code

1. Выберите экран в сценарии.
2. Добавьте блок **Текст**, **Условие** или любой другой, в котором поддержаны переменные.
3. Добавьте системную переменную `$userChannel`.

В результате при выполнении сценария будет получено значение канала, из которого пришел пользователь.

1. Выберите нужный экран в сценарии.
2. Добавьте системную переменную `$request.userChannel` в тэг ответа, условия или скрипта.

В результате при выполнении сценария будет получено значение канала, из которого пришел пользователь.

**Список доступных значений каналов в Jivo**

| Тип | Описание |
| --- | --- |
| WIDGET | Виджет на сайте |
| CHAT\_PAGE | Страница чат-виджета jivo |
| EMAIL | Электронная почта |
| TELEGRAM | Telegram |
| VIBER | Viber |
| VKONTAKTE | ВКонтакте |
| ODNOKLASSNIKI | Одноклассники |
| YANDEX | Яндекс. Мессенджер |
| AVITO | Avito |
| MOBILE\_SDK | Мобильное SDK |
| TELEPHONY | СМС-канал |
| ALIEXPRESS | Aliexpress |
| CHAT\_API | Канал для других интеграций |

Пример использования в сценарии:

```
state: where order
    intent: /где_заказ
    if: $request.userChannel === 'EMAIL'
        go!: /emailCheck
    elseif: $request.userChannel === 'WIDGET'
        go!: /widgetCheck
    else:
        go!: /allUserCheck
```

Заметили ошибку?

Выделите текст и нажмите `Ctrl` + `Enter`, чтобы сообщить нам о ней
