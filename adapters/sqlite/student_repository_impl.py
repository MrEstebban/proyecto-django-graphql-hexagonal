from core.repositories.student_repository import StudentRepository
from core.models import Student

class StudentRepositoryImpl(StudentRepository):
    def create_student(self, student):
        student.save()
        return student

    def delete_student(self, student_id):
        student = Student.objects.get(id=student_id)
        student.delete()

    def get_student_by_id(self, student_id):
        return Student.objects.get(id=student_id)

    def get_students(self):
        return Student.objects.all()

    def update_student(self, student):
        student.save()
        return student