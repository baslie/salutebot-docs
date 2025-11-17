---
title: "Используем код на JavaScript"
source_url: "https://developers.sber.ru/docs/ru/salutebot/scenario/blocks/jscode"
description: "Блок JS Код для чат-ботов | Разработка чат-ботов"
reading_time: 1
badges: ["SaluteBot", "Graph", "Code"]
breadcrumbs: ["SaluteBot", "Настраиваем сценарий", "", "SaluteBot", "Настраиваем сценарий", "Используем код на JavaScript"]
---

<!-- Бейджи: SaluteBot | Graph | Code -->

# Используем код на JavaScript

Обновлено 19 сентября 2024

[![](/assets/scenario/blocks/jscode/salutebot-new.png)
SaluteBot](../../overview.md)[![](/assets/scenario/blocks/jscode/Graph.png)
Graph](https://developers.sber.ru/docs/ru/va/graph/overview)[![](/assets/scenario/blocks/jscode/Code.png)
Code](https://developers.sber.ru/docs/ru/va/code/overview)

Блок **JS код** предназначен для выполнения в сценарии произвольного кода на JavaScript.

Код требуется указывать в поле **JS Код**.

В отличие от других блоков при обращении к переменным в JavaScript-коде блока **JS Код** необходимо указывать полный путь переменной:

```
$session.<название переменной>
```

Логику, заданную с помощью блока **Код**, также можно реализовать с помощью тега [`script`](https://developers.sber.ru/docs/ru/va/code/sa-dsl/tags/reaction-tags#teg-script) Code.

Заметили ошибку?

Выделите текст и нажмите `Ctrl` + `Enter`, чтобы сообщить нам о ней
