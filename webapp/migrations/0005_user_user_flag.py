# Generated by Django 2.0.7 on 2018-07-31 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0004_auto_20180725_1113'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='user_flag',
            field=models.BooleanField(default=0),
            preserve_default=False,
        ),
    ]
