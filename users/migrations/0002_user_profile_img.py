# Generated by Django 3.2.7 on 2021-11-09 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='profile_img',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
