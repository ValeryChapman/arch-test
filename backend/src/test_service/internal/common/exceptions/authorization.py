from internal.common.exceptions.default import DefaultException


class UsersError(DefaultException):
    pass


class UnauthorizedError(UsersError):
    pass
