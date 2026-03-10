import os


def check_if_file_exists(filepath):
    """Проверяет существование файла и возвращает текстовое описание."""
    if os.path.exists(filepath):
        return f"Файл {filepath} существует."
    else:
        return f"Файл {filepath} не найден."
