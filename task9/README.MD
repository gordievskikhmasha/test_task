В виду нехватки времени и технических возможностей моего ноутбука опишу, как сделать это тестовое задание в виде текста. 
1. В файле main.py я представила код веб-приложения на языке программирования Python. Я использовала fastapi. Кроме того, файл requirements.txt - файл с зависимостями FastAPI и Uvicorn, необходимый для корректной работы приложения. В результате проверки веб-приложение работает и готово к развертыванию на сервере. 
2. Далее необходимо развернуть приложение на Ubuntu Server 22.04 через systemd. На сервер необходимо установить все необходимые системные пакеты: python, pip и т.д. (python3 python3-venv python3-pip curl iputils-ping)
3. Создаем структуру проекта (mkdir ~/devtest). Создаем виртуальное окружение (python3 python3-venv python3-pip curl iputils-ping) и активируем его. файл main.py также переносим в эту директорию.
4. На сервере создаем отдельного системного пользователя - appuser. sudo chown -R appuser:appuser /opt/test-app - appuser владелец всех файлов в каталоге. 
5. Создаем службу веб-приложения. файл: /etc/systemd/system/devapp.service. Сам файл представлен в этом же репозитории (devapp.service). 
Дальнейшие команды: `` ` `sudo systemctl daemon-reload
sudo systemctl enable devapp
sudo systemctl start devapp`` ` `
6. Dockerfile 
