---
title: "Подключаем библиотеки и скрипты"
source_url: "https://github.com/baslie/salutebot-docs/blob/main/docs/scenario/scenario-management/preload-js-scripts.md"
description: "Документация для разработчиков | Разработка чат-ботов"
reading_time: 1
badges: ["SaluteBot", "Code"]
breadcrumbs: ["SaluteBot", "Настраиваем сценарий", "", "SaluteBot", "Настраиваем сценарий", "Подключаем библиотеки и скрипты"]
toc:
  - title: "Синтаксис"
    level: 2
    id: "sintaksis"
---

<!-- Бейджи: SaluteBot | Code -->

# Подключаем библиотеки и скрипты

Содержание раздела

* [Синтаксис](#синтаксис)

# Подключаем библиотеки и скрипты

Обновлено 25 марта 2025

[![](/assets/scenario/scenario-management/preload-js-scripts/salutebot-new.png)
SaluteBot](../../overview.md)[![](/assets/scenario/scenario-management/preload-js-scripts/Code.png)
Code](https://developers.sber.ru/docs/ru/va/code/overview)

Вы можете подключать собственные скрипты и JavaScript-библиотеки, со вспомогательными функциями, в файле конфигурации [`chatbot.yaml`](https://developers.sber.ru/docs/ru/salutebot/bot-steps/project-structure/configuration_file). Подключение скриптов с помощью конфигурационного файла сокращает время сборки чат-бота.

Подключение библиотек и сервисов позволяет использовать их функции в сценариях чат-бота. Так, для работы с [коллекциями](https://underscorejs.ru/#collections) и [массивами](https://underscorejs.ru/#arrays) вы можете использовать функции библиотеки Underscore.js, доступной по умолчанию. Для вызова функции библиотеки используйте нижнее подчеркивание `_`.

Вы также можете подключать скрипты и библиотеки внутри отдельных сценариев с помощью тега [`require`](https://developers.sber.ru/docs/ru/salutebot/bot-steps/project-structure/js). При этом подключать скрипт в файле конфигурации не надо.

## Синтаксис

Для подключения скрипта или библиотеки надо указать абсолютный путь до соответствующего файла в разделе `global` или `local`, в секции `scriptsPreLoad`:

* Скрипты раздела `global` загружаются при первой сборке чат-бота и сохраняются на все последующие сборки.
* Скрипты раздела `local` загружаются при каждой сборке чат-бота и сохраняются до его публикации. При этом файлы скриптов не надо паковать вместе с чат-ботом.

Оба раздела обязательны и не могут быть пустыми.

По умолчанию в `chatbot.yaml` любого проекта Code подключены библиотеки [Underscore.js](http://underscorejs.ru/) и [moment.js](https://momentjs.com/) , а также некоторые [сервисы JavaScript API](https://developers.sber.ru/docs/ru/va/code/js-api/overview):

```
scriptsPreLoad:
    global:
        - /jslib/moment.min.js
        - /jslib/underscore.js
        - /jsapi/common.js
        - /jsapi/http.js
    local:
        - /jsapi/mail.js
        - /jsapi/reactions.js
```

Заметили ошибку?

Выделите текст и нажмите `Ctrl` + `Enter`, чтобы сообщить нам о ней
