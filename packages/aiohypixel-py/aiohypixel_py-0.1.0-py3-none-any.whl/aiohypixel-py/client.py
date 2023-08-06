from asyncio import AbstractEventLoop, get_event_loop
from typing import Optional

from aiohttp import ClientSession

from .http import HTTPClient
from .models import Key

DEFAULT_MAX_RETRIES = 3


class HypixelClient:
    """Represents a Hypixel API client used to retrieve data from Hypixel's API.
    This client includes a bunch of features and is very modular so you aren't
    forced to use features you don't absolutely need.

    Parameters
    ----------
    token : str
        Your Hypixel API key.
    loop : Optional[AbstractEventLoop]
        A custom asyncio event loop if none is provided the client will create one.
    session : Optional[ClientSession]
        A custom aiohttp client session if none is provided the client will create one.
    max_retries : int,
        The max amount of times the client will retry a request before raising an
        exception, defaults to 3
    """

    def __init__(
        self,
        token: str,
        *,
        loop: Optional[AbstractEventLoop] = None,
        session: Optional[ClientSession] = None,
        max_retries: int = DEFAULT_MAX_RETRIES
    ) -> None:
        self.token = token
        self._loop = loop or get_event_loop()

        self._http = HTTPClient(token, session, max_retries=max_retries)

    def __del__(self) -> None:
        self._loop.run_until_complete(self._http.close())

    async def get_key_information(self) -> Key:
        """Returns information about the current API token you have supplied.

        Returns
        -------
        Key
            The information about the key.
        """
        response = await self._http.request("/key")

        data = response["record"]

        return Key(
            key=data["key"],
            owner=data["owner"],
            limit=data["limit"],
            queries_in_past_minute=data["queriesInPastMin"],
            total_queries=data["totalQueries"],
        )
