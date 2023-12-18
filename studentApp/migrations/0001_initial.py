# Generated by Django 4.2.5 on 2023-09-28 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('student_id', models.PositiveIntegerField()),
                ('email', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=15)),
                ('roll', models.PositiveIntegerField()),
                ('academicYear', models.DateField()),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Others', 'Others')], default='Male', max_length=50)),
                ('religion', models.CharField(choices=[('Islam', 'Islam'), ('Hindu', 'Hindu'), ('Buddha', 'Buddha'), ('Others', 'Others')], default='Islam', max_length=50)),
                ('blood', models.CharField(choices=[('B+', 'B+'), ('B-', 'B-'), ('A+', 'A+'), ('AB+', 'AB+'), ('AB-', 'AB-'), ('O-', 'O-'), ('O+', 'O+')], max_length=50)),
                ('gpa', models.FloatField()),
                ('age', models.PositiveIntegerField()),
                ('semester', models.CharField(choices=[('1st', '1st'), ('2nd', '2nd'), ('3rd', '3rd'), ('5th', '5th'), ('6th', '6th'), ('7th', '7th'), ('8th', '8th')], max_length=50)),
                ('section', models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')], max_length=50)),
                ('shift', models.CharField(choices=[('1st_Shift', '1st_Shift'), ('2nd_Shift', '2nd_Shift')], max_length=50)),
                ('image', models.ImageField(upload_to='prof_pc/')),
            ],
        ),
    ]