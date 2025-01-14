from data_structures import HashTable

TEST_DICT = {"a": 1, "b": 2, "c": 3}


def test_can_create() -> None:
    # Assemble / Act / Assert
    HashTable()


def test_can_create_different_size() -> None:
    # Assemble
    size = 5

    # Act
    ht = HashTable(size)

    # Assert
    assert ht.size == size


def test_creates_different_size_buckets() -> None:
    # Assemble
    size = 5

    # Act
    ht = HashTable(size)

    # Assert
    assert len(ht._buckets) == size


def test_can_create_from_dict() -> None:
    # Assemble / Act
    ht = HashTable.from_dict(TEST_DICT, 1)

    # Assert
    assert ht.to_dict() == TEST_DICT


def test_can_set() -> None:
    # Assemble
    ht = HashTable()

    # Act / Assert
    ht.set("a", 1)


def test_can_get() -> None:
    # Assemble
    ht = HashTable.from_dict(TEST_DICT, 1)

    # Act / Assert
    ht.get("a")


def test_can_get_set_value() -> None:
    # Assemble
    ht = HashTable()

    # Act / Assert
    ht.set("a", 1)

    # Assert
    assert ht.get("a") == 1


def test_can_pop() -> None:
    # Assemble
    ht = HashTable.from_dict(TEST_DICT, 1)

    # Act / Assert
    ht.pop("a")


def test_can_pop_key() -> None:
    # Assemble
    ht = HashTable.from_dict(TEST_DICT, 1)
    validation_dict = TEST_DICT.copy()
    validation_dict.pop("a")

    # Act
    ht.pop("a")

    # Assert
    assert ht.to_dict() == validation_dict


def test_can_delete() -> None:
    # Assemble
    ht = HashTable.from_dict(TEST_DICT, 1)

    # Act / Assert
    ht.delete("a")


def test_can_delete_key() -> None:
    # Assemble
    ht = HashTable.from_dict(TEST_DICT, 1)
    validation_dict = TEST_DICT.copy()
    validation_dict.pop("a")

    # Act
    ht.delete("a")

    # Assert
    assert ht.to_dict() == validation_dict


def test_can_check_has() -> None:
    # Assemble
    ht = HashTable.from_dict(TEST_DICT, 1)

    # Act / Assert
    assert ht.has("a")


def test_can_check_not_has() -> None:
    # Assemble
    ht = HashTable.from_dict(TEST_DICT, 1)

    # Act / Assert
    assert not ht.has("z")


def test_can_get_keys() -> None:
    # Assemble
    ht = HashTable.from_dict(TEST_DICT, 1)

    # Act / Assert
    assert ht.get_keys() == list(TEST_DICT.keys())


def test_can_get_values() -> None:
    # Assemble
    ht = HashTable.from_dict(TEST_DICT, 1)

    # Act / Assert
    assert ht.get_values() == list(TEST_DICT.values())
