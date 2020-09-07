# Generated by Django 3.0.8 on 2020-08-28 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20200827_1958'),
    ]

    operations = [
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_title', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=500)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('skills_learned', models.CharField(max_length=200)),
            ],
        ),
        migrations.AlterField(
            model_name='contactmessages',
            name='message',
            field=models.TextField(max_length=500),
        ),
    ]