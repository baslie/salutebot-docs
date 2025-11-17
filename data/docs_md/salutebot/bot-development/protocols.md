---
title: "Использование протоколов шифрования"
source_url: "https://github.com/baslie/salutebot-docs/blob/main/data/docs_md/salutebot/bot-development/protocols.md"
description: "Документация для разработчиков | Разработка чат-ботов"
reading_time: 1
badges: ["SaluteBot", "Code", "Graph"]
---

<!-- Бейджи: SaluteBot | Code | Graph -->

# Использование протоколов шифрования

Обновлено 25 июня 2024

[![](/assets/salutebot/bot-development/protocols/salutebot-new.png)
SaluteBot](../overview.md)[![](/assets/salutebot/bot-development/protocols/Code.png)
Code](https://developers.sber.ru/docs/ru/va/code/overview)[![](/assets/salutebot/bot-development/protocols/Graph.png)
Graph](https://developers.sber.ru/docs/ru/va/graph/overview)

Сервис поддерживают наборы алгоритмов (cipher suits) и версию сетевого протокола TLSv1.2, отвечающие требованиям стандартов безопасности.

Протокол позволяет обнаруживать следующие риски безопасности:

* Незаконное изменение сообщений.
* Перехват сообщений.
* Подделка сообщений.

Добавьте ssl\_ciphers в блок сервера в файле ssl.conf:

```
EECDH+ECDSA+AESGCM
EECDH+aRSA+AESGCM
EECDH+ECDSA+SHA384
EECDH+ECDSA+SHA256
EECDH+aRSA+SHA384
EECDH+aRSA+SHA256
EECDH+aRSA+RC4
EECDH EDH+aRSA HIGH
```

Исключения: `!RC4 !aNULL !eNULL !LOW !3DES !MD5 !EXP !PSK !SRP !DS`.

Шифрование на уровне данных

```
AES encrypt-algorithm:
'AES/CBC/PKCS5Padding' key-algorithm: 'AES'
PBKDF2WithHmacSHA256
```

Заметили ошибку?

Выделите текст и нажмите `Ctrl` + `Enter`, чтобы сообщить нам о ней
