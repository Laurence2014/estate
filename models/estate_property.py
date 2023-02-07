from odoo import fields, models

class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "estate property model"

    name = fields.Char(required=True)
    
    postcode = fields.Char((""), max_length=50)
    date_availability = fields.Date((""), auto_now=False, auto_now_add=False)
    expected_price = fields.Float(required=True)
    selling_price = fields.Float()
    bedrooms = fields.Integer()
    living_area = fields.Integer()
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer()
    