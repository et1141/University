# Generated by Django 3.2.3 on 2022-11-09 16:43

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
            name='Driver',
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
            name='Moto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=200)),
                ('brand', models.CharField(max_length=200)),
                ('size', models.IntegerField(blank=True, null=True)),
                ('cc', models.IntegerField(blank=True, null=True)),
                ('hp', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('country', models.CharField(blank=True, max_length=200, null=True)),
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
                ('artist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='brMotogp.artist')),
                ('guitar', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='brMotogp.guitar')),
            ],
        ),
        migrations.CreateModel(
            name='MotoPic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.URLField(max_length=500)),
                ('moto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='brMotogp.moto')),
            ],
        ),
        migrations.AddField(
            model_name='moto',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='brMotogp.team'),
        ),
        migrations.CreateModel(
            name='GuitarPic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.URLField(max_length=500)),
                ('guitar', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='brMotogp.guitar')),
            ],
        ),
        migrations.AddField(
            model_name='guitar',
            name='luthier',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='brMotogp.luthier'),
        ),
        migrations.CreateModel(
            name='Drives',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateSTART', models.IntegerField(blank=True, null=True)),
                ('dateEND', models.IntegerField(blank=True, null=True)),
                ('driver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='brMotogp.driver')),
                ('moto', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='brMotogp.moto')),
            ],
        ),
    ]
