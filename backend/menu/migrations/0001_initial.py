# Generated by Django 4.2.3 on 2024-04-20 17:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('url', models.CharField(max_length=200)),
                ('named_url', models.CharField(blank=True, max_length=100, null=True)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='menu.menuitem')),
            ],
            options={
                'verbose_name': 'Название',
                'verbose_name_plural': 'Названия',
                'ordering': ['-title'],
            },
        ),
    ]