# Generated by Django 4.0 on 2022-01-04 04:57

import courses.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_video_text_images_file_content'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='content',
            options={'ordering': ['order']},
        ),
        migrations.AlterModelOptions(
            name='module',
            options={'ordering': ['order']},
        ),
        migrations.AddField(
            model_name='content',
            name='order',
            field=courses.fields.OrderField(default=0, verbose_name='verbose_name'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='module',
            name='order',
            field=courses.fields.OrderField(default=0, verbose_name='verbose_name'),
            preserve_default=False,
        ),
    ]
