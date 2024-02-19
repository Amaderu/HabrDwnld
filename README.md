# habrArticleSrcDownloader

Скрипт python3 для скачивания исходников статей с [habr](https://habr.com/).


### Использование:
```
usage: main.py [-h] [-q] [-l] [-i] (-u USER_NAME_FOR_ARTICLES | -f USER_NAME_FOR_FAVORITES | -s ARTICLE_ID)

Скрипт для скачивания статей с https://habr.com/

options:
  -h, --help            show this help message and exit
  -q, --quiet           Quiet mode
  -l, --local-pictures  Использовать абсолютный путь к изображениям в сохранённых файлах
  -i, --meta-information
                        Добавить мета-информацию о статье в файл
  -u USER_NAME_FOR_ARTICLES
                        Скачать статьи пользователя
  -f USER_NAME_FOR_FAVORITES
                        Скачать закладки пользователя
  -s ARTICLE_ID         Скачать одиночную статью
```

Например:

```bash
./src/main.py -u habr
```
```bash
./src/main.py -f habr
```
```bash
./src/main.py -s 792190
```

Взять имя пользователя можно из ссылки профиля


#### Docker

Сборка образа:

```
docker build -t habrsaver .
```

Запуск контейнера:

```
docker run --rm --name habrsaver  \
            -v $(pwd)/article:/app/article \
            -v $(pwd)/favorites:/app/favorites \
            -v $(pwd)/singles:/app/singles \
            habrsaver -s 665254
```
