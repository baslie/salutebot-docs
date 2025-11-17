---
title: "Файлы JavaScript библиотек"
source_url: "https://github.com/baslie/salutebot-docs/blob/main/docs/bot-development/project-structure/js.md"
description: "Документация для разработчиков | Разработка чат-ботов"
reading_time: 1
badges: ["SaluteBot", "Code"]
---

<!-- Бейджи: SaluteBot | Code -->

# Файлы JavaScript библиотек

Обновлено 15 декабря 2023

[![](/assets/bot-development/project-structure/js/salutebot-new.png)
SaluteBot](../../overview.md)[![](/assets/bot-development/project-structure/js/Code.png)
Code](https://developers.sber.ru/docs/ru/va/code/overview)



---

`.js` — файлы js-библиотек.

Содержат JavaScript-код, который можно использовать в файлах сценариев. Содержат функции, логику обработки запросов, вызовы внешних систем, работу с памятью и пр.

`.js`-файлы подгружаются в начале сценария при помощи тега `require`:

```
require: scripts/functions.js
```

[Подробнее о работе с тегом `require`](https://developers.sber.ru/docs/ru/va/code/sa-dsl/tags/declarative-tags#require)

Заметили ошибку?

Выделите текст и нажмите `Ctrl` + `Enter`, чтобы сообщить нам о ней
