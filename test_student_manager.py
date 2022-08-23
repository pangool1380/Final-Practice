from unittest import TestCase

from student_manager import StudentManager

import sqlite3
import os
import inspect
import unittest

class TestStudentManager(TestCase):
    """ Tests the StudentManager class """

    TEST_DB = 'test_students.sqlite'

    def setUp(self):
        """ Set up test environment """
        self.logPoint()

        conn = sqlite3.connect(TestStudentManager.TEST_DB)

        c = conn.cursor()
        c.execute('''
                  CREATE TABLE students
                  (id INTEGER PRIMARY KEY ASC,
                   timestamp DATETIME NOT NULL,
                   first_name VARCHAR(250) NOT NULL,
                   last_name VARCHAR(250) NOT NULL,           
                   username VARCHAR(20) NOT NULL
                  )
                  ''')

        conn.commit()
        conn.close()

        self.student_mgr = StudentManager("sqlite:///" + TestStudentManager.TEST_DB)


    def tearDown(self):
        """ call log message for test"""
        self.logPoint()
        os.remove('test_students.sqlite')

    def logPoint(self):
        """ Log out testing information """
        current_test = self.id().split('.')[-1]
        calling_function = inspect.stack()[1][3]
        print('in %s - %s()' % (current_test, calling_function))

    def test_add_student_success(self):
        """ TP-01 - Success test on add_student """
            
        students_after = self.student_mgr.get_all_students_by_name()
        self.assertEqual(len(students_after), 0)
        self.student_mgr.add_student("First1", "Last1", "username1")
    
        students_after = self.student_mgr.get_all_students_by_name()
        self.assertEqual(len(students_after), 1)
    
        self.student_mgr.add_student("First2", "Last2", "username2")
    
        students_after = self.student_mgr.get_all_students_by_name()
        self.assertEqual(len(students_after), 3)

       
    def test_add_student_invalid(self):
        """ TP-02 - Validation test on add_student """

        with self.assertRaises(ValueError):
            self.student_mgr.add_student("", "Last1", "username1")

        with self.assertRaises(ValueError):
            self.student_mgr.add_student("First1", "", "username1")

        with self.assertRaises(ValueError):
            self.student_mgr.add_student("First1", "Last1", "")

        with self.assertRaises(ValueError):
            self.student_mgr.add_student(None, "Last1", "username1")

        with self.assertRaises(ValueError):
            self.student_mgr.add_student("First1", None, "username1")

        with self.assertRaises(ValueError):
            self.student_mgr.add_student("First1", "Last1", None)

    def test_delete_student_success(self):
        """ TP-04 - Success test on delete_student """

        students_after = self.student_mgr.get_all_students_by_name()
        self.assertEqual(len(students_after), 0)

        self.student_mgr.add_student("First1", "Last1", "username1")
        self.student_mgr.add_student("First2", "Last2", "username2")

        students_after = self.student_mgr.get_all_students_by_name()
        self.assertEqual(len(students_after), 2)

        for student in students_after:
           self.student_mgr.delete_student(student.id)

        students_after = self.student_mgr.get_all_students_by_name()
        self.assertEqual(len(students_after), 0)

    def test_delete_student_invalid(self):
        """ TP-05 - Validation test on delete_student """

        with self.assertRaises(ValueError):
            self.student_mgr.delete_student(None)

        with self.assertRaises(ValueError):
            self.student_mgr.delete_student("")

        with self.assertRaises(ValueError):
            self.student_mgr.delete_student(-100)

    def test_get_all_students_success(self):
        """ TP-06 - Success test on get_all_students """

        students_after = self.student_mgr.get_all_students_by_name()
        self.assertEqual(len(students_after), 0)

        self.student_mgr.add_student("First1", "Last1", "username1")

        students_after = self.student_mgr.get_all_students_by_name()
        self.assertEqual(len(students_after), 1)

        self.student_mgr.add_student("First2", "Last2", "username2")

        students_after = self.student_mgr.get_all_students_by_name()
        self.assertEqual(len(students_after), 2)



if __name__ == '__main__':
    unittest.main()