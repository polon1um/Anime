# Generated by Django 3.1.3 on 2020-11-13 17:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Жанр', 'verbose_name_plural': 'Жанры'},
        ),
        migrations.CreateModel(
            name='Manga',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('desc', models.TextField(blank=True)),
                ('avtor', models.CharField(max_length=128)),
                ('painter', models.CharField(max_length=128)),
                ('data', models.DateField()),
                ('page', models.IntegerField(default=0)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.category')),
            ],
            options={
                'verbose_name': 'Манга',
                'verbose_name_plural': 'Манга',
            },
        ),
    ]