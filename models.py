from dataclasses import dataclass
from typing import Dict


@dataclass(frozen=True)
class Geo:
    lat: str
    lng: str

    @classmethod
    def from_dict(cls, json: Dict) -> 'Geo':
        return Geo(
            json['lat'],
            json['lng'],
        )


@dataclass(frozen=True)
class Address:
    street: str
    suite: str
    city: str
    zipcode: str
    geo: Geo

    @classmethod
    def from_dict(cls, json: Dict) -> 'Address':
        return Address(
            json['street'],
            json['suite'],
            json['city'],
            json['zipcode'],
            Geo.from_dict(json['geo']),
        )


@dataclass(frozen=True)
class Company:
    name: str
    catch_phrase: str
    bs: str

    @classmethod
    def from_dict(cls, json: Dict) -> 'Company':
        return Company(
            json['name'],
            json['catchPhrase'],
            json['bs'],
        )


@dataclass(frozen=True)
class User:
    id_: int
    name: str
    username: str
    email: str
    address: Address
    phone: str
    website: str
    company: Company

    @classmethod
    def from_dict(cls, json: Dict) -> 'User':
        return User(
            json['id'],
            json['name'],
            json['username'],
            json['email'],
            Address.from_dict(json['address']),
            json['phone'],
            json['website'],
            Company.from_dict(json['company']),
        )


@dataclass(frozen=True)
class Task:
    id_: int
    user_id: int
    title: str
    completed: bool

    @classmethod
    def from_dict(cls, json: Dict) -> 'Task':
        return Task(
            json['id'],
            json['userId'],
            json['title'],
            json['completed'],
        )
