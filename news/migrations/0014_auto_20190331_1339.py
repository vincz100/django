# Generated by Django 2.1.7 on 2019-03-31 11:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0013_auto_20190331_1338'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='publication_date',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2019, 3, 31, 13, 39, 35, 193390)),
        ),
        migrations.AlterField(
            model_name='category',
            name='title',
            field=models.IntegerField(choices=[(0, 'Diagnostic'), (1, 'PADD'), (2, 'Concertation')], default=0, max_length=20),
        ),
    ]
