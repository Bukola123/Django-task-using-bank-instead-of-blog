# Generated by Django 2.2.5 on 2021-04-29 20:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0003_comment'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
