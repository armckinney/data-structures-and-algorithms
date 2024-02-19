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
