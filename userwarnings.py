"""User defined warnings for general use."""


class MissingArgumentsWarning(UserWarning):
    pass


class NotASetError(IndexError):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)
