import logging
import requests

API_URL="https://mehdiechchelh.com/api/rfr/"

# Type of the risk-free-rate to query
WITH_VA="with_va"
NO_VA="no_va"
NO_VA_SHOCK_DOWN="no_va_shock_down"
NO_VA_SHOCK_UP="no_va_shock_up"
WITH_VA_SHOCK_DOWN="with_va_shock_down"
WITH_VA_SHOCK_UP="with_va_shock_down"
VA="va"

def PATH_GET_RFR(type,region,params:dict):
    """add description """
    """params:dict"""
    return "/api/rfr/%s/%s/?%s" %(type,region,"&".join([i+"="+params[i] for i in params]))

def PATH_GET_OPTIONS(field):
    """add description"""
    return "/api/rfr/options/%s" %(field)


def options_rfr_types():
    """add description"""
    return ([WITH_VA,NO_VA,NO_VA_SHOCK_DOWN,NO_VA_SHOCK_UP,WITH_VA_SHOCK_DOWN,WITH_VA_SHOCK_UP,VA])

def api_get(path:str):
    url=API_URL+"/"+path
    resp=requests.get(url)
    return resp

