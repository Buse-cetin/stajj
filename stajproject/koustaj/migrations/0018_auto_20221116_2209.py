# Generated by Django 3.2.9 on 2022-11-16 19:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('koustaj', '0017_auto_20221116_2207'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ogrencibilgi',
            name='odegerlendirme',
        ),
        migrations.RemoveField(
            model_name='ogrencibilgi',
            name='ofirma',
        ),
        migrations.RemoveField(
            model_name='ogrencibilgi',
            name='ogretmen',
        ),
    ]
