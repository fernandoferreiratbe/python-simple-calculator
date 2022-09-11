# _*_ encoding: utf-8 _*_

class BadRequestError(Exception):

    def __init__(self, message="Default message value"):
        self.message = message
        super().__init__(self.message)
