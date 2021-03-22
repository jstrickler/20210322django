from django.core.management.base import BaseCommand, CommandError

from dogs_core.models import Dog, Breed

class Command(BaseCommand):
    help = 'Create a record for Snoopy'


    def add_arguments(self, parser):
        """
        Define options to manage.py command

        :param parser:
        :return: None
        """
        # parser.add_argument('<arg>', type=<type>)
        pass # not needed for this command

    def handle(self, *args, **options):
        """
        Code for manage.py command

        :param args: not used
        :param options: Dictionary of options as defined in add_arguments()
        :return: None
        """

        breed = Breed.objects.filter(name__icontains="beagle")
        if len(breed) == 0:  # if Beagle not in table
            breed = Breed(name="Beagle", abbr="BE")
            breed.save()
        else:
            breed = breed.first()

        snoopy = Dog(name="Snoopy", breed=breed, sex='m', weight=30)

        snoopy.save()

