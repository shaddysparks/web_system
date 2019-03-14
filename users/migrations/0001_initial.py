# Generated by Django 2.2b1 on 2019-03-14 15:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import users.utils


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('marital_status', models.CharField(choices=[('SINGLE', 'Single'), ('MARRIED', 'Married'), ('SEPARATED', 'Separated'), ('DIVORCED', 'Divorced'), ('WIDOW', 'Widow')], max_length=9)),
                ('image', models.ImageField(blank=True, default='default.png', upload_to=users.utils.get_image_filename)),
                ('mobile_number', models.CharField(blank=True, max_length=12, unique=True)),
                ('date_of_birth', models.DateTimeField()),
                ('sex', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('id_number', models.IntegerField(verbose_name='ID Number')),
                ('passport_number', models.CharField(blank=True, max_length=16, unique=True)),
                ('nationality', models.CharField(choices=[('DJIBOUTI', 'Djibouti'), ('ETHIOPIAN', 'Ethiopian'), ('KENYAN', 'Kenyan'), ('SOMALI', 'Somali'), ('TANZANIAN', 'Tanzanian'), ('YEMENI', 'Yemeni'), ('UGANDAN', 'Ugandan'), ('OTHER', 'Other')], max_length=36)),
                ('address', models.CharField(blank=True, max_length=30, verbose_name='Residential address')),
                ('town', models.CharField(blank=True, max_length=30)),
            ],
        ),
    ]