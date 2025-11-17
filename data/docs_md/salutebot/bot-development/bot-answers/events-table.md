---
title: "Типы событий event"
source_url: "https://github.com/baslie/salutebot-docs/blob/main/data/docs_md/salutebot/bot-development/bot-answers/events-table.md"
description: "Документация для разработчиков | Разработка чат-ботов"
page_type: "reference"
reading_time: 1
badges: ["SaluteBot", "Code"]
toc:
  - title: "Общие события"
    level: 2
    id: "obshie-sobytiya"
  - title: "События STS классификатора"
    level: 2
    id: "sobytiya-sts-klassifikatora"
  - title: "События чат-бота"
    level: 2
    id: "sobytiya-chat-bota"
---

<!-- Бейджи: SaluteBot | Code -->

# Типы событий event

Содержание раздела

* [Общие события](#общие-события)
* [События STS классификатора](#события-sts-классификатора)
* [События чат-бота](#события-чат-бота)

# Типы событий event

Обновлено 29 сентября 2025

[![](/assets/salutebot/bot-development/bot-answers/events-table/salutebot-new.png)
SaluteBot](../../overview.md)[![](/assets/salutebot/bot-development/bot-answers/events-table/Code.png)
Code](https://developers.sber.ru/docs/ru/va/code/overview)

[`event`](https://developers.sber.ru/docs/ru/va/code/sa-dsl/tags/declarative-tags) — реакция на событие, приходящее от чат-бота.





## Общие события

| **event** | Описание |
| --- | --- |
| `sessionDataSoftLimitExceeded` | [Достижение soft лимита сохранения данных в объект `$session`](https://developers.sber.ru/docs/ru/va/code/js-api/overflow-session-client-data) |
| `clientDataSoftLimitExceeded` | [Достижение soft лимита сохранения данных в объект `$client`](https://developers.sber.ru/docs/ru/va/code/js-api/overflow-session-client-data) |
| `sessionDataHardLimitExceeded` | [Достижение hard лимита сохранения данных в объект `$session`](https://developers.sber.ru/docs/ru/va/code/js-api/overflow-session-client-data) |
| `clientDataHardLimitExceeded` | [Достижение hard лимита сохранения данных в объект `$client`](https://developers.sber.ru/docs/ru/va/code/js-api/overflow-session-client-data) |






## События STS классификатора

| **event** | Описание |
| --- | --- |
| `match` | Отправленный текст распознан |
| `noMatch` | Отправленный текст не распознан |
| `timeLimit` | Превышение лимита на время обработки запроса |
| `lengthLimit` | Превышение лимита на количество символов |

## События чат-бота

| **event** | Описание |
| --- | --- |
| `uploadedAttachment` | Получен файл |
| `AGENT_LEFT` | Оператор закрыл чат |
| `noOperatorOnline` | Оператор не в сети |

Заметили ошибку?

Выделите текст и нажмите `Ctrl` + `Enter`, чтобы сообщить нам о ней
