# Generated by Django 4.2.2 on 2023-07-13 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('caresystem', '0002_event_info_event_place_alter_event_info_oldperson_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='event_info',
            name='status',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
