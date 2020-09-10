# Generated by Django 3.0.2 on 2020-09-10 11:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(blank=True, default='', max_length=150)),
                ('about', models.TextField(blank=True, default='')),
                ('profile_image', models.ImageField(blank=True, default='default/default_profile_image.png', upload_to='profile_image/%Y/%m/%d', verbose_name='Profile Image')),
                ('profile_image_thumbnail', models.ImageField(blank=True, upload_to='profile_image_thumbnail/%Y/%m/%d', verbose_name='Profile Image Thumbnail')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
