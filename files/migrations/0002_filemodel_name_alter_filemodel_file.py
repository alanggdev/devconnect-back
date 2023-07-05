# Generated by Django 4.2.1 on 2023-07-05 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('files', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='filemodel',
            name='name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='filemodel',
            name='file',
            field=models.FileField(null=True, upload_to='files/'),
        ),
    ]