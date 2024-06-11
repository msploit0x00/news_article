console.log("sdf");
frappe.ui.form.on('Generalization', {
  refresh(frm) {
    // your code here
    frm.add_custom_button(__('Get User Email Address'), function(){
      frappe.msgprint(frm.doc);
    }, __(""));
  },
  due_date(frm) {
    console.log('sdf')
  }
})
