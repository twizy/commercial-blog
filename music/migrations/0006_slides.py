# Generated by Django 2.2.5 on 2019-09-17 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0005_auto_20190916_1117'),
    ]

    operations = [
        migrations.CreateModel(
            name='Slides',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slides', models.ImageField(blank=True, null=True, upload_to='slides/')),
            ],
        ),
    ]
