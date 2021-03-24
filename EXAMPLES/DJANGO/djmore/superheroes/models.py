from django.db import models
import logging

logging.basicConfig(
    filename='superheroes.log',
    level=logging.INFO,
)
# .debug() logging.info('msg')  .warn()  .error() .critical()

class SuperheroManager(models.Manager):
    def get_fliers(self):
        return self.filter(powers__name__icontains="fly")

class Power(models.Model):
    name = models.CharField(max_length=32)
    description = models.CharField(max_length=512)

    def __str__(self):
        return self.name

class City(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name

class Enemy(models.Model):
    name = models.CharField(max_length=32)
    powers = models.ManyToManyField(Power)

    def __str__(self):
        return self.name

class Superhero(models.Model):
    name = models.CharField(max_length=32)
    real_name = models.CharField(max_length=32)
    secret_identity = models.CharField(max_length=32)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    powers = models.ManyToManyField(Power)
    enemies = models.ManyToManyField(Enemy)
    objects = SuperheroManager()  # replace default manager with custom

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name', '-city']
        # db_table = 'superhero'
        # managed = False    don't migrate this model
        # app_label = 'tables'

    def get_brief_enemies(self):
        enemies = [e.name.split()[-1] for e in self.enemies.all()]
        return '/'.join(enemies)

    def save(self, *args, **kwargs):
        logging.info("Created superhero {}".format(self.name))
        super().save(*args, **kwargs)
        # do something else here as needed

