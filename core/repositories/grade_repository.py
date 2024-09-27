from abc import ABC, abstractmethod

class GradeRepository(ABC):
    @abstractmethod
    def get_grade_by_id(self, grade_id: int) -> dict:
        pass

    @abstractmethod
    def get_grades(self) -> list:
        pass

    @abstractmethod
    def create_grade(self, grade: dict) -> dict:
        pass

    @abstractmethod
    def update_grade(self, grade_id: int, grade: dict) -> dict:
        pass

    @abstractmethod
    def delete_grade(self, grade_id: int) -> dict:
        pass

    @abstractmethod
    def get_grades_by_student_id(self, student_id: int) -> list:
        pass

    @abstractmethod
    def get_grades_by_course_id(self, course_id: int) -> list:
        pass

    @abstractmethod
    def get_grades_by_student_id_and_course_id(self, student_id: int, course_id: int) -> list:
        pass