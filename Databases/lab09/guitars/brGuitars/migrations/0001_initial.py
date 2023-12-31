# Generated by Django 3.2.3 on 2022-09-05 16:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('country', models.CharField(blank=True, max_length=200, null=True)),
                ('birth', models.IntegerField(blank=True, null=True)),
                ('death', models.IntegerField(blank=True, null=True)),
                ('pic', models.URLField(blank=True, max_length=500, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Guitar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=200)),
                ('year', models.IntegerField(blank=True, null=True)),
                ('top', models.CharField(blank=True, max_length=200, null=True)),
                ('bottom', models.CharField(blank=True, max_length=200, null=True)),
                ('sides', models.CharField(blank=True, max_length=200, null=True)),
                ('neck', models.CharField(blank=True, max_length=200, null=True)),
                ('fretboard', models.CharField(blank=True, max_length=200, null=True)),
                ('sadle', models.CharField(blank=True, max_length=200, null=True)),
                ('tuningMachines', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Luthier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('country', models.CharField(blank=True, max_length=200, null=True)),
                ('birth', models.IntegerField(blank=True, null=True)),
                ('death', models.IntegerField(blank=True, null=True)),
                ('pic', models.URLField(blank=True, max_length=500, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Recording',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('year', models.IntegerField(blank=True, null=True)),
                ('composer', models.CharField(max_length=200)),
                ('arrangement', models.CharField(blank=True, max_length=200, null=True)),
                ('audio', models.URLField(max_length=500)),
                ('artist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='brGuitars.artist')),
                ('guitar', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='brGuitars.guitar')),
            ],
        ),
        migrations.CreateModel(
            name='GuitarPic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.URLField(max_length=500)),
                ('guitar', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='brGuitars.guitar')),
            ],
        ),
        migrations.AddField(
            model_name='guitar',
            name='luthier',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='brGuitars.luthier'),
        ),
    ]
