# BeeScan - cканер фишинговых сайтов
![BeeScan logo](images/beescan.png)

## Задачи:
- владелец сайта (юр или физ)
- проверка домена на двойника
- проверка отзывов
- орфографические ошибки

## В разаработке:
- домен 3-го уровня

## Выполненные задачи:
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