from const import *
import api
import pandas as pd

def get_rfr(region,type=option_rfr_types()[0],year=None,month=None,format=["dataframe"]):
    
    format=format[0]
    if not(isinstance(region,str)):
        raise ValueError("'region' should be of length 1.")
    
    if isinstance(year,int):
        year= str(year)
    else:
        year= ",".join([str(x) for x in year]) if all([isinstance(x, int) for x in year]) else ""
    
    if isinstance(month,int):
        month=str(month)
    else:
        month=",".join([str(x) for x in month]) if all([isinstance(x, int) for x in month]) else ""
    
    path=PATH_GET_RFR(type, region,{"year":year, "month":month})
    resp=api.api_get(path)

    parse_rfr(resp, format)


def parse_rfr(resp,format):
    if format == "dataframe":
        return parse_rfr_to_df(resp)


def get_rfr_with_va(region,year=None,month=None,format=["dataframe"]):
    type=WITH_VA()
    get_rfr(region = region,type = type,year = year,month = month)


def get_rfr_no_va(region,year = None,month = None,format = ["dataframe"]):
    type=NO_VA()
    get_rfr(region = region,type = type,year = year,month = month)


def parse_rfr_to_df(resp):
    
    # Ensure that the reponse contains data
    content=resp["content"]
    if len(content) == 0:
        return {"data":pd.DataFrame(),metadata:pd.DataFrame(),format:"df"}
    
    # Metadata
    df_metadata=pd.DataFrame({key:[content[key]] for key in content if key!="data"})
    # Data
    df_data=pd.DataFrame({df_metadata["id"][0]:list(content["data"].values())})
    print("df_data : ",df_data)
    return {"data":df_data,"metadata":df_metadata,"format":"df"}


#resp=get_rfr( "FR","with_va", 2019, 12)
#resp=get_rfr("no_va", "FR", 2019, 12)
#print(resp)

# def print.eiopa_rfr(x, *args):
#     print("<eiopa_rfr>\n")
#     for i in len(x["metadata"]):
#         print(sprintf("%s > %s ...\n",x["metadata"]["id"][i],paste(x$data[1:3, i], collapse = ", ")))
#    }
#    invisible(x)
