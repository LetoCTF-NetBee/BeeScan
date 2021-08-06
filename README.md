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
### testRedirection:
- проверка на переадресацию. 
- принимает: URL 
- возращает: T/F и настоящий URL
- пример: checkers.testRedirection('larri.ru')
- 		 >>> False, 'https://www.aviasales.ru/' 

### scanDatabaseOpenphish:
- поиск домена по базе openphish
- принимает: URL 
- возращает: T/F и, если есть, сообщение ошибки
- пример: checkers.scanDatabaseOpenphish('http://larri.ru')
- 		 >>> True, "Not found in database"

### checkSSL:
- проверка SSL сертификата
- принимает: URL 
- возращает: T/F и, если есть, сообщение ошибки
- пример: checkers.checkSSL('http://larri.ru')
- 		 >>> False, 'SSL not found'

### checkValidDate:
- проверка даты регистрации домена 
- принимает: URL и ограничение в днях
- возращает: T/F и количество дней с решистрации домена
- пример: checkers.checkValidDate('http://larri.ru')
- 		 >>> True, 997

### testSecurity:
- проверка в базах Google и Yandex
- принимает: URL
- возращает: T/F каждого из источников
- пример: checkers.checkValidDate('http://larri.ru')
- 		 >>> True, True

### testBlackList:
- проверка в известных базах
- принимает: URL
- возращает: T/F каждого из источников
- пример: checkers.checkValidDate('http://larri.ru')
- 		 >>> True, True

### domen:
- проверка домена на его уровень
- принимает: URL
- возращает: T/F, уровень домена
- пример: checkers.checkValidDate('http://larri.ru')
- 		 >>> True, 2

### findDubl:
- поиск более известных сайтов-дубликатов 
- принимает: URL
- возращает: T/F и, если есть, оригинальный домен
- пример: checkers.checkValidDate('http://larri.ru')
- 		 >>> True

## Quickstart (Docker)
```bash
git clone https://github.com/LetoCTF-NetBee/BeeScan.git
cd BeeScan
docker-compose up -d --build
```