# Generated by Django 4.2.1 on 2023-06-05 03:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0006_remove_userprofilemodel_user_avatar_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofilemodel',
            name='user_posts',
        ),
    ]
