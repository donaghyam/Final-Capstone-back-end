# Generated by Django 4.0.5 on 2022-06-10 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_api', '0007_remove_useringredients_alpha_acids_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='useringredients',
            name='unit',
            field=models.CharField(default='oz', max_length=3),
        ),
    ]
