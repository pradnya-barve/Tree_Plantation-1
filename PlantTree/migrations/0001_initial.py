# Generated by Django 4.0 on 2022-09-20 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PlantaTree',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('username', models.CharField(max_length=50)),
                ('tree_name', models.CharField(choices=[('N', 'Neem'), ('K', 'Karanja'), ('M', 'Mango'), ('J', 'Jamun'), ('B', 'Banyan'), ('A', 'Amrood'), ('BB', 'Bamboo'), ('BE', 'Ber'), ('NI', 'Banyan')], max_length=100)),
                ('tree_planted_date', models.DateTimeField(auto_now_add=True)),
                ('tree_pictures', models.ImageField(upload_to='images/treePlantedImages/')),
                ('tree_description', models.TextField(default=models.CharField(choices=[('N', 'Neem'), ('K', 'Karanja'), ('M', 'Mango'), ('J', 'Jamun'), ('B', 'Banyan'), ('A', 'Amrood'), ('BB', 'Bamboo'), ('BE', 'Ber'), ('NI', 'Banyan')], max_length=100))),
                ('points', models.PositiveIntegerField(default=0, verbose_name='points')),
            ],
        ),
    ]
