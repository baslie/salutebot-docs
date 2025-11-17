---
title: "Именованные сущности"
source_url: "https://github.com/baslie/salutebot-docs/blob/main/data/docs_md/salutebot/bot-development/entities/named-entity.md"
description: "Документация для разработчиков | Разработка чат-ботов"
reading_time: 1
badges: ["SaluteBot", "Code"]
toc:
  - title: "Элементы справочника именованных сущностей"
    level: 2
    id: "elementy-spravochnika-imenovannyh-sushnostey"
---

<!-- Бейджи: SaluteBot | Code -->

# Именованные сущности

Содержание раздела

* [Элементы справочника именованных сущностей](#элементы-справочника-именованных-сущностей)

# Именованные сущности

Обновлено 13 февраля 2025

[![](/assets/salutebot/bot-development/entities/named-entity/salutebot-new.png)
SaluteBot](../../overview.md)[![](/assets/salutebot/bot-development/entities/named-entity/Code.png)
Code](https://developers.sber.ru/docs/ru/va/code/overview)

Именованная сущность — это слово или словосочетание, которое выделяет предмет или являение в ряде аналогичных предметов или явлений. Примерами именованных сущностей являются названия городов, стран, валют.

В сценарии чат-бота именованная сущность представляет собой [именованный паттерн](https://developers.sber.ru/docs/ru/va/code/nlp/patterns/named-patterns), заданный при помощи [справочника именованных сущностей](https://developers.sber.ru/docs/ru/va/code/project/csv).

## Элементы справочника именованных сущностей

Чтобы использовать элементы справочника именованных сущностей в именованном паттерне:

1. Указать название справочника и путь к нему в файле сценария `.sc`. Для этого используйте тег [`require`](https://developers.sber.ru/docs/ru/va/code/sa-dsl/tags/declarative-tags#require):

```
require: common/common-cities.csv
         name = RoamingRegions
         var = RoamingRegions
```

2. Задайте в файле `.js`-библиотек конвертер. Конвертер позволяет записывать информацию в поле `value` дерева разбора `parseTree` для паттерна. Например:

```
function RoamingRegionTagConverter($parseTree) {
    var id = $parseTree.RoamingRegions[0].value;
    return RoamingRegions[id].value;
}
```

Здесь:

* `RoamingRegionTagConverter` — название конвертера;
* `RoamingRegions` — название справочника именованных сущностей.

Возвращаемое значение записывается в поле `value`.

1. Объявить именованный паттерн. Используйте `$entity<>`:

```
$roamingRegion = $entity<RoamingRegions> || converter = RoamingRegionTagConverter
```

Именованные сущности можно использовать и без объявления именованного паттерна.

При подобном объявлении именованной сущности в `$parseTree` появляется элемент `value`, куда записывается id.

Заметили ошибку?

Выделите текст и нажмите `Ctrl` + `Enter`, чтобы сообщить нам о ней
