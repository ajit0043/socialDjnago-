# Generated by Django 3.2.10 on 2022-01-02 19:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accountss', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='friendmodel',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='current', to='accountss.usermodel'),
            preserve_default=False,
        ),
    ]
