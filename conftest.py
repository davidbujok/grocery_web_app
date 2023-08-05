from app import app, create_app
import pytest

@pytest.fixture
def app():
    app = create_app()
    return app


