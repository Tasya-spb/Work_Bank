import functools
from typing import Any, Callable, Optional


def log(filename: Optional[str] = None) -> Callable[[Callable[..., Any]], Callable[..., Any]]:

    def wrapper(func):
        @functools.wraps(func)
        def inner(*args, **kwargs):
            try:
                # Пытаемся выполнить функцию
                result = func(*args, **kwargs)
                log_message = f"{func.__name__} ok"
                return result
            except Exception as e:
                # Логируем ошибку, если она возникла
                log_message = (
                    f"{func.__name__} error: {type(e).__name__}. "
                    f"Inputs: {args}, {kwargs}"
                )
                raise e  # Пробрасываем ошибку дальше
            finally:
                # Записываем результат в файл или консоль
                if filename:
                    with open(filename, "a", encoding="utf-8") as f:
                        f.write(log_message + "\n")
                else:
                    print(log_message)
        return inner
    return wrapper
