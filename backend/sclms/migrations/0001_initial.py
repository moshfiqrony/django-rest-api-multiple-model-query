# Generated by Django 2.1.7 on 2019-02-19 16:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Campaign',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='CampaignDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('agentId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sclms.Agent')),
                ('campaignId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sclms.Campaign')),
            ],
        ),
        migrations.CreateModel(
            name='CL',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='campaigndetails',
            name='clId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sclms.CL'),
        ),
    ]
