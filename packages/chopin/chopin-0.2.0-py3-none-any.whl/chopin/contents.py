"""
Class definition that holds YouTube content.

"""

__all__ = (
    "Content",
)

from os import remove
from os.path import exists
from typing import List, Optional

from youtube_dl import YoutubeDL

from .errors import DownloadFails, FileRemoveFails


class Content(object):
    """class that holds the data of youtube content

    Attributes
    ----------
    url : str
        Youtube URL of this content
    id : str
        id for this content
    artists : List[str]
        players of this content
    path : str
        path where this content will be downloaded

    """

    def __init__(self, id: str, artists: List[str]) -> None:
        """
        Parameters
        ----------

        id : str
            id for this youtube content
        artists : List[str]
            players of this content

        """
        self.__id: str = id
        self.__artists: List[str] = artists
        self.__url: str = f"https://youtu.be/{self.__id}"
        self.__path : str = f"/tmp/{self.__id}.mp3"
        self.__downloaded : bool = False

    @property
    def url(self) -> str:
        return self.__url

    @property
    def id(self) -> str:
        return self.__id

    @property
    def artists(self) ->  List[str]:
        return self.__artists

    @property
    def path(self) -> str:
        return self.__path

    def __str__(self) -> str:
        return ("&".join(self.__artists) + "&").replace(" ", "_")

    def __dict__(self) -> dict:
        return {
            "id": self.__id,
            "artists": self.__artists,
        }

    def download(self, path: Optional[str] = None, force: bool= False) -> str:
        """download this content using `youtube-dl` library

        Parameters
        ----------
        path : Optional[str]
            path to save this content, extension must be `mp3`\\
            if `None`, save this content to default path; `/tmp/{id}.mp3`
        force : Optional[bool]
            if true, save this content, even if path already exists

        """

        if path is None:
            path = self.__path

        if not path.endswith(".mp3"):
            path += ".mp3"

        if not force and exists(path):
            raise DownloadFails("File already exists.")

        ydl_opts = {
            "format": "bestaudio/best",
            "outtmpl": path.replace(".mp3", ".%(ext)s"),
            "postprocessors": [{
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "192",
            }],
        }

        try:
            with YoutubeDL(ydl_opts) as ydl:
                ydl.download([self.__url])
            self.__path = path
            self.__downloaded = True
        except:
            raise DownloadFails("Error occured in youtube-dl.")

    def remove(self) -> None:
        """remove downloaded file"""

        if not self.__downloaded:
            raise FileRemoveFails("There is no downloaded file.")

        if not exists(self.__path):
            raise FileRemoveFails("File does not exist.")

        remove(self.__path)
        self.__downloaded = False

        return
