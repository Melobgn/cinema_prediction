# Generated by Django 4.2.10 on 2024-02-24 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PredApi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('State', models.CharField(max_length=2)),
                ('BankState', models.CharField(max_length=2)),
                ('RevLineCr', models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], max_length=1)),
                ('LowDoc', models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], max_length=1)),
                ('NewExist', models.IntegerField(choices=[(1, 'Existing business'), (2, 'New business')])),
                ('UrbanRural', models.IntegerField(choices=[(1, 'Urban'), (2, 'Rural'), (0, 'Undefined')])),
                ('FranchiseBinary', models.IntegerField()),
                ('Zip', models.IntegerField()),
                ('NAICS', models.IntegerField()),
                ('Term', models.IntegerField()),
                ('NoEmp', models.IntegerField()),
                ('CreateJob', models.IntegerField()),
                ('RetainedJob', models.IntegerField()),
                ('FranchiseCode', models.IntegerField()),
                ('GrAppv', models.FloatField()),
                ('SBA_Appv', models.FloatField()),
                ('Industry', models.CharField(max_length=50)),
                ('Prediction', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
