# Generated by Django 2.2.13 on 2021-02-16 22:46

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('email', models.EmailField(error_messages={'unique': 'El email que ingreso ya existe'}, max_length=254, unique=True, verbose_name='email addres')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Asignacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(blank=True, max_length=250, null=True)),
                ('portada', models.ImageField(blank=True, null=True, upload_to='Portada')),
                ('activo', models.BooleanField(default=True)),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('modificado', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Ciclo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('anio', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1990)])),
                ('activo', models.BooleanField(default=True)),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('modificado', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.CharField(blank=True, max_length=250, null=True)),
                ('activo', models.BooleanField(default=True)),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('modificado', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Estudiante',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('telefono_contacto', models.CharField(blank=True, max_length=15, null=True)),
                ('direccion_contacto', models.CharField(blank=True, max_length=250, null=True)),
                ('activo', models.BooleanField(default=True)),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('modificado', models.DateTimeField(auto_now=True)),
                ('asignacion_estudiante', models.ManyToManyField(related_name='estudiante_asignaciones', to='api.Asignacion')),
            ],
        ),
        migrations.CreateModel(
            name='Nivel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.CharField(blank=True, max_length=250, null=True)),
                ('activo', models.BooleanField(default=True)),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('modificado', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Profesion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.CharField(blank=True, max_length=250, null=True)),
                ('activo', models.BooleanField(default=True)),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('modificado', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Rol',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.CharField(blank=True, max_length=250, null=True)),
                ('activo', models.BooleanField(default=True)),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('modificado', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Seccion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('activo', models.BooleanField(default=True)),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('modificado', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tarea',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('descripcion', models.CharField(blank=True, max_length=250, null=True)),
                ('fecha_entrega', models.DateField()),
                ('hora_entrega', models.TimeField()),
                ('nota', models.FloatField(default=0)),
                ('archivo', models.FileField(upload_to='tarea_maestros')),
                ('permitir_archivo', models.BooleanField(default=True)),
                ('activo', models.BooleanField(default=True)),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('modificado', models.DateTimeField(auto_now=True)),
                ('asignacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='asignaciones', to='api.Asignacion')),
            ],
        ),
        migrations.CreateModel(
            name='Tarea_Estudinate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto', models.CharField(blank=True, max_length=250, null=True)),
                ('archivo', models.FileField(blank=True, null=True, upload_to='tarea_alumnos')),
                ('punteo', models.FloatField(default=0)),
                ('fecha_entregado', models.DateTimeField(auto_now=True)),
                ('activo', models.BooleanField(default=True)),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('modificado', models.DateTimeField(auto_now=True)),
                ('estudiante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='estudiantes', to='api.Estudiante')),
                ('tarea', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tareas', to='api.Tarea')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(blank=True, max_length=15, null=True)),
                ('address', models.CharField(blank=True, max_length=250, null=True)),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='Avatar')),
                ('is_first_login', models.BooleanField(default=True, help_text='Verifica si es la primera vez que se logueo en la aplicaion', verbose_name='first_login')),
                ('activo', models.BooleanField(default=True)),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('modificado', models.DateTimeField(auto_now=True)),
                ('rol', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='roles', to='api.Rol')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profiles', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('descripcion', models.CharField(blank=True, max_length=250, null=True)),
                ('archivo', models.FileField(upload_to='material_apoyo')),
                ('activo', models.BooleanField(default=True)),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('modificado', models.DateTimeField(auto_now=True)),
                ('asignacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='material_asignaciones', to='api.Asignacion')),
            ],
        ),
        migrations.CreateModel(
            name='Maestro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activo', models.BooleanField(default=True)),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('modificado', models.DateTimeField(auto_now=True)),
                ('maestro_profile', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='maestros_profiles', to='api.Profile')),
                ('profesion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='profesiones', to='api.Profesion')),
            ],
        ),
        migrations.CreateModel(
            name='Grado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.CharField(blank=True, max_length=250, null=True)),
                ('activo', models.BooleanField(default=True)),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('modificado', models.DateTimeField(auto_now=True)),
                ('nivel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='niveles', to='api.Nivel')),
            ],
        ),
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('descripcion', models.CharField(blank=True, max_length=250, null=True)),
                ('fecha', models.DateField()),
                ('hora', models.TimeField()),
                ('activo', models.BooleanField(default=True)),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('modificado', models.DateTimeField(auto_now=True)),
                ('ciclo_escolar', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ciclos', to='api.Ciclo')),
            ],
        ),
        migrations.AddField(
            model_name='estudiante',
            name='estudiante_profile',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profiles', to='api.Profile'),
        ),
        migrations.AddField(
            model_name='asignacion',
            name='asignacion_ciclo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='asignacion_ciclos', to='api.Ciclo'),
        ),
        migrations.AddField(
            model_name='asignacion',
            name='curso',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='asignacion_cursos', to='api.Curso'),
        ),
        migrations.AddField(
            model_name='asignacion',
            name='grado',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='asignacion_grados', to='api.Grado'),
        ),
        migrations.AddField(
            model_name='asignacion',
            name='maestro',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='asignacion_maestros', to='api.Maestro'),
        ),
        migrations.AddField(
            model_name='asignacion',
            name='seccion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='asignacion_secciones', to='api.Seccion'),
        ),
    ]
