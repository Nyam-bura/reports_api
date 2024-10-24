# Generated by Django 5.0.4 on 2024-10-24 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0002_interoperability_data_psp_agents_info_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReportsConfiguration',
            fields=[
                ('report_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('computational_frequency', models.CharField(choices=[('HH00', '00:00'), ('HH01', '01:00'), ('HH02', '02:00'), ('HH03', '03:00'), ('HH04', '04:00'), ('HH05', '05:00'), ('HH06', '06:00'), ('HH07', '07:00'), ('HH08', '08:00'), ('HH09', '09:00'), ('HH10', '10:00'), ('HH11', '11:00'), ('HH12', '12:00'), ('HH13', '13:00'), ('HH14', '14:00'), ('HH15', '15:00'), ('HH16', '16:00'), ('HH17', '17:00'), ('HH18', '18:00'), ('HH19', '19:00'), ('HH20', '20:00'), ('HH21', '21:00'), ('HH22', '22:00'), ('HH23', '23:00'), ('once_daily', '12:19'), ('once_monthly', '14:00 on the 1st day of the month')], max_length=50)),
                ('submission_frequency', models.CharField(choices=[('once_daily', '12:19'), ('once_monthly', '00:00 on the 1st day of the month'), ('annually', '00:00 on January 1st')], max_length=50)),
                ('report', models.CharField(max_length=65)),
            ],
        ),
    ]
