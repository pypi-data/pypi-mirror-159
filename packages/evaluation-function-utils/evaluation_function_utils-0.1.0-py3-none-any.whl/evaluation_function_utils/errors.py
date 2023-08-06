import json


class EvaluationException(Exception):
    """ 
    Exception to be used to return richer errors from evaluaton functions

    Provides a default `message` if not provided as keyword argument
    Allows adding any kwargs, which get passed onto the `error_dict` which
    is returned in the lambda function's response
    """
    default_msg = "An EvaluationException was raised when executing the evaluation function"

    def __init__(self, message=default_msg, **kwargs):
        self.message = message
        self.extra_args = kwargs
        super().__init__(self.message)

    def __repr__(self):
        return self.message

    @property
    def error_dict(self):
        return {
            "message": self.message,
            **self.extra_args,
        }
