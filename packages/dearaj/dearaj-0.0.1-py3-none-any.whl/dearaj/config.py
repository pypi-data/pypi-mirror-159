"""
This module defines

  - Widely used consts of mappings and paths, such as
    + GEN_PERIOD_DICT
    + PACKAGE_ABS_DIR
    + DATA_FILES_PATH

  - Basic low-level functions, such as
    + get_conf_file_info(conf)
    + get_conf_movie_info(conf)
    + get_conf_pdf(conf)
    + get_conf_vod_link(conf)
    + get_vod_chunks(conf)

  - Basic data structures / classes for the library, such as
    + Conference
    + Conferences

  - The main crawler(s)
    + get_conferences_of(
        nth: int,
        save: bool,
        to: str,
        sleep: Union[int, float]
      )
    + get_normal_page_of(nth: int, page: int)

"""
import pathlib
from typing import List, Union, Optional
from dataclasses import dataclass
import time
from faker import Faker

CONFIG_FILE_DIR: pathlib.Path = pathlib.Path(__file__)
PACKAGE_ABS_DIR: pathlib.Path = CONFIG_FILE_DIR.parent
DATA_FILES_PATH: pathlib.Path = PACKAGE_ABS_DIR / "data"


GEN_PERIOD_DICT: dict = {
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


def get_start_of(nth: int) -> str:
    return GEN_PERIOD_DICT[nth][0]


def get_end_of(nth: int) -> str:
    return GEN_PERIOD_DICT[nth][1]


def get_start_year_of(nth: int) -> int:
    return int(GEN_PERIOD_DICT[nth][0][:4])


def get_end_year_of(nth: int) -> int:
    return int(GEN_PERIOD_DICT[nth][1][:4])


def suffix_of(nth: int):
    return (
        "st"
        if nth % 10 == 1
        else "nd"
        if nth % 10 == 2
        else "rd"
        if nth % 10 == 3
        else "th"
    )


def get_normal_page_of(nth: int, page: int = 1) -> dict:
    start_year: int = get_start_year_of(nth)
    end_year: int = get_end_year_of(nth)
    import time

    url: str = f"https://w3.assembly.go.kr/vod/main/service/list.do?cmd=subList&menu=1&ct1={nth}&mc=&searchUpdateDate={start_year}&searchUpdateDate2={end_year}&searchCt2=&searchType_id=&mc_param2=&searchSelect=1&searchString=&curPages={page}&vv={int(time.time())}&"
    import requests
    import json

    return json.loads(
        requests.get(
            url,
            headers={
                "Accept": "application/json, text/javascript, */*; q=0.01",
                "User-Agent": Faker().user_agent(),
            },
        ).text
    )


@dataclass
class Conference:
    __slots__ = (
        "sami",
        "angun_type",
        "minutes",
        "ct1",
        "ct2",
        "ct3",
        "open_time",
        "date",
        "hand_lang",
        "mc",
        "conf_title",
        "comm_name",
        "qvod",
    )
    sami: str
    angun_type: list
    minutes: str
    ct1: str
    ct2: str
    ct3: str
    open_time: str
    date: str
    hand_lang: str
    mc: str
    conf_title: str
    comm_name: str
    qvod: int

    @property
    def vod_link(self) -> str:
        return get_conf_vod_link(self)

    @property
    def movie_list(self) -> list:
        return get_conf_vod_chunks(self)

    @property
    def movie_sublist(self) -> list:
        result: list = []
        for movie in self.movie_list:
            for chunk in movie["subList"]:
                result.append(chunk)
        return result

    @property
    def pdf(self) -> Optional[bytes]:
        return get_conf_pdf(self)

    def as_json(self) -> str:
        import json

        return json.dumps(
            {
                "sami": self.sami,
                "angunType": self.angun_type,
                "minutes": self.minutes,
                "ct1": self.ct1,
                "ct2": self.ct2,
                "ct3": self.ct3,
                "confOpenTime": self.open_time,
                "confDate": self.date,
                "handlang": self.hand_lang,
                "mc": self.mc,
                "confTitle": self.conf_title,
                "commName": self.comm_name,
                "qvod": self.qvod,
            }
        )


def get_conf_vod_link(conf: Conference) -> str:
    return f"https://w3.assembly.go.kr/vod/main/player.do?menu=1&mc={conf.mc}&ct1={conf.ct1}&ct2={conf.ct2}&ct3={conf.ct3}&wv=1&"


class get_conferences_of:
    """The crawler, craws by 'nth'"""

    __slots__ = "total_count", "last_page", "conferences"

    def __init__(
        self,
        *,
        nth: int,
        save: bool,
        to: str = "",
        sleep: Union[float, int] = 0.3,
    ):
        save_to_csv: bool = save
        save_to_csv_path: Union[str, pathlib.Path] = to
        if save_to_csv_path == "":
            save_to_csv_path = (
                PACKAGE_ABS_DIR
                / "data"
                / (str(nth) + f"_conferences_{time.strftime('%Y-%m-%d-%H-%M-%S')}.csv")
            )
        if save_to_csv:
            print(f"{save_to_csv_path = }")

        self.total_count: int = 0
        self.last_page: int = 0
        self.conferences: List[Conference] = []
        # # # # # # # # # # # # #
        # Getting the 1st page  #
        # # # # # # # # # # # # #
        first_page: dict = get_normal_page_of(nth)
        self.total_count = first_page["totCnt"]
        self.last_page = int(first_page["paging"]["moveLast"])
        for d in first_page["confList"]:
            current_conference: Conference = Conference(
                d["sami"],
                d["angunType"],
                d["minutes"],
                d["ct1"],
                d["ct2"],
                d["ct3"],
                d["confOpenTime"],
                d["confDate"],
                d["handlang"],
                d["mc"],
                d["confTitle"],
                d["commName"],
                d["qvod"],
            )
            self.conferences.append(current_conference)
            if save_to_csv:
                write_dir: Union[str, pathlib.Path] = save_to_csv_path
                import csv

                with open(write_dir, "a+", encoding="UTF-8") as output_fp:
                    writer = csv.writer(output_fp)
                    writer.writerow([current_conference.as_json()])
        time.sleep(sleep)
        for page_index in range(2, self.last_page + 1):
            current_page: dict = get_normal_page_of(nth, page_index)
            nb_items: int = len(current_page["confList"])
            if nb_items != 10 and page_index != self.last_page:
                raise RuntimeError("This is not the last page, yet items < 10")
            for d in current_page["confList"]:
                current_conference = Conference(
                    d["sami"],
                    d["angunType"],
                    d["minutes"],
                    d["ct1"],
                    d["ct2"],
                    d["ct3"],
                    d["confOpenTime"],
                    d["confDate"],
                    d["handlang"],
                    d["mc"],
                    d["confTitle"],
                    d["commName"],
                    d["qvod"],
                )
                self.conferences.append(current_conference)
                if save_to_csv:
                    import csv

                    with open(write_dir, "a+", encoding="UTF-8") as output_fp:
                        writer = csv.writer(output_fp)
                        writer.writerow([current_conference.as_json()])
            time.sleep(sleep)


class Conferences:
    """Reads csv files on the disk - has to work with local files."""

    __slots__ = "conferences", "generation"

    def __init__(self, nth: int):
        self.generation: int = nth
        self.conferences: List[Conference] = []
        data_csv_files: List[pathlib.Path] = list(
            DATA_FILES_PATH.glob(f"{nth}_conferences*.csv")
        )
        if len(data_csv_files) != 1:
            print(f"{data_csv_files = }, {len(data_csv_files) = }")
        else:
            data_csv_file: pathlib.Path = data_csv_files[0]
            import csv
            import json

            with open(data_csv_file, "r") as json_data_file:
                reader = csv.reader(json_data_file)
                for line in reader:
                    d: dict = json.loads(line[0])
                    current_conference = Conference(
                        d["sami"],
                        d["angunType"],
                        d["minutes"],
                        d["ct1"],
                        d["ct2"],
                        d["ct3"],
                        d["confOpenTime"],
                        d["confDate"],
                        d["handlang"],
                        d["mc"],
                        d["confTitle"],
                        d["commName"],
                        d["qvod"],
                    )
                    self.conferences.append(current_conference)

    def __iter__(self):
        return iter(self.conferences)

    def __getitem__(self, val):
        return self.conferences.__getitem__(val)

    def __repr__(self):
        return f"<{'Empty ' + self.__class__.__name__ + ' of ' + str(self.generation) + suffix_of(self.generation) if self.conferences == [] else self.__class__.__name__ + ' of ' + str(self.generation) + suffix_of(self.generation) + ', total: ' + str(len(self.conferences))}>"


def get_conf_movie_info(conf: Conference) -> dict:
    movie_info_link: str = f"https://w3.assembly.go.kr/vod/main/service/movie.do?cmd=movieInfo&mc={conf.mc}&ct1={conf.ct1}&ct2={conf.ct2}&ct3={conf.ct3}&no=&wv=1&vv={int(time.time())}&"
    import json
    import requests

    return json.loads(
        requests.get(
            movie_info_link,
            headers={
                "Accept": "application/json, text/javascript, */*; q=0.01",
                "User-Agent": Faker().user_agent(),
            },
        ).text
    )


def get_conf_file_info(conf: Conference) -> dict:
    conf_movie_info: dict = get_conf_movie_info(conf)
    parent_chunk: dict = conf_movie_info["movieList"][0]
    file_info_link: str = f"https://w3.assembly.go.kr/main/service/movie.do?cmd=fileInfo&mc={conf_movie_info['mc']}&ct1={conf_movie_info['ct1']}&ct2={conf_movie_info['ct2']}&ct3={conf_movie_info['ct3']}&no={parent_chunk['no']}&wv=1&xreferer=&vv={int(time.time())}&"
    import json
    import requests

    return json.loads(
        requests.get(
            file_info_link,
            headers={
                "Accept": "application/json, text/javascript, */*; q=0.01",
                "User-Agent": Faker().user_agent(),
            },
        ).text
    )


def get_conf_vod_chunks(conf: Conference) -> list:
    return get_conf_movie_info(conf)["movieList"]


def get_conf_pdf(conf: Conference) -> Optional[bytes]:
    """
    Get PDF **bytes** using http request. Returns None if PDF file not available.
    Use open(<path_to_new_file>, "wb").write(get_conf_pdf(<conf>)) to save the PDF file.
    """
    action: str = "http://likms.assembly.go.kr/record/mhs-10-040-0040.do"
    movie_info: dict = get_conf_movie_info(conf)
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # unlike 'ct1' to 'ct3', 'minutes' have different types under different situations (pages)  #
    # sometimes 'minutes' is a link, sometimes it's a number                                    #
    # for this kind of requested page, 'minutes' are links                                      #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    if movie_info["minutes"] == "":
        # # # # # # # # # # # # # # # # # # #
        # if no PDF available, return None  #
        # # # # # # # # # # # # # # # # # # #
        return
    import re

    print(movie_info["minutes"])
    confer_num: str = (
        re.search(r"conferNum=[^&]*", movie_info["minutes"])
        .group(0)
        .replace("conferNum=", "")
    )
    pdf_file_id: str = (
        re.search(r"pdfFileId=[^&]*", movie_info["minutes"])
        .group(0)
        .replace("pdfFileId=", "")
    )

    import requests

    # # # # # # # # # # #
    # HTTP POST method  #
    # # # # # # # # # # #
    respond = requests.post(
        action,
        data={
            "target": "I_TARGET",
            "enctype": "multipart/form-data",
            "conferNum": confer_num,
            "fileId": pdf_file_id,
        },
        headers={
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "User-Agent": Faker().user_agent(),
        },
    )
    # # # # # # # # # # # #
    # returns binary data #
    # # # # # # # # # # # #
    return respond.content
