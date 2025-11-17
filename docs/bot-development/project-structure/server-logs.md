---
title: "Логи сервера"
source_url: "https://developers.sber.ru/docs/ru/salutebot/bot-development/project-structure/server-logs"
description: "Документация для разработчиков | Разработка чат-ботов"
reading_time: 1
badges: ["SaluteBot", "Code"]
toc:
  - title: "Просмотр логов"
    level: 2
    id: "prosmotr-logov"
  - title: "Фильтрация и очистка логов"
    level: 2
    id: "filtratsiya-i-ochistka-logov"
---

<!-- Бейджи: SaluteBot | Code -->

# Логи сервера

Содержание раздела

* [Просмотр логов](#просмотр-логов)
* [Фильтрация и очистка логов](#фильтрация-и-очистка-логов)

# Логи сервера

Обновлено 15 декабря 2023

[![](/assets/bot-development/project-structure/server-logs/salutebot-new.png)
SaluteBot](../../overview.md)[![](/assets/bot-development/project-structure/server-logs/Code.png)
Code](https://developers.sber.ru/docs/ru/va/code/overview)

В логи сервера автоматически попадают сообщения, которые принимает и передает чат-бот, запущенный в канале распространения или в [тестовом виджете](../../testing/testing-debugging.md).

## Просмотр логов

Чтобы открыть панель с логами, нажмите кнопку **Логи** в левом нижнем углу рабочей области Code.

Логи сервера доступны на любой вкладке, внутри вкладки **Разработка**.

![Логи сервера в редакторе сценариев](/assets/bot-development/project-structure/server-logs/server-logs-2d13e0fe79bf7865ac2dd8c2a0c2ff47.png)

Используйте функцию [`log(message)`](https://developers.sber.ru/docs/ru/va/code/js-api/functions/log-message), чтобы выводить в логи произвольные сообщения. Произвольные сообщения помогают при отладке скриптов, встроенных в файлы сценариев.

## Фильтрация и очистка логов

Используйте фильтр **Все логгеры**, чтобы отфильтровать логи по источнику.

Используйте фильтр **Все события**, чтобы отфильтровать логи по уровню детализации (от `info` до `critical`).

Чтобы очистить префиксы записей, нажмите кнопку

![Очищать префиксы](/assets/bot-development/project-structure/server-logs/base64_4_5347b7d6.png)
.

Чтобы полностью очистить окно вывода логов, нажмите кнопку

![Очистить](/assets/bot-development/project-structure/server-logs/base64_5_a0faca0d.png)
.

Заметили ошибку?

Выделите текст и нажмите `Ctrl` + `Enter`, чтобы сообщить нам о ней
