# API Ferremas

# 📄 Estructura de Archivos y Funciones

| Archivo | Función Principal |
|:---|:---|
| app.py | Crea app Flask, configura MySQL, registra rutas |
| routes/routes.py | Define rutas HTTP (endpoints) |
| services/user_service.py | Lógica de negocio de usuarios |
| services/product_service.py | Lógica de negocio de productos |
| models/user.py | Define la entidad User |
| models/product.py | Define la entidad Product |
| db/database.py | Conecta a MySQL |
| utils/helpers.py | Helpers (vacío, para usar después) |

---

# 📄 Detalle de Cada Archivo

## 1. 📄 app.py
- Es el archivo principal que inicia toda la aplicación.
- Configura el servidor Flask.
- Configura la conexión a MySQL.
- Llama a `register_routes` para registrar las rutas.

## 2. 📂 api/routes/routes.py
- Define los **endpoints HTTP**.
- Cada ruta llama al **servicio correspondiente** para obtener o procesar datos.
- No hace lógica pesada aquí, solo recibe y responde.

## 3. 📂 api/services/user_service.py y api/services/product_service.py
- Contienen la **lógica de negocio**:
  - Consultar todos los usuarios.
  - Consultar todos los productos.
- Se conectan a **MySQL** usando el `cursor`.
- Devuelven los resultados en forma de **objetos (modelos)**.

## 4. 📂 api/models/user.py y api/models/product.py
- Modelan los datos:
  - Definen qué campos tiene un `User` (id, name, email).
  - Definen qué campos tiene un `Product` (id, name, price).
- Tienen un método `to_dict()` para convertir los objetos a JSON (util para respuestas de API).

## 5. 📂 api/db/database.py
- Se encarga de **crear la conexión a MySQL** usando `Flask-MySQLdb`.
- Define `init_db(app)` para inicializar el cliente de MySQL.

## 6. 📂 api/utils/helpers.py
- Actualmente **está vacío**, pero reservado para:
  - Funciones auxiliares futuras.
  - Validaciones, formateos de datos, helpers de errores, etc.