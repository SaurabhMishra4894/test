# -*- coding: utf-8 -*-
# Copyright (c) 2019, saurabh and Contributors
# See license.txt
from __future__ import unicode_literals

import frappe
import unittest

class TestMyProjects(unittest.TestCase):
	@frappe.whitelist()
	def methodname(doctype, project, filters):
		return frappe.db.sql(""" your query """.format(code= filters.get("client")))



