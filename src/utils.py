import json
import logging
import os
from typing import Any, Dict, List

# 1. Настройка путей (ИСПРАВЛЕНО: добавлено определение log_dir)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
log_dir = os.path.join(BASE_DIR, "..", "logs")
os.makedirs(log_dir, exist_ok=True)
log_path = os.path.join(log_dir, "utils.log")

# 2. Создание и настройка логера
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Очищаем старые хендлеры и настраиваем новые
if logger.hasHandlers():
    logger.handlers.clear()

file_handler = logging.FileHandler(log_path, mode='w', encoding='utf-8')
file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_transactions_from_json(file_path: str) -> List[Dict[str, Any]]:
    """Читает транзакции из JSON-файла. При любой ошибке возвращает []."""
    logger.info(f"Запрос на чтение транзакций из: {file_path}")

    if not os.path.exists(file_path):
        logger.error(f"Файл не найден по пути: {file_path}")
        return []

    try:
        # Проверка на пустой файл
        if not os.path.exists(file_path) or os.path.getsize(file_path) == 0:
            logger.error(f"Файл {file_path} пуст или не существует")
            return []

        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            if isinstance(data, list):
                logger.info(f"Успешно загружено {len(data)} транзакций")
                return data

            logger.error(f"Данные в {file_path} не являются списком")
            return []

    except (json.JSONDecodeError, OSError) as e:
        logger.error(f"Произошла ошибка при чтении файла {file_path}: {e}")
        return []

    return []