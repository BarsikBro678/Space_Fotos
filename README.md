# Космические фото

### Что делает этот проект

Данный проект с помощью библиотеки ```requests``` загружает в папку ```images``` фотографии космоса от Spase X, Nasa APOD(Astronomy Picture of the Day) и Nasa EPIC(Earth Polychromatic Imaging Camera).

### Как запустить

После установки ```requests```, необходимо создать в корневой папке файл с названием .env и записать в него:

```
NASA_API_KEY=xWOVfAhhBqaguZtiqQtkcJIJQBESmVJfzoGnPprc
```

Также создайте пустую папку ```images```, куда будут загружаться картинки.

Python3 должен быть уже установлен. Затем используйте pip (или pip3, есть конфликт с Python2) для установки зависимостей:

```
pip install -r requirements.txt
```

### Как запустить

Для запуска программы напишите в терминале питона команду ```python main.py```
