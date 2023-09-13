"""User defined warnings for general use."""


class MissingArgumentsWarning(UserWarning):
    pass


class FutureImplementationWarning(UserWarning):
    """
    To avoid having to reimplement it in future. We don't want to warn the user if he / she's trying to do something that would be unavoidable.
    """


class WorkInProgressWarning(UserWarning):
    """
    Warns the user that the code is being worked on and it might not work as
    intened or as the documentation describes.
    """
