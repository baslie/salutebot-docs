---
title: "Асихронная отправка сообщения боту"
source_url: "https://developers.sber.ru/docs/ru/salutebot/salutebot-chatapi/send-chat-api-message-async"
description: "Отправка запроса клиента или события в чат-приложении. В отличие от [POST /chatapi/bot/{token}](#operation/post-chatapi-token) в ответ на запрос придет только идентификатор запроса, а сообщение бота будет отправлено на вебхук, указанный в настройках канала Chat API."
reading_time: 1
breadcrumbs: ["", "Асихронная отправка сообщения боту"]
toc:
  - title: "Запрос"
    level: 2
    id: "zapros"
  - title: "Ответы"
    level: 2
    id: "responses"
---

# Асихронная отправка сообщения боту

Обновлено 29 июля 2025

Отправка запроса клиента или события в чат-приложении. В отличие от [POST /chatapi/bot/{token}](#operation/post-chatapi-token) в ответ на запрос придет только идентификатор запроса, а сообщение бота будет отправлено на вебхук, указанный в настройках канала Chat API.

## Запрос

## Ответы

200
400
404
408
500

OK

Invalid request payload

ChannelChat config not found for token {token} and channel CHATAPI

Request timeout

Internal server error

Loading...

Это полезный материал?

Заметили ошибку?
Выделите текст и нажмите
Ctrl
+
Enter
, чтобы сообщить нам об ошибке

[Отправка сообщения боту](send-chat-api-message-post.md)
[Получение асинхронных событий](get-chat-api-events.md)
