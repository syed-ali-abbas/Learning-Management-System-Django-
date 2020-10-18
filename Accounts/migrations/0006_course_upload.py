# Generated by Django 3.1.2 on 2020-10-17 09:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0005_auto_20201017_1351'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course_upload',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=100)),
                ('upload_file', models.FileField(upload_to='Course_Outline_Files/uploads')),
                ('class_name', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='Accounts.clas')),
            ],
        ),
    ]