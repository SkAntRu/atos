# Generated by Django 2.2.8 on 2019-12-16 11:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('meeting_room', '0023_auto_20191216_1257'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bid',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Автор заявки'),
        ),
    ]