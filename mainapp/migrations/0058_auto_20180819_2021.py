# Generated by Django 2.1 on 2018-08-19 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0057_add_status_to_relief_camp'),
    ]

    operations = [
        migrations.CreateModel(
            name='DataCollection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('document_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Document name')),
                ('document', models.FileField(blank=True, upload_to='camp_data')),
                ('tag', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'verbose_name': 'Data: Collection',
                'verbose_name_plural': 'Data: Collections',
            },
        ),
        migrations.DeleteModel(
            name='ReliefCampData',
        ),
    ]