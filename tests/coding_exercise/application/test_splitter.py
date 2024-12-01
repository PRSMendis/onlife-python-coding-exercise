from assertpy import assert_that
import pytest

from coding_exercise.application.splitter import Splitter
from coding_exercise.domain.model.cable import Cable


def test_should_not_return_none_when_splitting_cable():
    assert_that(Splitter().split(Cable(10, "coconuts"), 1)).is_not_none()


def test_split_single_time_returns_two_equal_cables():
    result = Splitter().split(Cable(10, "coconuts"), 1)

    assert_that(result).is_length(2)
    assert_that(result[0].length).is_equal_to(5)
    assert_that(result[1].length).is_equal_to(5)
    assert_that(result[0].name).is_equal_to("coconuts-0")
    assert_that(result[1].name).is_equal_to("coconuts-1")


def test_split_multiple_times_creates_correct_number_of_cables():
    result = Splitter().split(Cable(5, "coconuts"), 2)

    assert_that(result).is_length(5)
    assert_that([cable.length for cable in result]).is_equal_to([1, 1, 1, 1, 1])
    assert_that([cable.name for cable in result]).is_equal_to(
        ["coconuts-0", "coconuts-1", "coconuts-2", "coconuts-3", "coconuts-4"]
    )


def test_split_with_remainder_handles_uneven_distribution():
    result = Splitter().split(Cable(7, "coconuts"), 2)

    assert_that(result).is_length(4)
    assert_that([cable.length for cable in result]).is_equal_to([2, 2, 2, 1])
    assert_that([cable.name for cable in result]).is_equal_to(
        ["coconuts-0", "coconuts-1", "coconuts-2", "coconuts-3"]
    )


def test_split_remainder_into_larger_parts():
    cable = Cable(7, "coconuts")
    splitter = Splitter()
    result = splitter.split(cable, 1)

    assert len(result) == 3  # Two parts of 3, one part of 1
    assert [c.length for c in result] == [3, 3, 1]
    assert result[0].name == "coconuts-0"
    assert result[1].name == "coconuts-1"
    assert result[2].name == "coconuts-2"


def test_split_into_12_equal_parts_to_check_number_naming():
    cable = Cable(12, "coconuts")
    splitter = Splitter()
    result = splitter.split(cable, 11)  # Split 12 units into 12 parts

    # Verify the total number of cables
    assert len(result) == 12  # 12 cables in total

    # Verify that all cables have a length of 1
    assert all(c.length == 1 for c in result)

    # Verify the names of the resulting cables
    expected_names = [f"coconuts-{i:02d}" for i in range(12)]
    assert [c.name for c in result] == expected_names


def test_raises_error_when_times_exceeds_maximum():
    with pytest.raises(ValueError, match="Number of times must be between 1 and 64"):
        Splitter().split(Cable(10, "coconuts"), 65)


def test_raises_error_when_times_is_less_than_minimum():
    with pytest.raises(ValueError, match="Number of times must be between 1 and 64"):
        Splitter().split(Cable(10, "coconuts"), 0)


def test_raises_error_when_cable_length_too_short():
    with pytest.raises(ValueError, match="Cable length must be between 2 and 1024"):
        Splitter().split(Cable(1, "coconuts"), 1)


def test_raises_error_when_cable_length_too_long():
    with pytest.raises(ValueError, match="Cable length must be between 2 and 1024"):
        Splitter().split(Cable(1025, "coconuts"), 1)


def test_raises_error_when_splitting_would_create_cables_less_than_one():
    with pytest.raises(ValueError, match="Cannot split cable of length"):
        Splitter().split(Cable(2, "coconuts"), 2)
