# Generated by Django 3.0.4 on 2020-04-26 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_post_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='image',
        ),
        migrations.AddField(
            model_name='post',
            name='anteprima_immagine',
            field=models.ImageField(default='media/no-image.png', upload_to='media'),
        ),
        migrations.AddField(
            model_name='post',
            name='immagine',
            field=models.ImageField(default='media/no-image.png', upload_to='media'),
        ),
    ]
