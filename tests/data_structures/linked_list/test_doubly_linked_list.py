from data_structures import DoublyLinkedList

TEST_LIST = [1, 2, 3]


def test_can_create() -> None:
    # Assemble / Act / Assert
    DoublyLinkedList()


def test_can_verify_empty() -> None:
    # Assemble
    ll = DoublyLinkedList()

    # Act / Assert
    assert ll.empty


def test_can_append() -> None:
    # Assemble
    ll = DoublyLinkedList()
    value = 1

    # Act / Assert
    ll.append(value)


def test_can_append_iteratively() -> None:
    # Assemble
    ll = DoublyLinkedList()

    # Act
    for i in TEST_LIST:
        ll.append(i)

    # Assert
    assert ll.to_list() == TEST_LIST


def test_append_sets_head_and_tail() -> None:
    # Assemble
    ll = DoublyLinkedList()

    # Act / Assert
    for i in TEST_LIST:
        ll.append(i)

    # Assert
    assert ll.head.value == TEST_LIST[0]
    assert ll.tail.value == TEST_LIST[-1]


def test_can_prepend() -> None:
    # Assemble
    ll = DoublyLinkedList()

    # Act / Assert
    ll.prepend(1)


def test_can_prepend_iteratively() -> None:
    # Assemble
    ll = DoublyLinkedList()

    __test_list = TEST_LIST.copy()
    __test_list.reverse()

    # Act
    for i in __test_list:
        ll.prepend(i)

    # Assert
    assert ll.to_list() == TEST_LIST


def test_prepend_sets_head_and_tail() -> None:
    # Assemble
    ll = DoublyLinkedList()

    __test_list = TEST_LIST.copy()
    __test_list.reverse()

    # Act
    for i in __test_list:
        ll.prepend(i)

    # Assert
    assert ll.head.value == TEST_LIST[0]
    assert ll.tail.value == TEST_LIST[-1]


def test_pop_head_returns_head() -> None:
    # Assemble
    ll = DoublyLinkedList.from_list(TEST_LIST)

    # Act
    head = ll.pop()

    # Assert
    assert head == TEST_LIST[0]


def test_pop_tail_returns_tail() -> None:
    # Assemble
    ll = DoublyLinkedList.from_list(TEST_LIST)

    # Act
    tail = ll.pop(tail=True)

    # Assert
    assert tail == TEST_LIST[-1]


def test_pop_head_removes_head() -> None:
    # Assemble
    ll = DoublyLinkedList.from_list(TEST_LIST)

    # Act
    ll.pop()

    # Assert
    assert ll.to_list() == TEST_LIST[1:]


def test_pop_tail_removes_tail() -> None:
    # Assemble
    ll = DoublyLinkedList.from_list(TEST_LIST)

    # Act
    ll.pop(tail=True)

    # Assert
    assert ll.to_list() == TEST_LIST[:-1]


def test_pop_head_sets_head() -> None:
    # Assemble
    ll = DoublyLinkedList.from_list(TEST_LIST)

    # Act
    ll.pop()

    # Assert
    assert ll.head.value == TEST_LIST[1]


def test_pop_tail_sets_tail() -> None:
    # Assemble
    ll = DoublyLinkedList.from_list(TEST_LIST)

    # Act
    ll.pop(tail=True)

    # Assert
    assert ll.tail.value == TEST_LIST[-2]


def test_can_delete_head() -> None:
    # Assemble
    ll = DoublyLinkedList.from_list(TEST_LIST)

    # Act
    ll.delete(TEST_LIST[0])

    # Assert
    assert ll.to_list() == TEST_LIST[1:]


def test_delete_head_sets_head() -> None:
    # Assemble
    ll = DoublyLinkedList.from_list(TEST_LIST)

    # Act
    ll.delete(TEST_LIST[0])

    # Assert
    assert ll.head.value == TEST_LIST[1]


def test_can_delete_mid() -> None:
    # Assemble
    ll = DoublyLinkedList.from_list(TEST_LIST)
    index = 1

    __test_list = TEST_LIST.copy()
    __test_list.pop(index)

    # Act
    ll.delete(TEST_LIST[index])

    # Assert
    assert ll.to_list() == __test_list


def test_can_delete_tail() -> None:
    # Assemble
    ll = DoublyLinkedList.from_list(TEST_LIST)

    # Act
    ll.delete(TEST_LIST[-1])

    # Assert
    assert ll.to_list() == TEST_LIST[:-1]


def test_delete_tail_sets_tail() -> None:
    # Assemble
    ll = DoublyLinkedList.from_list(TEST_LIST)

    # Act
    ll.delete(TEST_LIST[-1])

    # Assert
    assert ll.tail.value == TEST_LIST[-2]


def test_can_delete_all_occurences() -> None:
    # Assemble
    __test_list = TEST_LIST.copy()
    __test_list.append(TEST_LIST[0])
    ll = DoublyLinkedList.from_list(__test_list)

    # Act
    ll.delete(TEST_LIST[0], all_occurences=True)

    # Assert
    assert ll.to_list() == TEST_LIST[1:]


def test_can_delete_only_one_occurences() -> None:
    # Assemble
    __test_list = TEST_LIST.copy()
    __test_list.append(TEST_LIST[0])
    ll = DoublyLinkedList.from_list(__test_list)

    # Act
    ll.delete(TEST_LIST[0], all_occurences=False)

    # Assert
    assert ll.to_list() == __test_list[1:]


def test_can_reverse() -> None:
    # Assemble
    ll = DoublyLinkedList.from_list(TEST_LIST)
    __test_list = TEST_LIST.copy()
    __test_list.reverse()

    # Act
    ll.reverse()

    # Assert
    assert ll.to_list() == __test_list


def test_can_convert_to_list() -> None:
    # Assemble
    ll = DoublyLinkedList()

    for i in TEST_LIST:
        ll.append(i)

    # Act / Assert
    assert ll.to_list() == TEST_LIST


def test_can_create_from_list() -> None:
    # Assemble / Act
    ll = DoublyLinkedList.from_list(TEST_LIST)

    # Assert
    assert ll.to_list() == TEST_LIST


def test_can_convert_to_string() -> None:
    # Assemble / Act
    ll = DoublyLinkedList.from_list(TEST_LIST)

    # Assert
    assert ll.to_string() == "".join([str(i) for i in TEST_LIST])


def test_can_make_circular() -> None:
    # Assemble
    ll = DoublyLinkedList.from_list(TEST_LIST)

    # Act
    ll.make_circular()

    # Assert
    assert ll.tail.next == ll.head


def test_can_access_previous() -> None:
    # Assemble
    ll = DoublyLinkedList.from_list(TEST_LIST)

    # Act / Assert
    assert ll.head.next.previous == ll.head
