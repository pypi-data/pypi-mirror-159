from asyncio import sleep
from typing import Any, Optional

from aiohttp import ClientSession

from .exceptions import DataNotPopulated, RequestFailed, TooManyRequests
from .ratelimiter import RateLimiter

HYPIXEL_API_URL = "https://api.hypixel.net"
DEFAULT_RATE_LIMIT = 120


class HTTPClient:
    def __init__(
        self, token: str, session: Optional[ClientSession] = None, *, max_retries: int = 3
    ) -> None:
        self._token = token
        self._max_retries = max_retries
        self._default_headers = {"API-Key": token}

        self._ratelimiter = RateLimiter()

        self.__session = session

    @property
    def _session(self) -> ClientSession:
        if self.__session is None or self.__session.closed:
            self.__session = ClientSession()

        return self.__session

    async def close(self) -> None:
        if self.__session and not self.__session.closed:
            await self.__session.close()

    async def request(
        self, route: str, query_parameters: Optional[dict[str, str]] = None
    ) -> Any:
        for attempt in range(self._max_retries):
            # Retry backoff logic.
            await sleep(attempt**2 * 0.4)

            async with self._ratelimiter as ratelimiter:
                async with self._session.get(
                    f"{HYPIXEL_API_URL}{route}", headers=self._default_headers
                ) as response:
                    rl_limit = int(
                        response.headers.get("RateLimit-Limit", DEFAULT_RATE_LIMIT)
                    )
                    rl_remaining = int(response.headers.get("RateLimit-Remaining", 0))
                    rl_reset_after = int(response.headers.get("RateLimit-Reset", 0))

                    if 200 <= response.status < 300:
                        if rl_limit - rl_remaining == rl_limit:
                            await ratelimiter.defer(rl_reset_after)

                        return await response.json()

                    if response.status == 429:
                        retry_after = int(response.headers.get("retry-after", 0))

                        await ratelimiter.defer(retry_after)

                        raise TooManyRequests

                    # This will almost never be raised but persumably Hypixel's using some
                    # sort of in memory database most likely Redis, and occasionally they
                    # need to repopulate said in memory database.
                    if response.status == 503:
                        raise DataNotPopulated

                    if response.status >= 500:
                        raise RequestFailed(
                            f"Failed to make request to {HYPIXEL_API_URL}{route} {response.status} server error."
                        )

        raise RequestFailed(
            f"Failed to make request to {HYPIXEL_API_URL}{route} after {self._max_retries} attempts."
        )
