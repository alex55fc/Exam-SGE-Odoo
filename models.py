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
    disponible = fields.Boolean()
    distribuidor = fields.Many2one(comodel_name='distribuidor', string='distribuidor')
    ingrediente = fields.Many2many(comodel_name='ingrediente', string='ingrediente')

    """
    Realiza un filtro de búsqueda para conocer las cervezas agotadas
    Realiza un filtro de búsqueda para conocer las cervezas disponibles
    Debes permitir buscar por Tipo, Contenido de alcohol, Volumen por unidad, Precio por unidad

    """
class loteproduccion(models.Model):
    _name = 'loteproduccion'
    fechainicio = fields.Date()
    fechaestimadafinalizacion = fields.Date()
    cantidadproducida = fields.Integer()
    estado = fields.Selection(selection=[
                                            ('proceso', 'En proceso'),
                                            ('completo', 'Completo'),
                                            ('esperaempaquetado', 'En espera de empaquetado')
                                    ],
                              required=True)
    empaquetado = fields.Many2one(comodel_name='empaquetado', string='empaquetado')

    
class ingrediente(models.Model):
    _name = 'ingrediente'
    name = fields.Char()
    tipo = fields.Selection(selection=[
                                            ('malta', 'Malta'),
                                            ('lupulo', 'Lúpulo'),
                                            ('levadura', 'Levadura'),
                                            ('agua', 'Agua'),
                                            ('otro', 'Otro')
                                    ],
                            required=True)
    cantidadisponible = fields.Float()
    cerveza = fields.Many2many(comodel_name='cerveza', string='cerveza')

class empaquetado(models.Model):
    _name = 'empaquetado'
    fechaempaquetado = fields.Date()
    cantidadempaquetada = fields.Integer()
    loteproduccion=fields.One2many(comodel_name='loteproduccion', inverse_name='empaquetado')
        

class distribuidor(models.Model):
    _name = 'distribuidor'
    name = fields.Char(required=True)
    direccion = fields.Text()
    telefono = fields.Integer()
    cerveza=fields.One2many(comodel_name='cerveza', inverse_name='distribuidor')
 
#Cervezas suministradas -> Un distribuidor puede suministrar varios tipos de cervezas


