# Generated by Django 3.0.1 on 2020-02-15 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_auto_20200215_1617'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admin',
            name='email',
            field=models.CharField(max_length=80),
        ),
        migrations.AlterField(
            model_name='enquiry',
            name='enquiry_email',
            field=models.EmailField(max_length=100),
        ),
        migrations.AlterField(
            model_name='user',
            name='useremail',
            field=models.EmailField(max_length=80),
        ),
    ]
