# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
# License: MIT. See LICENSE

import traceback
import frappe
import frappe.utils
from frappe import _





def get_context(context):
        form_data=frappe.form_dict
        content_no=form_data.get("content_no")
        #!PARAMETER CASE=>
        
        if content_no is None:
                 blog_links=frappe.db.get_all("Blog Content",fields=["*"],order_by="-modified",limit=15)
                 video_links=frappe.db.get_all("Video Content",fields=["*"],order_by="-modified",limit=15)
                 context.case="non_routed"
                 context.content = video_links
                 context.blog_links=blog_links
        else:
                content_data=blog_links=frappe.db.get_all("Blog Content",fields=["*"],order_by="-modified",
                filters={"name": content_no})
                print("cont")
                if len(content_data)>0:
                        content_data=content_data[0]
                        context.case="routed"
                        context.data = content_data
       
                else:
                      frappe.local.response["type"] = "redirect"
                      frappe.local.response["location"] = "/desk"
                      
                
        
        
        #!NON PARAMETER CASE=>
        

        
