# Generated by Django 2.1.4 on 2019-07-19 20:18

from django.db import migrations, models
import plugins.fields


class Migration(migrations.Migration):

    dependencies = [
        ('pipelineinstances', '0002_pipelineinstance_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='pipelineinstance',
            name='cpu_limit',
            field=plugins.fields.CPUField(null=True),
        ),
        migrations.AddField(
            model_name='pipelineinstance',
            name='gpu_limit',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='pipelineinstance',
            name='memory_limit',
            field=plugins.fields.MemoryField(null=True),
        ),
        migrations.AddField(
            model_name='pipelineinstance',
            name='number_of_workers',
            field=models.IntegerField(null=True),
        ),
    ]
