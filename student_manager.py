from turtle import st
from student import Student

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class StudentManager:
    """ Manager of student records """

    def __init__(self, db_name):
        if db_name is None or db_name == "":
            raise ValueError("Invalid database name")
        engine = create_engine(db_name)
        self._db_session = sessionmaker(bind=engine)
        self._db_session.configure(bind=engine)


    def add_student(self, first_name, last_name, username):
        """ Add a new student to the database """
        if first_name is None or first_name == "":
            raise ValueError("Invalid first name")
        if last_name is None or last_name == "":
            raise ValueError("Invalid last name")
        if username is None or username == "":
            raise ValueError("Invalid username")
        session = self._db_session()
        student = Student(first_name, last_name, username)
        session.add(student)
        session.commit()
        session.close()
        return student.to_dict()

    def delete_student(self, first_name, last_name, username):
        """ Delete a student from the database """
        if first_name is None or first_name == "":
            raise ValueError("Invalid first name")
        if last_name is None or last_name == "":
            raise ValueError("Invalid last name")
        if username is None or username == "":
            raise ValueError("Invalid username")
        session = self._db_session()
        student = session.query(Student).filter_by(first_name=first_name, last_name=last_name, username=username).first()
        if student is None:
            raise ValueError("Student not found")
        session.delete(student)
        session.commit()
        session.close()
        return student.to_dict()


    def get_all_students_by_name(self, first_name, last_name):
        """ Get all students with a given name """
        if first_name is None or first_name == "":
            raise ValueError("Invalid first name")
        if last_name is None or last_name == "":
            raise ValueError("Invalid last name")
        session = self._db_session()
        students = session.query(Student).filter_by(first_name=first_name, last_name=last_name).all()
        session.close()
        return [student.to_dict() for student in students]

        
       


        


