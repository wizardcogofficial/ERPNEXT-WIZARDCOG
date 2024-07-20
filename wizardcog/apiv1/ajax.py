import frappe

@frappe.whitelist(allow_guest=True,methods=["POST","GET"])
def create_enquiry(client_mail,enquiry_for,enquiry_message):
    try:
        enquiry = frappe.get_doc({
            'doctype': 'Client Enquiry',
            'client_mail': client_mail,
            'enquiry_for': enquiry_for,
            'enquiry_message': enquiry_message
        })
        enquiry.insert(ignore_permissions=True)
        frappe.db.commit()
        return 1
    except Exception as e:
        return 0

@frappe.whitelist(allow_guest=True,methods=["GET"])
def get_enquiry():
        return 0
