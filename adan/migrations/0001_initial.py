# Generated by Django 4.2.3 on 2023-07-31 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='adan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pray', models.CharField(max_length=255)),
                ('time', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]
