# Generated by Django 4.2.1 on 2023-06-05 04:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_postmodel_likes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postmodel',
            name='date',
            field=models.CharField(max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='postmodel',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]
