# Generated by Django 3.0.8 on 2020-07-22 03:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_drop_product_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('design', models.CharField(max_length=50)),
                ('amount', models.PositiveIntegerField()),
                ('status', models.CharField(choices=[('decline', 'Decline'), ('approved', 'Approved'), ('processing', 'Processing'), ('complete', 'Complete'), ('bulk', 'Bulk')], max_length=10)),
                ('created_date', models.DateField(auto_now_add=True)),
                ('buyer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='store.Buyer')),
                ('drop', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='store.Drop')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.Product')),
                ('type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='store.Type')),
                ('supplier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.Supplier')),
            ],
        ),
        migrations.CreateModel(
            name='Delivery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('courier_name', models.CharField(max_length=120)),
                ('created_date', models.DateField(auto_now_add=True)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.Order')),
            ],
        ),
    ]