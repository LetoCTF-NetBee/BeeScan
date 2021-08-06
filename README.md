# BeeScan - cканер фишинговых сайтов
![BeeScan logo](images/beescan.png)

## Задачи:
- владелец сайта (юр или физ)
- проверка отзывов
- орфографические ошибки

## В разаработке:


## Выполненные задачи:
- проверка домена на двойника
- домен 3-го уровня
- базы данных
- проверка существования
- дата регистрации
- SSL
- переадресация

## Описание модулей:
### redirection.py
- проверка на переадресацию. 
- принимает: URL 
- возращает: T/F и настоящий URL
- пример: redirection.testRedirection('http://larri.ru')
- вернет: False, 'https://www.aviasales.ru/' 

## Quickstart (Docker)
```bash
git clone https://github.com/LetoCTF-NetBee/BeeScan.git
cd BeeScan
docker-compose up -d --build
```