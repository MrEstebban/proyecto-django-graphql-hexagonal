from core.repositories.grade_repository import GradeRepository
from core.models import Grade

class GradeRepositoryImpl(GradeRepository):    
    def create_grade(self, grade):
        grade.save()
        return grade

    def delete_grade(self, grade_id):
        grade = Grade.objects.get(id=grade_id)
        grade.delete()

    def get_grade_by_id(self, grade_id):
        return Grade.objects.get(id=grade_id)

    def get_grades(self):
        return Grade.objects.all()

    def get_grades_by_course_id(self, course_id):
        return Grade.objects.filter(course_id=course_id)

    def get_grades_by_student_id(self, student_id):
        return Grade.objects.filter(student_id=student_id)

    def get_grades_by_student_id_and_course_id(self, student_id, course_id):
        return Grade.objects.filter(student_id=student_id, course_id=course_id)

    def update_grade(self, grade):
        grade.save()
        return grade