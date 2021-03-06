# Generated by Django 2.1.7 on 2019-05-02 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0004_auto_20190405_2153'),
    ]

    operations = [
        migrations.CreateModel(
            name='SolutionRating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.DecimalField(decimal_places=2, max_digits=5)),
                ('created', models.DateField(auto_now_add=True)),
                ('updated', models.DateField(auto_now=True)),
                ('solution', models.ForeignKey(blank=True, default=None, null=True, on_delete=None, to='manager.Solution')),
            ],
            options={
                'verbose_name': 'Оценка',
                'verbose_name_plural': 'Оценки',
            },
        ),
    ]
