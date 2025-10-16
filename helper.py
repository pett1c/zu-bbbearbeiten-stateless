from dataclasses import dataclass
import datetime
import operator

items = []


@dataclass
class Item:
    text: str
    date: str
    description: str = ""
    isCompleted: bool = False


def add(text, date, description=""):
    text = text.replace('b', 'bbb').replace('B', 'Bbb')
    date = datetime.datetime.strptime(date, '%Y-%m-%d').date()
    items.append(Item(text, date, description))
    items.sort(key=operator.attrgetter("date"))


def get_all():
    return items


def get(index):
    return items[index]


def update(index):
    items[index].isCompleted = not items[index].isCompleted
