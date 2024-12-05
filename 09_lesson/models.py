from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

# Создание базового класса для моделей
Base = declarative_base()


class Student(Base):
    __tablename__ = 'students'  # Название таблицы в базе данных

    # Идентификатор студента (уникальный, автоинкрементируемый)
    id = Column(Integer, primary_key=True, autoincrement=True)

    # Имя студента (строка с ограничением на длину до 100 символов)
    name = Column(String(100), nullable=False)

    # Возраст студента (целое число, не может быть пустым)
    age = Column(Integer, nullable=False)

    def __repr__(self):
        return f"<Student(id={self.id}, name={self.name}, age={self.age})>"