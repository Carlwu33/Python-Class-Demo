#!/usr/bin/env python3
import sys
from collections import Counter
class Person(object):
    """
    """
    def __init__(self, name):
        self.name = name

    def get_details(self):
        """

        """
        return self.name

    def get_grade(self):
        """
        """
        return self.grade

class Student(Person):
    """

    """
    def __init__(self, name, branch, year, grade):
        Person.__init__(self, name)
        self.branch = branch
        self.year = year
        self.grade = grade

    def get_details(self):
        """
        """
        return "{} studies {} and is in {} year.".format(self.name, self.branch, self.year)

    def get_grade(self):
        """
        """
        res = Counter(self.grade).most_common(4)
        n1 = 0
        n2 = 0
        for item in res:
            if item[0] !="D":
                n1 = +item[1]
            else:
                n2 += item[1]
        print("Pass: {}, Fail: {}".format(n1, n2))

class Teacher(Person):
    """

    """
    def __init__(self, name, papers, grade):
        Person.__init__(self, name)
        self.papers = papers
        self.grade = grade

    def get_details(self):
        return "{} teaches {}".format(self.name, ','.join(self.papers))

    def get_grade(self):
        s = []
        res = Counter(self.grade).most_common(4)
        for i, j in res:
            s.append("{}: {}".format(i,j))
        print(', '.join(s))

person1 = Person('Sachin')
if sys.argv[1] == "student":
    student1 = Student('Kushal' , 'CSE', 2005, sys.argv[2])
    student1.get_grade()
elif sys.argv[1] == "teacher":
    teacher1 = Teacher('Prashad',['python', 'c++'], sys.argv[2])
    teacher1.get_grade()


