from dataclasses import dataclass
import typing
import datetime


@dataclass
class Record:
    __slots__ = (
        "real_time",
        "play_time",
        "speak_type",
        "movie_title",
        "of",
        "date",
        "no",
        "mc",
        "ct",
        "pdf_link",
    )
    real_time: str
    play_time: str
    speak_type: str
    movie_title: str
    of: str
    date: datetime.datetime
    no: int
    mc: str
    ct: typing.Tuple[str, str, str]
    pdf_link: str

    @property
    def confer_num(self):
        import re

        return (
            re.search(r"conferNum=[^&]*", self.pdf_link)
            .group(0)
            .replace("conferNum=", "")
        )

    @property
    def pdf_file_id(self):
        import re

        return (
            re.search(r"pdfFileId=[^&]*", self.pdf_link)
            .group(0)
            .replace("pdfFileId=", "")
        )

    def has(self, o: typing.Union[object, str]):
        if isinstance(o, str):
            return o in self.movie_title
        else:
            return o.name in self.movie_title

    # I dunno if this will work yet
    @property
    def cc(self) -> dict:
        raise NotImplementedError

        import time

        time_stamp: int = int(time.time())
        link: str = f"https://w3.assembly.go.kr/main/service/smi.do?cmd=smiList&no={self.no}&mc={self.mc}&ct1={self.ct[0]}&ct2={self.ct[1]}&ct3={self.ct[2]}&v=20220203&vv={time_stamp}"
        import requests
        import json

        cc_data: dict = json.loads(requests.get(link).content)
        return cc_data
