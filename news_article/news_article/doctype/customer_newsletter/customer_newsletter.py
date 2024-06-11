# Copyright (c) 2023, Ahmed and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe import _
from datetime import datetime
from news_article.api.api import get_contacts_info


class CustomerNewsletter(Document):

    @frappe.whitelist()
    def send_email(self):
        recipients = [customer.email for customer in self.customer_email]
        args = self.as_dict()
        args["message"] = self.get_message()
        email_args = {
            "subject": self.subject,
            "sender": self.sender_email,
            "recipients": recipients,
            "attachments": self.get_attachments(),
            "template": "newsletter",
            "reference_doctype": self.doctype,
            "reference_name": self.name,
            "queue_separately": True,
            "send_priority": 0,
            "args": args
        }
        frappe.sendmail(**email_args)
        frappe.msgprint(_("Email sent successfully"))

    def get_message(self):
        content = frappe.render_template(self.body, {"doc": self.as_dict()})
        return content

    def get_attachments(self):
        return [{"file_url": row.attachment} for row in self.attachs]

    @frappe.whitelist()
    def get_customers_didnt_subscribe(self):
        year = datetime.now().year
        customer_paid = frappe.get_list("Sales Invoice",
                                        filters={
                                            "status": "Paid",
                                            "custom_annual_fees": 1,
                                            "creation":
                                            [">=", f"{year}-01-01"]
                                        },
                                        fields=["customer"])
        formatted_paid_customers = [
            customer["customer"] for customer in customer_paid
        ]
        contacts = []
        if formatted_paid_customers:
            unpaid_customer = frappe.get_list(
                "Customer",
                filters={"name": ["not in", formatted_paid_customers]},
                fields=["name"])
        else:
            unpaid_customer = frappe.get_list("Customer", fields=["name"])

        unpaid_customer = [customer["name"] for customer in unpaid_customer]
        contacts = get_contacts_info(unpaid_customer, is_json=False)
        print("contacts", contacts)

        return contacts
