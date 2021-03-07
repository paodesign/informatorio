<<<<<<< HEAD
# Generated by Django 3.0.10 on 2021-03-05 18:33
=======
# Generated by Django 3.0.10 on 2021-03-06 18:50
>>>>>>> ultima_version_categorias

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(

            name='Categoria',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('categoria_nombre', models.CharField(max_length=100, unique=True)),

            name='Post',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=100)),
                ('contenido', models.TextField()),
                ('fecha_publicacion', models.DateTimeField(auto_now_add=True)),
                ('categoria', models.CharField(max_length=100)),
                ('imagen', models.ImageField(blank=True, upload_to='post')),

            ],
        
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),

                ('contenido', models.TextField()),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Post')),
            ],
        ),
    ]
