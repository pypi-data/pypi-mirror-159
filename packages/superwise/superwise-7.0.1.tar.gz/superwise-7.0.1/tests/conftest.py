import pytest

from superwise.config import Config


def pytest_generate_tests(metafunc):
    if "mock_config_is_managed_env" in metafunc.fixturenames:
        # running mock_config_is_managed_env twice with request.param = True and then with request.param = False
        metafunc.parametrize("mock_config_is_managed_env", [True, False], indirect=True)


@pytest.fixture(scope="function")
def mock_config_is_managed_env(monkeypatch, request):
    is_managed = request.param
    monkeypatch.setattr(Config, "IS_MANAGED_ENV", is_managed)
