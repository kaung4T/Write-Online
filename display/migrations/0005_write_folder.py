# Generated by Django 3.2.9 on 2022-07-15 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('display', '0004_write_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='write',
            name='folder',
            field=models.CharField(blank=True, max_length=225, null=True),
        ),
    ]