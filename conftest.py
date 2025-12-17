import pytest

@pytest.fixture(autouse=True, scope="session", params=[1,2,5], ids=["Manjeet", "Parul", "Awatar"])
def db_connection(request):
    print(" Initiated connection to database ")
    yield request.param
    print(" Closing db connection ")