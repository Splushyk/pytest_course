from src.file_checker import check_if_file_exists


def test_file_exists_when_mock_returns_true(mocker):
    # 1. Запрашиваем фикстуру mocker

    # 2. "Патчим" (заменяем) функцию os.path.exists.
    #    Мы хотим, чтобы она всегда возвращала True.
    mocker.patch('os.path.exists', return_value=True)

    # 3. Вызываем наш код. Теперь, когда внутри check_if_file_exists
    #    будет вызван os.path.exists, на самом деле будет вызван наш мок.
    result = check_if_file_exists("/any/fake/path")

    # 4. Проверяем, что наша функция повела себя так,
    #    как будто файл действительно существует.
    assert result == "Файл /any/fake/path существует."


def test_file_not_exists_when_mock_returns_false(mocker):
    # В этом тесте мы хотим, чтобы os.path.exists вернула False
    mocker.patch('os.path.exists', return_value=False)

    result = check_if_file_exists("/another/fake/path")

    assert result == "Файл /another/fake/path не найден."