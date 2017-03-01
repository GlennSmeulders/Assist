# -*- coding: utf-8 -*-

from openerp import models, api


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    @api.multi
    def print_quotation(self):
        self.filtered(lambda s: s.state == 'draft').write({'state': 'sent'})
        if self.state == 'sale':
            return self.env['report'].get_action(self, 'xx_sale.report_saleorder')
        return self.env['report'].get_action(self, 'xx_sale.report_quotation')


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    @api.depends('product_uom_qty', 'discount', 'price_unit', 'tax_id', 'qty_delivered')
    def _compute_amount(self):
        if self.state == 'sale':
            for line in self:
                price = line.price_unit * (1 - (line.discount or 0.0) / 100.0)
                taxes = line.tax_id.compute_all(price, line.order_id.currency_id, line.qty_delivered,
                                                product=line.product_id, partner=line.order_id.partner_id)
                line.update({
                    'price_tax': taxes['total_included'] - taxes['total_excluded'],
                    'price_total': taxes['total_included'],
                    'price_subtotal': taxes['total_excluded'],
                })
        else:
            for line in self:
                price = line.price_unit * (1 - (line.discount or 0.0) / 100.0)
                taxes = line.tax_id.compute_all(price, line.order_id.currency_id, line.product_uom_qty,
                                                product=line.product_id, partner=line.order_id.partner_id)
                line.update({
                    'price_tax': taxes['total_included'] - taxes['total_excluded'],
                    'price_total': taxes['total_included'],
                    'price_subtotal': taxes['total_excluded'],
                })
