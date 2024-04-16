# Generated by Django 4.2.6 on 2024-01-12 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workapp', '0003_delete_people'),
    ]

    operations = [
        migrations.CreateModel(
            name='People',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('img', models.ImageField(upload_to='pics')),
                ('decs', models.TextField()),
            ],
        ),
    ]
