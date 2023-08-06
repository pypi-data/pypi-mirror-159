from contextlib import suppress
from typing import List

import httpx

from bs4 import BeautifulSoup


class ProxyProvider:
    def __init__(self):
        self.url = "https://www.sslproxies.org"

    async def __load__(self) -> List[str]:
        try:
            async with httpx.AsyncClient() as httpx_client:
                r = await httpx_client.get(
                    self.url,
                    timeout=5,
                )
        except Exception:
            return

        if r.status_code != 200:
            return

        bs4_object = BeautifulSoup(r.text, "html.parser")

        data = list()

        with suppress(Exception):
            for item in (
                bs4_object.find(
                    "table", {"class": "table table-striped table-bordered"}
                )
                .find("tbody")
                .find_all("tr")
            ):
                ip, port = tuple(a.text for a in item.find_all("td"))[:2]

                data.append("http://{}:{}".format(ip, port))

        return data[:50]
