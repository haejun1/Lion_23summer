# Generated by Django 4.2 on 2023-06-28 11:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('lionstudyapp', '0003_remove_lionstudyapp_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='lionstudyapp',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
    ]
