from asyncio import Lock, create_task, sleep
from typing import Type


class RateLimiter:
    def __init__(self) -> None:
        """A ratelimit handler for all HTTP requests to avoid 429's."""

        self._deferred = False

        self._lock = Lock()

    async def __aenter__(self) -> "RateLimiter":
        await self._lock.acquire()
        return self

    async def __aexit__(
        self, exc_type: Type[BaseException], exc_val: BaseException, exc_tb: BaseException
    ) -> None:
        if not self._deferred:
            self._lock.release()

    async def _unlock(self, after: float) -> None:
        await sleep(after)

        self._lock.release()
        self._deferred = False

    async def defer(self, after: float) -> None:
        self._deferred = True
        create_task(self._unlock(after))
