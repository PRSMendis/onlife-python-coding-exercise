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
        ["coconuts-00", "coconuts-01", "coconuts-02", "coconuts-03"]
    )
