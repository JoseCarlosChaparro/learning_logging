from fastapi import FastAPI, Depends, HTTPException, status
from sqlmodel import Session
from typing import List, Optional
from app.models import Item
from app.crud import (
    create_item, 
    get_items, 
    get_item_by_id,
    update_item,
    delete_item,
    ItemCRUDError
)
from app.core.logger import logger
from app.database import get_session, init_db

app = FastAPI()

@app.on_event("startup")
def on_startup():
    try:
        init_db()
        logger.info("Base de datos inicializada")
    except Exception as e:
        logger.error(f"Error al inicializar la base de datos: {str(e)}")
        raise

@app.post("/items/", response_model=Item, status_code=status.HTTP_201_CREATED)
def create(item: Item, session: Session = Depends(get_session)):
    """Crear un nuevo ítem"""
    try:
        return create_item(session, item)
    except ItemCRUDError as e:
        logger.error(f"Error en endpoint create: {str(e)}")
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    except Exception as e:
        logger.error(f"Error inesperado en endpoint create: {str(e)}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error interno del servidor")

@app.get("/items/", response_model=List[Item])
def read_all(session: Session = Depends(get_session)):
    """Obtener todos los ítems"""
    try:
        return get_items(session)
    except ItemCRUDError as e:
        logger.error(f"Error en endpoint read_all: {str(e)}")
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    except Exception as e:
        logger.error(f"Error inesperado en endpoint read_all: {str(e)}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error interno del servidor")

@app.get("/items/{item_id}", response_model=Item)
def read_one(item_id: int, session: Session = Depends(get_session)):
    """Obtener un ítem por su ID"""
    try:
        item = get_item_by_id(session, item_id)
        if not item:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, 
                detail=f"Ítem con ID {item_id} no encontrado"
            )
        return item
    except HTTPException:
        raise  # Re-lanza HTTPException tal como está
    except ItemCRUDError as e:
        logger.error(f"Error en endpoint read_one: {str(e)}")
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    except Exception as e:
        logger.error(f"Error inesperado en endpoint read_one: {str(e)}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error interno del servidor")

@app.put("/items/{item_id}", response_model=Item)
def update(item_id: int, item_data: dict, session: Session = Depends(get_session)):
    """Actualizar un ítem existente"""
    try:
        updated_item = update_item(session, item_id, item_data)
        if not updated_item:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, 
                detail=f"Ítem con ID {item_id} no encontrado"
            )
        return updated_item
    except HTTPException:
        raise  # Re-lanza HTTPException tal como está
    except ItemCRUDError as e:
        logger.error(f"Error en endpoint update: {str(e)}")
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    except Exception as e:
        logger.error(f"Error inesperado en endpoint update: {str(e)}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error interno del servidor")

@app.delete("/items/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete(item_id: int, session: Session = Depends(get_session)):
    """Eliminar un ítem"""
    try:
        deleted = delete_item(session, item_id)
        if not deleted:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, 
                detail=f"Ítem con ID {item_id} no encontrado"
            )
        return None  # 204 No Content no devuelve body
    except HTTPException:
        raise  # Re-lanza HTTPException tal como está
    except ItemCRUDError as e:
        logger.error(f"Error en endpoint delete: {str(e)}")
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    except Exception as e:
        logger.error(f"Error inesperado en endpoint delete: {str(e)}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error interno del servidor")