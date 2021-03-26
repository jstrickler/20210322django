from rest_framework.test import APIClient, APITestCase
from django.urls import reverse
from tate_core.models import Artist, Artwork

ARTIST_DATA = [
    ('001e1b75-03a2-4ce6-bdf8-520c3f2af721', 'Atkinson, John Augustus'),
    ('00459ad5-dd68-4cfe-a849-4f598996a04f', 'Rivers, Leopold'),
]

class TestFetchArtistDetail(APITestCase):

    fixtures = ['tate_core.yaml']

    def setUp(self):
        self.client = APIClient()

    def test_artist_guid_retrieves_correct_name(self):
        for guid, artist_name in ARTIST_DATA:
            artist_url = reverse('tate-api:artist-detail', args=(guid,))
            response = self.client.get(artist_url)
            self.assertEqual(response.data['name'], artist_name)

    def test_artist_name(self):
        for guid, artist_name in ARTIST_DATA:
            artist = Artist.objects.filter(pk=guid).first()
            self.assertEqual(artist.name, artist_name)
