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


@frappe.whitelist()
def get_committee_mail2(gen, customer_status):
    gen_doc = frappe.get_doc("Committee Generalization", gen)
    selected_committee = [
        gen_doc.committees
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

#    for contact in contacts_names:
#        if frappe.db.exists("Contact", contact["parent"]):
#            contact_doc = frappe.get_doc("Contact", contact["parent"])
#            if contact_doc.email_id:
#                name = contact_doc.first_name + " " if contact_doc.first_name else ""
#                name += contact_doc.last_name if contact_doc.last_name else ""
#
            contacts.append(
                {"email": customer_doc.custom_email, "name": customer_doc.name})
    return contacts


@frappe.whitelist()
def get_committee_mail2(gen, customer_status):
    gen_doc = frappe.get_doc("Committee Generalization", gen)
    selected_committee = [gen_doc.committees]

    customers = frappe.get_all(
        "Committees you would like to join",
        filters={"committees": ("in", selected_committee)},
        limit_page_length=5000,
        fields=["parent"]
    )

    contacts = []

    for customer in customers:
        customer_doc = frappe.get_doc("Customer", customer["parent"])
        if customer_doc.custom_customer_status == customer_status:
            # loop through the child table 'custom_emails'
            for row in customer_doc.get("custom_emails"):
                if row.email_id:  # only add if email exists
                    contacts.append({
                        "email": row.email_id,
                        "name": customer_doc.name
                    })

    return contacts


# @frappe.whitelist()
# def get_committee_mail2(gen, customer_status):
#     # جلب ال Committees من Generalization
#     gen_doc = frappe.get_doc("Committee Generalization", gen)
#     selected_committees = [c.the_commission for c in gen_doc.committees]

#     # جلب كل الـ Customers المرتبطين بهذه اللجان
#     customers = frappe.get_all(
#         "Committees you would like to join",
#         filters={"committees": ("in", selected_committees)},
#         fields=["parent"]
#     )

#     contacts = []
#     for cust in customers:
#         cust_doc = frappe.get_doc("Customer", cust["parent"])
#         if cust_doc.custom_customer_status == customer_status:
#             for row in cust_doc.get("custom_emails"):
#                 if row.email_id:
#                     contacts.append(
#                         {"email": row.email_id, "name": cust_doc.name})

#     return contacts

# @frappe.whitelist()
# def get_committee_mail2(gen, customer_status):
#     # 1️⃣ هات الدوك
#     gen_doc = frappe.get_doc("Committee Generalization", gen)

#     # 2️⃣ جمع كل القيم من child table زي النسخة اللي فوق بالظبط
#     # عدل الاسم حسب اسم الفيلد الحقيقي
#     selected_committees = [d.committes for d in gen_doc.committees]

#     # 3️⃣ هات كل الـ customers اللي join committees
#     customers = frappe.get_all(
#         "Committees you would like to join",
#         filters={"committees": ("in", selected_committees)},
#         fields=["parent"]
#     )

#     contacts = []

#     for cust in customers:
#         cust_doc = frappe.get_doc("Customer", cust["parent"])

#         if cust_doc.custom_customer_status == customer_status:
#             for row in cust_doc.get("custom_emails"):
#                 if row.email_id:
#                     contacts.append({
#                         "email": row.email_id,
#                         "name": cust_doc.name
#                     })

#     return contacts


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


@frappe.whitelist()
def get_authorities_contacts(authority_name):
    """
    جلب جهات الاتصال من Authority معينة
    للاستخدام في Dialog البحث

    Args:
        authority_name: اسم الـ Authority

    Returns:
        list: قائمة من القواميس تحتوي على authority, phone, email
    """
    try:
        if not authority_name:
            return []

        contacts_data = []

        # Get all contacts linked to this authority
        contacts = frappe.get_all(
            "Contact",
            filters={"custom_authority": authority_name},
            fields=["name"]
        )

        # For each contact, get detailed information
        for contact in contacts:
            contact_doc = frappe.get_doc("Contact", contact.name)

            # Get emails from email_ids child table
            emails = [row.email_id for row in contact_doc.get(
                "email_ids", []) if row.email_id]

            # Get phones from phone_nos child table
            phones = [row.phone for row in contact_doc.get(
                "phone_nos", []) if row.phone]

            # Create records - match emails and phones by index
            max_length = max(len(emails), len(phones), 1)

            for i in range(max_length):
                contacts_data.append({
                    "authority": authority_name,
                    "phone": phones[i] if i < len(phones) else "",
                    "email": emails[i] if i < len(emails) else ""
                })

        return contacts_data

    except Exception as e:
        frappe.log_error(message=str(
            e), title="get_authorities_contacts Error")
        return []


@frappe.whitelist()
def get_authorities_emails_for_newsletter(authorities_list):
    """
    جلب كل الإيميلات من Authorities معينة
    للاستخدام في إرسال Newsletter (اختياري - للمستقبل)

    Args:
        authorities_list: قائمة من أسماء الـ Authorities (JSON string or list)

    Returns:
        list: قائمة من الإيميلات فقط
    """
    try:
        # Parse JSON if string
        if isinstance(authorities_list, str):
            import json
            authorities_list = json.loads(authorities_list)

        if not authorities_list:
            return []

        all_emails = []

        # Loop through each authority
        for authority_name in authorities_list:
            # Get all contacts for this authority
            contacts = frappe.get_all(
                "Contact",
                filters={"custom_authority": authority_name},
                fields=["name"]
            )

            # Get emails from each contact
            for contact in contacts:
                contact_doc = frappe.get_doc("Contact", contact.name)

                # Get all emails from email_ids child table
                for email_row in contact_doc.get("email_ids", []):
                    if email_row.email_id:
                        all_emails.append(email_row.email_id)

        # Remove duplicates
        all_emails = list(set(all_emails))

        return all_emails

    except Exception as e:
        frappe.log_error(message=str(
            e), title="get_authorities_emails_for_newsletter Error")
        return []
