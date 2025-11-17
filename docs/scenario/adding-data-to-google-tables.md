---
title: "Добавляем данные в Google-таблицу"
source_url: "https://github.com/baslie/salutebot-docs/blob/main/docs/scenario/adding-data-to-google-tables.md"
description: "Добавляем данные в Google-таблицу | Разработка чат-ботов"
reading_time: 1
badges: ["SaluteBot", "Graph"]
breadcrumbs: ["SaluteBot", "Подключаем сторонние сервисы", "", "SaluteBot", "Подключаем сторонние сервисы", "Добавляем данные в Google-таблицу"]
toc:
  - title: "Предварительная настройка Google-таблицы"
    level: 2
    id: "predvaritelnaya-nastroyka-google-tablitsy"
  - title: "Добавление скрипта для работы с данными"
    level: 2
    id: "dobavlenie-skripta-dlya-raboty-s-dannymi"
  - title: "Создание HTTP-запроса к Google-таблице (POST)"
    level: 2
    id: "sozdanie-http-zaprosa-k-google-tablitse-post"
---

<!-- Бейджи: SaluteBot | Graph -->

# Добавляем данные в Google-таблицу

Содержание раздела

* [Предварительная настройка Google-таблицы](#предварительная-настройка-google-таблицы)
* [Добавление скрипта для работы с данными](#добавление-скрипта-для-работы-с-данными)
* [Создание HTTP-запроса к Google-таблице (POST)](#создание-http-запроса-к-google-таблице-post)

# Добавляем данные в Google-таблицу

Обновлено 7 октября 2025

[![](/assets/scenario/adding-data-to-google-tables/salutebot-new.png)
SaluteBot](../overview.md)[![](/assets/scenario/adding-data-to-google-tables/Graph.png)
Graph](https://developers.sber.ru/docs/ru/va/graph/overview)

## Предварительная настройка Google-таблицы

Для добавления данных в Google-таблицу предварительно настройте доступы. Для этого перейдите в таблицу и в правом верхнем углу выберите **Настройки доступа**. В параметрах доступа укажите **Все, у кого есть ссылка**.

## Добавление скрипта для работы с данными

Добавьте функцию получения данных и декодирования строковых переменных.

Для этого:

1. Выберите в Google-таблице пункт меню **Расширения** и далее - **Apps Script**.
2. Напишите функцию для обработки полученных данных.

В примере ниже в качестве данных передается три переменные:

* `userName` – строковый тип данных;
* `userLastname` – строковый тип данных;
* `phone` – целый тип данных.

Текст функции:

```
function doPost(request) {
  const {userName,userLastname,phone} = request.parameter    //получение параметров
  const sheet = SpreadsheetApp.getActiveSheet() //получение активного листа
  const lastRow = sheet.getLastRow() + 1        //получение последней строчки таблицы

  sheet.getRange(`A${lastRow}`).setValue(userName) //вывод значения переменной userName в столбец А
  sheet.getRange(`B${lastRow}`).setValue(userLastname) //вывод значения переменной userLastname в столбец B
  sheet.getRange(`C${lastRow}`).setValue(phone)    //вывод значения переменной phone в столбец C

  return 0
}
```

3. Нажмите **Начать развертывание** и далее — **Новое развертывание**.

Каждое изменение функции требует новое развертывание.

4. Выберите тип развертывания - **Веб-приложение**.
5. При появлении окна с запросом доступа нажмите **Предоставить доступ**.
6. Нажмите **Начать развертывание**.
7. Скопируйте URL в поле **Веб-приложение**. Ссылка имеет следующий вид: `https://script.google.com/macros/s/AKf....`.
8. Добавьте к скопированной ссылке параметры и присвойте значения переменным:

```
https://script.google.com/macros/s/AKf...?userName={{$session.userName}}&userLastname={{$session.userLastname}}&phone={{$session.phone}}
```

## Создание HTTP-запроса к Google-таблице (POST)

1. Перейдите в личный кабинет Studio и откройте проект SaluteBot на инструменте Graph.
2. Добавьте в проект блоки для ввода имени, фамилии и телефона.
3. На отдельный экран добавьте блок **JS-код** для кодирования строковых переменных и вставьте туда следующий код:

```
$session.userName = encodeURI($session.userName);
$session.userLastname = encodeURI($session.userLastname)
```

4. На этот же экран добавьте блок **HTTP-запрос**.
5. В поле URL вставьте ранее полученную ссылку.

В результате данные, полученные из чат-бота, будут добавлены в Google-таблицу.

Заметили ошибку?

Выделите текст и нажмите `Ctrl` + `Enter`, чтобы сообщить нам о ней
