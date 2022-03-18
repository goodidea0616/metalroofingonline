# Generated by Django 2.0.5 on 2018-11-28 15:07

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HeaderMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', tinymce.models.HTMLField(verbose_name='Message')),
                ('active', models.BooleanField(default=True)),
                ('colour', models.CharField(blank=True, choices=[('Blue', 'Blue'), ('Grey', 'Grey'), ('Green', 'Green'), ('Red', 'Red'), ('Yellow', 'Yellow'), ('Teal', 'Teal'), ('Light Grey', 'Light Grey'), ('Dark Grey', 'Dark Grey')], default='Blue', max_length=120, null=True)),
            ],
        ),
    ]
