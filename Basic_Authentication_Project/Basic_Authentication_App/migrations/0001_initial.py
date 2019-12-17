# Generated by Django 2.0.5 on 2019-05-03 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Emp',
            fields=[
                ('empid', models.IntegerField(primary_key=True, serialize=False)),
                ('empname', models.CharField(max_length=20)),
                ('salary', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]
