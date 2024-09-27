from adapters.sqlite.student_repository_impl import StudentRepositoryImpl
from core.models import Student

class StudentService:
    def __init__(self):
        self.student_repository = StudentRepositoryImpl()

    def create_student(self, first_name, last_name, email, student_id):
        student = Student(first_name=first_name, last_name=last_name, email=email, id=student_id)
        return self.student_repository.create_student(student)

    def delete_student(self, student_id):
        self.student_repository.delete_student(student_id)

    def update_student(self, first_name, last_name, email, student_id):
        student = self.student_repository.get_student_by_id(student_id)
        student.first_name = first_name
        student.last_name = last_name
        student.email = email
        return self.student_repository.update_student(student)

    def get_students(self):
        return self.student_repository.get_students()

    def get_student(self, student_id):
        return self.student_repository.get_student_by_id(student_id)