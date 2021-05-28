Simple currency scrapper service.

SCRAP THE DATA

``
POST /scrap/
`` - get the currency data from the provided site and write it to the file `currency.json`

Params

- `from_currency` - currency to be converted from
- `to_currency` - currency to be converted to
- `scrap_site` - name of the site to be used

GET THE LIST OF SITES

``
GET /scrap-sites/ 
`` - list of the sites where it can be scrapped


ADD NEW SITE

``
POST /scrap-sites/
`` - add new scrap site to use. Adds next to old sites in the file `scrap_sites.json`

Params:

- ``site_url`` - url of the site where the requests shoul be made

- ``api_key`` - api key in order to make sure it is secure

- ``site_name`` - name of the site
