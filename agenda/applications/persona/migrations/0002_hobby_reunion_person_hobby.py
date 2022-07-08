# Generated by Django 4.0.6 on 2022-07-07 04:58

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('persona', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hobby',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('hobby', models.CharField(max_length=50, verbose_name='Pasatiempo')),
            ],
            options={
                'verbose_name': 'Hobby',
                'verbose_name_plural': 'Hobbies',
            },
        ),
        migrations.CreateModel(
            name='Reunion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('fecha', models.DateField()),
                ('hora', models.TimeField()),
                ('asunto', models.CharField(max_length=100, verbose_name='Asunto de reunion')),
                ('persona', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='persona.person')),
            ],
            options={
                'verbose_name': 'Reunion',
                'verbose_name_plural': 'Reunion',
            },
        ),
        migrations.AddField(
            model_name='person',
            name='hobby',
            field=models.ManyToManyField(to='persona.hobby'),
        ),
    ]
