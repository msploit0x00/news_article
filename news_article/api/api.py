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
        limit_page_length=5000,
        fields=["parent"])
    filtered_customers = []
    contacts = []

    for customer in customers:
        customer_doc = frappe.get_doc("Customer", customer["parent"])
        if customer_doc.custom_customer_status == customer_status:
            filtered_customers.append(customer_doc.name)
    # contacts_names = frappe.get_all("Dynamic Link",
    #                                 filters={
    #                                     "link_doctype": "Customer",
    #                                     "link_name": ["in", filtered_customers]
    #                                 },
    #                                 fields=["parent"])
    # for contact in contacts_names:
    #     if frappe.db.exists("Contact", contact["parent"]):
    #         contact_doc = frappe.get_doc("Contact", contact["parent"])
    #         if contact_doc.email_id:
    #             name = contact_doc.first_name + " " if contact_doc.first_name else ""
    #             name += contact_doc.last_name if contact_doc.last_name else ""

            contacts.append(
                {"email": customer_doc.custom_email, "name": customer_doc.name})
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


# @frappe.whitelist()
# def get_committee_mail2(gen, customer_status):
#     gen_doc = frappe.get_doc("Committee Generalization", gen)
#     selected_committee = [
#         gen_doc.committees
#     ]

#     customers = frappe.get_all(
#         "Committees you would like to join",
#         filters={"committees": ("in", selected_committee)},
# 	limit_page_length=5000,
#         fields=["parent"])
#     filtered_customers = []
#     contacts = []
#     for customer in customers:
#         customer_doc = frappe.get_doc("Customer", customer["parent"])
#         if customer_doc.custom_customer_status == customer_status:
#             filtered_customers.append(customer_doc.name)
#     # contacts_names = frappe.get_all("Dynamic Link",
#     #                                 filters={
#     #                                     "link_doctype": "Customer",
#     #                                     "link_name": ["in", filtered_customers]
#     #                                 },
#     #                                 fields=["parent"])

# #    for contact in contacts_names:
# #        if frappe.db.exists("Contact", contact["parent"]):
# #            contact_doc = frappe.get_doc("Contact", contact["parent"])
# #            if contact_doc.email_id:
# #                name = contact_doc.first_name + " " if contact_doc.first_name else ""
# #                name += contact_doc.last_name if contact_doc.last_name else ""
# #
#             contacts.append({"email": customer_doc.custom_email, "name": customer_doc.name})
#     return contacts


# @frappe.whitelist()
# def get_committee_mail2(gen, customer_status):
#     gen_doc = frappe.get_doc("Committee Generalization", gen)
#     selected_committee = [gen_doc.committees]

#     customers = frappe.get_all(
#         "Committees you would like to join",
#         filters={"committees": ("in", selected_committee)},
#         limit_page_length=5000,
#         fields=["parent"]
#     )

#     contacts = []

#     for customer in customers:
#         customer_doc = frappe.get_doc("Customer", customer["parent"])
#         if customer_doc.custom_customer_status == customer_status:
#             # loop through the child table 'custom_emails'
#             for row in customer_doc.get("custom_emails"):
#                 if row.email_id:  # only add if email exists
#                     contacts.append({
#                         "email": row.email_id,
#                         "name": customer_doc.name
#                     })

#     return contacts


@frappe.whitelist()
def get_committee_mail2(gen, customer_status):
    # جلب ال Committees من Generalization
    gen_doc = frappe.get_doc("Generalization", gen)
    selected_committees = [c.the_commission for c in gen_doc.committees]

    # جلب كل الـ Customers المرتبطين بهذه اللجان
    customers = frappe.get_all(
        "Committees you would like to join",
        filters={"committees": ("in", selected_committees)},
        fields=["parent"]
    )

    contacts = []
    for cust in customers:
        cust_doc = frappe.get_doc("Customer", cust["parent"])
        if cust_doc.custom_customer_status == customer_status:
            for row in cust_doc.get("custom_emails"):
                if row.email_id:
                    contacts.append(
                        {"email": row.email_id, "name": cust_doc.name})

    return contacts


@frappe.whitelist()
def get_generalzation_email(gen, customer_status):
    """
    جلب كل الإيميلات من العملاء المرتبطين باللجان الموجودة في Generalization معين
    """
    try:
        gen_doc = frappe.get_doc("Generalization", gen)
        selected_committees = [c.the_commission for c in gen_doc.committees]

        customers = frappe.get_all(
            "Committees you would like to join",
            filters={"committees": ("in", selected_committees)},
            fields=["parent"]
        )

        contacts = []
        for cust in customers:
            cust_doc = frappe.get_doc("Customer", cust["parent"])
            if cust_doc.custom_customer_status == customer_status:
                for row in cust_doc.get("custom_emails") or []:  # حماية لو فاضية
                    if row.email_id:
                        contacts.append({
                            "email": row.email_id,
                            "name": cust_doc.name
                        })

        return contacts or []  # ⚠️ ضمان رجوع array دائماً
    except Exception as e:
        frappe.log_error(message=str(e), title="get_committee_mail2 Error")
        return []
