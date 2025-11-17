---
title: "Ответы чат-бота"
source_url: "https://github.com/baslie/salutebot-docs/blob/main/docs/bot-development/bot-answers/overview.md"
reading_time: 1
badges: ["SaluteBot", "Code"]
---

<!-- Бейджи: SaluteBot | Code -->

# Ответы чат-бота

Обновлено 13 февраля 2025

[![](/assets/bot-development/bot-answers/overview/salutebot-new.png)
SaluteBot](../../overview.md)[![](/assets/bot-development/bot-answers/overview/Code.png)
Code](https://developers.sber.ru/docs/ru/va/code/overview)

В Code вы можете создавать сообщения различных типов:

* [текстовые](https://developers.sber.ru/docs/ru/va/code/response/message-types#text);
* [подсказки в диалоге с пользователем](https://developers.sber.ru/docs/ru/va/code/response/message-types#buttons);
* [изображения](https://developers.sber.ru/docs/ru/va/code/response/message-types#image);
* [произвольные ответы](https://developers.sber.ru/docs/ru/va/code/response/message-types#raw).

Произвольные ответы позволяют передавать [команды](https://developers.sber.ru/docs/ru/va/api/smartapp-api-commands) и [действия](https://developers.sber.ru/docs/ru/va/api/smartapp-api-actions), которые соответствуют протоколу SmartApp API.

Ответы сохраняются в массиве `$response.replies` , который содержит [строго типизированные элементы](https://developers.sber.ru/docs/ru/va/code/response/message-types). Массив наполняется с помощью метода `$response.replies.push()`.

Заметили ошибку?

Выделите текст и нажмите `Ctrl` + `Enter`, чтобы сообщить нам о ней
