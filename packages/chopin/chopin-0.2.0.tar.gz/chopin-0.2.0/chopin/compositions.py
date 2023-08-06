"""
Class definition that holds Chopin composition.

"""

import hashlib
from typing import List, Optional, Union

from .contents import Content
from .errors import InvalidHashValue


class Composition(object):
    """Chopin composition data

    Attributes
    ----------
    title : str
        title of this composition
    opus : int | str
        opus number (Op.) of this composition\\
        Basically, type is `int`, but in the case of a posthumous work\\
        or opus having sub-number, type is `str`.
    no : Optional[int]
        the number of this composition (No) if there is an identical opus number
    youtube_dls : List[Content]
        hold youtube contents

    """

    def __init__(self, title: str, opus: Union[int, str], sub_opus: Optional[int] = None,
                 no: Optional[int] = None, youtube_dls: List[dict] = [],
                 md5: str = "") -> None:
        self.__title: str = title
        self.__opus: Union[int, str] = opus
        self.__sub_opus: Union[int, None] = sub_opus
        self.__no: Union[int, None] = no
        self.__youtube_dls: List[Content] = [Content(**ydl) for ydl in youtube_dls]
        self.__md5: str = md5
        if md5 != hashlib.md5(self.__title.encode()).hexdigest():
            raise InvalidHashValue("Hash value is invalid.")

    @property
    def title(self) -> str:
        return self.__title

    @property
    def opus(self) -> Union[int, str]:
        return self.__opus

    @property
    def sub_opus(self) -> Union[int, None]:
        return self.__sub_opus

    @property
    def no(self) -> Union[int, None]:
        return self.__no

    @property
    def youtube_dls(self) -> List[Content]:
        return self.__youtube_dls

    @property
    def md5(self) -> str:
        return self.__md5

    def __str__(self) -> str:
        text = f"{self.__title} Op.{self.__opus}"
        if self.__sub_opus is not None:
            text += f"-{self.__sub_opus}"
        if self.__no is not None:
            text += f" No.{self.__no}"
        return text

    def __dict__(self) -> dict:
        return {
            "title": self.__title,
            "opus": self.__opus,
            "sub_opus": self.__sub_opus,
            "no": self.__no,
            "youtube_dls": self.youtube_dls,
            "md5": self.__md5,
        }

    def filename(self, index: int, ext: str = "mp3") -> str:
        """generate file name consisting of the composition title, Op., No,\\
           and artists name.

        Parameters
        ----------
        index : int
            index of contents list, If the index is outside of the range, \\
            it is treated as the remainder divided by the length of list.
        ext : str
            file extension, default is `mp3`.

        """

        index %= len(self.__youtube_dls)
        ydl = self.__youtube_dls[index]

        if not ext.startswith("."):
            ext = "." + ext

        return f"{self} {ydl}{ext}".replace(" ", "_").replace("Op.","").replace("No.", "")
