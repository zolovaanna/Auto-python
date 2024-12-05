import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Загружаем переменные из файла .env
load_dotenv()

# Получаем URL базы данных из переменных окружения
DATABASE_URL = os.getenv("DATABASE_URL")

# Проверяем, что DATABASE_URL установлен, иначе выбрасываем ошибку
if not DATABASE_URL:
    raise ValueError("DATABASE_URL is not set in the environment variables")

# Создаем SQLAlchemy движок для подключения к базе данных
engine = create_engine(DATABASE_URL)

# Создаем фабрику сессий, привязанную к движку
Session = sessionmaker(bind=engine)

# Инициализируем сессию для взаимодействия с базой данных
session = Session()