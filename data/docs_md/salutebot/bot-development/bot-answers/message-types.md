---
title: "Типы сообщений"
source_url: "https://github.com/baslie/salutebot-docs/blob/main/data/docs_md/salutebot/bot-development/bot-answers/message-types.md"
description: "Документация для разработчиков | Разработка чат-ботов"
reading_time: 1
badges: ["SaluteBot", "Code"]
toc:
  - title: "text"
    level: 2
    id: "text"
  - title: "buttons"
    level: 2
    id: "buttons"
  - title: "image"
    level: 2
    id: "image"
  - title: "raw"
    level: 2
    id: "raw"
  - title: "Параметры"
    level: 3
    id: "parametry8"
  - title: "Синтаксис"
    level: 3
    id: "sintaksis18"
  - title: "Использование в сценарии"
    level: 3
    id: "ispolzovanie-v-stsenarii15"
  - title: "Параметры"
    level: 3
    id: "parametry13"
  - title: "Синтаксис"
    level: 3
    id: "sintaksis1"
  - title: "Использование в сценарии"
    level: 3
    id: "ispolzovanie-v-stsenarii1"
  - title: "Параметры"
    level: 3
    id: "parametry22"
  - title: "Синтаксис"
    level: 3
    id: "sintaksis22"
  - title: "Использование в сценарии"
    level: 3
    id: "ispolzovanie-v-stsenarii22"
  - title: "Параметры"
    level: 3
    id: "parametry32"
  - title: "Синтаксис"
    level: 3
    id: "sintaksis32"
  - title: "Ответ на ошибочный запрос"
    level: 3
    id: "otvet-na-oshibochnyy-zapros"
---

<!-- Бейджи: SaluteBot | Code -->

# Типы сообщений

Содержание раздела

* [text](#text)
* [Параметры](#параметры)
* [Синтаксис](#синтаксис)
* [Использование в сценарии](#использование-в-сценарии)
* [buttons](#buttons)
* [Параметры](#параметры)
* [Синтаксис](#синтаксис)
* [Использование в сценарии](#использование-в-сценарии)
* [image](#image)
* [Параметры](#параметры)
* [Синтаксис](#синтаксис)
* [Использование в сценарии](#использование-в-сценарии)
* [raw](#raw)
* [Параметры](#параметры)
* [Синтаксис](#синтаксис)
* [Ответ на ошибочный запрос](#ответ-на-ошибочный-запрос)

Развернуть

# Типы сообщений

Обновлено 13 февраля 2025

[![](/assets/salutebot/bot-development/bot-answers/message-types/salutebot-new.png)
SaluteBot](../../overview.md)[![](/assets/salutebot/bot-development/bot-answers/message-types/Code.png)
Code](https://developers.sber.ru/docs/ru/va/code/overview)

## text

Простой текстовый ответ, каждый элемент выводится отдельным сообщением.

### Параметры

* `text` — текст ответа, который будет показан в диалоге;
* `tts` — задает голосовую реплику чат-бота без разметки синтеза речи;

### Синтаксис

```
{
    "type": "text",
    "text": "string",
    "tts": "string",
}
```

В тексте ответа можно использовать подстановки и функции, в рамках тега `a:` и в `$reaction.answer`. Внутри скобок `{{ }}` может находиться любое валидное выражение на JavaScript, можно использовать те же переменные и функции, что и в скриптах.

### Использование в сценарии

Добавление ответа в `$response`:

```
script: var reply = {
    type: 'text',
    text: 'мой ответ',
};
$response.replies = $response.replies || [];
$response.replies.push(reply);
```

Модификация ответов. В примере используется [`postProcess`](https://developers.sber.ru/docs/ru/va/code/js-api/pre-post-process). Если ответ повторяется, чат-бот заменит его на фразу «Что-то я повторяюсь».

```
init:
    bind("postProcess", function($context) {
        var currentAnswer = $context.response.replies.reduce(function(allAnswers, reply) {
            allAnswers += reply.type === "text" ? reply.text : "";
            return allAnswers;
        },"");

        if ($context.session.lastAnswer === currentAnswer) {
            $context.response.replies = [
            {
                "type":"text",
                "text":"Что-то я повторяюсь"
            }
            ];
        }
        $context.session.lastAnswer = currentAnswer;
    });

theme: /
    state:
        q!: как твои дела
        a: У меня все хорошо!
        a: А у тебя как?
```

## buttons

Тип ответа `buttons` добавляет кнопки в чат с пользователем.

Кнопки могут содержать ссылки на внешние адреса или на [состояния сценария чат-бота](https://developers.sber.ru/docs/ru/va/code/sa-dsl/tags/declarative-tags).

Чтобы отключить возможность вводить текст в чате с ботом, укажите параметр `"force_reply": "true"`. Отключение ввода текста работает только при запуске бота в чате Jivo. Проверить отключение ввода текста в тестовом виджете нельзя.

### Параметры

* `text` — название кнопки.
* `url` — ссылка.
* `force_reply` — отключает ввод текста.

### Синтаксис

```
{
    "type": "buttons",
    "buttons": [
        {
            "text": "Переход по адресу",
            "url": "https://example.com",
            "force_reply": true
        },
        {
            "text": "Другая кнопка"
        }
    ]
}
```

Чтобы добавить переход к состоянию чат-бота, данные тега `buttons` должны соответствовать шаблону `<json-node> -> <string>`. В левой части валидный JsonNode — строка или объект, определяющие название подсказки. В правой части — строка, определяющая путь до [состояния](https://developers.sber.ru/docs/ru/va/code/sa-dsl/tags/declarative-tags), в которое перейдет чат-бот по нажатию кнопки.

```
 state: Buttons
        q!: * start
        a: Подсказка внизу экрана
        buttons:
            "Название подсказки" -> /NormalButtons/2   //после стрелки указывается путь до состояния, в которое будет совершен переход
```

Кнопки могут содержать подстановку параметров в имени и указанном пути для перехода.

```
 state: Buttons
        q!: * start
        a: Подстановка параметров в подсказках:
        buttons:
            "Имя кнопки" -> /NormalButtons/2
            "подстановка параметров как в {{ 'имени' }} так и в пути для перехода" -> {{ './3' }}
```

Переход на внешний адрес задается в подсказке следующим образом:

```
state:
  a: Нажмите кнопку, чтобы перейти на адрес
  buttons:
    {text:"Перейти", "url": "https://example.com"}
```

Отключение ввода текста в чате с пользователем:

```
state:
  a: Нажмите кнопку. Сейчас вы не можете писать в чате.
  buttons:
    {text:"Перейти", "url": "https://example.com", "force_reply": "true"}
```

### Использование в сценарии

Две кнопки с переходом к состоянию чат-бота и переходом на внешний адрес (ввод текста отключен):

```
state:
  a: Текст сообщения
  buttons:
    "Привет" -> ../Hello
    {"text":"Отправить контакты", "url": "https://example.com"}
    {"text":"Продолжить", "force_reply": "true"}
```

Подсказки заданные с помощью тега `script`:

```
script: var reply = {
    type: 'buttons',
    buttons: [
        {
            text: 'Переход по адресу',
            url: 'https://example.com',
            force_reply: true //отключение ввода текста в чате с пользователем
        },
        {
            text: 'Переход к стейту',
        },
    ],
};
$response.replies = $response.replies || [];
$response.replies.push(reply);
```

## image

Вывод изображения.

### Параметры

* `imageUrl` — веб-адрес изображения из раздела **Контент**.
* `hash` — хэш изображения из раздела **Контент**.

### Синтаксис

```
{
    "type": "image",
    "imageUrl": "веб-адрес изображения из раздела Контент",
    "hash": "хэш изображения из раздела Контент"
}
```

### Использование в сценарии

```
script: $response.replies = $response.replies || [];
$response.replies.push({
    type: 'image',
    imageUrl: 'https://testimageurl.jpg',
    hash: '5debe321a4cc700c9ba138edd5e98f71',
});
```

## raw

Используется для передачи настраиваемого типа ответа.

Тестовый виджет не отображает ответы с типом `raw`, если они передаются с помощью `$context.response.replies`.

### Параметры

* `body` — тело ответа, содержание которого будет добавлено в поле `payload` протокола чат-бота. Параметры, идентифицирующие пользователя, подставляются автоматически.

### Синтаксис

```
{
  "type":"raw",            //тип сообщения
  "body":{ ... },          //тело ответа
}
```

### Ответ на ошибочный запрос

Если чат-бот запущен по ошибке и не знает ответа запрос, вы можете сообщить об этом с помощью пустого сообщения [`NOTHING_FOUND`](https://developers.sber.ru/docs/ru/va/api/smartapp-api-responses#nothing-found).

```
$response.replies = $response.replies || [];
$response.replies.push({
    type: 'raw',
});
```

Заметили ошибку?

Выделите текст и нажмите `Ctrl` + `Enter`, чтобы сообщить нам о ней
