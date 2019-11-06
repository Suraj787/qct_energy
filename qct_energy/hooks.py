# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "qct_energy"
app_title = "qct energy"
app_publisher = "suraj varade"
app_description = "qct energy"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "varade.suraj787@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/qct_energy/css/qct_energy.css"
# app_include_js = "/assets/qct_energy/js/qct_energy.js"

# include js, css files in header of web template
# web_include_css = "/assets/qct_energy/css/qct_energy.css"
# web_include_js = "/assets/qct_energy/js/qct_energy.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
doctype_js = {
	"Quotation": "public/js/attachment_trans.js"
}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "qct_energy.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "qct_energy.install.before_install"
# after_install = "qct_energy.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "qct_energy.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"qct_energy.tasks.all"
# 	],
# 	"daily": [
# 		"qct_energy.tasks.daily"
# 	],
# 	"hourly": [
# 		"qct_energy.tasks.hourly"
# 	],
# 	"weekly": [
# 		"qct_energy.tasks.weekly"
# 	]
# 	"monthly": [
# 		"qct_energy.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "qct_energy.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "qct_energy.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "qct_energy.task.get_dashboard_data"
# }

