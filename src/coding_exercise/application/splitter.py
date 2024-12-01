from coding_exercise.domain.model.cable import Cable

print("test1243")


class SplitterConfig:
    MIN_TIMES: int = 1
    MAX_TIMES: int = 64
    MIN_LENGTH: int = 2
    MAX_LENGTH: int = 1024


class Splitter:

    def __init__(self, config: SplitterConfig = None):
        self.config = config or SplitterConfig()

    def __validate(self, cable: Cable, times: int) -> None:
        """Validate input constraints for cable length and number of times."""
        if not (self.config.MIN_TIMES <= times <= self.config.MAX_TIMES):
            raise ValueError(
                f"Number of times must be between {self.config.MIN_TIMES} and {self.config.MAX_TIMES}, got {times}"
            )

        if not (self.config.MIN_LENGTH <= cable.length <= self.config.MAX_LENGTH):
            raise ValueError(
                f"Cable length must be between {self.config.MIN_LENGTH} and {self.config.MAX_LENGTH}, got {cable.length}"
            )

        # Check if splitting would result in cables less than 1
        if cable.length // (times + 1) < 1:
            raise ValueError(
                f"Cannot split cable of length {cable.length} into {times} parts"
            )

    def split(self, cable: Cable, times: int) -> list[Cable]:
        """
        Splits a given cable into multiple cables.

        Args:
            cable (Cable): The cable to be split.
            times (int): The number of times the cable should be split.

        Returns:
            list[Cable]: A list of split cables.

        Raises:
            SomeException: If there is an error during the split process.

        """
        self.__validate(cable, times)

        # Calculate the length of each split
        split_length = self._calculate_split_length(cable.length, times)

        # Generate split cables
        split_cables = self._generate_split_cables(cable, split_length, times)

        return split_cables

    def _calculate_split_length(self, total_length: int, times: int) -> int:
        """Calculate the split length."""
        return total_length // (times + 1)

    def _generate_split_cables(
        self, original_cable: Cable, split_length: int, times: int
    ) -> list[Cable]:
        """Generate split cables with each cable being named numerically."""

        # Calculate the number of full-length splits and remainder
        number_of_splits = times + 1

        split_cables = []

        for i in range(number_of_splits):
            cable_name = (
                f"{original_cable.name}-{i:01d}"
                if number_of_splits < 10
                else f"{original_cable.name}-{i:02d}"
            )
            split_cables.append(Cable(split_length, cable_name))

        return split_cables
