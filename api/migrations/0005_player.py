# Generated by Django 2.2.3 on 2019-07-31 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20190731_0505'),
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('current_room', models.IntegerField(default=0)),
                ('cooldown', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('status', models.BooleanField(default=False)),
                ('encumbrance', models.IntegerField(default=0)),
                ('speed', models.IntegerField(default=0)),
                ('gold', models.IntegerField(default=0)),
            ],
        ),
    ]