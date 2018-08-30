# -*- coding: utf-8 -*-

from odoo import models, api


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    def _get_tax_group_name(self, tax):
        tax_id = self.env['account.tax'].browse(tax)
        if tax_id.tax_group_id:
            return tax_id.tax_group_id.name
        else:
            return ""

    @api.multi
    def get_itbis_amount(self, sale_id, price_unit, discount):
        self.ensure_one()
        currency = sale_id and sale_id.pricelist_id.currency_id or None
        price = price_unit * (1 - (discount or 0.0) / 100.0)
        taxes = self.tax_id.compute_all(
            price, currency, self.product_uom_qty, product=self.product_id,
            partner=sale_id.partner_id)
        itbis_amount = 0
        tax_lst = taxes['taxes']
        if tax_lst:
            itbis_amount = sum([tax['amount'] for tax in tax_lst
                                if str(self._get_tax_group_name(tax['id'])).startswith('ITBIS')
                                and tax['amount'] > 0])
        return itbis_amount
