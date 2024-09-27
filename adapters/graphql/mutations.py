import graphene
from graphene_django import DjangoObjectType
from core.models import Student, Grade
from core.services.grade_service import GradeService
from core.services.student_service import StudentService

class StudentType(DjangoObjectType):
    class Meta:
        model = Student
        fields = ("id", "first_name", "last_name", "email")

class GradeType(DjangoObjectType):
    class Meta:
        model = Grade
        fields = ("id", "student_id", "subject", "grade")

# Mutación para crear un estudiante
class CreateStudent(graphene.Mutation):
    class Arguments:
        first_name = graphene.String(required=True)
        last_name = graphene.String(required=True)
        email = graphene.String(required=True)
        student_id = graphene.String(required=True)

    student = graphene.Field(StudentType)

    def mutate(self, info, first_name, last_name, email, student_id):
        student_service = StudentService()
        student = student_service.create_student(first_name, last_name, email, student_id)
        return CreateStudent(student=student)

# Mutación para actualizar un estudiante
class UpdateStudent(graphene.Mutation):
    class Arguments:
        first_name = graphene.String(required=True)
        last_name = graphene.String(required=True)
        email = graphene.String(required=True)
        student_id = graphene.String(required=True)

    student = graphene.Field(StudentType)

    def mutate(self, info, first_name, last_name, email, student_id):
        student_service = StudentService()
        student = student_service.update_student(first_name, last_name, email, student_id)
        return UpdateStudent(student=student)

# Mutación para eliminar un estudiante
class DeleteStudent(graphene.Mutation):
    class Arguments:
        student_id = graphene.String(required=True)

    message = graphene.String()

    def mutate(self, info, student_id):
        student_service = StudentService()
        student_service.delete_student(student_id)
        return DeleteStudent(message=f"Estudiante {student_id} eliminado")

# Mutación para crear una nota
class CreateGrade(graphene.Mutation):
    class Arguments:
        student_id = graphene.String(required=True)
        subject = graphene.String(required=True)
        grade = graphene.Float(required=True)
        grade_id = graphene.String(required=True)

    grade = graphene.Field(GradeType)

    def mutate(self, info, student_id, subject, grade, grade_id):
        grade_service = GradeService()
        grade = grade_service.create_grade(student_id, subject, grade, grade_id)
        return CreateGrade(grade=grade)

# Mutación para actualizar una nota
class UpdateGrade(graphene.Mutation):
    class Arguments:
        student_id = graphene.String(required=True)
        subject = graphene.String(required=True)
        grade = graphene.Float(required=True)
        grade_id = graphene.String(required=True)

    grade = graphene.Field(GradeType)

    def mutate(self, info, student_id, subject, grade, grade_id):
        grade_service = GradeService()
        grade = grade_service.update_grade(student_id, subject, grade, grade_id)
        return UpdateGrade(grade=grade)

# Mutación para eliminar una nota
class DeleteGrade(graphene.Mutation):
    class Arguments:
        grade_id = graphene.String(required=True)

    message = graphene.String()

    def mutate(self, info, grade_id):
        grade_service = GradeService()
        grade_service.delete_grade(grade_id)
        return DeleteGrade(message=f"Nota {grade_id} eliminada")

# Clase principal para registrar todas las mutaciones
class Mutation(graphene.ObjectType):
    create_student = CreateStudent.Field()
    update_student = UpdateStudent.Field()
    delete_student = DeleteStudent.Field()
    create_grade = CreateGrade.Field()
    update_grade = UpdateGrade.Field()
    delete_grade = DeleteGrade.Field()