import pytest
from sqlalchemy import create_engine, inspect
from sqlalchemy.orm import sessionmaker
from models import Base, Student
from db_config import DATABASE_URL


# Создаем сессию для тестов
@pytest.fixture(scope="module")
def db_session():
    engine = create_engine(DATABASE_URL)
    session_factory = sessionmaker(bind=engine)

    # Проверяем, существуют ли таблицы, чтобы избежать повторного их создания
    if not inspect(engine).has_table("students"):
        Base.metadata.create_all(engine)  # Убедимся, что таблицы созданы

    session = session_factory()
    yield session
    session.rollback()  # Откат изменений
    session.close()
    engine.dispose()


def test_add_student(db_session):
    student = Student(name="John Doe", age=20)
    db_session.add(student)
    db_session.commit()

    # Проверяем, что студент добавлен
    added_student = db_session.query(Student).filter_by(name="John Doe").first()
    assert added_student is not None, "Student was not added to the database."
    assert added_student.age == 20, f"Expected age 20, but got {added_student.age}"


def test_update_student(db_session):
    student = db_session.query(Student).filter_by(name="John Doe").first()
    student.age = 21
    db_session.commit()

    # Проверяем, что возраст обновился
    updated_student = db_session.query(Student).filter_by(name="John Doe").first()
    assert updated_student.age == 21, f"Expected age 21, but got {updated_student.age}"


def test_delete_student(db_session):
    student = db_session.query(Student).filter_by(name="John Doe").first()
    db_session.delete(student)
    db_session.commit()

    # Проверяем, что студент удален
    deleted_student = db_session.query(Student).filter_by(name="John Doe").first()
    assert deleted_student is None, "Student was not deleted from the database."
