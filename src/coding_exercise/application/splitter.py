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
        self.__validate(cable, times)

        return []
