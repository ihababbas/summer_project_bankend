# Generated by Django 4.2.3 on 2023-07-18 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='QuestionsData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=100)),
                ('questions', models.TextField()),
                ('correct', models.CharField(max_length=200)),
                ('wrong1', models.CharField(max_length=200)),
                ('wrong2', models.CharField(max_length=200)),
                ('wrong3', models.CharField(max_length=200)),
            ],
        ),
    ]