import typing
from dataclasses import dataclass
import json
import requests

__all__ = ["get_speechers"]


def get_speechers(start: str, end: str) -> list:
    """e.g. get_speechers("2018-07-01", "2019-07-01")"""
    sy, sm, sd = start.split("-")
    ey, em, ed = end.split("-")

    # Turning into Republic of China Calendar
    from_year_republiccalendar: str = str(int(sy) - 1911)
    to_year_republiccalendar: str = str(int(ey) - 1911)

    from dataclasses import dataclass

    @dataclass
    class JsonObject:
        __slots__ = (
            "meeting_date",
            "meeting_status",
            "meeting_name",
            "meeting_content",
            "speechers",
            "meeting_unit",
        )
        meeting_date: str
        meeting_status: str
        meeting_name: str
        meeting_content: str
        speechers: str
        meeting_unit: str

    arginurl_start = f"{from_year_republiccalendar}{sm}{sd}"
    arginurl_end = f"{to_year_republiccalendar}{em}{ed}"

    __url: str = f"https://www.ly.gov.tw/WebAPI/LegislativeSpeech.aspx?from={arginurl_start}&to={arginurl_end}&meeting_unit=&mode=JSON"
    respond = requests.get(__url)
    __received: list = json.loads(respond.content)

    return __received


@dataclass
class Ly:
    name: str
    english_name: str
    gender: str
    generation: int
    party: str
    region: str
    group: list
    until: str

    def __eq__(self, o: typing.Union["Ly", str]):
        if isinstance(o, str):
            return o == self.name
        else:
            return o.name == self.name

    def to_csv(self, path: str):
        import csv

        with open(path, "a+") as file:
            writer = csv.writer(file)
            writer.writerow(
                [
                    self.name,
                    self.english_name,
                    self.gender,
                    self.generation,
                    self.party,
                    self.region,
                    self.group,
                    self.until,
                ]
            )


class LyList:
    """List of TW LYs."""

    __slots__ = "generation", "members"

    def __init__(self, *, nth: int):
        self.generation: int = nth
        self.members: typing.List[Ly] = []
        import csv

        this_file_path: str = "/".join(__file__.split("/")[:-1])
        with open(
            f"{this_file_path}/{nth}_ly_data.csv", "r", encoding="UTF-8"
        ) as ly_csv:
            reader = csv.reader(ly_csv)
            for line in reader:
                # print(line[0], line[1], line[2], line[3])
                _person = Ly(
                    line[0],  # Name
                    line[1],  # English Name
                    line[2],  # Gender
                    int(line[3]),  # Generation
                    line[4],  # Party
                    line[5],  # Region
                    line[6],  # Group
                    line[7],  # Until
                )
                self.members.append(_person)

    def __iter__(self):
        return iter(self.members)

    def __repr__(self):
        count_female: int = 0
        count_male: int = 0
        for person in self.members:
            if person.gender == "男":
                count_male += 1
            elif person.gender == "女":
                count_female += 1
        return f"<LyList(tw), gen={self.generation}, male:{count_male}, female:{count_female}, total:{len(self.members)}>"


# For internal use only. It has BUG.
class LyPage:
    """Page that stores the list of Taiwan congressmen. For internal / dev use only"""

    __slots__ = "page"

    def __init__(self, *, nth: int):
        person_line_pattern: str = r"<td><a href=(?:(?!</a></td>).)*"
        this_file_path: str = "/".join(__file__.split("/")[:-1])
        with open(
            f"{this_file_path}/tw_{nth}_ly_list.mhtml", "r", encoding="UTF-8"
        ) as html:
            self.page = html.read()
        import re

        found: list = re.findall(person_line_pattern, self.page)
        pre_name_pattern: str = r"<td><a href=.*border=0>"

        for each in found:
            ########
            # Link #
            ########
            person_link = "https://lis.ly.gov.tw" + re.search(
                r"<a href=.*? ", each
            ).group(0).replace("<a href=", "")

            ########
            # Name #
            ########
            person_name = re.sub(pre_name_pattern, "", each)
            person_name = re.sub(r"<.*>", "", person_name)

            # print(person_name, person_link)

            person_page = requests.get(person_link)

            person_page.encoding = "UTF-8"
            print(person_page.text)
            information = re.findall(r"class=dett01.*\n", person_page.text)
            for index, each in enumerate(information):
                information[index] = (
                    each.replace("<tr><td class=dett01>", "")
                    .replace("</td><td class=dett02>", " ")
                    .replace("</td></tr>", "")
                    .replace("class=dett01>", "")
                    .replace("<table width=100%><tr><td width=50%>", "")
                    .replace("</td> <td width=50%>", ",")
                    .replace(" <tr><td width=50%>", ",")
                    .replace("</table>", "")
                    .replace("<br>", "")
                    .replace("\n", "")
                    .replace("姓名 ", "")
                    .replace("英文", "")
                    .replace("性別 ", "")
                    .replace("任期 ", "")
                    .replace("黨籍 ", "")
                    .replace("選區 ", "")
                    .replace("委員會 ", "")
                    .replace("到職日期 ", "")
                    .replace("</td>", "")
                )
            Ly(
                information[0],
                information[1],
                information[2],
                information[3],
                information[4],
                information[5],
                information[6],
                information[7],
            ).to_csv(f"./{nth}_ly_data.csv")
            print("")
            import time

            time.sleep(3)
