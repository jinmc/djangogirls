# Generated by Django 3.0.6 on 2020-05-23 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20200523_0705'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job_heykorean',
            name='published_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]