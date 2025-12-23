from data_structures import LRUCache


def test_can_create() -> None:
    # Assemble / Act / Assert
    LRUCache(10)


def test_can_verify_empty() -> None:
    # Assemble
    cache = LRUCache(10)

    # Act / Assert
    assert cache.size == 0
    assert cache.get("msg") is None


def test_can_set_and_get() -> None:
    # Assemble
    cache = LRUCache(10)
    key = "a"
    value = 1

    # Act
    cache.set(key, value)

    # Assert
    assert cache.get(key) == value
    assert cache.size == 1


def test_capacity_limit() -> None:
    # Assemble
    cache = LRUCache(2)
    cache.set("a", 1)
    cache.set("b", 2)

    # Act
    cache.set("c", 3)

    # Assert
    assert cache.size == 2
    assert cache.get("a") is None
    assert cache.get("b") == 2
    assert cache.get("c") == 3


def test_get_promotes_key() -> None:
    # Assemble
    cache = LRUCache(2)
    cache.set("a", 1)
    cache.set("b", 2)

    # Act
    cache.get("a")  # Access 'a', making 'b' the LRU
    cache.set("c", 3)

    # Assert
    assert cache.get("a") == 1
    assert cache.get("b") is None
    assert cache.get("c") == 3


def test_set_updates_value_and_promotes() -> None:
    # Assemble
    cache = LRUCache(2)
    cache.set("a", 1)
    cache.set("b", 2)

    # Act
    cache.set("a", 10)  # Update 'a', promoting it
    cache.set("c", 3)  # Should evict 'b'

    # Assert
    assert cache.get("a") == 10
    assert cache.get("b") is None
    assert cache.get("c") == 3


def test_capacity_one() -> None:
    # Assemble
    cache = LRUCache(1)

    # Act
    cache.set("a", 1)
    assert cache.get("a") == 1
    cache.set("b", 2)

    # Assert
    assert cache.get("a") is None
    assert cache.get("b") == 2


def test_can_create_from_dict() -> None:
    # Assemble
    input_dict = {"a": 1, "b": 2}

    # Act
    cache = LRUCache.from_dict(input_dict)

    # Assert
    assert cache.to_dict() == input_dict
    assert cache.capacity == 2


def test_can_convert_to_dict() -> None:
    # Assemble
    cache = LRUCache(2)
    cache.set("a", 1)
    cache.set("b", 2)

    # Act
    result = cache.to_dict()

    # Assert
    assert result == {"a": 1, "b": 2}


def test_can_convert_to_string() -> None:
    # Assemble
    cache = LRUCache(2)
    cache.set("a", 1)
    cache.set("b", 2)

    # Act
    result = cache.to_string()

    # Assert
    assert result == '{"a": 1, "b": 2}'
