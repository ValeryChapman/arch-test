class DefaultException(Exception):

    def __init__(self, message: str, traceback: Exception | None = None):
        self.message = message
        self.traceback = traceback
        super().__init__(message, traceback)
