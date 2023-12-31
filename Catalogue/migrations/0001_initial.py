# Generated by Django 4.2.3 on 2023-08-06 19:07

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.functions.text


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('articleName', models.CharField(max_length=200, verbose_name='Article Name')),
                ('keywords', models.TextField(max_length=2000, verbose_name='Keywords')),
                ('notes', models.TextField(blank=True, max_length=2000, verbose_name='Notes')),
                ('summary', models.CharField(blank=True, max_length=500, verbose_name='Summary')),
            ],
        ),
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('authorName', models.CharField(max_length=200, verbose_name="Author's Name")),
                ('notes', models.CharField(blank=True, max_length=200, verbose_name='Notes')),
            ],
        ),
        migrations.CreateModel(
            name='Edition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('editionName', models.CharField(max_length=200, verbose_name='Name of Edition')),
                ('publicationDate', models.DateField(blank=True, verbose_name='Publication Date')),
            ],
        ),
        migrations.CreateModel(
            name='Publication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('publicationName', models.CharField(max_length=200, verbose_name="Publication's Name")),
                ('publicationNotes', models.CharField(blank=True, max_length=200, verbose_name='Notes')),
                ('publicationType', models.CharField(choices=[('NEWSPAPER', 'Newspaper'), ('MAGAZINE', 'Magazine')], max_length=200, verbose_name='Publication Type')),
            ],
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('publisherName', models.CharField(max_length=200, verbose_name="Publisher's Name")),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tagName', models.CharField(max_length=20, verbose_name='Tag')),
                ('tagDescriptor', models.CharField(blank=True, max_length=200, verbose_name='Description')),
            ],
        ),
        migrations.AddConstraint(
            model_name='tag',
            constraint=models.UniqueConstraint(django.db.models.functions.text.Lower('tagName'), name='tagNameUnique'),
        ),
        migrations.AddField(
            model_name='publication',
            name='publisher',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='Catalogue.publisher'),
        ),
        migrations.AddField(
            model_name='edition',
            name='publication',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='Catalogue.publication'),
        ),
        migrations.AddField(
            model_name='author',
            name='tag',
            field=models.ManyToManyField(blank=True, to='Catalogue.tag'),
        ),
        migrations.AddField(
            model_name='article',
            name='author',
            field=models.ManyToManyField(blank=True, to='Catalogue.author'),
        ),
        migrations.AddField(
            model_name='article',
            name='edition',
            field=models.ManyToManyField(blank=True, to='Catalogue.edition'),
        ),
        migrations.AddField(
            model_name='article',
            name='tag',
            field=models.ManyToManyField(blank=True, to='Catalogue.tag'),
        ),
    ]
