# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError

       
#Taula amb els productes
class jutti_products(models.Model):
    """Productos"""
    
    _name = 'jutti.products'
    _description = "description"
    _price = 'price'

    name = fields.Char(string="Name", size=20, required=True, help='Name of the product')

    stock = fields.Integer(string="Stock",size=100, required=True)

    price = fields.Float(string="Price",size=100, digits=(2,0))

    manufacturating_date = fields.Date()

    description = fields.Text(string="Description", help="Description of the film")

    talla = fields.Integer(string="Size", size=10, required=True)

    material_name = fields.Many2one('jutti.materials', required=True)

    color_id = fields.Selection([('black', 'Black'), ('white', 'White')], required=True, string="Color",
                             default='black')

    suela_name = fields.Many2one('jutti.materials', required=True)

    tipology_id = fields.Selection([('jutti original', 'Jutti Original'), ('jutti 1', 'Jutti #1')], required=True, string="Tipology",
                             default='jutti original')

    @api.constrains('stock')
    @api.constrains('talla')
    @api.constrains('price')

    def _check_values(self):
        for record in self:
            if record.stock < 0:
                raise ValidationError("stock can't be lower than 0")
            elif record.price < 0:
                raise ValidationError("price can't be lower than 0")
            elif record.talla < 0:
                raise ValidationError("size can't be lower than 0")



class jutti_diseñador(models.Model):
    """clients"""
    _name = 'jutti.diseñador'
    _description = "diseñadores"


    name = fields.Text(string='nombre diseñador', size=30)
        
    nif = fields.Text(string='nif', size=30, required=True)

    address = fields.Text(string="Address", required=False, sixe=50)

    city = fields.Text(string='city', size=50)

    tel = fields.Text(string='phone number', size=20, required=True)

    country = fields.Text(string='country', size=20)

    zip = fields.Text(string='zip', size=10)


class jutti_materials(models.Model):
    """materials"""
    _name = 'jutti.materials'
    _description = "materials to build"


    name = fields.Text(string='Material name', size=30)

    quantity = fields.Integer(string='quantity', size=100, required=True)

    material_type = fields.Selection([('sole', 'Sole'), ('upper side material', 'Upper Side Material')], required=True,
                                   string="Material type",
                                   default='sole')

    @api.constrains('quantity')
    def _check_quantity(self):
        for record in self:
            if record.quantity < 0:
                raise ValidationError("Quantity can't be lower than 0")

class jutti_pedidos(models.Model):
    """Pedidos"""
    _name = 'jutti.pedidos'
    _description = "Pedidos de la tienda"

    fecha_pedido = fields.Date(string="Fecha del pedido", required=True, default=fields.Date.today())
    cliente_name = fields.Many2one('jutti.diseñador', string="Cliente", required=True)
    producto_name = fields.Many2one('jutti.products', string="Producto", required=True)
    cantidad = fields.Integer(string="Cantidad", required=True, default=1)
    precio_total = fields.Float(string="Precio total", compute="_compute_precio_total")

    @api.depends('cantidad', 'producto_name.price')
    def _compute_precio_total(self):
        for record in self:
            record.precio_total = record.cantidad * record.producto_name.price

    # @api.constrains('cantidad')
    # def _check_stock(self):
    #     for record in self:
    #         if record.cantidad > record.producto_name.stock:
    #             raise ValidationError("we don't have that amount at the moment")

    @api.onchange('cantidad')
    def _update_stock(self):
        if self.producto_name and self.producto_name.stock < self.cantidad:
            raise ValidationError('No hay suficiente stock disponible.')
        self.producto_name.stock -= self.cantidad