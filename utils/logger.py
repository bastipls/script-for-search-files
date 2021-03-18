import logging
import os
from config import settings
def create_folder( name):
        # si la carpeta ya existe entonces no la crea de nuevo
        if not os.path.isdir(f"{settings.BASE_DIR}\\{name}"):
            path = os.path.join(f"{settings.BASE_DIR}\\", name)
            os.mkdir(path)
def setup_logger( name, log_file, level=logging.DEBUG):
        create_folder(name='logs')
        formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
        handler = logging.FileHandler(log_file)
        handler.setFormatter(formatter)
        logger = logging.getLogger(name)
        logger.setLevel(level)
        logger.addHandler(handler)
        return logger