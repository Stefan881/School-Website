# Generated by Django 4.2.7 on 2023-11-17 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_alter_record_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='record',
            name='Reg_No',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
