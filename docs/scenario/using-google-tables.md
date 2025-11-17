---
title: "Используем данные из Google-таблиц"
source_url: "https://github.com/baslie/salutebot-docs/blob/main/docs/scenario/using-google-tables.md"
description: "Используем данные из Google-таблиц | Разработка чат-ботов"
reading_time: 1
badges: ["SaluteBot", "Graph"]
breadcrumbs: ["SaluteBot", "Подключаем сторонние сервисы", "", "SaluteBot", "Подключаем сторонние сервисы", "Используем данные из Google-таблиц"]
---

<!-- Бейджи: SaluteBot | Graph -->

# Используем данные из Google-таблиц

Обновлено 13 декабря 2023

[![](/assets/scenario/using-google-tables/salutebot-new.png)
SaluteBot](../overview.md)[![](/assets/scenario/using-google-tables/Graph.png)
Graph](https://developers.sber.ru/docs/ru/va/graph/overview)

Если вы используете Google таблицы для хранения данных, например, списка рецептов или каталога товаров, вы можете получить их в чат-боте с помощью блока [**HTTP-запрос**](blocks/http-request.md).

Блок получает данные только с первого листа таблицы.

Для чтения данных из таблицы, к ней надо предоставить [доступ по ссылке](https://support.google.com/drive/answer/2494822?hl=ru&co=GENIE.Platform%3DDesktop) .

Для чтения данных из разных Google таблиц в зависимости от ввода пользователя:

1. Добавьте в сценарий экран с блоком [**Ввод текста**](blocks/conditions.md).

   Блок сохраняет в переменную `$table` реплику пользователя, в зависимости от которой выбирается таблица.

   ![Сохранение ввода пользователя](/assets/scenario/using-google-tables/table-reading-user-input-c91375d28b901452b00aed057a1c8508.png)
2. Добавьте экран с блоком [**Условия**](blocks/text-entry.md).

   В результате проверки условий, блок сохраняет идентификатор таблицы в переменную `$id`, которая используется при запросе данных.

   ![Блок Условия](/assets/scenario/using-google-tables/table-reading-conditions-47348ed714d02851ab013e1e591677d0.png)

   Пример условий:

   ```
   $id = ($sheet == "Таблица 1") ? "<Идентификатор первой таблицы>" : false
   $id = ($sheet == "Таблица 2") ? "<Идентификатор второй таблицы>" : false
   $id = ($sheet == "Таблица 3") ? "<Идентификатор третьей таблицы>" : false
   ```

   Идентификатор находится в веб-адресе таблицы в виде строки из букв и цифр.
3. Добавьте экран с блоком **HTTP-запрос**, который будет запрашивать данные из таблицы.

   В поле **URL** блока укажите адрес сервиса, который преобразует данные таблицы в формат JSON:

   ```
   https://smartapp-code.sberdevices.ru/tools/api/googlesheet2json?sheet=1&id=${id}
   ```

   Блок использует HTTP метод GET для обращения к таблице с помощью переменной, полученной от блока **Условия**. Результат запроса сохраняется в переменной `$content` с помощью системной переменной [`$httpResponse`](https://developers.sber.ru/docs/ru/va/graph/variables/system_variables).

   ![Параметры блока HTTP-запрос](/assets/scenario/using-google-tables/table-reading-request-3c894ec9cf81875e16186dfcd806109c.png)
4. Добавьте экран с блоком **Текст**, чтобы проверить результат чтения данных.

   В блоке укажите переменную `$content`, полученную в результате HTTP-запроса.

   ![Вывод данных таблицы](/assets/scenario/using-google-tables/table-reading-output-e48da272f00298942a6b1f48503dc56f.png)

Пример сценария чтения данных из разных Google таблиц в зависимости от ввода пользователя:

![Сценарий чтения данных из таблиц](/assets/scenario/using-google-tables/table-reading-scenario-3ed4afbc3c3c207785ac4b1a19e77916.png)

Заметили ошибку?

Выделите текст и нажмите `Ctrl` + `Enter`, чтобы сообщить нам о ней
