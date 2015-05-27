from checkio_referee import RefereeBase
from checkio_referee import representations, covercodes


import settings_env
from tests import TESTS


cover = """def cover(func, data):
    return func(*[str(x) for x in data])
"""


class Referee(RefereeBase):
    TESTS = TESTS
    ENVIRONMENTS = settings_env.ENVIRONMENTS

    DEFAULT_FUNCTION_NAME = "boolean"
    CALLED_REPRESENTATIONS = {
        "python_3": representations.unwrap_arg_representation,
        "python_2": representations.unwrap_arg_representation,
        "javascript": representations.unwrap_arg_representation
    }
    ENV_COVERCODE = {
        "python_3": covercodes.py_unwrap_args,
    }
