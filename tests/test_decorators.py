import pytest
from src.decorators import log


# --- Сценарии для консоли (без filename) ---
def test_log_console_success(capsys):
    """Проверка успешного выполнения функции с выводом в консоль."""

    @log()
    def add(x, y):
        return x + y

    add(1, 2)
    captured = capsys.readouterr()
    assert captured.out.strip() == "add ok"


def test_log_console_error(capsys):
    """Проверка логирования ошибки в консоль."""

    @log()
    def divide(x, y):
        return x / y

    with pytest.raises(ZeroDivisionError):
        divide(10, 0)

    captured = capsys.readouterr()
    # Проверяем формат: имя_функции error: тип_ошибки. Inputs: (args), {kwargs}
    assert "divide error: ZeroDivisionError. Inputs: (10, 0), {}" in captured.out


# --- Сценарии для файла (с аргументом filename) ---
def test_log_file_success(tmp_path):
    """Проверка записи успешного результата в файл."""
    log_file = tmp_path / "test_log.txt"

    @log(filename=str(log_file))
    def multiply(x, y):
        return x * y

    multiply(3, 4)

    with open(log_file, "r", encoding="utf-8") as f:
        content = f.read().strip()

    assert content == "multiply ok"


def test_log_file_error(tmp_path):
    """Проверка записи ошибки в файл."""
    log_file = tmp_path / "error_log.txt"

    @log(filename=str(log_file))
    def get_element(lst, index):
        return lst[index]

    with pytest.raises(IndexError):
        get_element([1, 2], 5)

    with open(log_file, "r", encoding="utf-8") as f:
        content = f.read().strip()

    assert "get_element error: IndexError. Inputs: ([1, 2], 5), {}" in content


def test_log_preserves_metadata():
    """Проверка, что декоратор сохраняет имя и документацию функции."""

    @log()
    def my_test_func():
        """Docstring."""
        return True

    assert my_test_func.__name__ == "my_test_func"
    assert my_test_func.__doc__ == "Docstring."
