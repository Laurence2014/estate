from odoo import fields, models
import datetime

class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "estate property model"

    name = fields.Char(required=True)
    
    postcode = fields.Char((""), max_length=50)
    date_availability = fields.Date(string ='Date', copy=False, default=datetime.datetime.now() + datetime.timedelta(days=90))
    expected_price = fields.Float(required=True)
    selling_price = fields.Float(readonly=True, copy=False)
    bedrooms = fields.Integer(default=2.0)
    living_area = fields.Integer()
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer()
    garden_orientation = fields.Selection([('north', 'North'), ('south', 'South'), ('east', 'East'), ('west', 'West')], string="Orientation")
    active = fields.Selection([('true', 'True'), ('false', 'False')], string="Active", default=False, required=True)
    state = fields.Selection([('new', 'New'), ('offer received', 'Offer Received'), ('offer accepted', 'Offer Accepted'), ('sold', 'Sold'), ('canceled', 'Canceled')], required=True, copy=False, default=False)