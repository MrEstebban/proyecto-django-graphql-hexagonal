
# Proyecto Django con Arquitectura Hexagonal, SQLite y GraphQL

Este proyecto utiliza Django para construir una API que sigue la arquitectura hexagonal, utiliza SQLite como base de datos y GraphQL como interfaz de entrada.

## Requisitos Previos

1. **Docker**: Asegúrate de tener Docker instalado en tu sistema.
3. **Git**: Recomendado para clonar el respositorio en tu máquina.

## Instalación

### 1. Clonar el Repositorio

Clona este repositorio en tu máquina local:

```bash
git clone https://github.com/MrEstebban/proyecto-django-graphql-hexagonal
cd proyecto-django-graphql-hexagonal
```

### 2. Construir la Imagen Docker

Primero, asegúrate de estar en el directorio donde se encuentra tu `Dockerfile`. Luego, ejecuta el siguiente comando para construir la imagen Docker:

```sh
docker build -t proyecto-django-graphql .
```


### 3. Ejecutar el Contenedor Docker

Una vez que la imagen Docker se haya construido correctamente, puedes ejecutar el contenedor con el siguiente comando:

```bash
docker run -p 8000:8000 proyecto-django-graphql
```

La API estará disponible en el navegador en la dirección `http://127.0.0.1:8000/graphql`

## Uso de la API GraphQL

Puedes acceder al playground de GraphQL en `http://127.0.0.1:8000/graphql`. Desde ahí podrás ejecutar consultas y mutaciones para interactuar con el sistema de estudiantes y notas.

### Consultas Ejemplo

#### Obtener todos los estudiantes y notas:

```graphql
query{
  allStudents {
    id
    firstName
    lastName
    email
  }
  allGrades{
    id
    studentId
    subject
    grade
  }
}
```

#### Crear un nuevo estudiante:

```graphql
mutation{
  createStudent(
    studentId: "2",
    firstName: "Mariana",
    lastName: "Suarez",
    email: "mariana@gmail.com"
  ){
    student{
      id
      firstName
      lastName
      email
    }
  }
}
```

#### Crear una nueva nota:

```graphql
mutation{
  createGrade(
    gradeId: "3",
    studentId: "1",
    subject: "Inglés",
    grade: 5.0
  ){
    grade{
      id
      studentId
      subject
      grade
    }
  }
  
}
```

#### Eliminar un estudiante

```graphql
mutation{
  deleteStudent(studentId: "1")
  {
    message
  }
}
```

#### Eliminar una nota

```graphql
mutation{
  deleteGrade(gradeId: "1")
  {
    message
  }
}
```

#### Actualizar información de estudiante

```graphql
mutation{
  updateStudent(
    studentId: "2"
    email: "mariana@gmail.com",
    firstName: "Mariana",
    lastName: "Smith"
  )
  {
    student
    {
      id
      firstName
      lastName
      email
    }
  }
}
```

#### Actualizar información de nota
```graphql
mutation {
  updateGrade(
    gradeId: "2",
    studentId: "1",
    subject: "Fisica",
    grade: 4.5
  ) {
    grade {
      id
      studentId
      subject
      grade
    }
  }
}
```
