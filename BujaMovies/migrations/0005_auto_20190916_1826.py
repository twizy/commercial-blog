# Generated by Django 2.2.3 on 2019-09-16 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BujaMovies', '0004_auto_20190908_1343'),
    ]

    operations = [
        migrations.AddField(
            model_name='films',
            name='realisateur',
            field=models.CharField(blank=True, default='Lui-même', max_length=50, verbose_name='Réalisateur'),
        ),
        migrations.AddField(
            model_name='films',
            name='studio',
            field=models.CharField(default='ok', max_length=30, verbose_name='Studio'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='avis',
            name='dislikes',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='avis',
            name='likes',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='films',
            name='description',
            field=models.CharField(max_length=500, verbose_name='Description'),
        ),
    ]
