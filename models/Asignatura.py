from odoo import models, fields, api

class Asignatura(models.Model):
    _name = 'escuela.asignatura'
    _description = 'Modelo para gestionar las asignaturas'

    codigo = fields.Char(string='Código de Asignatura', required=True)
    nombre = fields.Char(string='Nombre de Asignatura', required=True)
    numero_horas = fields.Integer(string='Número de Horas', required=True)
    grupos_ids = fields.Many2many('escuela.grupo', string='Grupos')
