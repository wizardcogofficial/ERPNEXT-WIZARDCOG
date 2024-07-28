
import frappe
from  ..apitils.response import api_response
from datetime import datetime
from bs4 import BeautifulSoup
@frappe.whitelist(allow_guest=False,methods=["GET"])
def getItemList(limit=100,offset=0):

    #TODO 1: limit offset int format check
    try:
        limit = int(limit)
        offset = int(offset)
    except:
        return api_response(status=False, data=[], message="Please Enter Proper Limit and Offset", status_code=400)
    #!limit and offset upper limit validation
    if limit > 200 or limit < 0 or offset<0:
        return api_response(status=False, data=[], message="Limit exceeded 500", status_code=400)
    #!timestamp non empty validation
    #!timestamp format validation
 

    item_list = frappe.get_all("Item",
        fields=["item_group as item_category_name",
                "item_name as item_name",
                "item_code as item_code",
                "description as item_description",
                "stock_uom as item_stock_uom",
                "modified as updated_at",
                "weight_per_unit",
                "weight_uom",
                "name as id"
                ],
            limit=limit,
            start=offset,
            order_by='-modified'
        )
    #!==========================================================================================
    for item in item_list:
         if item.item_description:
            soup = BeautifulSoup(item.item_description, 'html.parser')
            item.item_description = soup.get_text()

    #!==========================================================================================
    item_list_with_timestamp = frappe.get_all("Item")
    data_size=len(item_list_with_timestamp)
    #!==============================================================================================
    if len(item_list)==0:
        return api_response(status=True, data=[], message="Empty Content", status_code=204)
    else:
        return api_response(status=True, 
                            data=item_list, 
                            message="Successfully Fetched Items", 
                            status_code=200,
                            data_size=data_size)
