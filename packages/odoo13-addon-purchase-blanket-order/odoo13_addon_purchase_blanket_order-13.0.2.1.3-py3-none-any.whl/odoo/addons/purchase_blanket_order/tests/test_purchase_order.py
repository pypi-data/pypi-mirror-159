# Copyright (C) 2018 ForgeFlow S.L. (https://www.forgeflow.com)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
from datetime import date, timedelta

from odoo import fields
from odoo.tests import common


class TestPurchaseOrder(common.TransactionCase):
    def setUp(self):
        super().setUp()
        self.blanket_order_obj = self.env["purchase.blanket.order"]
        self.blanket_order_line_obj = self.env["purchase.blanket.order.line"]
        self.purchase_order_obj = self.env["purchase.order"]
        self.purchase_order_line_obj = self.env["purchase.order.line"]

        self.partner = self.env["res.partner"].create(
            {"name": "TEST SUPPLIER", "supplier_rank": 1}
        )
        self.payment_term = self.env.ref("account.account_payment_term_30days")

        # Seller IDS
        seller = self.env["product.supplierinfo"].create(
            {"name": self.partner.id, "price": 30.0}
        )

        self.product = self.env["product.product"].create(
            {
                "name": "Demo",
                "categ_id": self.env.ref("product.product_category_1").id,
                "standard_price": 35.0,
                "seller_ids": [(6, 0, [seller.id])],
                "type": "consu",
                "uom_id": self.env.ref("uom.product_uom_unit").id,
                "default_code": "PROD_DEL01",
            }
        )
        self.product_2 = self.env["product.product"].create(
            {
                "name": "Demo 2",
                "categ_id": self.env.ref("product.product_category_1").id,
                "standard_price": 35.0,
                "seller_ids": [(6, 0, [seller.id])],
                "type": "consu",
                "uom_id": self.env.ref("uom.product_uom_unit").id,
                "default_code": "PROD_DEL02",
            }
        )
        self.validity = date.today() + timedelta(days=365)
        self.date_schedule_1 = date.today() + timedelta(days=10)
        self.date_schedule_2 = date.today() + timedelta(days=20)

    def create_blanket_order_01(self):
        blanket_order = self.blanket_order_obj.create(
            {
                "partner_id": self.partner.id,
                "validity_date": fields.Date.to_string(self.validity),
                "payment_term_id": self.payment_term.id,
                "line_ids": [
                    (
                        0,
                        0,
                        {
                            "product_id": self.product.id,
                            "product_uom": self.product.uom_id.id,
                            "date_schedule": fields.Date.to_string(
                                self.date_schedule_1
                            ),
                            "original_uom_qty": 20.0,
                            "price_unit": 30.0,
                        },
                    ),
                    (
                        0,
                        0,
                        {
                            "product_id": self.product.id,
                            "product_uom": self.product.uom_id.id,
                            "date_schedule": fields.Date.to_string(
                                self.date_schedule_2
                            ),
                            "original_uom_qty": 20.0,
                            "price_unit": 30.0,
                        },
                    ),
                ],
            }
        )
        blanket_order.sudo().onchange_partner_id()
        return blanket_order

    def create_blanket_order_02(self):
        blanket_order = self.blanket_order_obj.create(
            {
                "partner_id": self.partner.id,
                "validity_date": fields.Date.to_string(self.validity),
                "payment_term_id": self.payment_term.id,
                "line_ids": [
                    (
                        0,
                        0,
                        {
                            "product_id": self.product.id,
                            "product_uom": self.product.uom_id.id,
                            "original_uom_qty": 20.0,
                            "price_unit": 30.0,
                        },
                    ),
                    (
                        0,
                        0,
                        {
                            "product_id": self.product_2.id,
                            "product_uom": self.product.uom_id.id,
                            "original_uom_qty": 20.0,
                            "price_unit": 30.0,
                        },
                    ),
                ],
            }
        )
        blanket_order.sudo().onchange_partner_id()
        return blanket_order

    def test_01_create_purchase_order(self):
        blanket_order = self.create_blanket_order_01()
        blanket_order.sudo().action_confirm()
        bo_lines = self.blanket_order_line_obj.search(
            [("order_id", "=", blanket_order.id)]
        )
        self.assertEqual(len(bo_lines), 2)

        po = self.purchase_order_obj.create(
            {
                "partner_id": self.partner.id,
                "order_line": [
                    (
                        0,
                        0,
                        {
                            "name": self.product.name,
                            "product_id": self.product.id,
                            "product_qty": 5.0,
                            "product_uom": self.product.uom_po_id.id,
                            "date_planned": date.today(),
                            "price_unit": 10.0,
                        },
                    )
                ],
            }
        )
        po_line = po.order_line[0]
        po_line.with_context(from_purchase_order=True).name_get()
        po_line.onchange_product_id()
        self.assertEqual(po_line._get_eligible_bo_lines(), bo_lines)
        bo_line_assigned = self.blanket_order_line_obj.search(
            [("date_schedule", "=", fields.Date.to_string(self.date_schedule_1))]
        )
        self.assertEqual(po_line.blanket_order_line, bo_line_assigned)

    def test_02_create_purchase_order(self):
        blanket_order = self.create_blanket_order_02()
        blanket_order.sudo().action_confirm()
        bo_lines = self.blanket_order_line_obj.search(
            [("order_id", "=", blanket_order.id)]
        )
        self.assertEqual(len(bo_lines), 2)

        po = self.purchase_order_obj.create(
            {
                "partner_id": self.partner.id,
                "order_line": [
                    (
                        0,
                        0,
                        {
                            "name": self.product.name,
                            "product_id": self.product.id,
                            "product_qty": 5.0,
                            "product_uom": self.product.uom_po_id.id,
                            "date_planned": date.today(),
                            "price_unit": 10.0,
                        },
                    )
                ],
            }
        )
        po_line = po.order_line[0]
        po_line.with_context(from_purchase_order=True).name_get()
        po_line.onchange_product_id()
        self.assertEqual(
            po_line._get_eligible_bo_lines(),
            bo_lines.filtered(lambda l: l.product_id == self.product),
        )
        bo_line_assigned = self.blanket_order_line_obj.search(
            [
                ("order_id", "=", blanket_order.id),
                ("product_id", "=", self.product.id),
                ("date_schedule", "=", False),
            ]
        )
        self.assertEqual(po_line.blanket_order_line, bo_line_assigned)
