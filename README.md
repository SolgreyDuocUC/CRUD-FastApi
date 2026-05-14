# API Robust User CRUD - FastAPI

Este proyecto es una implementación profesional de una API RESTful para la gestión de usuarios, desarrollada con FastAPI, SQLAlchemy y Pydantic. Sigue una arquitectura modular diseñada para ser escalable y mantenible.

## Funcionalidades Principales

- Operaciones CRUD completas (Crear, Leer, Actualizar, Eliminar).
- Validación de datos exhaustiva con Pydantic.
- Persistencia de datos mediante SQLAlchemy ORM (SQLite por defecto).
- Hasheo de contraseñas seguro con bcrypt.
- Documentación interactiva automática (Swagger UI y ReDoc).
- Estructura de carpetas basada en el patrón Repositorio-Servicio.

## Requisitos del Sistema

- Python 3.12 o superior.
- Administrador de paquetes pip.
- (Opcional) Entorno virtual configurado.

## Instalación y Configuración

Siga estos pasos de forma secuencial para poner en marcha el entorno de desarrollo:

1. **Clonar el repositorio o situarse en la carpeta raíz:**
   Asegúrese de estar en la carpeta donde se encuentra el archivo `requirements.txt`.

2. **Crear el entorno virtual (Recomendado):**

   ```powershell
   python -m venv venv
   ```

3. **Activar el entorno virtual:**

   - **En Windows:**

     ```powershell
     .\venv\Scripts\activate
     ```

   - **En Linux/macOS:**

     ```bash
     source venv/bin/activate
     ```

4. **Instalar dependencias:**

   ```powershell
   pip install -r requirements.txt
   ```

## Ejecución de la Aplicación

Existen diversas formas de iniciar el servidor dependiendo de sus necesidades:

### Opción A: Desde la raíz del proyecto (Uso Estándar)

Este es el método recomendado para desarrollo con recarga automática:

```powershell
.\venv\Scripts\uvicorn main:app --reload --app-dir src
```

### Opción B: Ejecución directa del script principal

Útil para depuración rápida:

```powershell
python src/main.py
```

## Estructura del Proyecto

```text
CRUD FastApi/
├── src/
│   ├── config/         # Configuración de base de datos
│   ├── controllers/    # Definición de rutas y endpoints
│   ├── models/         # Modelos de SQLAlchemy (Base de datos)
│   ├── repositories/   # Lógica de acceso a datos
│   ├── schemas/        # Modelos de Pydantic (Validación)
│   ├── utils/          # Utilidades (Hasheo, etc.)
│   └── main.py         # Punto de entrada de la aplicación
├── requirements.txt    # Lista de dependencias
└── pyproject.toml      # Configuración del proyecto Python
```

## Errores Comunes y Soluciones

### 1. "uvicorn" no se reconoce como un comando

**Causa:** El entorno virtual no ha sido activado o uvicorn no se instaló correctamente.
**Solución:** Use la ruta completa: `.\venv\Scripts\uvicorn main:app --reload --app-dir src`.

### 2. ModuleNotFoundError: No module named 'src'

**Causa:** Las rutas de importación no coinciden con la raíz de ejecución.
**Solución:** Este proyecto ha sido estandarizado para usar la carpeta `src` como raíz de importación. Asegúrese de ejecutar los comandos desde la raíz del proyecto usando el flag `--app-dir src`.

### 3. ModuleNotFoundError: No module named 'sqlalchemy' (u otros paquetes)

**Causa:** No se han instalado las dependencias en el entorno virtual actual.
**Solución:** Ejecute `pip install -r requirements.txt` con el entorno virtual activo.

### 4. Errores de Base de Datos (SQLite)

**Causa:** Permisos de escritura denegados o archivo bloqueado.
**Solución:** Asegúrese de que el proceso de Python tiene permisos en la carpeta raíz para crear el archivo `sql_app.db`.

## Documentación de la API

Una vez iniciada la aplicación, puede acceder a la documentación interactiva en:

- **Swagger UI:** [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **ReDoc:** [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)
"# CRUD-FastApi" 
