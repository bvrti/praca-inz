# Generated by Django 4.0.4 on 2022-05-30 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_malfunction_date_alter_malfunction_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='malfunction',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
