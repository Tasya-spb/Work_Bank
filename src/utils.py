import json
import os
from typing import Any, Dict, List


def get_transactions_from_json(file_path: str) -> List[Dict[str, Any]]:
    """Читает транзакции из JSON-файла. При любой ошибке возвращает []."""
    if not os.path.exists(file_path):
        return []

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            if isinstance(data, list):
                return data
            return []  # Если в файле не список (например, число или строка)
    except (json.JSONDecodeError, OSError):
        # ОЧЕНЬ ВАЖНО: здесь должен быть return [], а не просто pass или print
        return []
