from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('trk', '0002_alter_document_id_alter_fuelentry_id_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id',             models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('display_name',   models.CharField(blank=True, default='', max_length=100)),
                ('bio',            models.TextField(blank=True, default='', max_length=300)),
                ('dob',            models.DateField(blank=True, null=True)),
                ('avatar',         models.ImageField(blank=True, null=True, upload_to='avatars/')),
                ('unit_distance',  models.CharField(choices=[('km', 'Kilometres (km)'), ('mi', 'Miles (mi)')], default='km', max_length=5)),
                ('unit_volume',    models.CharField(choices=[('L', 'Litres (L)'), ('gal', 'Gallons (gal)')], default='L', max_length=5)),
                ('theme_preference', models.CharField(choices=[('dark', 'Dark'), ('light', 'Light'), ('auto', 'Auto (system)')], default='dark', max_length=10)),
                ('notify_service', models.BooleanField(default=True)),
                ('notify_docs',    models.BooleanField(default=True)),
                ('notify_fuel',    models.BooleanField(default=False)),
                ('updated_at',     models.DateTimeField(auto_now=True)),
                ('user',           models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
            options={'verbose_name': 'User Profile'},
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id',           models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category',     models.CharField(choices=[('bug', 'Bug Report'), ('feature', 'Feature Request'), ('ui', 'UI / Design'), ('general', 'General Feedback')], default='general', max_length=50)),
                ('message',      models.TextField(max_length=2000)),
                ('submitted_at', models.DateTimeField(auto_now_add=True)),
                ('user_agent',   models.CharField(blank=True, default='', max_length=300)),
                ('user',         models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={'verbose_name': 'Feedback', 'verbose_name_plural': 'Feedback Submissions', 'ordering': ['-submitted_at']},
        ),
    ]
