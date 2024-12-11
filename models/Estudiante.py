from odoo import models, fields, api

class Estudiante(models.Model):
    _name = 'escuela.estudiante'
    _description = 'Modelo para gestionar los estudiantes'

    nombre = fields.Char(string='Nombre', required=True)
    apellidos = fields.Char(string='Apellidos', required=True)
    edad = fields.Integer(string='Edad', required=True)
    grupo_id = fields.Many2one('escuela.grupo', string='Grupo', ondelete='set null')
    
    