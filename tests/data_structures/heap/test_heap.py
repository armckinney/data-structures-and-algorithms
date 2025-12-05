from data_structures.heap.heap import Heap


def test_can_create() -> None:
    # Assemble / Act / Assert
    Heap()


def test_can_verify_empty() -> None:
    # Assemble
    heap = Heap()

    # Act / Assert
    assert heap.is_empty()


def test_can_verify_not_empty() -> None:
    # Assemble
    heap = Heap()
    heap.push(1)

    # Act / Assert
    assert not heap.is_empty()


def test_can_push_and_pop_min_heap() -> None:
    # Assemble
    heap = Heap()
    values = [5, 3, 8, 1, 2]

    # Act
    for v in values:
        heap.push(v)

    # Assert
    assert heap.pop() == 1
    assert heap.pop() == 2
    assert heap.pop() == 3
    assert heap.pop() == 5
    assert heap.pop() == 8
    assert heap.is_empty()


def test_can_push_and_pop_max_heap() -> None:
    # Assemble
    heap = Heap(comparator=lambda a, b: a > b)
    values = [5, 3, 8, 1, 2]

    # Act
    for v in values:
        heap.push(v)

    # Assert
    assert heap.pop() == 8
    assert heap.pop() == 5
    assert heap.pop() == 3
    assert heap.pop() == 2
    assert heap.pop() == 1
    assert heap.is_empty()


def test_peek() -> None:
    # Assemble
    heap = Heap()
    heap.push(5)
    heap.push(1)

    # Act / Assert
    assert heap.peek() == 1
    assert not heap.is_empty()


def test_from_list() -> None:
    # Assemble
    values = [5, 3, 8, 1, 2]

    # Act
    heap = Heap.from_list(values)

    # Assert
    assert heap.pop() == 1
    assert heap.pop() == 2
    assert heap.pop() == 3
    assert heap.pop() == 5
    assert heap.pop() == 8


def test_to_list() -> None:
    # Assemble
    heap = Heap()
    heap.push(1)
    heap.push(2)

    # Act
    result = heap.to_list()

    # Assert
    assert 1 in result
    assert 2 in result
    assert len(result) == 2
