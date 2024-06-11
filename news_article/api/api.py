import frappe
import json

@frappe.whitelist()
def get_committee_mail(gen, customer_status):
    gen_doc = frappe.get_doc("Generalization", gen)
    selected_committee = [
        committee.the_commission for committee in gen_doc.committees
    ]

    customers = frappe.get_all(
        "Committees you would like to join",
        filters={"committees": ("in", selected_committee)},
        fields=["parent"])
    filtered_customers = []
    for customer in customers:
        customer_doc = frappe.get_doc("Customer", customer["parent"])
        if customer_doc.custom_customer_status == customer_status:
            filtered_customers.append(customer_doc.name)
    contacts_names = frappe.get_all("Dynamic Link",
                                    filters={
                                        "link_doctype": "Customer",
                                        "link_name": ["in", filtered_customers]
                                    },
                                    fields=["parent"])
    contacts = []
    for contact in contacts_names:
        if frappe.db.exists("Contact", contact["parent"]):
            contact_doc = frappe.get_doc("Contact", contact["parent"])
            if contact_doc.email_id:
                name = contact_doc.first_name + " " if contact_doc.first_name else ""
                name += contact_doc.last_name if contact_doc.last_name else ""

                contacts.append({"email": contact_doc.email_id, "name": name})
    return contacts
    
    
    
    
    
    



@frappe.whitelist()
def get_contacts_info(customers, is_json=True):
    if is_json:
        customers = json.loads(customers)
        
    contacts_names = frappe.get_all("Dynamic Link",
                                    filters={
                                        "link_doctype": "Customer",
                                        "link_name": ["in", customers]
                                    },
                                    fields=["parent"])

    contacts = []
    for contact in contacts_names:
        if frappe.db.exists("Contact", contact["parent"]):
            contact_doc = frappe.get_doc("Contact", contact["parent"])
            if contact_doc.email_id:
                name = contact_doc.first_name + " " if contact_doc.first_name else ""
                name += contact_doc.last_name if contact_doc.last_name else ""

                contacts.append({"email": contact_doc.email_id, "name": name})
    return contacts 
    
    
    
    
    
    
    
    
    
    
    
@frappe.whitelist()
def get_committee_mail2(gen, customer_status):
    gen_doc = frappe.get_doc("Committee Generalization", gen)
    selected_committee = [
        gen_doc.committees
    ]

    customers = frappe.get_all(
        "Committees you would like to join",
        filters={"committees": ("in", selected_committee)},
        fields=["parent"])
    filtered_customers = []
    for customer in customers:
        customer_doc = frappe.get_doc("Customer", customer["parent"])
        if customer_doc.custom_customer_status == customer_status:
            filtered_customers.append(customer_doc.name)
    contacts_names = frappe.get_all("Dynamic Link",
                                    filters={
                                        "link_doctype": "Customer",
                                        "link_name": ["in", filtered_customers]
                                    },
                                    fields=["parent"])
    contacts = []
    for contact in contacts_names:
        if frappe.db.exists("Contact", contact["parent"]):
            contact_doc = frappe.get_doc("Contact", contact["parent"])
            if contact_doc.email_id:
                name = contact_doc.first_name + " " if contact_doc.first_name else ""
                name += contact_doc.last_name if contact_doc.last_name else ""

                contacts.append({"email": contact_doc.email_id, "name": name})
    return contacts
