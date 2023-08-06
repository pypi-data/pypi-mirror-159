"""
The main program of `chopin` LIBRARY, providing various functions.

"""

__all__ = (
    "Chopin",
)

from json import load
from os.path import abspath, dirname
from random import choice
from typing import List, Optional

from .compositions import Composition
from .contents import Content


class Chopin(object):
    """class to holds chopin compositions data"""

    def __init__(self) -> None:
        path = dirname(abspath(__file__)) + "/data/{}.json"

        with open(path.format("compositions"), "r") as f:
            compositions = load(f)
        with open(path.format("contents"), "r") as f:
            contents = load(f)

        self.__data: List[Composition] = []

        for comp in compositions:
            youtube_dls = []
            for cont in contents:
                if comp["title"] == cont["title"]:
                    youtube_dls.append({
                        "id": cont["id"],
                        "artists": cont["artists"]
                    })
            kwargs: dict = comp
            kwargs.update({"youtube_dls": youtube_dls})
            self.__data.append(Composition(**kwargs))

    def get(self) -> Composition:
        """randomly return `Composition` that is not empty `Content`"""

        while True:
            compo = choice(self.__data)
            if compo.youtube_dls != []:
                return compo

    def download(self, path: Optional[str] = None) -> Content:
        """download one composition at random and return its path"""

        content = choice(self.get().youtube_dls)
        content.download(path=path, force=True)
        return content

    def url(self) -> str:
        """randomly return Youtube url of the composition"""

        content = choice(self.get().youtube_dls)
        return content.url
