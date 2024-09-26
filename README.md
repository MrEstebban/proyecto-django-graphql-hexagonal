
# Proyecto Django con Arquitectura Hexagonal, Cassandra y GraphQL

Este proyecto utiliza Django para construir una API que sigue la arquitectura hexagonal, utiliza Cassandra como base de datos y GraphQL como interfaz de entrada.

### Arquitectura Hexagonal (o Puertos y Adaptadores)

La **arquitectura hexagonal**, también conocida como **arquitectura de puertos y adaptadores**, es un estilo arquitectónico que promueve la separación de la lógica de negocio de una aplicación de los detalles de implementación de los componentes externos. Esto se logra mediante la definición de interfaces (puertos) y la implementación de estas interfaces en componentes específicos (adaptadores).

#### ¿Cómo Funciona?

1. **Dominio (Núcleo o Core):** Aquí se encuentra toda la lógica de negocio de la aplicación, sin dependencia de ningún framework, base de datos o sistema externo.
2. **Puertos:** Son interfaces que definen cómo los componentes externos (como bases de datos, APIs externas, interfaces de usuario) interactúan con la lógica de negocio. Hay dos tipos principales:
   * **Puertos de Entrada:** Para recibir datos externos y enviarlos a la lógica de negocio. Ejemplos: controladores HTTP, clientes GraphQL, CLI.
   * **Puertos de Salida:** Para enviar datos desde la lógica de negocio a componentes externos. Ejemplos: repositorios para bases de datos, APIs externas.
3. **Adaptadores:** Implementan los puertos, traduciéndolos a tecnologías específicas. Ejemplos: un adaptador que traduce un puerto de entrada en un controlador GraphQL, o un puerto de salida en un repositorio Cassandra.

## Requisitos Previos

1. **Python 3.9+**: Asegúrate de tener Python instalado en tu sistema.
2. **Cassandra**: Instala y configura Cassandra. Puedes seguir las [instrucciones oficiales](https://cassandra.apache.org/_/quickstart.html).
3. **Virtualenv**: Recomendado para crear un entorno virtual aislado.

## Instalación

### 1. Clonar el Repositorio

Clona este repositorio en tu máquina local:

```bash
git clone https://github.com/MrEstebban/proyecto-django-arqui-hex
cd proyecto-django-arqui-hex
```

### 2. Crear y Activar un Entorno Virtual

```bash
python -m venv venv
source env/bin/activate  # En Windows: env\Scripts\activate
```

### 3. Instalar Dependencias

Instala los paquetes requeridos utilizando el archivo `requirements.txt`:

```bash
pip install -r requirements.txt
```

### 4. Configurar Variables de Entorno

Crea un archivo `.env` en la raíz del proyecto con la siguiente estructura:

```
SECRET_KEY=django-insecure-your-secret-key
DEBUG=True
DATABASE_NAME=school
DATABASE_HOST=127.0.0.1
DATABASE_PORT=9042
DATABASE_USER=cassandra_user
DATABASE_PASSWORD=cassandra_password
```

Asegúrate de actualizar los valores según tu configuración de Cassandra.

### 5. Migraciones de Base de Datos

Ejecuta el siguiente comando para sincronizar las tablas de Cassandra con los modelos de Django:

```bash
python manage.py sync_cassandra
```

### 6. Ejecutar el Servidor de Desarrollo

Inicia el servidor de desarrollo de Django:

```bash
python manage.py runserver
```

La API estará disponible en `http://127.0.0.1:8000/graphql`.

## Uso de la API GraphQL

Puedes acceder al playground de GraphQL en `http://127.0.0.1:8000/graphql`. Desde ahí podrás ejecutar consultas y mutaciones para interactuar con el sistema de estudiantes y notas.

### Consultas Ejemplo

#### Obtener todos los estudiantes:

```graphql
query {
  students {
    id
    firstName
    lastName
    email
  }
}
```

#### Crear un nuevo estudiante:

```graphql
mutation {
  createStudent(id: "1", firstName: "John", lastName: "Doe", email: "john@example.com") {
    student {
      id
      firstName
      lastName
      email
    }
  }
}
```