# Generated by Django 2.1.8 on 2019-06-15 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('port', '0003_auto_20190615_1449'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventtype',
            name='type_detail',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
