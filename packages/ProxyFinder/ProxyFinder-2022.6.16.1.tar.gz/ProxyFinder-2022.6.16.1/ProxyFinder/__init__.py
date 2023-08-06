import asyncio
import copy
import httpx

from contextlib import suppress
from ProxyFinder.ProxyProviders import free_proxy_list, sslproxies


def get_loop():
    with suppress(Exception):
        return asyncio.get_running_loop()
    return asyncio.new_event_loop()


class ProxyFinder:
    def __init__(self):
        self.unchecked = list()
        self.checked = list()

        self.providers = [free_proxy_list.ProxyProvider(), sslproxies.ProxyProvider()]

    async def __load__(self):
        while True:
            for provider in self.providers:
                self.unchecked.extend(
                    a for a in await provider.__load__() if a not in self.unchecked
                )
            await asyncio.sleep(10 * 60)

    async def __check__(self):
        while True:
            if not self.checked and not self.unchecked:
                await asyncio.sleep(3)
                continue

            for proxy in copy.deepcopy([*self.checked, *self.unchecked]):
                try:
                    async with httpx.AsyncClient(proxies=proxy) as httpx_client:
                        r = await httpx_client.get(
                            "http://ip-api.com/json",
                            timeout=1,
                        )

                        if r.status_code != 200:
                            raise ConnectionError()

                        self.checked.append(proxy)
                except Exception:
                    if proxy in self.checked:
                        self.checked.remove(proxy)
                    if proxy in self.unchecked:
                        self.unchecked.remove(proxy)
                    continue

            await asyncio.sleep(10 * 60)

    def start(self, loop=None):
        if loop is None:
            loop = asyncio.get_running_loop()

        loop.create_task(self.__load__())
        loop.create_task(self.__check__())
