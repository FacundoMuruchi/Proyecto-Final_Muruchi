# Generated by Django 4.2.6 on 2023-11-19 22:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0006_alter_post_post'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Usuario',
        ),
        migrations.AddField(
            model_name='post',
            name='creator',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
