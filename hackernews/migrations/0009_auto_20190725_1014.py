# Generated by Django 2.2.3 on 2019-07-25 04:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hackernews', '0008_auto_20190725_1004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='link',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='news',
            name='title',
            field=models.TextField(),
        ),
    ]
