from odoo import api, models, fields
#clases
class distribuidor(models.Model):
    _name = 'distribuidor'
    name = fields.Char(required=True)
    direccion = fields.Text()
    telefono = fields.Integer()
#Cervezas suministradas -> Un distribuidor puede suministrar varios tipos de cervezas


