# -*- coding: utf-8 -*-

"""Form validation using WTForms"""


from flask_wtf import Form
from wtforms import IntegerField, StringField
from wtforms.validators import DataRequired


class PurchaseForm(Form):
    """Validates Klarna On-Demand form data"""
    amount = IntegerField('Amount', validators=[DataRequired()])
    currency = StringField('Currency', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    name = StringField('Name', validators=[DataRequired()])
    origin_proof = StringField('Origin proof', validators=[DataRequired()])
    reference = StringField('Reference', validators=[DataRequired()])
    userToken = StringField('User token', validators=[DataRequired()])
