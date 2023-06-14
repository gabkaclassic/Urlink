from handling.data.entities.links import Link
from handling.utils.generators import random_string
from app.urlink import db


def __generate_random_string():
    formatted = random_string()

    while exists_by_formatted(formatted):
        formatted = random_string()

    return formatted


def create(owner_id, original, title, base_url):
    key = Link.__generate_random_string()
    formatted = base_url + 'ref/' + key

    link = Link(
        title,
        original,
        formatted,
        key,
        owner_id=owner_id
    )
    db.session.add(link)
    db.session.commit()

    return formatted


def get_by_key(key):
    return Link.query.filter_by(key=key).first()


def exists_by_formatted(formatted):
    return get_by_key(formatted) is not None


def get_all_by_owner(owner_id):
    return Link.query.filter_by(owner=owner_id).all()
