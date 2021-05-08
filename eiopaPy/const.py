def API_URL():
    return "https://mehdiechchelh.com/"

# Type of the risk-free-rate to query
def WITH_VA():
    return "with_va"
def NO_VA():
    return "no_va"
def NO_VA_SHOCK_DOWN():
    return "no_va_shock_down"
def NO_VA_SHOCK_UP():
    return "no_va_shock_up"
def WITH_VA_SHOCK_DOWN():
    return "with_va_shock_down"
def WITH_VA_SHOCK_UP():
    return "with_va_shock_down"
def VA():
    return "va"

def PATH_GET_RFR(type,region,params):
    """add description """
    """params:dict"""
    return "/api/rfr/%s/%s/?%s" %(type,region,"&".join([elm+"="+params[elm] for elm in params]))

def PATH_GET_OPTIONS(field):
    """add description"""
    return "/api/rfr/options/%s" %(field)


def option_rfr_types():
    """add description"""
    return ([WITH_VA(),NO_VA(),NO_VA_SHOCK_DOWN(),NO_VA_SHOCK_UP(),WITH_VA_SHOCK_DOWN(),WITH_VA_SHOCK_UP(),VA()])

