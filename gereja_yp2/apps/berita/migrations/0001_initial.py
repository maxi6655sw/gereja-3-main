from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='Kategori',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=100, unique=True)),
                ('slug', models.SlugField(blank=True, unique=True)),
            ],
            options={
                'verbose_name': 'Kategori',
                'verbose_name_plural': 'Kategori',
                'ordering': ['nama'],
            },
        ),
        migrations.CreateModel(
            name='Berita',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('judul', models.CharField(max_length=200)),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('gambar', models.ImageField(blank=True, null=True, upload_to='berita/')),
                ('isi', models.TextField()),
                ('ringkasan', models.TextField(blank=True, null=True)),
                ('tanggal', models.DateField(default=django.utils.timezone.now)),
                ('penulis', models.CharField(default='Admin', max_length=100)),
                ('kategori', models.ForeignKey(
                    null=True,
                    on_delete=django.db.models.deletion.SET_NULL,
                    related_name='berita',
                    to='berita.kategori',
                )),
            ],
            options={
                'verbose_name': 'Berita',
                'verbose_name_plural': 'Berita',
                'ordering': ['-tanggal'],
            },
        ),
    ]
