from .models import Student, Course

def get_students_over_20():
    """DRC: {<name> | Student(name, age) ∧ age > 20}"""
    return Student.objects.filter(age__gt=20).values('name')

def get_students_with_grade_A():
    """DRC: {<s.name> | Student(s) ∧ Course(c) ∧ c.student_id = s.id ∧ c.grade = 'A'}"""
    return Student.objects.filter(course__grade='A').distinct()
