---
title: "Подключение классификатора"
source_url: "https://github.com/baslie/salutebot-docs/blob/main/docs/bot-development/classificator/connection-classificator.md"
reading_time: 2
badges: ["SaluteBot", "Code"]
toc:
  - title: "Настройка конфигурационного файла"
    level: 2
    id: "nastroyka-konfiguratsionnogo-fayla"
  - title: "Настройка параметров классификации"
    level: 2
    id: "nastroyka-parametrov-klassifikatsii"
  - title: "Конфигурация алгоритма классификатора"
    level: 2
    id: "konfiguratsiya-algoritma-klassifikatora"
  - title: "morphology"
    level: 3
    id: "morphology"
  - title: "tokenizer"
    level: 3
    id: "tokenizer"
  - title: "vocabulary"
    level: 3
    id: "vocabulary"
  - title: "lengthLimit, timeLimit"
    level: 3
    id: "length-limit-time-limit"
  - title: "engine"
    level: 3
    id: "engine"
  - title: "noMatchThreshold"
    level: 3
    id: "no-match-threshold"
  - title: "parameters: algorithm"
    level: 3
    id: "parameters-algorithm"
---

<!-- Бейджи: SaluteBot | Code -->

# Подключение классификатора

Содержание раздела

* [Настройка конфигурационного файла](#настройка-конфигурационного-файла)
* [morphology](#morphology)
* [tokenizer](#tokenizer)
* [vocabulary](#vocabulary)
* [lengthLimit, timeLimit](#lengthlimit-timelimit)
* [Настройка параметров классификации](#настройка-параметров-классификации)
* [engine](#engine)
* [noMatchThreshold](#nomatchthreshold)
* [parameters: algorithm](#parameters-algorithm)
* [Конфигурация алгоритма классификатора](#конфигурация-алгоритма-классификатора)

Развернуть

# Подключение классификатора

Обновлено 25 марта 2025

[![](/assets/bot-development/classificator/connection-classificator/salutebot-new.png)
SaluteBot](../../overview.md)[![](/assets/bot-development/classificator/connection-classificator/Code.png)
Code](https://developers.sber.ru/docs/ru/va/code/overview)

Ниже перечислены шаги подключения классификатора к чат-боту.

## Настройка конфигурационного файла

Первый шаг – это задание параметров в конфигурационном файле чат-бота `chatbot.yaml`.

### morphology

Позволяет выбрать библиотеку для морфологического анализа слов. Используется при обработке паттернов `~`, `$lemma`, `$morph`, а так же в функции `$nlp.parseMorph`.

Укажите одну из библиотек:

* `aot` — используется библиотека от [AOT.ru](http://www.aot.ru/technology.html) ;
* `default` — используется стандартная библиотека, наиболее подходящий анализатор для русского языка.
* `pyMorphy` — используется библиотека pyMorphy, наиболее качественный анализатор для русского языка.

### tokenizer

Токенизатор позволяет задать правила, используемые для разбиения текста на слова.

Поддерживаемые типы токенизаторов:

* `regexp` — простой токенизатор на регулярных выражениях.
* `srx` — конфигурируемый токенизатор на базе [настраиваемых правил сегментации](https://en.wikipedia.org/wiki/Segmentation_Rules_eXchange) . При указании данного токенизатора потребуется указать файл грамматики в параметре `srxPath`.
* `default` — способ сегментации по умолчанию. Является предпочтительной опцией при совместном использовании паттернов и классификатора.

### vocabulary

Словарь весов слов по ранжированию паттернов. По умолчанию: `common-vocabulary.json`.

### lengthLimit, timeLimit

Позволяет изменить лимиты на размер входящего сообщения и на время обработки nlp-модуля.

Параметры по умолчанию:

```
nlp:
    lengthLimit:
        enabled: true
        symbols: 400
        words: 100000
    timeLimit:
        enabled: true
        timeout: 10000
```

Для `lengthLimit`:

* `symbols` — устанавливает лимит на количество символов во входящем сообщении. При превышении этого лимита сработает событие `lengthLimit`, которое может быть обработано в сценарии чат-бота тегом `event: lengthLimit`.
* `words` — устанавливает лимит на количество слов во входящем сообщении. При превышении этого лимита сработает событие `lengthLimit`, которое может быть обработано в сценарии чат-бота тегом `event: lengthLimit`.

Счетчик `words` приравнивает символы `! , . : ; ?" ' ( ) * / [ \ ] { | }` к словам, учитывайте это при указании лимита.

Для `timeLimit`:

* `timeout` — устанавливает максимальное время обработки запроса в nlp-модуле в миллисекундах. При превышении этого лимита сработает событие `timeLimit`, которое может быть обработано в сценарии чат-бота тегом `event: timeLimit`.

Пример nlp-модуля:

```
nlp:                                    // параметры для nlp-функции платформы
  morphology: default                   // библиотека для морфологического анализа слов
  tokenizer: default                   // токенизатор, задает правила для разбиения текста на слова
  vocabulary: common-vocabulary.json    // словарь весов слов для ранжирования паттернов
  lengthLimit:
    enabled: true
    symbols: 400                        // лимит на количество символов во входящем сообщении
    words: 100000                       // лимит на количество слов во входящем сообщении
  timeLimit:
    enabled: true
    timeout: 10000                      // максимальное время обработки запроса в nlp-модуле в миллисекундах
```

## Настройка параметров классификации

Второй шаг — это задание параметров классификации.

### engine

Тип классификатора, по умолчанию `sts`.

### noMatchThreshold

Значение нижнего порога похожести, при котором нужно считать фразы непохожими. В ходе разработки классификатора было эмпирически определено, что оптимальное значение этого параметра `0.2`.

### parameters: algorithm

Тип используемого алгоритма классификации. Используется `match-aligner` — основной тип для sts-классификатора. Также вы можете использовать `aligner` и `aligner2` — альтернативная реализация алгоритма классификации.

## Конфигурация алгоритма классификатора

Третий шаг — это конфигурация алгоритма классификатора. По умолчанию все параметры уже настроены. Необходимо только указать словарь весов, который совпадает со словарем из блока `nlp`. По умолчанию: `common-vocabulary.json`.

Пример конфигурационного файла `chatbot.yaml` с подключенным классификатором:

```
name: demo

entryPoint:
  - main.sc

tests:
  exclude:
    - tests.xml

messages:
    onError:
        defaultMessage: Ой, кажется, что-то пошло не так.
        locales:
            ru: Ой, кажется, что-то пошло не так.

nlp:                                    // параметры для nlp-функции платформы
  morphology: default                   // библиотека для морфологического анализа слов
  tokenizer: default                    // токенизатор, задает правила для разбиения текста на слова
  vocabulary: common-vocabulary.json    // словарь весов слов для ранжирования паттернов
  lengthLimit:
    enabled: true
    symbols: 400                        // лимит на количество символов во входящем сообщении
    words: 100000                       // лимит на количество слов во входящем сообщении
  timeLimit:
    enabled: true
    timeout: 10000                      // максимальное время обработки запроса в nlp-модуле в миллисекундах

classifier:                             // параметры для классификатора
  enable: true
  engine: sts                           // тип классификатора
  noMatchThreshold: 0.2
  parameters:
    algorithm: aligner2                 // алгоритм классификации

aligner:
  vocabulary: common-vocabulary.json

exampleGroups:
    - src/dictionaries/examples.json    // указывается при использовании группы примеров
```

Заметили ошибку?

Выделите текст и нажмите `Ctrl` + `Enter`, чтобы сообщить нам о ней
