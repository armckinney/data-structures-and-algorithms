from data_structures_and_algorithms.core import JsonConfigurationProvider
from tests.conftest import TEST_CONFIG_FILE


def test_can_create() -> None:
    # Assemble / Act / Assert
    JsonConfigurationProvider(TEST_CONFIG_FILE)


def test_can_get_config() -> None:
    # Assemble
    config = JsonConfigurationProvider(TEST_CONFIG_FILE)

    # Act / Assert
    config.get("data_path")

