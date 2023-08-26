"""User defined errors and exceptions."""

class NotASetError(TypeError):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)
