"""testing views and tasks"""
from django.test import TestCase
from .tasks import get_pages_and_process_with_regex
from .models import PageExtract, RegexModel

class CeleryTaskTestCase(TestCase):
    """ test for celerys tasks """
    def test_scrape_task(self):
        """ tests get response and scrape data"""
        data = {
            "url_base":"https://pokemondb.net/pokedex/all",
            "regex":"View Pokedex foView Pokedex for #[0-9]+ ([A-Za-z]+).>r #[0-9]+ ([A-Za-z]+).>"
        }
        regex = RegexModel.objects.create(name="NAME", pattern=data["regex"])
        page = PageExtract.objects.create(url_base=data["url_base"])
        page.regex.add(regex)

        result = get_pages_and_process_with_regex.delay(data,page.id)
        print(result.successful(),type(result.successful()))
        self.assertFalse(result.successful())
