import pytest

@pytest.fixture(autouse=True, scope="session")
def db_connection():
    print(" Initiated connection to database ")
    yield
    print(" Closing db connection ")