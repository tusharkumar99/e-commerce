# Generated by Django 3.1.4 on 2021-02-06 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_auto_20210131_0147'),
    ]

    operations = [
        migrations.CreateModel(
            name='contactus',
            fields=[
                ('message_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('message', models.CharField(max_length=300)),
                ('email', models.CharField(max_length=50)),
            ],
        ),
    ]
