from odoo.addons.component.core import Component
from odoo.addons.base_rest import restapi
import json


class ResCurrency(Component):
    _inherit = 'base.rest.service'
    _name = 'res.currency.service'
    _usage = 'Res Currency'
    _collection = 'contact.services.private.services'
    _description = """
         API Services to search currencies
    """
    
    @restapi.method(
        [(["/<string:name>/search"], "GET")],
        output_param=restapi.CerberusValidator("_validator_search"),
        auth="public",
    )
    
    def search(self, name):
        dict = {}
        list = []
        if name == "all":
            res_currency = self.env["res.currency"].search([])
        else:
            res_currency = self.env["res.currency"].search([('name','=',name)])
        if res_currency:
            for item in res_currency:
                dict = {
                         "id": item.id,
                        "name": item.name
                      }
                list.append(dict)
            res = {
                "res_currency": list
            }
        else:
            res = {
                    "message": "No existe un equipo con este nombre"
                  }
        return res
    
    def _validator_search(self):
        res = {
                "res_currency": {"type":"list", 
                                       "schema": { 
                                        "type": "dict",
                                        "schema": {
                                                    "id": {"type":"integer", "required": False},
                                                    "name": {"type":"string", "required": True},
                                                    "message": {"type":"string", "required": False}
                                                  }
                                       }
                               }
            }
        return res
