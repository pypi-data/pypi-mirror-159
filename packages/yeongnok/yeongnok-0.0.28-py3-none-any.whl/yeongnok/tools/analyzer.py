"""

"""
import sys
from typing import Union


__all__ = ["get_activities_of"]


def get_activities_of(person, *, at: int = 0, path: str = ".") -> list:
    sys.path.append("..")
    from yeongnok.congressman import Congressman

    if at == 0:
        at = person.generation

    if not isinstance(person, Congressman):
        if isinstance(person, str):
            person = Congressman(
                name=person,
                generation=0,
                party="",
                group=[],
                region="",
                n=0,
                how="",
                gender="",
            )
        else:
            raise TypeError("Must be of the type 'Congressman' or 'str'")

    import os
    import re
    import csv
    import json
    import pprint

    suffix: str = (
        "st"
        if at % 10 == 1
        else "nd"
        if at % 10 == 2
        else "rd"
        if at % 10 == 3
        else "th"
    )
    matched: bool = False

    # # # Logic of analyzing file on disk
    # # # Same code reused later, by copy & pasting
    for file in os.listdir(path):
        if re.match(rf"[0]*{at}(st|nd|rd|th)", file) and file.endswith(".csv"):
            result: list = []
            matched = True
            with open(f"{path}/{file}", "r") as f:
                reader = csv.reader(f)
                for index, line in enumerate(reader):
                    data: dict = json.loads(line[-1])
                    for i, d in enumerate(data):
                        if person.name in d["movieTitle"]:
                            result.append(
                                f"{d['realTime'] if d['realTime'] is not None else '??:??:??'} {person.name} {d['speakType']}, {line[0]} {line[1]} {line[2]}, {line[3]}, {d['movieTitle']}"
                            )

            return result

    print(
        f"[WARNING]  {person.name}({person.party}) {at}{suffix}: CSV file not found in {'current directory' if path == '.' or './' else path}.\n"
        if not matched
        else "\n[OK]"
    )
    print(
        f"           Download CSV file from 'https://github.com/anzhi0708/yeongnok'? [yes/no]"
    )
    user_input: str = input("\n[YES/no]:  ")
    if user_input.lower() in ("y", "yes", "ye", " ") or user_input == "":
        print("           Now downloading...")
        import wget

        try:
            wget.download(
                f"https://github.com/anzhi0708/yeongnok/raw/main/{at}{suffix}_20220706-000000.csv"
            )
            for file in os.listdir():
                if re.match(rf"[0]*{at}(st|nd|rd|th)", file) and file.endswith(".csv"):
                    print(f"\n[ANALYZER] {path=}, {file=}, {at}{suffix} Assembly")
                    result = []
                    matched = True
                    with open(f"{file}", "r") as f:
                        reader = csv.reader(f)
                        for index, line in enumerate(reader):
                            data = json.loads(line[-1])
                            for i, d in enumerate(data):
                                if person.name in d["movieTitle"]:
                                    result.append(
                                        f"{d['realTime'] if d['realTime'] is not None else '??:??:??:??'} {person.name} {d['speakType']}, {line[0]} {line[1]} {line[2]}, {line[3]}, {d['movieTitle']}"
                                    )
                    return result
        except:
            print(
                f"[ANALYZER] Error occured when getting {person.name}({person.party})'s data online:"
            )
            print(
                f"           Could not download ** {at}{suffix} ** data from 'github.com/anzhi0708'."
            )
            print("           Download from 'https://w3.assembly.go.kr/' instead?")

            user_input = input("\n[YES/no]:  ")

            if user_input.lower() in ("y", "yes", "ye", "", " "):
                print(
                    f"\n[CRAWLER]  Downloading {at}{suffix} assembly data from ** Korean government website **"
                )
                print("\n           This could take ~20 minutes.\n")

                import time

                start_time: str = time.strftime("%Y%m%d-%H%M%S")
                from yeongnok.site import page

                result = []

                for pg in page(1, -1, nth=at):
                    pg.to_csv(f"{path}/{at}{suffix}_{start_time}.csv")
                    for _d in pg.data:
                        d = json.loads(pg.data[_d]["essential_json"])
                        for o in d:
                            if person.name in o["movieTitle"]:
                                result.append(
                                    f"{o['realTime'] if o['realTime'] is not None else '??:??:??:??'} {person.name} {o['speakType']}, {pg.data[_d]['date']} {pg.data[_d]['time']} {pg.data[_d]['group']} {pg.data[_d]['title']}, {o['movieTitle']}"
                                )
                return result
            elif user_input.lower() in ("n", "no", "noo"):
                print(
                    f"[STOPPED]  Will not analyze {person.name}({person.party})'s data.\n"
                )
                return []
            else:
                print("           Unknown command.")
                print(
                    f"[STOPPED]  Will not analyze {person.name}({person.party})'s data.\n"
                )
                return []
    else:
        print(f"[STOPPED]  Could not find {at}{suffix} Assembly CSV data")
        print(f"           Will not analyze {person.name}({person.party})'s data.\n")
        return []

    return []
