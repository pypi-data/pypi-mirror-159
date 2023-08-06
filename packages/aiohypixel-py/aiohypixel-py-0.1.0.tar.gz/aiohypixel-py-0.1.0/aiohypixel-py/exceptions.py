class AIOHypixelException(Exception):
    """Base exception class for all AIOHypixel errors."""

    pass


class TooManyRequests(AIOHypixelException):
    """Raised when Hypixel's API returns a 429 as a result of sending too many requests or being so called 'rate limited'"""

    pass


class RequestFailed(AIOHypixelException):
    """Raised when the request to Hypixel's API fails after the max amount of retries is reached."""

    pass


class DataNotPopulated(AIOHypixelException):
    """Raised when Hypixel's API data has not been populated."""

    pass
