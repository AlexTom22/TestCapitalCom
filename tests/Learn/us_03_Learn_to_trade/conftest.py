import pytest
from datetime import datetime

# URL = "https://capital.com/learn-to-trade"


@pytest.fixture(
    scope="class",
    params=[
        # "ar",
        # "bg",
        # "cn",
        # "cs",
        # "da",
        # "de",
        # "el",
        "",  # "en"
        # "es",
        # "et",
        # "fi",
        # "fr",
        # "hr",
        # "hu",
        # "id",
        # "it",
        # "lt",
        # "lv",
        # "nl",
        # "pl",
        # "pt",
        # "ro",
        # "ru",
        # "sk",
        # "sl",
        # "sv",
        # "th",
        # "vi",
        # "zh",
    ],
)
# Выбор языка
def cur_language(request):
    print(f"Current test language - {request.param}")
    return request.param


# Выбор лицензии
@pytest.fixture(
    scope="class",
    params=[
        # "ASIC",
        "FCA",
        # "CYSEC",
        # "NBRB",
        # "CCSTV",
        # "SEY",
        # "BAH",
    ],
)
def cur_license(request):
    print(f"Current test license - {request.param}")
    return request.param


# Выбор роли
@pytest.fixture(
    scope="class",
    params=[
        "NoReg",
        # "Reg_NoAuth",
        # "Auth",
    ],
)
def cur_role(request):
    print(f"Current test role - {request.param}")
    return request.param


# Тайм штамп
@pytest.fixture()
def datetime_now():
    return str(datetime.now())
