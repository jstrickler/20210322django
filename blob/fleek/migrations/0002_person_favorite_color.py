# Generated by Django 3.1.7 on 2021-03-22 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fleek', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='favorite_color',
            field=models.CharField(default='red', max_length=16),
            preserve_default=False,
        ),
    ]