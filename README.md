# Обрезка ссылок с помощью Битли

Позволяет сокращать ссылки или смотреть количество переходов по уже сокращённой ссылке через Bitly API.
(Для просмотра количества переходов нужна платная подписка)

### Как установить и использовать

Что бы работать с программой, необходим токен Bitly API.
Что бы его получить, сначала надо будет зарегистрироваться на сайте, а потом сгенерировать [здесь](https://app.bitly.com/settings/api).

После этого, создайте в установленной программе файл `.env` и впишите туда свой токен:
```dotenv
BITLY_API=Ваш токен
```

Python3 должен быть уже установлен. 
Затем используйте `pip` (или `pip3`, есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```

Что бы запустить программу нужно будет написать следующее:
```
python main.py Ваша ссылка или битлинк
```
Программа автоматически сделает битлинк, если вы ввели ссылку или покажет количество переходов, если вы ввели свой битлинк.
### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).
