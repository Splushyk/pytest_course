def greet(name):
    """Печатает приветствие в консоль."""
    print(f"Hello, {name}!")


def test_greet_prints_correct_output(capsys):
    # 1. Запрашиваем фикстуру

    # 2. Вызываем функцию, которая печатает в консоль
    greet("World")

    # 3. "Читаем" всё, что было захвачено
    captured = capsys.readouterr()

    # 4. Проверяем, что захваченный stdout соответствует ожиданиям
    assert captured.out == "Hello, World!\n"


def test_another_greet(capsys):
    greet("Alice")
    captured = capsys.readouterr()
    assert captured.out == "Hello, Alice!\n"
    # Проверяем, что в stderr ничего не попало
    assert captured.err == ""