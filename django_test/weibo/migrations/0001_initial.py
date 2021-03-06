# Generated by Django 2.0.3 on 2018-04-19 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Weibo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('content', models.TextField(max_length=1000)),
                ('author', models.CharField(max_length=30)),
                ('website', models.URLField(blank=True)),
                ('blog_date', models.DateField(blank=True, null=True)),
            ],
        ),
    ]
