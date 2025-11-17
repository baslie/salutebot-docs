---
title: "Работа с модулями sys.modules"
source_url: "https://developers.sber.ru/docs/ru/salutebot/bot-development/project-structure/sys-modules"
description: "Документация для разработчиков | Разработка чат-ботов"
reading_time: 1
badges: ["SaluteBot", "Code"]
toc:
  - title: "Cинтаксис и использование"
    level: 2
    id: "cintaksis-i-ispolzovanie"
---

<!-- Бейджи: SaluteBot | Code -->

# Работа с модулями sys.modules

Содержание раздела

* [Cинтаксис и использование](#cинтаксис-и-использование)

# Работа с модулями sys.modules

Обновлено 29 ноября 2023

[![](/assets/bot-development/project-structure/sys-modules/salutebot-new.png)
SaluteBot](../../overview.md)[![](/assets/bot-development/project-structure/sys-modules/Code.png)
Code](https://developers.sber.ru/docs/ru/va/code/overview)

`sys.modules` — модули, на которые можно ссылаться в сценарии и переиспользовать контент из них: файлы сценариев, JS-библиотек, справочников.

## Cинтаксис и использование

Файлы модуля подгружаются из внутренних ресурсов приложения или из папки `botserver-modules`.

Укажите путь к `botserver-modules` в файле `application.yml`:

```
systemModulesFolder: /folder/other-folder/botserver-modules
```

Пример структуры папки `botserver-modules`:

```
/opt/sberdevices/botserver-modules


├── common
│   ├── chatbot.yaml
│   ├── declarations.js
│   ├── src
│   └── test
└── dictionaries
    └── main_dictionary
```

Для вызова модуля в сценарии укажите:

```
require: <вызываемый файл>
  module = sys.<имя папки c вызываемым файлом>
```

Здесь префикс `sys` соответствует указанному в `application.yml` пути. Таким образом, требуется указывать только конечную папку с файлом.

Вызовите модуль в сценарии, например:

```
require: common.js
  module = sys.common
```

Здесь:

* `require: common.js` — вызываем скрипт, который будет использоваться в сценарии.
* `module = sys.common` — указываем папку, в которой находится файл скрипта.

Теперь контент из вызванного файла модуля можно использовать в сценарии проекта.

Заметили ошибку?

Выделите текст и нажмите `Ctrl` + `Enter`, чтобы сообщить нам о ней
