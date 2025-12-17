import pytest

@pytest.fixture(autouse=True, scope="session", ids=["Manjeet", "Parul", "Awatar"])
def db_connection(request):
    print(" Initiated connection to database ")
    yield
    print(" Closing db connection ")