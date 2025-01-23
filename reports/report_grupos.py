# reports/report_grupos.py
from odoo import models, api

class ReportGrupos(models.AbstractModel):
    # Debe coincidir EXACTAMENTE con el "report_name" definido en el XML,
    # pero con 'report.' delante
    _name = 'report.escuela.report_grupos'
    _description = 'Informe QWeb de Grupos'

    @api.model
    def _get_report_values(self, docids, data=None):
        # docids son los IDs de los grupos seleccionados
        grupos = self.env['escuela.grupo'].browse(docids)

        return {
            'docs': grupos,          # la lista de grupos
            'doc_model': 'escuela.grupo',
        }
