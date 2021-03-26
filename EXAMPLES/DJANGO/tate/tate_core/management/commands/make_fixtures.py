from django.core.management.base import BaseCommand, CommandError
import os
import yaml

class Command(BaseCommand):
    help = 'Loads data from CSV'

    def add_arguments(self, parser):
        parser.add_argument('data_folder', type=str)
        parser.add_argument('max_records', type=int, default=12)

    def handle(self, *args, **options):
        fixture_file = os.path.join(options['data_folder'], 'tate_core.yaml')
        temp_file = os.path.join(options['data_folder'], 'temp.yaml')

        with open(fixture_file) as fixture_in:
            data = yaml.safe_load(fixture_in)

            fixture_records = []
            count = 0

            for record in data:
                if record['model'] == 'tate_core.artist':
                    fixture_records.append(record)
                    artworks = [a for a in data if a['model'] == 'tate_core.artwork' if a['fields']['artist'] == record['pk']]
                    fixture_records.extend(artworks)
                    count += 1
                if count == options['max_records']:
                    break


        with open(temp_file, 'w') as fixture_out:
            yaml.dump(fixture_records, fixture_out)

        os.rename(temp_file, fixture_file)

        self.stdout.write(self.style.SUCCESS(f'Successfully created {count} fixtures'))
