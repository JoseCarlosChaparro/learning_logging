from sqlmodel import Session, select
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from app.models import Item
from app.core.logger import logger
from typing import List, Optional

class ItemCRUDError(Exception):
    """Excepción personalizada para operaciones CRUD de Item"""
    pass

def create_item(session: Session, item: Item) -> Item:
    """
    Crea un nuevo ítem en la base de datos
    
    Args:
        session: Sesión de la base de datos
        item: Ítem a crear
        
    Returns:
        Item: El ítem creado con su ID asignado
        
    Raises:
        ItemCRUDError: Si hay un error al crear el ítem
    """
    try:
        logger.info(f"Creando ítem: {item.name}")
        session.add(item)
        session.commit()
        session.refresh(item)
        logger.info(f"Ítem creado exitosamente con ID: {item.id}")
        return item
        
    except IntegrityError as e:
        session.rollback()
        error_msg = f"Error de integridad al crear ítem '{item.name}': {str(e)}"
        logger.error(error_msg)
        raise ItemCRUDError(error_msg) from e
        
    except SQLAlchemyError as e:
        session.rollback()
        error_msg = f"Error de base de datos al crear ítem '{item.name}': {str(e)}"
        logger.error(error_msg)
        raise ItemCRUDError(error_msg) from e
        
    except Exception as e:
        session.rollback()
        error_msg = f"Error inesperado al crear ítem '{item.name}': {str(e)}"
        logger.error(error_msg)
        raise ItemCRUDError(error_msg) from e

def get_items(session: Session) -> List[Item]:
    """
    Obtiene todos los ítems de la base de datos
    
    Args:
        session: Sesión de la base de datos
        
    Returns:
        List[Item]: Lista de todos los ítems
        
    Raises:
        ItemCRUDError: Si hay un error al consultar los ítems
    """
    try:
        logger.info("Consultando todos los ítems")
        items = session.exec(select(Item)).all()
        logger.info(f"Se encontraron {len(items)} ítems")
        return items
        
    except SQLAlchemyError as e:
        error_msg = f"Error de base de datos al consultar ítems: {str(e)}"
        logger.error(error_msg)
        raise ItemCRUDError(error_msg) from e
        
    except Exception as e:
        error_msg = f"Error inesperado al consultar ítems: {str(e)}"
        logger.error(error_msg)
        raise ItemCRUDError(error_msg) from e

def get_item_by_id(session: Session, item_id: int) -> Optional[Item]:
    """
    Obtiene un ítem por su ID
    
    Args:
        session: Sesión de la base de datos
        item_id: ID del ítem a buscar
        
    Returns:
        Optional[Item]: El ítem encontrado o None si no existe
        
    Raises:
        ItemCRUDError: Si hay un error al consultar el ítem
    """
    try:
        logger.info(f"Consultando ítem con ID: {item_id}")
        item = session.get(Item, item_id)
        
        if item:
            logger.info(f"Ítem encontrado: {item.name}")
        else:
            logger.info(f"No se encontró ítem con ID: {item_id}")
            
        return item
        
    except SQLAlchemyError as e:
        error_msg = f"Error de base de datos al consultar ítem con ID {item_id}: {str(e)}"
        logger.error(error_msg)
        raise ItemCRUDError(error_msg) from e
        
    except Exception as e:
        error_msg = f"Error inesperado al consultar ítem con ID {item_id}: {str(e)}"
        logger.error(error_msg)
        raise ItemCRUDError(error_msg) from e

def update_item(session: Session, item_id: int, item_data: dict) -> Optional[Item]:
    """
    Actualiza un ítem existente
    
    Args:
        session: Sesión de la base de datos
        item_id: ID del ítem a actualizar
        item_data: Datos a actualizar
        
    Returns:
        Optional[Item]: El ítem actualizado o None si no existe
        
    Raises:
        ItemCRUDError: Si hay un error al actualizar el ítem
    """
    try:
        logger.info(f"Actualizando ítem con ID: {item_id}")
        item = session.get(Item, item_id)
        
        if not item:
            logger.warning(f"No se encontró ítem con ID: {item_id} para actualizar")
            return None
            
        # Actualizar solo los campos proporcionados
        for field, value in item_data.items():
            if hasattr(item, field):
                setattr(item, field, value)
                
        session.add(item)
        session.commit()
        session.refresh(item)
        
        logger.info(f"Ítem actualizado exitosamente: {item.name}")
        return item
        
    except IntegrityError as e:
        session.rollback()
        error_msg = f"Error de integridad al actualizar ítem con ID {item_id}: {str(e)}"
        logger.error(error_msg)
        raise ItemCRUDError(error_msg) from e
        
    except SQLAlchemyError as e:
        session.rollback()
        error_msg = f"Error de base de datos al actualizar ítem con ID {item_id}: {str(e)}"
        logger.error(error_msg)
        raise ItemCRUDError(error_msg) from e
        
    except Exception as e:
        session.rollback()
        error_msg = f"Error inesperado al actualizar ítem con ID {item_id}: {str(e)}"
        logger.error(error_msg)
        raise ItemCRUDError(error_msg) from e

def delete_item(session: Session, item_id: int) -> bool:
    """
    Elimina un ítem por su ID
    
    Args:
        session: Sesión de la base de datos
        item_id: ID del ítem a eliminar
        
    Returns:
        bool: True si se eliminó exitosamente, False si no existía
        
    Raises:
        ItemCRUDError: Si hay un error al eliminar el ítem
    """
    try:
        logger.info(f"Eliminando ítem con ID: {item_id}")
        item = session.get(Item, item_id)
        
        if not item:
            logger.warning(f"No se encontró ítem con ID: {item_id} para eliminar")
            return False
            
        session.delete(item)
        session.commit()
        
        logger.info(f"Ítem eliminado exitosamente: {item.name}")
        return True
        
    except SQLAlchemyError as e:
        session.rollback()
        error_msg = f"Error de base de datos al eliminar ítem con ID {item_id}: {str(e)}"
        logger.error(error_msg)
        raise ItemCRUDError(error_msg) from e
        
    except Exception as e:
        session.rollback()
        error_msg = f"Error inesperado al eliminar ítem con ID {item_id}: {str(e)}"
        logger.error(error_msg)
        raise ItemCRUDError(error_msg) from e