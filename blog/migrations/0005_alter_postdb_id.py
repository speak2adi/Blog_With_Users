# Generated by Django 4.1.1 on 2022-11-28 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_postdb_delete_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postdb',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
