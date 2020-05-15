#!/usr/bin/env python3

class Person(object):
    """
    """
    def __init__(self, name, grade):
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
            if item[0] !=D:
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
        res = Counter(self.grade).most_commom(4)


