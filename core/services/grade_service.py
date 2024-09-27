from core.models import Grade, Student
from adapters.sqlite.grade_repository_impl import GradeRepositoryImpl

class GradeService:
    def __init__(self):
        self.grade_repository = GradeRepositoryImpl()

    def create_grade(self, student_id, subject, grade, grade_id):
        grade = Grade(student_id=student_id, subject=subject, grade=grade, id=grade_id)
        return self.grade_repository.create_grade(grade)

    def delete_grade(self, grade_id):
        self.grade_repository.delete_grade(grade_id)

    def update_grade(self, student_id, subject, grade, grade_id):
        grade_obj = self.grade_repository.get_grade_by_id(grade_id)
        grade_obj.student_id = student_id
        grade_obj.subject = subject
        grade_obj.grade = grade
        return self.grade_repository.update_grade(grade_obj)
    
    def get_grade(self, grade_id):
        return self.grade_repository.get_grade_by_id(grade_id)
    
    def get_grades(self):
        return self.grade_repository.get_grades()
    
    def get_grades_by_student(self, student_id):
        return self.grade_repository.get_grades_by_student_id(student_id)
    
    def get_grades_by_course(self, course_id):
        return self.grade_repository.get_grades_by_course_id(course_id)
    
    def get_grades_by_student_and_course(self, student_id, course_id):
        return self.grade_repository.get_grades_by_student_id_and_course_id(student_id, course_id)
