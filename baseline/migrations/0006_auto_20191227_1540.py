# Generated by Django 2.2 on 2019-12-27 15:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('baseline', '0005_auto_20191227_1540'),
    ]

    operations = [
        migrations.RenameField(
            model_name='linuxscanres',
            old_name='iptabledOutputPolicyIfDrop',
            new_name='iptablesOutputPolicyIfDrop',
        ),
    ]