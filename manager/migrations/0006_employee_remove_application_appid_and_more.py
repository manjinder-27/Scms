# Generated by Django 4.2.2 on 2023-06-27 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0005_remove_application_isapproved'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.CharField(max_length=30, null=True)),
                ('name', models.CharField(max_length=30, null=True)),
                ('father', models.CharField(max_length=30, null=True)),
                ('phone', models.CharField(max_length=30, null=True)),
                ('aadhar', models.CharField(max_length=13, null=True)),
                ('job', models.CharField(max_length=30, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='application',
            name='appId',
        ),
        migrations.RemoveField(
            model_name='application',
            name='fatherName',
        ),
        migrations.RemoveField(
            model_name='application',
            name='firstName',
        ),
        migrations.RemoveField(
            model_name='application',
            name='lastName',
        ),
        migrations.RemoveField(
            model_name='application',
            name='phoneNumber',
        ),
        migrations.RemoveField(
            model_name='application',
            name='studentClass',
        ),
        migrations.RemoveField(
            model_name='student',
            name='admNum',
        ),
        migrations.RemoveField(
            model_name='student',
            name='fatherName',
        ),
        migrations.RemoveField(
            model_name='student',
            name='firstName',
        ),
        migrations.RemoveField(
            model_name='student',
            name='lastName',
        ),
        migrations.RemoveField(
            model_name='student',
            name='phoneNumber',
        ),
        migrations.RemoveField(
            model_name='student',
            name='studentClass',
        ),
        migrations.AddField(
            model_name='application',
            name='aadhar',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='application',
            name='appliedAs',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='application',
            name='appliedFor',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='application',
            name='father',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='application',
            name='name',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='application',
            name='phone',
            field=models.CharField(max_length=13, null=True),
        ),
        migrations.AddField(
            model_name='application',
            name='uid',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='aadhar',
            field=models.CharField(max_length=13, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='adm',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='cls',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='father',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='name',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='phone',
            field=models.CharField(max_length=30, null=True),
        ),
    ]