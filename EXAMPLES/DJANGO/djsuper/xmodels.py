# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class SuperheroesCity(models.Model):
    name = models.CharField(unique=True, max_length=32)

    class Meta:
        managed = False
        db_table = 'superheroes_city'


class SuperheroesEnemy(models.Model):
    name = models.CharField(unique=True, max_length=32)

    class Meta:
        managed = False
        db_table = 'superheroes_enemy'


class SuperheroesEnemyPowers(models.Model):
    enemy = models.ForeignKey(SuperheroesEnemy, models.DO_NOTHING)
    power = models.ForeignKey('SuperheroesPower', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'superheroes_enemy_powers'
        unique_together = (('enemy', 'power'),)


class SuperheroesPower(models.Model):
    description = models.CharField(max_length=512)
    name = models.CharField(unique=True, max_length=32)

    class Meta:
        managed = False
        db_table = 'superheroes_power'


class SuperheroesSuperhero(models.Model):
    real_name = models.CharField(max_length=32)
    secret_identity = models.CharField(max_length=32)
    city = models.ForeignKey(SuperheroesCity, models.DO_NOTHING)
    name = models.CharField(unique=True, max_length=32)

    class Meta:
        managed = False
        db_table = 'superheroes_superhero'


class SuperheroesSuperheroEnemies(models.Model):
    superhero = models.ForeignKey(SuperheroesSuperhero, models.DO_NOTHING)
    enemy = models.ForeignKey(SuperheroesEnemy, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'superheroes_superhero_enemies'
        unique_together = (('superhero', 'enemy'),)


class SuperheroesSuperheroPowers(models.Model):
    superhero = models.ForeignKey(SuperheroesSuperhero, models.DO_NOTHING)
    power = models.ForeignKey(SuperheroesPower, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'superheroes_superhero_powers'
        unique_together = (('superhero', 'power'),)
