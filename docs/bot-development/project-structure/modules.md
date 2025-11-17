---
title: "Работа с модулями"
source_url: "https://github.com/baslie/salutebot-docs/blob/main/docs/bot-development/project-structure/modules.md"
description: "Документация для разработчиков | Разработка чат-ботов"
reading_time: 1
badges: ["SaluteBot", "Code"]
toc:
  - title: "Cинтаксис"
    level: 4
    id: "cintaksis"
  - title: "Работа сmodule"
    level: 4
    id: "rabota-s-module"
---

<!-- Бейджи: SaluteBot | Code -->

# Работа с модулями

Содержание раздела

* [Cинтаксис](#cинтаксис)
* [Работа с module](#работа-сmodule)

# Работа с модулями

Обновлено 15 декабря 2023

[![](/assets/bot-development/project-structure/modules/salutebot-new.png)
SaluteBot](../../overview.md)[![](/assets/bot-development/project-structure/modules/Code.png)
Code](https://developers.sber.ru/docs/ru/va/code/overview)



---

В конфигурационном файле `chatbot.yaml` в секции `dependencies` определяется список зависимостей проекта.

`module` — одна из возможных зависимостей. Это готовые модули, на которые вы можете ссылаться и переиспользовать контент из них: файлы сценариев, JS-библиотек, справочников.

[Подробнее о конфигурационном файле и зависимостях](https://developers.sber.ru/docs/ru/salutebot/bot-steps/project-structure/configuration_file)





#### Cинтаксис

Указываются модули в зависимостях `dependencies` конфигурационного файла `chatbot.yaml`.

Параметры `module`:

| Поле | Возможные значения | Описание |
| --- | --- | --- |
| `name` | `<name>` | Имя модуля, которое будет использоваться при подключении файлов в директиве `require`. |
| `type` | `module` | Папка репозитория относительно пути `<projectFolder>,` которая содержит модуль. |






#### Работа с `module`

Рассмотрим пример подключения модуля. Зададим в конфигурационном файле имя и папку модуля в `dependencies`:

```
name: games-test

entryPoint: main.sc

dependencies:
    - name: common
      type: module
```

Далее вызовем в сценарии файлы из модуля при помощи `require`:

```
require: text/text.sc
    module = common

require: number/number.sc
    module = common

require: common.js
    module = common

require: city/city.sc
    module = common

require: city/cities-ru.csv
    name = Cities
    var = $Cities
    module = common
```

[Подробнее об использовании тега `require`](https://developers.sber.ru/docs/ru/va/code/sa-dsl/tags/declarative-tags#require)

Теперь контент из вызванных файлов модуля можно использовать в сценарии проекта. Например, сценарий `main.sc`:

```
require: number/number.sc
    module = common

require: common.js
    module = common

require: city/city.sc
    module = common

require: city/cities-ru.csv
    name = Cities
    var = $Cities
    module = common

theme: /

    state: Text
        q: $Text
        a: Вы сказали: {{ $parseTree._Text }}

    state: NumberPattern
        q: * $Number *
        a: Число: {{$parseTree._Number}}

    state: CityPattern
        q: * $City *
        a: Город: {{$parseTree._City.name}}

    state: NoMatch
        q: *
        a: Извините, я вас не понимаю.
```

Зависимости скачиваются в папку `modules` при деплое через веб-интерфейс.

Заметили ошибку?

Выделите текст и нажмите `Ctrl` + `Enter`, чтобы сообщить нам о ней
