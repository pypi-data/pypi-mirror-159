"""
    This program was written on July 2nd, 2022
    by Anji Wong (anzhi0708@hufs.ac.kr, anzhi0708@gmail.com),
    **for research use only.**

    Even through I tried to access KR Assembly data by
    using its Open API service,
    some critical data was missing in the returned json / xml string.

    So I had to manually write this web crawler.
    Hopefully this will help me finishing my paper.

    Since we are trying to keep sending http requests
    to the KR Assembly website,
    we have to keep the request's frequency on a relatively low level,
    **so that we won't be end up in jail.**
    This is important, especially when you have no basic knowledge of
    the principles of http services.
    So please always write `time.sleep(n)` and keep n greater than 2.
"""

import re
import os

__version__ = "0.0.18"

from .request import send
from .site import page
from .record import Record
from .congressman import Congressman, List
from .tools.analyzer import get_activities_of
from .period import period
from .tools import downloader
from .region import tw
from .meeting import *
from .pdfminer_six import pdfminer

__all__ = [
    "get_activities_of",
    "page",
    "send",
    "Congressman",
    "List",
    "period",
    "Record",
    "tw",
    "Meeting",
    "Meetings",
    "pdfminer",
]

print(
    "[INFO]     This program was written in July 2022,\n"
    + " " * 11
    + "currently supports the 6th to the 20th assembly data, partly supports the 21st assembly."
)


detected: list = []

for file in os.listdir():
    for nth in range(6, 21):
        if re.search(rf"^{nth}.*\.csv$", file):
            detected.append(nth)

print(f"[DATA]     Found:   {sorted(detected)}")

ls_missing: list = []

for n in range(6, 21):
    if n not in detected:
        ls_missing.append(n)

print(f"           Missing: {ls_missing if ls_missing != [] else None}")

SUFFIX: dict = {
    6: "th",
    7: "th",
    8: "th",
    9: "th",
    10: "th",
    11: "st",
    12: "nd",
    13: "rd",
    14: "th",
    15: "th",
    16: "th",
    17: "th",
    18: "th",
    19: "th",
    20: "th",
    21: "st",
}


for nth in ls_missing:
    try:
        print(f"\n[DATA]     Fetching data...({nth}{SUFFIX[nth]})")
        downloader.download(nth)
    except:
        print(
            f"\n[DATA]     Could not download {nth}{SUFFIX[nth]} assembly data from 'github.com/anzhi0708'.\n"
        )
