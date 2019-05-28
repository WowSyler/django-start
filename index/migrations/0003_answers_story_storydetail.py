# Generated by Django 2.2.1 on 2019-05-26 20:38

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0002_auto_20190524_0033'),
    ]

    operations = [
        migrations.CreateModel(
            name='Story',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='StoryDetail',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('detail', models.CharField(max_length=200)),
                ('storyid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='index.Story')),
            ],
        ),
        migrations.CreateModel(
            name='Answers',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('storyid', models.CharField(max_length=200)),
                ('adetail', models.CharField(max_length=200)),
                ('returnSdId', models.CharField(max_length=200)),
                ('storydetailid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='index.StoryDetail')),
            ],
        ),
    ]
