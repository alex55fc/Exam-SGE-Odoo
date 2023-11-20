from odoo import api, models, fields
#clases
class cerveza(models.Model):
    _name = 'cerveza'
    name = fields.Char(required=True)
    tipo = fields.Char()
    descripcion = fields.Text()
    contenidoalcohol = fields.Float()
    preciounidad = fields.Float()
    volumenunidad = fields.Float()
    """disponible = fields.Boolean(string='Disponible', compute='_compute_disponible')
    Disponible -> fields.Boolean, calculado automáticamente en función del inventario
    Realiza un filtro de búsqueda para conocer las cervezas agotadas
    Realiza un filtro de búsqueda para conocer las cervezas disponibles
    Debes permitir buscar por Tipo, Contenido de alcohol, Volumen por unidad, Precio por unidad

    """
class distribuidor(models.Model):
    _name = 'distribuidor'
    name = fields.Char(required=True)
    direccion = fields.Text()
    telefono = fields.Integer()
#Cervezas suministradas -> Un distribuidor puede suministrar varios tipos de cervezas


