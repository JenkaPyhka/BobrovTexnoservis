# Generated by Django 4.0.3 on 2022-06-25 16:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_rename_checkbox_message_checkbox'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='CheckBox',
            new_name='Checkbox',
        ),
    ]
