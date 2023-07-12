from support.assertion_errors import AssertionErrors


class Assertions:
    @staticmethod
    def assert_equal(actual, expected):
        assert actual == expected, AssertionErrors.EQUAL.format(expected, actual)