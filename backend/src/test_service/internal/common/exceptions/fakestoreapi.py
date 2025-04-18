from internal.common.exceptions.default import DefaultException


class FakeStoreAPIError(DefaultException):
    pass


class RequestFailed(FakeStoreAPIError):
    pass
