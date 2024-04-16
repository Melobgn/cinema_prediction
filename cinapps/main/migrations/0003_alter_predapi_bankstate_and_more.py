# Generated by Django 4.2.10 on 2024-02-24 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_predapi'),
    ]

    operations = [
        migrations.AlterField(
            model_name='predapi',
            name='BankState',
            field=models.CharField(choices=[('OH', 'Ohio'), ('IN', 'Indiana'), ('DE', 'Delaware'), ('SD', 'South Dakota'), ('AL', 'Alabama'), ('FL', 'Florida'), ('GA', 'Georgia'), ('OR', 'Oregon'), ('MN', 'Minnesota'), ('NC', 'North Carolina'), ('MS', 'Mississippi'), ('SC', 'South Carolina'), ('TX', 'Texas'), ('LA', 'Louisiana'), ('IA', 'Iowa'), ('CA', 'California'), ('TN', 'Tennessee'), ('VA', 'Virginia'), ('MA', 'Massachusetts'), ('RI', 'Rhode Island'), ('PA', 'Pennsylvania'), ('MO', 'Missouri'), ('WA', 'Washington'), ('UT', 'Utah'), ('IL', 'Illinois'), ('WV', 'West Virginia'), ('KS', 'Kansas'), ('WI', 'Wisconsin'), ('NJ', 'New Jersey'), ('NY', 'New York'), ('CT', 'Connecticut'), ('MD', 'Maryland'), ('NH', 'New Hampshire'), ('ND', 'North Dakota'), ('MT', 'Mont')], max_length=2),
        ),
        migrations.AlterField(
            model_name='predapi',
            name='FranchiseBinary',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='predapi',
            name='Industry',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='predapi',
            name='State',
            field=models.CharField(choices=[('IN', 'Indiana'), ('CT', 'Connecticut'), ('NJ', 'New Jersey'), ('FL', 'Florida'), ('NC', 'North Carolina'), ('IL', 'Illinois'), ('OK', 'Oklahoma'), ('AR', 'Arkansas'), ('MN', 'Minnesota'), ('CA', 'California'), ('SC', 'South Carolina'), ('TX', 'Texas'), ('LA', 'Louisiana'), ('IA', 'Iowa'), ('OH', 'Ohio'), ('TN', 'Tennessee'), ('MS', 'Mississippi'), ('MD', 'Maryland'), ('VA', 'Virginia'), ('MA', 'Massachusetts'), ('PA', 'Pennsylvania'), ('OR', 'Oregon'), ('ME', 'Maine'), ('KS', 'Kansas'), ('MI', 'Michigan'), ('AK', 'Alaska'), ('WA', 'Washington'), ('CO', 'Colorado'), ('WY', 'Wyoming'), ('UT', 'Utah'), ('WV', 'West Virginia'), ('MO', 'Missouri'), ('AZ', 'Arizona'), ('ID', 'Idaho'), ('RI', 'Rhode Island'), ('NY', 'New York'), ('NH', 'New Hampshire'), ('NM', 'New Mexico'), ('NV', 'Nevada'), ('ND', 'North Dakota'), ('VT', 'Vermont'), ('WI', 'Wisconsin'), ('MT', 'Montana'), ('AL', 'Alabama'), ('GA', 'Georgia'), ('KY', 'Kentucky'), ('NE', 'Nebraska'), ('SD', 'South Dakota'), ('DE', 'Delaware'), ('DC', 'District of Columbia'), ('HI', 'Hawaii')], max_length=2),
        ),
    ]
