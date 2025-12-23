import pytest

from data_structures import BloomFilter


def test_can_create() -> None:
    # Assemble / Act / Assert
    bf = BloomFilter()
    assert bf.size == 100
    assert bf.num_hashes == 3


def test_can_create_custom_size() -> None:
    # Assemble / Act / Assert
    bf = BloomFilter(size=200, num_hashes=5)
    assert bf.size == 200
    assert bf.num_hashes == 5


def test_can_add_and_check() -> None:
    # Assemble
    bf = BloomFilter()
    item = "apple"

    # Act
    bf.add(item)

    # Assert
    assert bf.check(item)


def test_definitive_negative() -> None:
    # Assemble
    bf = BloomFilter()
    item = "apple"

    # Act / Assert
    # Empty filter should return False (unless all bits are miraculously set by 0 init, impossible)
    assert bf.check(item) is False


def test_multiple_items() -> None:
    # Assemble
    bf = BloomFilter(size=1000, num_hashes=5)
    items = ["apple", "banana", "cherry"]

    # Act
    for item in items:
        bf.add(item)

    # Assert
    for item in items:
        assert bf.check(item)


def test_check_not_present() -> None:
    # Assemble
    bf = BloomFilter(size=1000, num_hashes=5)

    # Act
    bf.add("apple")

    # Assert
    # "zebra" is likely not in the filter (though false positive is theoretically possible)
    # With this size and items, probability is extremely low.
    # Note: If this test flakes due to bad luck, increase size.
    assert bf.check("zebra") is False


def test_serialization() -> None:
    # Assemble
    bf = BloomFilter()
    bf.add("test_item")

    # Act
    data = bf.to_dict()
    bf_new = BloomFilter.from_dict(data)

    # Assert
    assert bf_new.size == bf.size
    assert bf_new.num_hashes == bf.num_hashes
    assert bf_new.check("test_item")
    assert bf_new.check("not_item") is False


def test_value_errors() -> None:
    with pytest.raises(ValueError):
        BloomFilter(size=0)
    with pytest.raises(ValueError):
        BloomFilter(num_hashes=0)
