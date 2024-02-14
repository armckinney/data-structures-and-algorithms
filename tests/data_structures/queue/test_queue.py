from data_structures import Queue

TEST_LIST = [1, 2, 3]


def test_can_create() -> None:
    # Assemble / Act / Assert
    Queue()


def test_can_verify_empty() -> None:
    # Assemble
    q = Queue()

    # Act / Assert
    assert q.empty


def test_can_verify_not_empty() -> None:
    # Assemble
    q = Queue()
    q.enqueue(1)

    # Act / Assert
    assert not q.empty


def test_can_enqueue() -> None:
    # Assemble
    q = Queue()
    value = 1

    # Act / Assert
    q.enqueue(value)


def test_can_enqueue_iteratively() -> None:
    # Assemble
    q = Queue()

    # Act
    for i in TEST_LIST:
        q.enqueue(i)

    # Assert
    assert q.to_list() == TEST_LIST


def test_can_peek() -> None:
    # Assemble
    q = Queue()

    # Act / Assert
    q.peek()


def test_can_peek_value() -> None:
    # Assemble
    q = Queue.from_list(TEST_LIST)

    # Act / Assert
    assert q.peek() == TEST_LIST[0]


def test_peek_does_not_dequeue() -> None:
    # Assemble
    q = Queue.from_list(TEST_LIST)

    # Act / Assert
    q.peek()

    # Assert
    assert len(q.to_list()) == len(TEST_LIST)


def test_enqueue_does_not_change_next_dequeue() -> None:
    # Assemble
    q = Queue()
    validation_peeks = []

    # Act / Assert
    for i in TEST_LIST:
        q.enqueue(i)
        validation_peeks.append(q.peek())

    # Assert
    assert all([peek == TEST_LIST[0] for peek in validation_peeks])


def test_can_dequeue() -> None:
    # Assemble
    q = Queue()
    value = 1

    q.enqueue(value)

    # Act / Assert
    q.dequeue()


def test_dequeues_value() -> None:
    # Assemble
    q = Queue()
    value = 1

    q.enqueue(value)

    # Act / Assert
    assert q.dequeue() == value


def test_can_dequeue_empty() -> None:
    # Assemble
    q = Queue()

    # Act / Assert
    assert not q.dequeue()


def test_dequeue_to_next() -> None:
    # Assemble
    q = Queue.from_list(TEST_LIST)

    # Act / Assert
    for i in TEST_LIST:
        assert q.dequeue() == i


def test_can_convert_to_list() -> None:
    # Assemble
    q = Queue()

    for i in TEST_LIST:
        q.enqueue(i)

    # Act / Assert
    assert q.to_list() == TEST_LIST


def test_can_create_from_list() -> None:
    # Assemble / Act
    q = Queue.from_list(TEST_LIST)

    # Assert
    assert q.to_list() == TEST_LIST


def test_can_convert_to_string() -> None:
    # Assemble / Act
    q = Queue.from_list(TEST_LIST)

    # Assert
    assert q.to_string() == "".join([str(i) for i in TEST_LIST])
