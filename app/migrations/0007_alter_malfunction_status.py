# Generated by Django 4.0.4 on 2022-05-30 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_alter_malfunction_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='malfunction',
            name='status',
            field=models.CharField(default='Pending', max_length=20),
        ),
    ]
