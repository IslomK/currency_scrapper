import marshmallow
from marshmallow import Schema, fields, ValidationError


class ScrapSite(Schema):
    from_currency = fields.String(required=True)
    to_currency = fields.String(required=True)
    scrap_site = fields.String(required=True)


class AddScrapSite(Schema):
    site_url = fields.String(required=True)
    api_key = fields.String(required=False)
    site_name = fields.String(required=True)