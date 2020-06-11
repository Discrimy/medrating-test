from dataclasses import dataclass, field
from dataclasses_json import dataclass_json, LetterCase, config


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass(frozen=True)
class Geo:
    lat: str
    lng: str


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass(frozen=True)
class Address:
    street: str
    suite: str
    city: str
    zipcode: str
    geo: Geo


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass(frozen=True)
class Company:
    name: str
    catch_phrase: str
    bs: str


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass(frozen=True)
class User:
    id_: int = field(metadata=config(field_name='id'))
    name: str
    username: str
    email: str
    address: Address
    phone: str
    website: str
    company: Company


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass(frozen=True)
class Task:
    id_: int = field(metadata=config(field_name='id'))
    user_id: int
    title: str
    completed: bool
