# -*- coding: utf-8 -*-
# Copyright (c) 2019, saurabh and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class MyProjects(Document):
	def __init__(self, *args, **kwargs):
		super(MyProjects, self).__init__(*args, **kwargs)
		if frappe.local.form_dict.get('cmd') == 'login' or frappe.local.request.path == "/api/method/myprojects":
			if self.returnProjects:return

@frappe.whitelist(allow_guest=True)
def returnProjects(self):
	return frappe.get_all("My Projects", limit_page_lenght=1)[0]


