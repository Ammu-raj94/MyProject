from odoo import fields, models


class SaleOrderLineInherit(models.Model):
    _inherit = "sale.order.line"
    package_id = fields.Many2one('sale.package', string="Package")


class SaleOrderInherit(models.Model):
    _inherit = "sale.order"
    package_id = fields.Many2many('sale.package', string="Package")
    pack_info = fields.Text()


class Package(models.Model):
    _name = "sale.package"
    _rec_name = 'Name'
    _description = "sale package"

    Name = fields.Char()
    Width = fields.Float()
    Height = fields.Float()
    Length = fields.Float()
    Maximum_weight = fields.Float()
