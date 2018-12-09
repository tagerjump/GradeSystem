import unittest
import os
import time
from prettytable import PrettyTable

def open_tables(dir):
    try:
        students = open(os.getcwd()+ dir + '/students.txt' , 'r')
        grades = open(os.getcwd()+ dir + '/grades.txt', 'r')
        instructors = open(os.getcwd()+ dir + '/instructors.txt', 'r')
    except FileNotFoundError:
        print("Can't Find Three tables in: " + dir)
        raise FileNotFoundError
    else:
        with students, grades, instructors:
            student_str_list = students.readlines()

            grade_str_list = grades.readlines()

            instructor_str_list = instructors.readlines()

            student_data = dict()
            instructor_data = dict()
            course_data = dict()
            for student_str in student_str_list:
                student_str = student_str.strip('\n')
                student = str.split(student_str, '\t')
                cwid, name, major = student
                student_data[cwid] = (name, [],major)
            for instructor_str in instructor_str_list:
                instructor_str = instructor_str.strip('\n')
                instructor = str.split(instructor_str, '\t')
                cwid, name, dept = instructor
                instructor_data[cwid] = (name, [], dept)
            for grade_str in grade_str_list:
                grade_str = grade_str.strip('\n')
                grade = str.split(grade_str, '\t')
                cwid, course, grade_course, instructor_cwid = grade
                if grade_course != 'F':
                    student_data[cwid][1].append(course)
                if course_data.get('course') is None:
                    course_data[course] = (cwid, instructor_data[instructor_cwid][0], instructor_data[instructor_cwid][2], 1)
                else:
                    course_data[course][3] += 1


            return student_data, course_data



def main():
    student_data, course_data = open_tables('')
    pt_students = PrettyTable(field_names=['CWId', 'Name', 'Completed Courses'])
    pt_courses = PrettyTable(field_names=['CWId', 'Name', 'Dept', 'Course, Students'])

    for cwid, value in student_data.items():
        pt_students.add_row([cwid, value[0], value[1]])

    for cwid, value in course_data.items():
        pt_courses.add_row([cwid, value[0], value[1], value[2]])

    print(pt_students)
    print(pt_courses)


class TestTables(unittest.TestCase):
    def test_tables(self):
        student_data, course_data = open_tables('')
        self.assertEqual(student_data['11714'], ('Morton, A', ['SYS 611', 'SYS 645'], 'SYEN'))
        self.assertEqual(student_data['10103'], ('Baldwin, C', ['SSW 567', 'SSW 564', 'SSW 687', 'CS 501'], 'SFEN'))
        self.assertEqual(course_data['SSW 540'], ('11788', 'Einstein, A', 'SFEN', 1))

if __name__ == '__main__':
    main()
    time.sleep(0.1)
    unittest.main(exit = False, verbosity = 2)
