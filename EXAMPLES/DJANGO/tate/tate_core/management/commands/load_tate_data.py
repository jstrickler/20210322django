from django.core.management.base import BaseCommand, CommandError
import csv
import os

# change "tate_core" to your app name and models to your model names if necessary
from tate_core.models import Artwork, Artist

class Command(BaseCommand):
    help = 'Loads data from CSV'

    def add_arguments(self, parser):
        parser.add_argument('data_folder', type=str)

    def handle(self, *args, **options):
        artist_file = os.path.join(options['data_folder'], 'artist_data.csv')
        artwork_file = os.path.join(options['data_folder'], 'artwork_data.csv')

        # load artists
        with open(artist_file) as artist_in:
            rdr = csv.reader(artist_in)
            next(rdr)  # skip header line
            for id,name,gender,dates,yearOfBirth,yearOfDeath,placeOfBirth,placeOfDeath,url in rdr:
                yearOfBirth = yearOfBirth if yearOfBirth else None
                yearOfDeath = yearOfDeath if yearOfDeath else None
                artist = Artist(tate_id=id, name=name, place_of_birth=placeOfBirth, birth_year=yearOfBirth,
                                death_year=yearOfDeath, tate_url=url)
                artist.save()

        with open(artwork_file) as artwork_in:
            rdr = csv.reader(artwork_in)
            next(rdr)  # skip header line
            for (id,accession_number,artist,artistRole,artistId,title,dateText,medium,creditLine,
                 year,acquisitionYear,dimensions,width,height,depth,units,inscription,thumbnailCopyright,
                 thumbnailUrl,url) in rdr:

                artist = Artist.objects.filter(tate_id=artistId).first()

                artwork = Artwork(
                    title=title,
                    date_text=dateText,
                    thumbnail_url=thumbnailUrl,
                    tate_url=url,
                    artist=artist,
                )
                artwork.save()

        self.stdout.write(self.style.SUCCESS('Successfully loaded data'))
