# Generated by Django 3.1.7 on 2021-03-26 12:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('abc_garments', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Materials',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('status', models.BooleanField(default=True)),
            ],
        ),
        migrations.AddField(
            model_name='employee',
            name='supervisor',
            field=models.IntegerField(default=0),
        ),
        migrations.CreateModel(
            name='PartTimeWork',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('worked_hour', models.IntegerField()),
                ('worked_date', models.DateField()),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='abc_garments.employee')),
            ],
        ),
        migrations.CreateModel(
            name='MaterialsUsed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('employee_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='abc_garments.employee')),
                ('materials_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='abc_garments.materials')),
            ],
        ),
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('delivery_date', models.DateField()),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='abc_garments.employee')),
            ],
        ),
    ]
