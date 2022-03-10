# Generated by Django 4.0.2 on 2022-03-10 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_libraries_toilets'),
    ]

    operations = [
        migrations.CreateModel(
            name='banks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=255)),
                ('Description', models.TextField()),
                ('Location', models.TextField()),
                ('Rating', models.FloatField()),
                ('Image', models.URLField()),
                ('Price', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='hospitals',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=255)),
                ('Description', models.TextField()),
                ('Location', models.TextField()),
                ('Rating', models.FloatField()),
                ('Image', models.URLField()),
                ('Price', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='malls',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=255)),
                ('Description', models.TextField()),
                ('Location', models.TextField()),
                ('Rating', models.FloatField()),
                ('Image', models.URLField()),
                ('Price', models.FloatField()),
            ],
        ),
    ]
