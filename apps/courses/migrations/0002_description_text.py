# Generated by Django 2.1 on 2018-08-15 01:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='description',
            name='text',
            field=models.TextField(null=True),
        ),
    ]