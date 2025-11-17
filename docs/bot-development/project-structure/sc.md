---
title: "Файлы сценариев"
source_url: "https://developers.sber.ru/docs/ru/salutebot/bot-development/project-structure/sc"
description: "Документация для разработчиков | Разработка чат-ботов"
reading_time: 1
badges: ["SaluteBot", "Code"]
toc:
  - title: "Пример файла сценария"
    level: 2
    id: "primer-fayla-stsenariya"
---

<!-- Бейджи: SaluteBot | Code -->

# Файлы сценариев

Содержание раздела

* [Пример файла сценария](#пример-файла-сценария)

# Файлы сценариев

Обновлено 15 декабря 2023

[![](/assets/bot-development/project-structure/sc/salutebot-new.png)
SaluteBot](../../overview.md)[![](/assets/bot-development/project-structure/sc/Code.png)
Code](https://developers.sber.ru/docs/ru/va/code/overview)

Файлы сценариев — это основные файлы, задающие правила работы чат-бота. Имеют расширение `.sc`. Сценарий работы чат-бота разрабатывается при помощи [SmartApp DSL](https://developers.sber.ru/docs/ru/va/code/sa-dsl/overview).

`main.sc` или `entryPoint.sc` — главный файл сценария чат-бота, с которого начинается загрузка сценария. Файл находится в папке `src`, где также могут находиться файлы с дополнительными сценариями, словари в формате `.csv` и скрипты в формате `.js`.

Файл сценария — древовидная структура. Степень вложенности управляется отступами, подобно языкам python и yaml. Файл включает: тему, список стейтов, паттерны, подгружаемые файлы и реакции.

В начале сценария можно подключить другие сценарии или js-файлы с помощью тега `require`:

```
require: scenarios/*.sc
require: scripts/functions.js
```

## Пример файла сценария

Для работы сценария надо [включить отправку команду `/start`](../../dialog/start.md) при запуске чат-бота.

```
patterns:
    $hello = (start)

theme: /

    state: Hello
        q!: $hello *
        a: Здравствуйте!
        go!: /Can I Help You?

    state: Can I Help You?
        a: Я могу вам помочь?

        state: Yes
            q!: * { (*можете|*можешь) * помочь } *
            q: * [думаю] (да|*можете|*можешь|надеюсь|хотелось бы) *
            a: Что Вас интересует?

        state: No
            q: * [да] [уже] (ничем|не надо|не нужно) [спасибо] *
            a: Хорошо. Буду рад помочь вам в следующий раз!
```

Заметили ошибку?

Выделите текст и нажмите `Ctrl` + `Enter`, чтобы сообщить нам о ней
