# Generated by Django 3.0.4 on 2020-06-23 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mydream', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('story', models.CharField(max_length=800)),
                ('img', models.ImageField(upload_to='pics')),
                ('title', models.CharField(max_length=200)),
            ],
        ),
    ]
