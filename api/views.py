import json

from flask.views import MethodView
from flask import request, make_response
from marshmallow import ValidationError

from api.exceptions import BadRequest
from api.schemas import ScrapSite, AddScrapSite
from utils.helper import get_data_from_site, write_data_to_file, write_new_site


class ScrapView(MethodView):
    def post(self):
        json_data = request.get_json()

        if not json_data:
            raise BadRequest("No input data provided")

        try:
            data = ScrapSite().load(json_data)
        except ValidationError as err:
            raise BadRequest(err.messages)

        from_currency = data.get('from_currency')
        to_currency = data.get('to_currency')
        scrap_site_url = data.get('scrap_site')

        value = get_data_from_site(from_currency, to_currency, scrap_site_url)

        try:
            write_data_to_file(
                currency_from=from_currency,
                currency_to=to_currency,
                value=value,
                site=scrap_site_url
            )
        except Exception as ex:
            raise ex

        return make_response({
            "from": from_currency,
            "to": to_currency,
            "value": value
        })


class ScrapSites(MethodView):
    def get(self):
        with open('scrap_sites.json', 'r+') as json_file:
            file_data = json.load(json_file)

        return file_data

    def post(self):
        json_data = request.get_json()

        if not json_data:
            raise BadRequest("No input data provided")

        try:
            data = AddScrapSite().load(json_data)
        except ValidationError as err:
            raise BadRequest(err.messages)

        site_name = data.get('site_name')
        site_url = data.get('site_url')
        api_key = data.get('api_key')

        try:
            write_new_site(
                site_name=site_name,
                site_url=site_url,
                api_key=api_key
            )
        except Exception as ex:
            raise ex

        return make_response()