# Generated by Django 3.1.2 on 2020-10-30 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0006_course_upload'),
    ]

    operations = [
        migrations.CreateModel(
            name='terms',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.DateField(default=2020)),
                ('season', models.CharField(default=None, max_length=30)),
            ],
        ),
    ]