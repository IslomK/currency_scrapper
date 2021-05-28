import datetime
import json

import requests

from api.exceptions import NotFoundError, InternalServerError


def get_data_from_site(from_currency, to_currency, scrap_site):
    currency = f'{from_currency}_{to_currency}'

    site_details = get_site_details(scrap_site)

    if not site_details:
        raise NotFoundError("No site found in the system with this sitename")

    try:
        resp = requests.get(site_details.get('url'), params={"q": currency, "apiKey": site_details.get("apiKey")})
    except Exception as ex:
        raise ex

    if not resp.ok:
        raise InternalServerError('Send request to {} error'.format(scrap_site))

    try:
        resp_data = resp.json()
    except ValueError as ex:
        raise InternalServerError('Parse {} response to json error. Error - {}'.format(scrap_site, ex))

    return resp_data.get('results').get(currency).get('val')


def get_site_details(site_name):
    resp = None
    with open('scrap_sites.json', 'r') as json_file:
        data = json.load(json_file)

        site_details = data.get(site_name)

        if site_details:
            resp = {
                "url": site_details.get('url'),
                "apiKey": site_details.get('apiKey'),
            }

    return resp


def write_new_site(site_name, site_url, api_key):

    with open('scrap_sites.json', 'r+') as json_file:

        file_data = json.load(json_file)

        file_data.update({site_name: {
            "url": site_url,
            "apiKey": api_key
        }})

        json_file.seek(0)

        json.dump(file_data, json_file, indent=4)

    return


def write_data_to_file(currency_from, currency_to, value, site):
    with open('currency.json', 'r+') as json_file:
        file_data = json.load(json_file)

        current_date = datetime.datetime.now().date().__str__()

        file_data.setdefault(current_date, {})

        file_data.get(current_date).update({f'{currency_from}_{currency_to}': value})
        json_file.seek(0)

        json.dump(file_data, json_file, indent=4)

    return
