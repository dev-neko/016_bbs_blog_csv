# Generated by Django 3.1.7 on 2021-04-21 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0014_delete_searchquerymodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdatamodel',
            name='md_ac_id',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='userdatamodel',
            name='md_ac_pass',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='userdatamodel',
            name='md_line_token',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='userdatamodel',
            name='md_to_email',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
