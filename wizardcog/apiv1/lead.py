
import frappe
from  ..apitils.response import api_response
from datetime import datetime
from bs4 import BeautifulSoup
@frappe.whitelist(allow_guest=False,methods=["GET"])
def getLeadList(limit=100,offset=0):

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
 

    lead_list = frappe.get_all("Lead",
        fields=["*"],
            limit=limit,
            start=offset,
            order_by='-modified'
        )
    #!==========================================================================================
    #!==========================================================================================
    lead_list = frappe.get_all("Item")
    data_size=len(lead_list)
    #!==============================================================================================
    if len(lead_list)==0:
        return api_response(status=True, data=[], message="Empty Content", status_code=204)
    else:
        return api_response(status=True, 
                            data=lead_list, 
                            message="Successfully Fetched Items", 
                            status_code=200,
                            data_size=data_size)
