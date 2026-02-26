import pytest

@pytest.fixture(autouse=True, scope="session", ids=["Manjeet", "Parul", "Awatar"])
def db_connection(request):
    print(" Initiated connection to database ")
    yield
    print(" Closing db connection ")

# conftest.py
def pytest_addoption(parser):
    parser.addoption(
        "--env",
        action="store",
        default="qa",
        help="Environment to run tests against"
    )

def pytest_sessionstart(session):
    print("Session started")

def pytest_sessionfinish(session, exitstatus):
    print("Session finished", exitstatus)

def pytest_collection_modifyitems(config, items):
    for item in items:
        pass