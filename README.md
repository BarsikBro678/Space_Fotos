# Космические фото

### Что делает этот проект

Данный проект с помощью библиотеки ```requests``` загружает в папку ```images``` фотографии космоса от Spase X, Nasa APOD(Astronomy Picture of the Day) и Nasa EPIC(Earth Polychromatic Imaging Camera).

### Как установить

После установки ```requests```, необходимо создать в корневой папке файл с названием ```.env``` и записать в него:

```
NASA_API_KEY=xWOVfAhhBqaguZtiqQtkcJIJQBESmVJfzoGnPprc
BOT_TELEGRAM_TOKEN=5826364594:AAFl8T4jZ4T67XkHy4JcLZa6CVJQs49h0YM
``` 

Также напишите в файл ```.env``` чат ID канала в которые бот будет выкладывать картинки, a также время между их публикацией.

```
TG_CHAT_ID=ваш чат ID
BOT_TIME=время
```

Python3 должен быть уже установлен. Затем используйте pip (или pip3, есть конфликт с Python2) для установки зависимостей:

```
pip install -r requirements.txt
```

### Как запустить

Для запуска программы напишите в терминале питона команду ```python telegram.py```.
