

def coursestudents(student_list:list, course:str) -> list:
    """
    This function takes a list of Student objects and a course name as arguments.
    It returns a list of names of students who attend the course.
    """
    return [student.name for student in student_list if student.attends(course)]