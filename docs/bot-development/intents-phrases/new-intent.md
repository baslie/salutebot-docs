---
title: "Создание интента"
source_url: "https://github.com/baslie/salutebot-docs/blob/main/docs/bot-development/intents-phrases/new-intent.md"
description: "Документация для разработчиков | Разработка чат-ботов"
reading_time: 1
badges: ["SaluteBot", "Code", "Brain"]
toc:
  - title: "Подключение SmartApp Brain"
    level: 2
    id: "podklyuchenie-smart-app-brain"
  - title: "Создание интента"
    level: 2
    id: "sozdanie-intenta1"
  - title: "Заполнение слотов для интента"
    level: 3
    id: "zapolnenie-slotov-dlya-intenta"
  - title: "Экспорт и импорт интентов"
    level: 3
    id: "eksport-i-import-intentov"
---

<!-- Бейджи: SaluteBot | Code | Brain -->

# Создание интента

Содержание раздела

* [Подключение SmartApp Brain](#подключение-smartapp-brain)
* [Создание интента](#создание-интента)
* [Заполнение слотов для интента](#заполнение-слотов-для-интента)
* [Экспорт и импорт интентов](#экспорт-и-импорт-интентов)

# Создание интента

Обновлено 25 июня 2024

[![](/assets/bot-development/intents-phrases/new-intent/salutebot-new.png)
SaluteBot](../../overview.md)[![](/assets/bot-development/intents-phrases/new-intent/Code.png)
Code](https://developers.sber.ru/docs/ru/va/code/overview)[![](/assets/bot-development/intents-phrases/new-intent/Brain.png)
Brain](https://developers.sber.ru/docs/ru/va/code/nlp/overview)

Интент — ключевая единица NLU-сервиса, объединяющая в себе набор фраз, намерение пользователя и другую метаинформацию.

Подробнее об [использовании интентов в сценарии](https://developers.sber.ru/docs/ru/va/code/sa-dsl/tags/intents-tags), [определении интентов](https://developers.sber.ru/docs/ru/va/chat/voice-interface/command-recognition/intent-detection) и [настройке правил активации](https://developers.sber.ru/docs/ru/va/chat/voice-interface/command-recognition/rule_activation).





## Подключение SmartApp Brain

Чтобы использовать в своем чат-боте интенты и [сущности](https://developers.sber.ru/docs/ru/va/code/nlp/entities/overview), вам нужно подключить в проект SmartApp Brain.

Для этого укажите в конфигурационном файле [`chatbot.yaml`](https://developers.sber.ru/docs/ru/salutebot/bot-steps/project-structure/configuration_file) параметры:

```
language: ru
botEngine: v2

sts:
    noMatchThreshold: 0.2
caila:
    noMatchThreshold: 0.2
```

Где:

* `language` — язык [классификатора](https://developers.sber.ru/docs/ru/va/code/nlp/classificator/overview). Возможные значения: `ru` — русский, `en` — английский.
* `noMatchThreshold` — порог срабатывания классификатора. Число в диапазоне от 0 до 1. Значение по умолчанию `0.2`. Если классификатор не может отнести фразу ни к одному из классов с заданной степенью уверенности, создается событие [`event: noMatch`](https://developers.sber.ru/docs/ru/va/chat/voice-interface/command-recognition/intent-detection).

SmartApp Brain подключен во всех проектах по умолчанию.

## Создание интента

Войдите в проект, на панели управления нажмите *Редактор* > *Интенты*. Вы перешли в справочник интентов для проекта.

Нажмите *Создать интент*. Заполните поля:

* *Название* — укажите название интента. Полный путь интента рассчитывается автоматически и отображается под полем ввода, он используется при обращении к интенту из сценария.
* *Описание* — укажите дополнительное описание или комментарий.
* *Ответ* — укажите стандартный ответ на интент. Вы можете обратиться к нему из сценария как `$context.intent.answer`.
* *Тренировочные фразы* — укажите примеры тренировочных фраз для распознавания данного интента.

Вы можете также создать вложенный интент. Уровень вложенности интентов не ограничен.

Интенты формирую дерево на правой панели. Узлы дерева отсортированы в лексикографическом порядке. Для каждого узла указывается число примеров фраз в данном интенте и через символ `/` число всех дочерних фраз.



### Заполнение слотов для интента

*Slots (слоты)* — данные, которые клиент передает с запросом или в процессе дозапроса. У каждого слота есть обязательные атрибуты: Имя, Тип.

Подробнее о процессе дозапроса информации [Slot filling](../slot-filling/overview.md).

Для заполнения слотов нажмите *Добавить слот*. Заполните поля:

* *Название* — название слота.
* *Сущность* — выберите из списка сущность, [определяющую тип данных](https://developers.sber.ru/docs/ru/va/code/nlp/slot-filling/fields), которые попадут в слот. Вы можете использовать как [системные, так и кастомные сущности](https://developers.sber.ru/docs/ru/va/chat/voice-interface/command-recognition/entities/custom-entities).
* *Обязательно* — переведите переключатель в активное положение, если слот является обязательным для заполнения.
* *Массив* — переведите переключатель в активное положение, чтобы в слот помещались все сущности данного типа, оформленные как массив.
* *Вопросы* — укажите вопросы, которые будут использованы при процессе *Slot filling*.



### Экспорт и импорт интентов

Для экспорта интентов перейдите к списку проектов > напротив проекта нажмите иконку

![downoload](/assets/bot-development/intents-phrases/new-intent/base64_4_cec747b0.png)
. В экспортированном архиве в файле `caila_import.json` все данные проекта по работе с NLU-ядром Brain.



Вы можете использовать этот архив или отдельные файлы для загрузки в новый проект.

Для этого создайте проект нажмите иконку

![more](/assets/bot-development/intents-phrases/new-intent/base64_5_737761be.png)
> *Загрузить* > выберите архив проекта.

Также вы можете импортировать интенты на странице *Интенты*. Для этого сформируйте `.json` файл следующего формата:

```
{
    "classes": [
        {
            "path": "/PlayGames/Games", // путь к интенту
            "description": "", // описание
            "disabled": false, // при `false` интент активен
            "phrases": [
                "давай поиграем в какие-нибудь игры" // тренировочные фразы
            ]
        },
        {
            "path": "/PlayGames/Games/CanYouPlay",
            "description": "",
            "disabled": false,
            "phrases": ["ты умеешь во что-нибудь играть?", "ты знаешь какие-нибудь игры?", "ты знаешь как играть?"]
        }
    ]
}
```

Вверху дерева интентов нажмите *Импорт* > загрузите файл.

Заметили ошибку?

Выделите текст и нажмите `Ctrl` + `Enter`, чтобы сообщить нам о ней
