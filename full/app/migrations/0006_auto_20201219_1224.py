# Generated by Django 3.1.4 on 2020-12-19 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20201219_1059'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('cover_pic', models.FileField(upload_to='media/%Y%M%D')),
                ('description', models.TextField()),
                ('added_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AlterField(
            model_name='student',
            name='is_registered',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]
