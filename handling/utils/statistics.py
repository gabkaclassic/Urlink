from requests import get

from handling.data.services.links_service import *
from handling.data.services.visit_service import statistics as statistics_by_link


DEFAULT_VAL = 'Unknown'
COUNTRY = 'country'
REGION = 'region'
CITY = 'city'

async def get_location(ip):
    info = get(LOCATION_API_PATTERN.format(ip=ip)).json()

    country = info[COUNTRY] if COUNTRY in info else DEFAULT_VAL
    region = info[REGION] if REGION in info else DEFAULT_VAL
    city = info[CITY] if CITY in info else DEFAULT_VAL

    return {
        COUNTRY: country,
        REGION: region,
        CITY: city,
    }


async def registration_visit(ip, key):
    location = get_location(ip)
    link = get_by_key(key)
    await create(link, await location)

    return link.original


async def get_statistics(id):
    links = get_all_by_owner(id)
    statistics = []
    for link in links:
        statistics.append(await statistics_by_link(link))
    res = [tuple(row) for l1 in statistics for l2 in l1 for row in l2]

    return res


LOCATION_API_PATTERN = 'https://ipinfo.io/{ip:s}/json'
