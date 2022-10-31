# Generated by Django 3.2.9 on 2022-10-29 21:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('koustaj', '0006_giris'),
    ]

    operations = [
        migrations.AddField(
            model_name='ogrencibilgi',
            name='basvuru_dosyası',
            field=models.BooleanField(default=False, verbose_name='Başvuru Dosyası'),
        ),
        migrations.AddField(
            model_name='ogrencibilgi',
            name='odegerlendirme',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='koustaj.degerlendirme'),
        ),
    ]
