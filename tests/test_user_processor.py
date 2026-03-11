import pytest
import requests
from src.user_processor import get_user_full_name


def test_get_user_full_name_success(mocker):
    # --- Фаза подготовки (Arrange) ---

    # 1. Создаем "фальшивый" объект ответа, который имитирует
    #    успешный ответ от `requests`.
    #    У него должен быть метод .json() и .raise_for_status()
    mock_response = mocker.Mock()
    mock_response.raise_for_status.return_value = None  # Метод ничего не делает
    mock_response.json.return_value = {
        "data": {
            "id": 2,
            "email": "janet.weaver@reqres.in",
            "first_name": "Janet",
            "last_name": "Weaver"
        }
    }

    # 2. Патчим `requests.get`. Путь к нему указывается там,
    #    ГДЕ ОН ИСПОЛЬЗУЕТСЯ (`src.user_processor.requests.get`).
    #    Мы говорим, что при вызове он должен вернуть наш `mock_response`.
    mocker.patch("src.user_processor.requests.get", return_value=mock_response)

    # --- Фаза действия (Act) ---

    # 3. Вызываем нашу функцию. Она "думает", что делает реальный запрос,
    #    но на самом деле получает наш `mock_response`.
    full_name = get_user_full_name(2)

    # --- Фаза проверки (Assert) ---

    # 4. Проверяем, что наша функция правильно обработала
    #    подсунутые ей данные.
    assert full_name == "Janet Weaver"


def test_get_user_full_name_api_error(mocker):
    # Настраиваем мок так, чтобы он вызывал ошибку,
    # как это делает реальный `requests`.
    mocker.patch(
        "src.user_processor.requests.get",
        side_effect=requests.exceptions.RequestException("API is down")
    )

    # Проверяем, что наша функция корректно "пробрасывает"
    # эту ошибку наверх.
    with pytest.raises(requests.exceptions.RequestException):
        get_user_full_name(123)
