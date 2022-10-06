from itertools import islice


class Student:

    def __init__(self, name, surname, number, *grades):
        self._name = name
        self._surname = surname
        self._number = number
        if not len(grades) == 5:
            raise ValueError('Grades invalid input')
        for i in grades:
            if not 59 < i < 101:
                raise ValueError('Grades invalid input')
        self._grades = grades
        self._average_score = None

    @property
    def grades(self):
        return self._grades

    @grades.setter
    def grades(self, marks):
        for i in marks:
            if not 59 < i < 101:
                raise ValueError('Grades invalid input')
        self._grades = marks
        self._average_score = None

    @property
    def get_average(self):
        if self._average_score is None:
            return sum(self._grades) / len(self._grades)
        return self._average_score

    @property
    def data(self):
        return self._name, self._surname

    @data.setter
    def data(self, info):
        self._name = info[0]
        self._surname = info[1]

    def __str__(self):
        # Return the string representation of the current student
        return f'{self._name}, {self._surname}, {self._number}, {self._grades}\n'


class Group:
    def __init__(self, faculty, course, name, *students):
        if not 2 < len(faculty) < 5:
            raise ValueError('invalid input')
        self._faculty = faculty
        if course not in [1, 2, 3, 4, 5, 6]:
            raise TypeError('Invalid input')
        self._course = course
        if not len(name) == 5:
            raise ValueError('invalid input')
        self._name = name
        if len(students) > 20:
            raise ValueError('group cant be > 20')
        self._group = Group.check(students)

    def __str__(self):
        # Return the string representation of the current group
        return f'Group info: {self._faculty}, {self._course}, {self._name}\n\n' + ''.join([str(i) for i in self._group])

    @staticmethod
    def check(students):
        # Function is used for checking the correction of the current group
        # so in a group can't be students with the same Name and Surname
        arr = []
        for i, j in zip(students, tuple(i + 1 for i in range(len(students)))):
            if any(i.data == x.data for x in tuple(islice(students, j, len(students)))):
                raise ValueError('Two students with the same name and surname')
            arr.append(i)
        return arr

    def best_students(self):
        return sorted(self._group, key=lambda x: x.get_average,  reverse=True)[:5]


St1 = Student("Bohort", "Gwawr", "407-999-3868", 86, 99, 100, 77, 81)
St2 = Student("Kayla", "Siarhei", "802-656-2527", 60, 60, 98, 63, 61)
St3 = Student("Olev", "Masoud", "240-249-0602", 86, 99, 88, 77, 81)
St4 = Student("Andon", "Bopha", "510-701-4631", 78, 78, 65, 63, 61)
St5 = Student("Akamu", "Emmanuelle", "+3804649855", 60, 60, 65, 63, 61)
St6 = Student("Emma", "Onyekachukwu", "925-676-6820", 99, 98, 90, 88, 79)
St7 = Student("Tiidrik", "Penjani", "662-456-3343", 60, 98, 65, 63, 61)

group = Group("TEF", 2, "TB-11", St1, St2, St3, St4, St5, St6, St7)

print(group)
print(''.join(str(i) for i in group.best_students()))
