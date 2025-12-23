from data_structures import Stack

TEST_LIST = [1, 2, 3]
REVERSE_TEST_LIST = TEST_LIST.copy()
REVERSE_TEST_LIST.reverse()


def test_can_create() -> None:
    # Assemble / Act / Assert
    Stack()


def test_can_verify_empty() -> None:
    # Assemble
    stack = Stack()

    # Act / Assert
    assert stack.empty


def test_can_verify_not_empty() -> None:
    # Assemble
    stack = Stack()
    stack.push(1)

    # Act / Assert
    assert not stack.empty


def test_can_push() -> None:
    # Assemble
    stack = Stack()
    value = 1

    # Act / Assert
    stack.push(value)


def test_can_push_iteratively() -> None:
    # Assemble
    stack = Stack()

    # Act
    for i in TEST_LIST:
        stack.push(i)

    # Assert
    assert stack.to_list() == REVERSE_TEST_LIST


def test_can_peek() -> None:
    # Assemble
    stack = Stack()

    # Act / Assert
    stack.peek()


def test_can_peek_value() -> None:
    # Assemble
    stack = Stack.from_list(TEST_LIST)

    # Act / Assert
    assert stack.peek() == REVERSE_TEST_LIST[0]


def test_peek_does_not_pop() -> None:
    # Assemble
    stack = Stack.from_list(TEST_LIST)

    # Act / Assert
    stack.peek()

    # Assert
    assert len(stack.to_list()) == len(TEST_LIST)


def test_push_changes_next_dequeue() -> None:
    # Assemble
    stack = Stack()
    validation_peeks = []

    # Act / Assert
    for i in TEST_LIST:
        stack.push(i)
        validation_peeks.append(stack.peek())

    # Assert
    assert all([peek == TEST_LIST[index] for index, peek in enumerate(validation_peeks)])


def test_can_pop() -> None:
    # Assemble
    stack = Stack()
    value = 1

    stack.push(value)

    # Act / Assert
    stack.pop()


def test_pops_value() -> None:
    # Assemble
    stack = Stack()
    value = 1

    stack.push(value)

    # Act / Assert
    assert stack.pop() == value


def test_can_dequeue_empty() -> None:
    # Assemble
    stack = Stack()

    # Act / Assert
    assert not stack.pop()


def test_pop_to_next() -> None:
    # Assemble
    stack = Stack.from_list(TEST_LIST)

    # Act / Assert
    for i in REVERSE_TEST_LIST:
        assert stack.pop() == i


def test_can_convert_to_list() -> None:
    # Assemble
    stack = Stack()

    for i in TEST_LIST:
        stack.push(i)

    # Act / Assert
    assert stack.to_list() == REVERSE_TEST_LIST


def test_can_create_from_list() -> None:
    # Assemble / Act
    stack = Stack.from_list(TEST_LIST)

    # Assert
    assert stack.to_list() == REVERSE_TEST_LIST


def test_can_convert_to_string() -> None:
    # Assemble / Act
    stack = Stack.from_list(TEST_LIST)

    # Assert
    assert stack.to_string() == "".join([str(i) for i in REVERSE_TEST_LIST])
