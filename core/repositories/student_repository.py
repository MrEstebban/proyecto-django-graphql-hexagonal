from abc import ABC, abstractmethod

class StudentRepository():
    @abstractmethod
    def get_student_by_id(self, student_id: int) -> dict:
        pass

    @abstractmethod
    def get_students(self) -> list:
        pass

    @abstractmethod
    def create_student(self, student: dict) -> dict:
        pass

    @abstractmethod
    def update_student(self, student_id: int, student: dict) -> dict:
        pass

    @abstractmethod
    def delete_student(self, student_id: int) -> dict:
        pass