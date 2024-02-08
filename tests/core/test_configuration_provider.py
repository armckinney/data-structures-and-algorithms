from typing import Any

import pytest
from data_structures_and_algorithms.core import ConfigurationProvider


def test_cannot_create() -> None:
    # Assemble / Act / Assert
    with pytest.raises(TypeError):
        ConfigurationProvider()  # type: ignore


def test_can_subclass() -> None:
    # Assemble
    class TestConfigurationProvider(ConfigurationProvider):
        def get_config(self) -> None:
            pass

        def get(self, key: str) -> Any:
            pass

    # Act / Assert
    TestConfigurationProvider()

