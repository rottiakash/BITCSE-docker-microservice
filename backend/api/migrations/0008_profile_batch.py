# Generated by Django 2.2.3 on 2020-02-14 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_marks'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='batch',
            field=models.CharField(default='A1', max_length=2),
            preserve_default=False,
        ),
    ]
