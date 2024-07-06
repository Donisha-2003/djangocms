# Generated by Django 3.1.1 on 2024-06-30 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0012_stu'),
    ]

    operations = [
        migrations.CreateModel(
            name='Walkin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('walkin_date', models.DateField()),
                ('sales_person', models.CharField(max_length=20)),
                ('stu_name', models.CharField(max_length=20)),
                ('mobile', models.IntegerField(max_length=10)),
                ('parent_number', models.IntegerField(max_length=10)),
                ('course_recom', models.CharField(max_length=20)),
                ('join_date', models.DateField()),
            ],
        ),
        migrations.AlterField(
            model_name='customuser',
            name='user_type',
            field=models.CharField(choices=[(1, 'HOD'), (2, 'Staff'), (3, 'Cro'), (4, 'Stu')], default=1, max_length=1),
        ),
    ]
