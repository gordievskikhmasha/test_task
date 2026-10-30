1. В файле main.py я представила код веб-приложения на языке программирования Python. Я использовала fastapi. Кроме того, файл requirements.txt - файл с зависимостями FastAPI и Uvicorn, необходимый для корректной работы приложения. В результате проверки веб-приложение работает и готово к развертыванию на сервере. 
2. Далее необходимо развернуть приложение на Ubuntu Server 22.04 через systemd. На сервер необходимо установить все необходимые системные пакеты: python, pip и т.д. (python3 python3-venv python3-pip curl iputils-ping)
3. Создаем структуру проекта (mkdir ~/devtest). Создаем виртуальное окружение (python3 python3-venv python3-pip curl iputils-ping) и активируем его. файл main.py также переносим в эту директорию.
4. На сервере создаем отдельного системного пользователя - appuser. sudo chown -R appuser:appuser /opt/test-app - appuser владелец всех файлов в каталоге. 
5. Создаем службу веб-приложения. файл: /etc/systemd/system/devapp.service. Сам файл представлен в этом же репозитории (devapp.service). 
Дальнейшие команды: 
`` ` `sudo systemctl daemon-reload
sudo systemctl enable devapp
sudo systemctl start devapp`` ` `
6. Dockerfile. Сборка образа: docker build -t test-app:1.0 .
Запуск контейнера: ``docker run -d \
  --name test-app \
  --restart unless-stopped \
  -p 8000:8000 \
  test-app:1.0``
7. ....
8. Создадим еще одну виртуальную машину с двумя сетевыми интерфейсами. Первый NAT. Второй внутренняя сеть (назовем ее internal-net). У первой машины один сетевой адаптер - внутренняя сеть: internal-net.
Настройка сети на первой виртуальной машине ( с двумя сетевыми адаптерами). enp0s3 - внешний интерфейс, enp0s8 - внутренний интерфейс. Настройка через netplan. 
''
network:
  version: 2
  ethernets:
    enp0s3:
      dhcp4: true
    enp0s8:
      dhcp4: false
      addresses:
        - 192.168.100.1/24 ''
