# -*- coding: utf-8 -*-

from openerp import models, fields, api, _
from openerp.osv import osv
from openerp.exceptions import except_orm, ValidationError
from StringIO import StringIO
import urllib2, httplib, urlparse, gzip, requests, json
import openerp.addons.decimal_precision as dp
import logging
import datetime
from openerp.fields import Date as newdate

#Get the logger
_logger = logging.getLogger(__name__)


class ResPartner(models.Model):
	_inherit = 'res.partner'

	rev = fields.Char(string='CouchDB Rev')

class ProductProduct(models.Model):
	_inherit = 'product.product'

	rev = fields.Char(string='CouchDB Rev')

