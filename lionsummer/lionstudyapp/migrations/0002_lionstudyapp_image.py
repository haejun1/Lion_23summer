# Generated by Django 4.2 on 2023-06-26 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lionstudyapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='lionstudyapp',
            name='image',
            field=models.ImageField(default=2, upload_to=''),
            preserve_default=False,
        ),
    ]
