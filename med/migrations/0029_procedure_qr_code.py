# Generated by Django 3.1.5 on 2021-04-18 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('med', '0028_auto_20210418_2144'),
    ]

    operations = [
        migrations.AddField(
            model_name='procedure',
            name='qr_code',
            field=models.ImageField(blank=True, upload_to='qr_codes'),
        ),
    ]
