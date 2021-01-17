# Start telegram bot on server
Речь пойдет - о том, как запустить `python`(с ботами на другом языке это тоже сработает, но я для примера взял телеграм бот на питоне) бота на сервере.

Использовать мы будем `systemd`

> `systemd` – cистемный менеджер, демон инициализации других демонов в Linux. Проще говоря, systemd запустит бота и будет перезапускать его в случае падения.
А одна из главных проблем с ботами на Python их вечное падение из-за ошибок  
На самом деле с такой проблемой вы столкнетесь скорее из-за телеграмма, потому что их сервера часто перезапускают и следовательно бот просто даст ошибку и отключится. 
***
### Все дальнейшие действия я буду выполнять на `Ubuntu 18.04.5 LTS` сервере.  
Посмотреть версию ubuntu можно командой `lsb_release -a`:
```bash
server ~  lsb_release -a    

No LSB modules are available.
Distributor ID: Ubuntu
Description:    Ubuntu 18.04.5 LTS
Release:        18.04
Codename:       bionic
```
Для начала установим `systemd`:
```bash
sudo apt-get install systemd
```

Далее нам нужно создать файл с расширением `.service` в папке `~/etc/systemd/system`:
```bash
server ~ touch /etc/systemd/system/bot.service <--- я для примера указал имя bot но вы можете указать свое  
```

далее открыть данный файл через любой текстовый редактор, я буду использовать `vim`, и вставить туда такое содержимое(подставив свои данные):
```bash
  [Unit]
  Description='Описание вашего бота(не обязательно писать что-то осмысленное)'
  After=syslog.target
  4 After=network.target  
  [Service]
  Type=simple
  User='Имя рут пользователя' 
  WorkingDirectory='Путь до дериктории с файлами бота'
  ExecStart=/usr/bin/python3 'полный путь до файла бота'
  RestartSec=10
  Restart=always
  
  [Install]
  WantedBy=multi-user.target
```
Далее вы можете столкнуть с ошибкой, когда попытаетесь сохрнаить файл:
```bash
"/etc/systemd/system/bot.service"
"/etc/systemd/system/bot.service" E212: Can't open file for writing
```
Что бы исправить ее, вместо обычной записи файла `:w!` используйте `:w !sudo tee % > /dev/null` и все !  
Теперь вам нужно прописать следующие комманды:
```bash
server ~ sudo systemctl daemon-reload
server ~ sudo systemctl enable bot
server ~ sudo systemctl start bot
server ~ sudo systemctl status bot
```
Если вы сделали все правильно то увидите следующее сообщение: 
```bash
server ~  sudo systemctl status bot                                                                                            
● bot.service - 'Ваше описание'
   Loaded: loaded (/etc/systemd/system/bot.service; enabled; vendor preset: enabled)
   Active: active (running) since Sun 2021-01-17 00:10:45 UTC; 1s ago
 Main PID: 00000 (python3)
   CGroup: /system.slice/bot.service
           └─00000 /usr/bin/python3 'полный путь до файла бота'

Jan 17 00:10:45 CalmWorld systemd[1]: Started 'Ваше описание'.
```

Вот и все ! ...(*￣０￣)ノ ваш бот запущен и готов к работе.
