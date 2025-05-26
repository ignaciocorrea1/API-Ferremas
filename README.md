# **API Ferremas**

El desarrollo de una APIRestful permitirá a Ferremas la comunicación con su base de datos interna como también la integración con sistemas externos, tales como Transbank para el proceso de pago y Mindicador para la conversión de divisas. 

## Tecnologías utilizadas 📖

La API fue desarrollada con las siguientes tecnologías:

1. **Flask:** Framework de Python que permite crear aplicaciones web y APIS Restful de forma rápida, sencilla y modular.

## Arquitectura utilizada 🏛️

La API de ferremas se basa en una arquitectura limpia, la idea principal detrás de esta arquitectura es separar las preocupaciones en diferentes capas bien definidas, con reflas estrictas sobre cómo deben interactuar entre sí.

La arquitectura limpia se separa de la siguiente forma:

- **Capa de Entidades (Entities):** Contiene las entidades centrales y los objetos del negocio. Son clases o estructuras que encapsulan los datos principales del negocio.
  
- **Capa de Casos de Uso (Use Cases):** Contiene la lógica de la aplicación y coordina la interacción entre las entidades. Encapsulan la lógica de negocio específica para cada función o acción que debe realizar la aplicación.
  
- **Capa de Interfaces:** Esta capa conecta la lógica interna del sistema con lo exterior. Además, convierten los datos entre el formato que utiliza el exterior y el de las capas internas. 

- **Capa de Infraestructura:** Es la capa más externa y se encuentran los accesos a base de datos, servicios externos, frameworks, bibliotecas, etc.

![Imagen de como es la Arquitectura limpia](https://i.blogs.es/28531a/clean/450_1000.webp)

## Requisitos previos 🔧

Es necesario que tengas los siguientes programas instalados para que el proyecto se ejecute correctamente:

- ``` Python 3.13.1+ ```

- ``` Pip 25.1.1+ ```
  
- ``` Flask 3.1.0+ ```

Para verificar que los tengas:

1. Abre la terminal y verifica la instalación de **Python** con **"python --version"**
2. En la terminal, verifica la instalación de **Pip** con **"pip --version"**
3. En la terminal, verifica la instalación de **Flask** con **"Flask --version"**

## Ejecución 🚀

Sigue los siguientes pasos para instalar las dependencias del proyecto:

1. Abre la terminal y verifica que en la carpeta en que te encuentras se encuentran los files requirements.txt y app.y con: "ls" o "dir".
2. Ejecuta el comando **"pip install -r requirements.txt"**.
2. Ejecuta el comando **"python app.py"** para iniciar la aplicación

> [!WARNING]
> Para que puedas ver los productos es necesario crear la base de datos en MySQL, el script para su creación se encuentra en el mismo directorio, "script_ferremas.sql".


## Integrantes 🤝

- Joaquín Armijo
- Ignacio Correa
- Fernando Flores
- Jaime Vergara
