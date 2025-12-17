import pytest

@pytest.fixture(autouse=True)
def db_connection():
    print(" Initiated connection to database ")
    yield
    print(" Closing db connection ")