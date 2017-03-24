# -*- coding: utf-8 -*-

from odoo import http
from odoo.http import request


class OurController(http.Controller):

    @http.route('/wwwdemo', type='http', auth='public')
    def handler(self):
        values = False

        return request.render("website_demo.default_view", values)
