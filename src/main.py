from fastapi import FastAPI
from config.database import engine, Base
from controllers import user_controller

# =========================================
# Inicialización de Base de Datos
# =========================================
# Esto crea las tablas si no existen
Base.metadata.create_all(bind=engine)

# =========================================
# Inicialización de FastAPI
# =========================================
app = FastAPI(
    title="API Robust User CRUD",
    description="Backend con FastAPI, SQLAlchemy y Pydantic",
    version="1.0.0"
)

# =========================================
# Registro de Routers
# =========================================
app.include_router(user_controller.router)


# =========================================
# HOME
# =========================================
@app.get("/", tags=["Home"])
def home():
    return {
        "mensaje": "Bienvenido a la API de Usuarios Robusta",
        "docs": "/docs"
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
