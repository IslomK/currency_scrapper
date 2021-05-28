from api.views import ScrapView, ScrapSites
from api import app

# the application endpoints with the corresponding view Classes
app.add_url_rule('/scrap/', view_func=ScrapView.as_view('scrap_view'))
app.add_url_rule('/scrap-sites/', view_func=ScrapSites.as_view('scrap_sites_view'))