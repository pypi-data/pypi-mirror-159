from dataclasses import dataclass, field
from .record import Record

__all__ = ["Meeting", "Meetings"]


@dataclass
class Meeting:

    __slots__ = (
        "date",
        "open_time",
        "kind",
        "title",
        "tag",
        "video_link",
        "ct1",
        "ct2",
        "ct3",
        "mc",
        "pdf_link",
        "essential_json",
        "has_downloadable_pdf",
    )
    date: str  # e.g. 2022-07-04
    open_time: str  # e.g. 14:11
    kind: str  # e.g. 본회의
    title: str
    tag: str
    video_link: str

    # These 4 properties were defined by the government webpage.#
    ct1: str  # Generation (nth)
    ct2: str  # 회수
    ct3: str  # 차수 or something, can't recall.
    mc: str  # Defined by the webpage admin

    pdf_link: str
    essential_json: str

    def __repr__(self):
        pdf_status_desc: str = (
            "available"
            if self.confer_num != "" and self.pdf_file_id != ""
            else "NOT available"
        )
        return f"{self.__class__.__name__}(date={self.date}, open_time={self.open_time}, kind={self.kind}, title={self.title}, tag={self.tag}, video_link={self.video_link}, ct1={self.ct1}, ct2={self.ct2}, ct3={self.ct3}, mc={self.mc}, confer_num={self.confer_num}, pdf_file_id={self.pdf_file_id}) PDF {pdf_status_desc}"

    @property
    def records(self) -> list:
        import json

        result: list = []
        record_list: list = json.loads(self.essential_json)
        for record in record_list:
            result.append(
                Record(
                    record["realTime"],
                    record["playTime"],
                    record["speakType"],
                    record["movieTitle"],
                    self.title,
                    self.date,
                    record["no"],
                    self.mc,
                    (self.ct1, self.ct2, self.ct3),
                    self.pdf_link,
                )
            )
        return result

    @property
    def confer_num(self) -> str:
        import re

        try:
            return (
                re.search(r"conferNum=[^&]*", self.pdf_link)
                .group(0)
                .replace("conferNum=", "")
            )
        except:
            import sys

            self.has_downloadable_pdf: bool = False
            print("\n")
            print(f"[WARNING]  {self.title}", file=sys.stderr)
            print(f"[WARNING]  Failed to get `confer_num`.", file=sys.stderr)
            print(
                f"           Some meetings have no PDF record, e.g. 도널드 J. 트럼프 미국 대통령 국회 연설 (2017.11.08)."
            )
            print(
                f"[DEBUG]    {self.ct1 =}, {self.ct2 =}, {self.ct3 =}", file=sys.stderr
            )
            print(f"[DEBUG]    {self.pdf_link =}")
            print(f"[DEBUG]    {self.video_link = }")
            print("\n")
            return ""

    @property
    def pdf_file_id(self) -> str:
        import re

        try:
            return (
                re.search(r"pdfFileId=[^&]*", self.pdf_link)
                .group(0)
                .replace("pdfFileId=", "")
            )
        except:
            import sys

            print("\n")
            print(f"[WARNING]  {self.title}", file=sys.stderr)
            print(
                f"[WARNING]  This meeting has no ** regular ** records.",
                file=sys.stderr,
            )
            print(
                f"[DEBUG]    {self.ct1 =}, {self.ct2 =}, {self.ct3 =}", file=sys.stderr
            )
            print(f"[DEBUG]    {self.pdf_link =}")
            print(f"[DEBUG]    {self.video_link = }")
            print("\n")
            if self.pdf_link:
                import requests

                page_src = requests.get("https:" + self.pdf_link).text
                img_file_num = (
                    re.findall(r"fn_fileDown(.*);", page_src)[0]
                    .split(",")[1]
                    .replace("'", "")
                    .replace(")", "")
                )
                print(f"[DEBUG]    {self.pdf_link =}, {img_file_num =}")
                # raise RuntimeError
                return img_file_num
            else:
                return ""

    def download_pdf(self, path: str = ".") -> None:
        self.has_downloadable_pdf = True
        tmp = self.confer_num, self.pdf_file_id
        if None in tmp or "" in tmp:
            self.has_downloadable_pdf = False
            print(f"conferNum, pdfFileId: {tmp}")

        if self.has_downloadable_pdf:
            import requests

            respond = requests.post(
                "http://likms.assembly.go.kr/record/mhs-10-040-0040.do",
                data={
                    "target": "I_TARGET",
                    "enctype": "multipart/form-data",
                    "conferNum": self.confer_num,
                    "fileId": self.pdf_file_id,
                },
            )
            with open(
                f"{path}/{self.date}_{self.ct1}.{self.ct2}.{self.ct3}.{self.mc}.pdf",
                "wb+",
            ) as pdf_output:
                pdf_output.write(respond.content)

    def show_pdf(self):
        file_path: str = (
            f"{self.date}_{self.ct1}.{self.ct2}.{self.ct3}.{self.mc}.pdf",
            "wb+",
        )
        import sys

        if sys.platform.startswith("darwin"):
            import os

            if os.system(f"open {file_path}") != 0:
                self.download_pdf()
        elif sys.platform.startswith("linux"):
            import os

            if os.system(f"xdg-open {file_path}") != 0:
                self.download_pdf()
        elif sys.platform.startswith("win32"):
            if os.startfile(file_path) != 0:
                self.download_pdf()
        else:
            import os

            if os.system(f"xdg-open {file_path}") != 0:
                self.download_pdf()

    def __iter__(self):
        return iter(self.records)


class Meetings:
    __slots__ = "generation", "suffix", "ls"

    def __init__(self, *, nth: int):
        self.suffix: str = (
            "st"
            if str(nth)[-1] == "1"
            else "nd"
            if str(nth)[-1] == "2"
            else "rd"
            if str(nth)[-1] == "3"
            else "th"
        )
        self.generation: int = nth
        self.ls: list = []
        package_root: str = "/".join(__file__.split("/")[:-1])
        import csv

        with open(
            f"{package_root}/{nth}{self.suffix}_20220706-000000.csv", "r"
        ) as meeting_data:
            reader = csv.reader(meeting_data)
            for line in reader:
                self.ls.append(
                    Meeting(
                        line[0],
                        line[1],
                        line[2],
                        line[3],
                        line[4],
                        line[5],
                        line[6],
                        line[7],
                        line[8],
                        line[9],
                        line[10],
                        line[11],
                    )
                )

    def __iter__(self):
        return iter(self.ls)

    def __repr__(self):
        return f"{self.__class__.__name__}(generation: {self.generation}{self.suffix}, total: {len(self.ls)})"

    def __getitem__(self, n):
        return self.ls.__getitem__(n)
