frappe.ui.form.on("Quotation",{
refresh: function(frm) {
    frm.add_custom_button(__("Load Attachments"), function(foo) {

	frappe.call({
		method:"qct_energy.item_attachment.attach_trans.attach_all_docs",
		args: {
			document: cur_frm.doc,
			
		}, 
		callback: function(r) { 
			
		}
	});
    });
    }
});