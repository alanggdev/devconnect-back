# Generated by Django 4.2.1 on 2023-06-05 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0007_remove_userprofilemodel_user_posts'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofilemodel',
            name='user_avatar',
            field=models.ImageField(null=True, upload_to='profile/avatar/'),
        ),
        migrations.AddField(
            model_name='userprofilemodel',
            name='user_description',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='userprofilemodel',
            name='user_status',
            field=models.CharField(max_length=25, null=True),
        ),
    ]
