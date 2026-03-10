# Ничего импортировать для tmp_path не нужно!

def test_file_creation_and_reading(tmp_path):
    # tmp_path - это объект pathlib.Path, указывающий на временную папку
    # Например: /tmp/pytest-of-user/pytest-0/test_file_creation_and_reading0
    print(f"Временная папка: {tmp_path}")

    # Создаем поддиректорию внутри временной папки
    data_dir = tmp_path / "data" # Удобный синтаксис pathlib для соединения путей
    data_dir.mkdir()

    # Создаем путь к нашему файлу
    file_path = data_dir / "my_file.txt"

    # Записываем в файл текст с помощью удобного метода
    file_path.write_text("Hello from tmp_path!")

    # Проверяем, что файл существует и содержит правильный текст
    assert file_path.exists()
    assert file_path.read_text() == "Hello from tmp_path!"

# Вам не нужно писать НИКАКОГО кода для очистки. Pytest сделает все за вас.