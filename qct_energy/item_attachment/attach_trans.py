import frappe
import json

@frappe.whitelist()
def attach_all_docs(document, method=None):
	document = json.loads(document)
	current_attachments=[]
	print("@@@@@@@@@@@@_---------------------")
	a=("""select file_url from `tabFile` where attached_to_doctype = "Item" and attached_to_name = 'test' """)
	print(a)
	b=frappe.db.sql(a, as_dict=True)
	for file_url in b :
		current_attachments.append(file_url.file_url)
		count = 0
		for item_doc in document["items"]:
			print("$$$$$$$$$$$$$$$$$$$")
			print(item_doc)
			#frappe.msgprint(item_doc)
			# Check to see if the quantity is = 1
			print("VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV")
			print(item_doc["item_code"])
			if item_doc["item_code"]:
				item = frappe.get_doc("Item",item_doc["item_code"])
				print("SSSSSSSSSSSSSSSSSSSSSSSSSSSSS")
				print(item)
	
				attachments = []
				# Get the path for the attachments
				if item.drawing_attachment:
					attachments.append(item.drawing_attachment)
				if item.stp_attachment:
					attachments.append(item.stp_attachment)
				if item.dxf_attachment:
					attachments.append(item.dxf_attachment)
				if item.x_t_attachment:
					attachments.append(item.x_t_attachment)
			
				for attach in attachments:
					# Check to see if this file is attached to the one we are looking for
					if not attach in current_attachments:
						count = count + 1
						save_url(attach, document["doctype"], document["name"], "Home/Attachments")
						frappe.msgprint("Attached {0} files".format(count))