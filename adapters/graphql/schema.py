'''
Archivo principal para definir el esquema de GraphQL
y conectar los resolvers y mutaciones.
'''
import graphene
from graphene_django import DjangoObjectType
from core.models.student import Student
from core.models.grade import Grade
#from core.services.student_service import StudentService
#from core.services.grade_service import GradeService

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
    
    def resolve_all_grades(self, info):
        #grade_service = GradeService()
        return Grade.objects.all()
    
    def resolve_student_by_id(self, info, student_id):
        #student_service = StudentService()
        return Student.objects.get(id=student_id)
    
    def resolve_grades_by_student(self, info, student_id):
        #grade_service = GradeService()
        return Grade.objects.filter(student_id=student_id)

# Mutación para crear un estudiante
class CreateStudent(graphene.Mutation):
    class Arguments:
        first_name = graphene.String(required=True)
        last_name = graphene.String(required=True)
        email = graphene.String(required=True)
        student_id = graphene.String(required=True)

    student = graphene.Field(StudentType)

    def mutate(self, info, first_name, last_name, email, student_id):
        student = Student(first_name=first_name, last_name=last_name, email=email, id=student_id)
        student.save()
        return CreateStudent(student=student)

class CreateGrade(graphene.Mutation):
    class Arguments:
        student_id = graphene.String(required=True)
        subject = graphene.String(required=True)
        grade = graphene.Float(required=True)
        grade_id = graphene.String(required=True)

    grade = graphene.Field(GradeType)

    def mutate(self, info, student_id, subject, grade, grade_id):
        grade = Grade(student_id=student_id, subject=subject, grade=grade, id=grade_id)
        grade.save()
        return CreateGrade(grade=grade)

class DeleteStudent(graphene.Mutation):
    class Arguments:
        student_id = graphene.String(required=True)

    message = graphene.String()

    def mutate(self, info, student_id):
        student = Student.objects.get(id=student_id)
        student.delete()
        return DeleteStudent(message=f"Estudiante {student_id} eliminado")

class DeleteGrade(graphene.Mutation):
    class Arguments:
        grade_id = graphene.String(required=True)

    message = graphene.String()

    def mutate(self, info, grade_id):
        grade = Grade.objects.get(id=grade_id)
        grade.delete()
        return DeleteGrade(message=f"Nota {grade_id} eliminada")

class UpdateStudent(graphene.Mutation):
    class Arguments:
        first_name = graphene.String(required=True)
        last_name = graphene.String(required=True)
        email = graphene.String(required=True)
        student_id = graphene.String(required=True)

    student = graphene.Field(StudentType)

    def mutate(self, info, first_name, last_name, email, student_id):
        student = Student.objects.get(id=student_id)
        student.first_name = first_name
        student.last_name = last_name
        student.email = email
        student.save()
        return UpdateStudent(student=student)
    
class UpdateGrade(graphene.Mutation):
    class Arguments:
        student_id = graphene.String(required=True)
        subject = graphene.String(required=True)
        grade = graphene.Float(required=True)
        grade_id = graphene.String(required=True)

    grade = graphene.Field(GradeType)

    def mutate(self, info, student_id, subject, grade, grade_id):
        try:
            grade_obj = Grade.objects.get(id=grade_id)
            grade_obj.student_id = student_id
            grade_obj.subject = subject
            grade_obj.grade = grade
            grade_obj.save()
            
            # Devolver el objeto actualizado
            return UpdateGrade(grade=grade_obj)
        except Grade.DoesNotExist:
            raise Exception("Grade not found")
        except Exception as e:
            raise Exception(f"An error occurred: {str(e)}")

# Clase principal para registrar todas las mutaciones
class Mutation(graphene.ObjectType):
    create_student = CreateStudent.Field()
    update_student = UpdateStudent.Field()
    delete_student = DeleteStudent.Field()
    create_grade = CreateGrade.Field()
    update_grade = UpdateGrade.Field()
    delete_grade = DeleteGrade.Field()
schema = graphene.Schema(query=Query, mutation=Mutation)
