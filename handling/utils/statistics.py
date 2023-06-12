from requests import get
from handling.data.models.visits import Visit
from handling.data.models.links import Link


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
    link = Link.get_by_key(key)
    print(link)
    await Visit.create(link, await location)

    return link.original


async def get_statistics(id):
    links = Link.get_all_by_owner(id)
    statistics = []
    for link in links:
        statistics.append(await Visit.statistics(link))
    res = [tuple(row) for l1 in statistics for l2 in l1 for row in l2]

    return res


LOCATION_API_PATTERN = 'https://ipinfo.io/{ip:s}/json'
