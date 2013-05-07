class courseInfo(object):

    def __init__(self, courseName):
        self.courseName = courseName
        self.psetsDone = []
        self.grade = "No Grade"

    def setPset(self, pset, score):
        self.psetsDone.append((pset, score))

    def getPset(self, pset):
        for (p, score) in self.psetsDone:
            if p == pset:
                return score

    def setGrade(self, grade):
        if self.grade == "No Grade":
            self.grade = grade

    def getGrade(self):
        return self.grade
# ==============================


class InvalidPasswordException(Exception):
    """
    InvalidPasswordException is raised when an invalid password is entered.
    You can use InvalidPasswordException as is, you do not need to
    modify/add any code.
    """
    def __str__(self):
        return "Invalid password was entered!"


class edx(object):
    def __init__(self, courses):
        self.myCourses = []
        for course in courses:
            self.myCourses.append(courseInfo(course))

    def setGrade(self, grade, course="6.01x", password=None):
        """
        grade: integer greater than or equal to 0 and less than or equal to 100
        course: string
        password: string

        This method sets the grade in the courseInfo object named by `course`, depending on
        if the proper password is supplied.

        The password must match the default teacher's password.

        If the password is omitted, a "Password Required" message should be returned.

        If the password is incorrect, an `InvalidPasswordException` should be raised.

        If `course` was not part of the initialization, then no grade is set, and no
        error is thrown.

        The method does not return a value.
        """
        if password is None:
            return 'Password Required'
        elif password == 'Go Beavers':
            for i in self.myCourses:
                if course == i.courseName:
                    i.setGrade(grade)
        else:
            raise InvalidPasswordException

    def getGrade(self, course="6.02x", password=None):
        """
        course: string
        password: string

        This method gets the grade in the the courseInfo object named by `course`, depending on
        if the proper password is supplied.

        The password must match the default student's password.

        If the password is omitted, a "Password Required" message should be returned.

        If the password is incorrect, an `InvalidPasswordException` should be raised.

        returns: the integer grade for `course`.
        If `course` was not part of the initialization, returns -1.
        """
        if password is None:
            return 'Password Required'
        elif password == 'edX Rocks':
            for i in self.myCourses:
                if course == i.courseName:
                    return i.getGrade()
        else:
            raise InvalidPasswordException
        return -1

    def setPset(self, pset, score, course="6.00x"):
        """
        pset: a string or a number
        score: an integer between 0 and 100
        course: string

        The `score` of the specified `pset` is set for the
        given `course` using the courseInfo object.

        If `course` is not part of the initialization, then no pset score is set,
        and no error is thrown.
        """
        for i in self.myCourses:
            if course == i.courseName:
                i.setPset(pset, score)

    def getPset(self, pset, course="6.00x"):
        """
        pset: a string or a number
        score: an integer between 0 and 100
        course: string

        returns: The score of the specified `pset` of the given
        `course` using the courseInfo object.
        If `course` was not part of the initialization, returns -1.
        """
        for i in self.myCourses:
            if course == i.courseName:
                return i.getPset(pset)
        return -1
