from . import __version__ as app_version

app_name = "news_article"
app_title = "News Article"
app_publisher = "mina"
app_description = "alternative news letter"
app_email = "mina.m@datasofteg.com"
app_license = "GNU V3"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/news_article/css/news_article.css"
# app_include_js = "public/js/generalization/generalization.js"

# include js, css files in header of web template
# web_include_css = "/assets/news_article/css/news_article.css"
# web_include_js = "/assets/news_article/js/news_article.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "news_article/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
doctype_js = {"Generalization" : "public/js/generalization/generalization.js",
              "Meeting": "public/js/meeting.js"}
# doctype_list_js = {"doctype" : "public/js/generalization_list.js"}
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

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
#	"methods": "news_article.utils.jinja_methods",
#	"filters": "news_article.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "news_article.install.before_install"
# after_install = "news_article.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "news_article.uninstall.before_uninstall"
# after_uninstall = "news_article.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "news_article.utils.before_app_install"
# after_app_install = "news_article.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "news_article.utils.before_app_uninstall"
# after_app_uninstall = "news_article.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "news_article.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
#	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
#	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
#	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
#	"*": {
#		"on_update": "method",
#		"on_cancel": "method",
#		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
#	"all": [
#		"news_article.tasks.all"
#	],
#	"daily": [
#		"news_article.tasks.daily"
#	],
#	"hourly": [
#		"news_article.tasks.hourly"
#	],
#	"weekly": [
#		"news_article.tasks.weekly"
#	],
#	"monthly": [
#		"news_article.tasks.monthly"
#	],
# }

# Testing
# -------

# before_tests = "news_article.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
#	"frappe.desk.doctype.event.event.get_events": "news_article.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
#	"Task": "news_article.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["news_article.utils.before_request"]
# after_request = ["news_article.utils.after_request"]

# Job Events
# ----------
# before_job = ["news_article.utils.before_job"]
# after_job = ["news_article.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
#	{
#		"doctype": "{doctype_1}",
#		"filter_by": "{filter_by}",
#		"redact_fields": ["{field_1}", "{field_2}"],
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_2}",
#		"filter_by": "{filter_by}",
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_3}",
#		"strict": False,
#	},
#	{
#		"doctype": "{doctype_4}"
#	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
#	"news_article.auth.validate"
# ]
