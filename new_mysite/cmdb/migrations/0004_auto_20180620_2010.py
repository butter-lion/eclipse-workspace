# Generated by Django 2.0.5 on 2018-06-20 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmdb', '0003_auto_20180620_2007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='ctime',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='creattime',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
