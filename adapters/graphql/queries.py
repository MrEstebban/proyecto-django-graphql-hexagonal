'''
Define las consultas de GraphQL para listar
 y obtener información de estudiantes y notas.
'''
import graphene
from graphene_django import DjangoObjectType
from core.models.student import Student
from core.models.grade import Grade
#from core.services.student_service import StudentService
#from core.services.grade_service import GradeService

# Definición de tipos para GraphQL
class StudentType(DjangoObjectType):
    class Meta:
        model = Student
        fields = ("id", "first_name", "last_name", "email")

class GradeType(DjangoObjectType):
    class Meta:
        model = Grade
        fields = ("id", "student_id", "subject", "grade")

# Consultas de GraphQL
class Query(graphene.ObjectType):
    all_students = graphene.List(StudentType)
    all_grades = graphene.List(GradeType)
    student_by_id = graphene.Field(StudentType, student_id=graphene.String(required=True))
    grades_by_student = graphene.List(GradeType, student_id=graphene.String(required=True))

    def resolve_all_students(self, info):
        #student_service = StudentService()
        return Student.objects.all()


