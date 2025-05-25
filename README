# Learning Logging 📚

Un proyecto de aprendizaje para implementar logging efectivo en aplicaciones FastAPI con SQLModel, enfocado en el manejo de excepciones y mejores prácticas de desarrollo.

## 🎯 Objetivo del Proyecto

Este proyecto fue creado como práctica para aprender:
- Configuración avanzada de logging en Python
- Manejo de excepciones en FastAPI
- Operaciones CRUD completas con SQLModel
- Buenas prácticas de desarrollo de APIs REST

## 🛠️ Tecnologías Utilizadas

- **FastAPI** - Framework web moderno para Python
- **SQLModel** - ORM moderno basado en SQLAlchemy y Pydantic
- **Poetry** - Gestión de dependencias y entornos virtuales
- **Uvicorn** - Servidor ASGI para desarrollo
- **Python 3.12** - Versión de Python utilizada

## 📁 Estructura del Proyecto

```
learning_logging/
├── app/
│   ├── core/
│   │   └── logger.py          # Configuración de logging
│   ├── logs/
│   │   └── app.log           # Archivo de logs
│   ├── __init__.py
│   ├── main.py               # Aplicación FastAPI principal
│   ├── models.py             # Modelos SQLModel
│   ├── crud.py               # Operaciones CRUD
│   └── database.py           # Configuración de base de datos
├── pyproject.toml            # Configuración de Poetry
└── README.md
```

## 🚀 Instalación y Configuración

### Prerrequisitos
- Python 3.12+
- Poetry (recomendado) o pip

### 1. Clonar el repositorio
```bash
git clone https://github.com/tu-usuario/learning_logging.git
cd learning_logging
```

### 2. Instalar dependencias con Poetry
```bash
poetry install
```

### 3. Activar el entorno virtual
```bash
poetry shell
```

### 4. Ejecutar la aplicación
```bash
poetry run uvicorn app.main:app --reload
```

La aplicación estará disponible en: http://127.0.0.1:8000

## 📖 Documentación de la API

Una vez que la aplicación esté ejecutándose, puedes acceder a:

- **Swagger UI**: http://127.0.0.1:8000/docs
- **ReDoc**: http://127.0.0.1:8000/redoc

## 🔧 Endpoints Disponibles

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| `GET` | `/items/` | Obtener todos los ítems |
| `GET` | `/items/{id}` | Obtener un ítem específico |
| `POST` | `/items/` | Crear un nuevo ítem |
| `PATCH` | `/items/{id}` | Actualizar parcialmente un ítem |
| `DELETE` | `/items/{id}` | Eliminar un ítem |

### Ejemplos de uso:

#### Crear un ítem
```bash
curl -X POST "http://127.0.0.1:8000/items/" \
     -H "Content-Type: application/json" \
     -d '{"name": "Mi Producto", "description": "Descripción del producto"}'
```

#### Actualizar parcialmente
```bash
curl -X PATCH "http://127.0.0.1:8000/items/1" \
     -H "Content-Type: application/json" \
     -d '{"name": "Producto Actualizado"}'
```

## 📊 Sistema de Logging

### Características principales:
- **Rotación automática** de archivos de log (máx. 5MB por archivo)
- **Backup automático** (mantiene 3 archivos históricos)
- **Soporte UTF-8** completo para caracteres especiales y acentos
- **Dual output**: consola y archivo
- **Niveles configurables**: INFO, WARNING, ERROR

### Configuración del Logger:
```python
# Ubicación: app/core/logger.py
- Archivos de log en: app/logs/app.log
- Formato: 'YYYY-MM-DD HH:MM:SS | LEVEL | LOGGER | MESSAGE'
- Encoding: UTF-8 (maneja acentos correctamente)
```

## 🛡️ Manejo de Excepciones

El proyecto implementa un sistema robusto de manejo de excepciones:

### Niveles de manejo:
1. **Excepciones de CRUD personalizadas** (`ItemCRUDError`)
2. **Excepciones de SQLAlchemy** (errores de base de datos)
3. **Excepciones HTTP** (códigos de estado apropiados)
4. **Rollback automático** en transacciones fallidas

### Códigos de estado HTTP:
- `200` - OK (consultas exitosas)
- `201` - Created (ítem creado)
- `204` - No Content (eliminación exitosa)
- `400` - Bad Request (errores de validación)
- `404` - Not Found (ítem no encontrado)
- `500` - Internal Server Error (errores del servidor)

## 🧪 Funcionalidades de Aprendizaje

### 1. **Logging Avanzado**
- Configuración de `RotatingFileHandler`
- Manejo de encoding UTF-8
- Formateo personalizado de mensajes
- Separación de logs por nivel

### 2. **CRUD Completo**
- Operaciones Create, Read, Update, Delete
- Validación de datos con Pydantic
- Manejo de relaciones con SQLModel

### 3. **Manejo de Errores**
- Try-catch específicos por tipo de error
- Logging de errores para debugging
- Respuestas HTTP apropiadas

### 4. **Buenas Prácticas**
- Separación de responsabilidades
- Código documentado
- Type hints
- Estructura modular

## 📝 Notas de Desarrollo

### Problemas resueltos durante el desarrollo:

1. **Imports relativos**: Configuración correcta de la estructura de módulos
2. **Encoding UTF-8**: Manejo de acentos en logs
3. **Excepciones SQLAlchemy**: Rollback automático en errores
4. **Documentación automática**: Schemas y response models

### Lecciones aprendidas:
- Importancia del encoding en sistemas de logging
- Diferencias entre PUT y PATCH en APIs REST
- Configuración de Poetry para proyectos FastAPI
- Manejo de sesiones de base de datos

## 🤝 Contribuciones

Este es un proyecto de aprendizaje personal, pero las sugerencias y mejoras son bienvenidas.

## 📄 Licencia

Este proyecto está bajo la Licencia MIT - ver el archivo LICENSE para más detalles.

## 🙏 Agradecimientos

- Documentación oficial de FastAPI
- Comunidad de SQLModel
- Recursos de aprendizaje de Python logging

---

*Proyecto creado con fines educativos - 2025*