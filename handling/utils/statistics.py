from requests import get
from handling.data.models import Visit, Link


async def get_location(ip):
    info = get(LOCATION_API_PATTERN.format(ip=ip)).json()

    return {
        'country': info['country'],
        'region': info['region'],
        'city': info['city'],
    }


async def registration_visit(ip, formatted):
    location = get_location(ip)
    link = Link.get_by_formatted(formatted)
    await Visit.create(link, location)

    return link.original
    


LOCATION_API_PATTERN = 'https://ipinfo.io/{ip:s}/json'
