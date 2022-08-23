from flask import Flask
from flask import request
from flask import Response

from student_manager import StudentManager

import json

app = Flask(__name__)

DB_NAME = "sqlite:///school.sqlite"


@app.route('/students/all', methods=['GET'])
def get_all_students():
    """ Gets all student records """
    manager = StudentManager(DB_NAME)
    students = manager.get_all_students_by_name()
    return Response(json.dumps(students), mimetype='application/json')


@app.route('/students', methods=['POST'])
def add_student():
    """ Adds a new student record """
    manager = StudentManager(DB_NAME)
    first_name = request.form.get('first_name')
    last_name = request.form.get('last_name')
    username = request.form.get('username')
    student = manager.add_student(first_name, last_name, username)
    return Response(json.dumps(student), mimetype='application/json')  



@app.route('/students/<int:id>', methods=['DELETE'])
def delete_student(id):
    """ Deletes a student record """
    manager = StudentManager(DB_NAME)
    student = manager.delete_student(id)
    return Response(json.dumps(student), mimetype='application/json')




if __name__ == "__main__":
    app.run()
