# Generated by Django 4.2.6 on 2023-11-18 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_rename_name_post_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post',
            field=models.IntegerField(choices=[(1, 'Story'), (2, 'Poem')]),
        ),
    ]
