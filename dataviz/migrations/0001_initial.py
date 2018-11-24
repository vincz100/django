# Generated by Django 2.1.3 on 2018-11-22 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Statistiques',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codgeo', models.CharField(max_length=5)),
                ('libgeo', models.TextField(null=True)),
                ('epci', models.CharField(max_length=9)),
                ('libepci', models.TextField(null=True)),
                ('dep', models.CharField(max_length=2)),
                ('libdep', models.TextField(null=True)),
                ('reg', models.CharField(max_length=2)),
                ('libreg', models.TextField(null=True)),
                ('d68_pop', models.FloatField()),
                ('d75_pop', models.FloatField()),
                ('d82_pop', models.FloatField()),
                ('d90_pop', models.FloatField()),
                ('d99_pop', models.FloatField()),
                ('p10_pop', models.FloatField()),
                ('p15_pop', models.FloatField()),
                ('varpop_6875', models.FloatField()),
                ('varpop_7582', models.FloatField()),
                ('varpop_8290', models.FloatField()),
                ('varpop_9099', models.FloatField()),
                ('varpop_9910', models.FloatField()),
                ('varpop_1015', models.FloatField()),
            ],
            options={
                'verbose_name': 'statistiques communale',
                'ordering': ['codgeo'],
            },
        ),
    ]
