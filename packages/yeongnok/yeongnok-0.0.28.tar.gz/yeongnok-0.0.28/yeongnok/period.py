import objprint
import datetime
import typing
from .record import Record


__all__ = ["period"]


class period:
    """Metainfo records that contains 'essential person' data, in a given period."""

    __slots__ = (
        "result",
        "start",
        "end",
        "data",
        "min_date",
        "max_date",
        "csv_files",
    )
    GEN_PERIOD = {
        21: ("2020-05-30", "2024-05-29"),
        20: ("2016-05-30", "2020-05-29"),
        19: ("2012-05-30", "2016-05-29"),
        18: ("2008-05-30", "2012-05-29"),
        17: ("2004-05-30", "2008-05-29"),
        16: ("2000-05-30", "2004-05-29"),
        15: ("1996-05-30", "2000-05-29"),
        14: ("1992-05-30", "1996-05-29"),
        13: ("1988-05-30", "1992-05-29"),
        12: ("1985-04-11", "1988-05-29"),
        11: ("1981-04-11", "1985-04-10"),
        10: ("1979-03-12", "1980-10-27"),
        9: ("1973-03-12", "1979-03-11"),
        8: ("1971-07-01", "1972-10-17"),
        7: ("1967-07-01", "1971-06-30"),
        6: ("1963-12-17", "1967-06-30"),
    }

    def __init__(self, start_date: str, end_date: str):

        self.start: datetime.datetime = datetime.datetime.strptime(
            start_date, "%Y-%m-%d"
        )
        self.end: datetime.datetime = datetime.datetime.strptime(end_date, "%Y-%m-%d")
        self.data: typing.List[dict] = []

        # # # Getting file that satisfys given range # # #
        import os
        import re

        package_root_dir: str = __file__.replace("/period.py", "")

        page_data_list: list = os.listdir(package_root_dir)
        self.csv_files: list = []
        for key in self.GEN_PERIOD.keys():
            period_start = datetime.datetime.strptime(
                self.GEN_PERIOD[key][0], "%Y-%m-%d"
            )
            period_end = datetime.datetime.strptime(self.GEN_PERIOD[key][1], "%Y-%m-%d")
            if period_start <= self.start <= period_end:
                _nth_start: int = key
            if period_start <= self.end <= period_end:
                _nth_end: int = key
        for _nth in range(_nth_start, _nth_end + 1):
            for single_file in page_data_list:
                if re.search(rf"^{_nth}(st|nd|rd|th).*\.csv$", single_file):
                    self.csv_files.append(package_root_dir + "/" + single_file)

        import csv

        self.result: typing.List[Record] = []
        for csv_file in self.csv_files:
            # # # Reading CSV # # #
            with open(csv_file, "r") as _csv_file:
                reader = csv.reader(_csv_file)
                for line in reader:
                    record_date: datetime.datetime = datetime.datetime.strptime(
                        line[0], "%Y-%m-%d"
                    )
                    if self.start <= record_date <= self.end:  # Get the right range
                        record: dict = {
                            "date": line[0],
                            "time": line[1],
                            "group": line[2],
                            "title": line[3],
                            "link": line[5],
                            "ct1": line[6],
                            "ct2": line[7],
                            "ct3": line[8],
                            "mc": line[9],
                            "pdf_link": "https:" + line[10],
                            "essential_json": line[11],  # VOD Metadata
                        }

                        # mc: str = ""
                        # mc = re.findall(r"mc=[^&]*", record["link"])[0].replace(
                        # "mc=", ""
                        # )

                        import json

                        # # # # # # # # # # # # # # # # # # # #
                        #                                     #
                        #  __dict: single VOD metadata chunk  #
                        #                                     #
                        # # # # # # # # # # # # # # # # # # # #

                        __dicts: typing.List[dict] = json.loads(
                            record["essential_json"]
                        )

                        for __dict in __dicts:
                            self.result.append(
                                Record(
                                    __dict["realTime"]
                                    if __dict["realTime"] is not None
                                    else "??:??:??",
                                    __dict["playTime"],
                                    __dict["speakType"],
                                    __dict["movieTitle"],
                                    record["title"],
                                    datetime.datetime.strptime(
                                        record["date"], "%Y-%m-%d"
                                    ),
                                    __dict["no"],
                                    # mc,
                                    record["mc"],
                                    (record["ct1"], record["ct2"], record["ct3"]),
                                    record["pdf_link"],
                                ),
                            )
        if self.result != []:
            self.min_date = self.result[0].date
            self.max_date = self.result[0].date
        else:
            self.min_date = self.max_date = datetime.datetime.max

        for each_record in self.result:
            if each_record.date <= self.min_date:
                self.min_date = each_record.date
            if each_record.date >= self.max_date:
                self.max_date = each_record.date

    def __iter__(self):
        return self.result.__iter__()

    def download_pdf(self, path: str = "", delta_time: typing.Union[int, float] = 2):
        queue = []
        import requests
        import time

        for record in self.result:
            if (record.confer_num, record.pdf_file_id) not in queue:
                queue.append((record.confer_num, record.pdf_file_id))

                respond = requests.post(
                    "http://likms.assembly.go.kr/record/mhs-10-040-0040.do",
                    data={
                        "target": "I_TARGET",
                        "enctype": "multipart/form-data",
                        "conferNum": record.confer_num,
                        "fileId": record.pdf_file_id,
                    },
                )
                with open(
                    f"{path}/{record.date.strftime('%Y-%m-%d')}_{record.ct[0]}.{record.ct[1]}.{record.ct[2]}.{record.mc}.pdf",
                    "wb+",
                ) as pdf_output:
                    pdf_output.write(respond.content)
                time.sleep(delta_time)


"""
# test
p = period("1998-08-01", "2008-01-01")
print(p.min_date, p.max_date, p.csv_files)
ls = [r for r in p if r.has("박근혜")]

print(ls[0])
print(ls[-1])
"""
