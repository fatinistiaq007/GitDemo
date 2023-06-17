import pytest


@pytest.fixture(scope="class")
def setup():
    print("I will be executing first.")
    yield
    print("I will be executing last.")


@pytest.fixture()
def dataLoad():
    print("User profile data is being created.")
    return ["Fatin", "Istiaq", "fatin.istiaq.com"]


@pytest.fixture(params=[("chrome" , "Fatin" ,"Shakib"), ("Firefox" , "Istiaq"), ("IE", "FI")])
def crossBrowser(request):
    return request.param

