# Generated by Django 2.1.8 on 2019-06-15 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('port', '0004_eventtype_type_detail'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='is_dealing',
            field=models.BooleanField(default=False),
        ),
    ]
