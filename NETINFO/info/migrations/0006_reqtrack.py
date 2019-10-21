# Generated by Django 2.2.5 on 2019-10-15 03:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0005_auto_20190930_0322'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReqTrack',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('url', models.CharField(max_length=250)),
                ('ip', models.CharField(max_length=250)),
                ('resp_status_code', models.CharField(blank=True, max_length=250, null=True)),
            ],
        ),
    ]