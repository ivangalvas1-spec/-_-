Использовал ИИ только в третьем задании, чтобы узнать, как запустить тг-бота через Docker-контейнер. Конкретно Deepseek. 

#Объяснение:
Как запустить бота через Docker (задача 3):
Нужны установленные Docker и Docker Compose.

requirements.txt:
pyTelegramBotAPI>=4.14

docker-compose.yml:
services:
  bot:
    build: .
    container_name: telegram-bot
    env_file: .env
    restart: unless-stopped


.env.example (скопируйте в .env и введите токен):
BOT_TOKEN=your_telegram_bot_token_here


.dockerignore и .gitignore:
.env
__pycache__/
venv/


Запуск на сервере:
cp .env.example .env            # вписать новый токен
docker compose up -d --build
docker compose logs -f          # должно появиться «Бот запущен»


Без Compose:
docker build -t telegram-bot .
docker run -d --name telegram-bot --env-file .env --restart unless
