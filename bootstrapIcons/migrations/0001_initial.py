# Generated by Django 4.2.2 on 2023-06-26 01:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bootstrap_icons',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('sno2', models.PositiveIntegerField(null=True, unique=True)),
                ('name', models.CharField(max_length=255)),
                ('path', models.CharField(max_length=500)),
                ('format_download', models.CharField(default='svg', max_length=10)),
                ('category', models.CharField(max_length=60)),
                ('svgname', models.CharField(max_length=200)),
                ('searchtag', models.CharField(db_index=True, max_length=700)),
            ],
            options={
                'verbose_name': 'Bootstrap Icons',
                'verbose_name_plural': 'Bootstrap Icons',
            },
        ),
    ]
