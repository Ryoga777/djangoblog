# Generated by Django 3.0.6 on 2020-05-10 08:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0006_auto_20200510_0843'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='anteprima_immagine',
        ),
    ]
