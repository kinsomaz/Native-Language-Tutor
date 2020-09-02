# Generated by Django 3.1 on 2020-08-27 19:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('language', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField(blank=True, max_length=500, null=True)),
                ('avatar', models.ImageField(blank=True, default='default.jpg', null=True, upload_to='avatar')),
                ('gender', models.CharField(choices=[('Female', 'Female'), ('Male', 'Male')], default='Male', max_length=30)),
                ('languages', models.ManyToManyField(to='language.Language')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]