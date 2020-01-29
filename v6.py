"""
V6 Boardfile and Decoder Library
"""

from typing import NamedTuple, List
from enum import Enum

class Template:
    def __init__(self, template_dict):
        self.screens = template_dict["screens"]
        self.tags = template_dict["tags"]
        all_fields = []
        i = 0
        for screen in self.screens:
            screen_title = screen["title"].lower()
            for row in screen["layout"]:
                for field in row:
                    all_fields.append((screen_title, field["name"], i))
                    i += 1
        for tag in self.tags:
            all_fields.append((None, tag, i))
            i += 1
        self.all_fields = all_fields


    def lookup(self, screen_name: str, field_name: str):
        screen_low = screen_name.lower()
        for field in self.all_fields:
            if field[0] == screen_low and field[1] == field_name:
                return field[2]
        raise IndexError()

    def lookup_tag(self, tag_name: str):
        return self.lookup(None, tag_name)


class Boardfile:
    def __init__(self, bf_dict):
        self.bf_dict = bf_dict
        self.year = bf_dict["year"]
        self.revision = bf_dict["revision"]
        self.robot_scout = Template(bf_dict["robot_scout"])
        self.super_scout = Template(bf_dict["super_scout"])


class DataPoint(NamedTuple):
    type_index: int
    value: int
    time: float


class Board(Enum):
    R1 = "R1"
    R2 = "R2"
    R3 = "R3"
    B1 = "B1"
    B2 = "B2"
    B3 = "B3"
    RX = "RX"
    BX = "BX"


class Entry(NamedTuple):
    match: str
    team: str
    scout: str
    board: Board
    timestamp: int
    data_points: List[DataPoint]
    comments: str

    def count(self, type_index):
        cnt = 0
        for dp in self.data_points:
            if dp.type_index == type_index:
                cnt += 1
        return cnt

    def last_value(self, type_index):
        for dp in reversed(self.data_points):
            if dp.type_index == type_index:
                return dp
        return None 

    @property
    def match_number(self):
        return int(self.match.split("_")[-1])

    @property
    def team_number(self):
        return int(self.team)

    @property
    def is_super_scout(self):
        return self.board == Board.RX or self.board == Board.BX


def from_b64(ch: str):
    n = ord(ch)
    if ch == "/":
        return 63
    if ch == "+":
        return 62
    if 48 <= n <= 57:
        return n + 4
    if 65 <= n <= 90:
        return n - 65
    if 97 <= n <= 122:
        return n - 71
    raise ValueError()


def decode_dp(sequence: str, start_index: int):
    a = from_b64(sequence[start_index])
    b = from_b64(sequence[start_index + 1])
    c = from_b64(sequence[start_index + 2])
    d = from_b64(sequence[start_index + 3])
    value = (b & 0b111100) >> 2 
    time = (b & 0b11) << 12 | c << 6 | d
    return DataPoint(a, value, time / 100.0)


def decode_all_dp(sequence: str):
    if len(sequence) % 4 != 0:
        raise ValueError()
    return [decode_dp(sequence, i) for i in range(0, len(sequence), 4)]


def parse_entry(encoded: str) -> Entry :
    sp = encoded.split(":")
    sp[3] = Board(sp[3]) # convert from string to Board
    sp[4] = int(sp[4], base=16) # convert to int timestamp
    sp[5] = decode_all_dp(sp[5]) # decode the data
    return Entry(*sp)


def parse_all_entries(all_entries: str):
    return [parse_entry(e) for e in all_entries.split("\n")]
