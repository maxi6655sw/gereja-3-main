from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='JadwalMisa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_misa', models.CharField(max_length=100)),
                ('hari', models.DateField()),
                ('waktu', models.TimeField()),
                ('gambar', models.ImageField(blank=True, null=True, upload_to='jadwal/')),
            ],
            options={
                'verbose_name': 'Jadwal Misa',
                'verbose_name_plural': 'Jadwal Misa',
                'ordering': ['hari', 'waktu'],
            },
        ),
    ]
