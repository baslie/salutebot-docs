---
title: "Слот-филлинг"
source_url: "https://developers.sber.ru/docs/ru/salutebot/bot-development/slot-filling/overview"
description: "Слот-филлинг для чат-ботов | Разработка чат-ботов"
reading_time: 1
badges: ["SaluteBot", "Code"]
---

<!-- Бейджи: SaluteBot | Code -->

# Слот-филлинг

Обновлено 15 декабря 2023

[![](/assets/bot-development/slot-filling/overview/salutebot-new.png)
SaluteBot](../../overview.md)[![](/assets/bot-development/slot-filling/overview/Code.png)
Code](https://developers.sber.ru/docs/ru/va/code/overview)

Слот-филлинг (англ. slot filling) — процесс дозапроса данных для выполнения запроса пользователя. Полученные при дозапросе данные доступны в сценарии.

Слоты (англ. slots) — данные, которые клиент передает с запросом или в процессе дозапроса. У каждого слота есть обязательные атрибуты: `Имя`, `Тип`.

Модуль слот-филлинга подключается в [файле основного сценария](https://developers.sber.ru/docs/ru/va/code/project/sc) с помощью тега [`require`](https://developers.sber.ru/docs/ru/va/code/sa-dsl/tags/declarative-tags#require2):

```
require: slotfilling/slotFilling.sc
  module = sys.zb-common
```

Заметили ошибку?

Выделите текст и нажмите `Ctrl` + `Enter`, чтобы сообщить нам о ней
