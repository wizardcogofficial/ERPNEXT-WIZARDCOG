# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
# License: MIT. See LICENSE

import traceback
import frappe
import frappe.utils
from frappe import _


def home_page_content():
        data=frappe.db.get_all("Home Page Content",fields=["name as id",
                                                           "title",
                                                           "summary",
                                                           "image",
                                                           "description"],
                                                           order_by="-modified") 
        return data


def home_page_content_by_id(id):
        data=frappe.db.get_all("Home Page Content",filters={"name":id},
                fields=["name as id",
                        "title",
                        "summary",
                        "image",
                        "price_range",
                        "description"]) 
        if len(data)>0:
                data=data[0]
        else:
                data=None
        return data



def get_context(context):
      
        form_data=frappe.form_dict
        content_no=form_data.get("content_no")
        #!PARAMETER CASE=>
        
        if content_no is None:
                content=home_page_content()
                context.case="non_routed"
                context.content=content
        else:
                content_data=home_page_content_by_id(content_no)
                context.case="routed"
                context.content = content_data
        
        
        #!NON PARAMETER CASE=>
        

        
