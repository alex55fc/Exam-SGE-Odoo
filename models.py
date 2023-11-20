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
class loteproduccion(models.Model):
    #Cerveza -> un lote de producción es asociado a una única cerveza
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

#Un ingrediente puede ser utilizado en la producción de varias cervezas y una cerveza puede requerir varios ingredientes

class empaquetado(models.Model):
    _name = 'empaquetado'
    fechaempaquetado = fields.Date()
    cantidadempaquetada = fields.Integer()
    #Lote de Producción -> el empaquetado está asociado a uno o varios lotes de producción

class distribuidor(models.Model):
    _name = 'distribuidor'
    name = fields.Char(required=True)
    direccion = fields.Text()
    telefono = fields.Integer()
#Cervezas suministradas -> Un distribuidor puede suministrar varios tipos de cervezas


