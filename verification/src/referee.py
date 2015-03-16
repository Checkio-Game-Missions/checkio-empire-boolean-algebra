from checkio_referee import RefereeBase
from checkio_referee import representations

import settings
import settings_env
from tests import TESTS


cover = """def cover(func, data):
    return func(*[str(x) for x in data])
"""


class Referee(RefereeBase):
    TESTS = TESTS
    EXECUTABLE_PATH = settings.EXECUTABLE_PATH
    CURRENT_ENV = settings_env.CURRENT_ENV
    FUNCTION_NAME = "boolean"
    CALLED_REPRESENTATIONS = {
        "python_3": representations.unwrap_arg_representation,
        "python_2": representations.unwrap_arg_representation,
        "javascript": representations.unwrap_arg_representation
    }
    ENV_COVERCODE = {
        "python_2": cover,
        "python_3": cover,
        "javascript": None
    }
