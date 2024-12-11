from odoo import models, fields, api

class Grupo(models.Model):
    _name = 'escuela.grupo'
    _description = 'Modelo para gestionar los grupos de estudiantes'

    descripcion = fields.Text(string='Descripción del Grupo', required=True)
    modulo_profesional = fields.Selection(
        selection=[('SMR', 'SMR'), ('DAM', 'DAM'), ('DAW', 'DAW'), ('ASIR', 'ASIR')],
        string='Módulo Profesional',
        default='SMR',
        required=True
    )
    curso = fields.Selection(
        selection=[('1', '1'), ('2', '2')],
        string='Curso',
        default='1',
        required=True
    )
    estudiantes_ids = fields.One2many('escuela.estudiante', 'grupo_id', string='Estudiantes')
    asignaturas_ids = fields.Many2many('escuela.asignatura', string='Asignaturas')