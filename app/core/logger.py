import logging
from logging.handlers import RotatingFileHandler
import os
import sys

LOG_DIR = "app/logs"
os.makedirs(LOG_DIR, exist_ok=True)

logger = logging.getLogger("app_logger")
logger.setLevel(logging.INFO)

# Evitar duplicar handlers si ya están configurados
if not logger.handlers:
    formatter = logging.Formatter(
        '%(asctime)s | %(levelname)s | %(name)s | %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )

    # Handler para consola
    stream_handler = logging.StreamHandler(sys.stdout)
    stream_handler.setFormatter(formatter)
    stream_handler.setLevel(logging.INFO)

    # Handler para archivo con UTF-8 y rotación
    file_handler = RotatingFileHandler(
        filename=os.path.join(LOG_DIR, "app.log"),
        maxBytes=5_000_000,
        backupCount=3,
        encoding='utf-8'  # ¡Esta es la línea clave!
    )
    file_handler.setFormatter(formatter)
    file_handler.setLevel(logging.INFO)

    # Agregar handlers
    logger.addHandler(stream_handler)
    logger.addHandler(file_handler)

# Función de prueba para verificar que funciona
def test_logger():
    """Prueba el logger con caracteres especiales"""
    logger.info("=== PRUEBA DE LOGGER ===")
    logger.info("Caracteres con acentos: ñáéíóú ¿¡")
    logger.info("Creando ítem: Configuración")
    logger.warning("Advertencia con ñ: niño")
    logger.error("Error con información especial")
    logger.info("=== FIN PRUEBA ===")

# Ejecutar prueba si se ejecuta directamente
if __name__ == "__main__":
    test_logger()