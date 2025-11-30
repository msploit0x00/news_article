// Copyright (c) 2023, Ahmed and contributors
// For license information, please see license.txt

frappe.ui.form.on('Customer Newsletter', {
  refresh: function(frm) {
    if(!frm.doc.__unsaved && frm.doc.custom_sent_email_direct === 1) {
      frm.add_custom_button(__('Send Email'), function(){
        frm.call("send_email").then(() => {
          cosnole.log("done");
        });
      }, __(""));
    }
  },
  get_customer_didnt_subscribe(frm) {
    frm.call("get_customers_didnt_subscribe").then((r) => {
      let contacts = r.message;
      for (let contact of contacts) {
        cur_frm.add_child("customer_email", {
          email: contact.email,
          customer_name: contact.name,
        });
      }
      cur_frm.refresh_fields();
    });
  }
})
