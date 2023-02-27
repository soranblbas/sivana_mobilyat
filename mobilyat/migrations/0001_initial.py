# Generated by Django 4.1.7 on 2023-02-27 12:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Customer",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("customer_name", models.CharField(blank=True, max_length=50)),
                ("customer_mobile", models.CharField(blank=True, max_length=50)),
                ("customer_address", models.TextField(blank=True)),
                ("city", models.CharField(blank=True, max_length=50)),
            ],
            options={
                "verbose_name_plural": "2. Customers",
            },
        ),
        migrations.CreateModel(
            name="ItemDetail",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=50)),
                ("detail", models.TextField(blank=True)),
            ],
            options={
                "verbose_name_plural": "7. Items Detail",
            },
        ),
        migrations.CreateModel(
            name="ItemPrice",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("item_price", models.FloatField()),
                (
                    "item",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="mobilyat.itemdetail",
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "6. Item Price",
            },
        ),
        migrations.CreateModel(
            name="Price_List",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("price_list", models.CharField(blank=True, max_length=50)),
            ],
            options={
                "verbose_name_plural": "Price_List",
            },
        ),
        migrations.CreateModel(
            name="Purchase",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("invoice_number", models.SlugField(default=0)),
                ("date", models.DateTimeField()),
            ],
            options={
                "verbose_name_plural": "8. Purchase Invoice",
            },
        ),
        migrations.CreateModel(
            name="SaleInvoice",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("invoice_number", models.SlugField(editable=False)),
                ("piad", models.BooleanField(default="No")),
                ("date", models.DateTimeField()),
                (
                    "customer_name",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="mobilyat.customer",
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "3. Sale Invoice",
            },
        ),
        migrations.CreateModel(
            name="Unit",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=50)),
                ("short_name", models.CharField(max_length=50)),
            ],
            options={
                "verbose_name_plural": "5. Units",
            },
        ),
        migrations.CreateModel(
            name="Vendor",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("full_name", models.CharField(max_length=50)),
                ("address", models.TextField(blank=True)),
                ("mobile", models.CharField(blank=True, max_length=15)),
                ("status", models.BooleanField(blank=True, default=False)),
                ("note", models.TextField(blank=True)),
            ],
            options={
                "verbose_name_plural": "1. Vendors",
            },
        ),
        migrations.CreateModel(
            name="SaleItem",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("qty", models.PositiveSmallIntegerField(default=1)),
                ("total_amt", models.FloatField(default=0, editable=False)),
                ("sale_date", models.DateTimeField(auto_now_add=True)),
                (
                    "item",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="mobilyat.itemdetail",
                    ),
                ),
                (
                    "item_price",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="mobilyat.itemprice",
                    ),
                ),
                (
                    "sales_invoice",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="mobilyat.saleinvoice",
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "9. Sales Item",
            },
        ),
        migrations.CreateModel(
            name="PurchaseItem",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("qty", models.FloatField()),
                ("total_amt", models.FloatField(default=0, editable=False)),
                ("pur_date", models.DateTimeField(auto_now_add=True)),
                ("note", models.TextField(blank=True)),
                (
                    "item",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="mobilyat.itemdetail",
                    ),
                ),
                (
                    "item_price",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="mobilyat.itemprice",
                    ),
                ),
                (
                    "purchase_invoice",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="mobilyat.purchase",
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "9. Purchased Item",
            },
        ),
        migrations.AddField(
            model_name="purchase",
            name="vendor",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="mobilyat.vendor"
            ),
        ),
        migrations.CreateModel(
            name="Payment_Entry",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("invoice_number", models.SlugField(editable=False)),
                ("paid_amount", models.FloatField(blank=True)),
                ("payment_date", models.DateTimeField(blank=True)),
                ("note", models.TextField(blank=True)),
                (
                    "customer_name",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="mobilyat.customer",
                    ),
                ),
                (
                    "sales_invoice",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="mobilyat.saleinvoice",
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "8. Payment Entry",
            },
        ),
        migrations.AddField(
            model_name="itemprice",
            name="price_list",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="mobilyat.price_list"
            ),
        ),
        migrations.AddField(
            model_name="itemdetail",
            name="unit",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="mobilyat.unit"
            ),
        ),
        migrations.CreateModel(
            name="Inventory",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("pur_qty", models.FloatField(default=0, null=True)),
                ("sale_qty", models.FloatField(default=0, null=True)),
                ("total_bal_qty", models.FloatField(default=0)),
                (
                    "item",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="mobilyat.itemdetail",
                    ),
                ),
                (
                    "purchase",
                    models.ForeignKey(
                        default=0,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="mobilyat.purchase",
                    ),
                ),
                (
                    "sale",
                    models.ForeignKey(
                        default=0,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="mobilyat.saleinvoice",
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "10. Stock Details",
            },
        ),
    ]
