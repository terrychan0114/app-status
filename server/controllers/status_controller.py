import connexion
import six
import pandas as pd
from pandas import ExcelFile
import json
from flask import Response
from loguru import logger
from datetime import datetime

from server.models.status_info import StatusInfo  # noqa: E501
from server import util

# file = "/usr/src/app/doc/kaizen_board.xlsx"
file = "C:/Users/ENGINEERING-FLN1/Documents/Automation/Projects/software_ws/demo_shared_drive/kaizen_board.xlsx"

def get_my_key(obj,sorting):
    return obj[sorting]

def get_statusnj(sorting):  # noqa: E501
    """Get all status at Paterson

     # noqa: E501

    :param sorting: This is getting the suggestion status with sorting order
    :type sorting: str

    :rtype: List[StatusInfo]
    """
    df = pd.read_excel(file, sheet_name='NJ')

    result = df.to_json(orient="records")
    df_json = json.loads(result)

    for i in range(len(df_json)):
        df_json[i]["ticket_num"] = df_json[i].pop("Ticket Number")
        df_json[i]["suggestion"] = df_json[i].pop("Suggestion")
        df_json[i]["req_person"] = df_json[i].pop("Requested person")
        df_json[i]["res_person"] = df_json[i].pop("Responsible person")
        df_json[i]["status"] = df_json[i].pop("Status")
        df_json[i]["urgency"] = df_json[i].pop("Urgency")
        try:
            timestamp = df_json[i]["Date added"]/1000
            date = datetime.fromtimestamp(timestamp)
            df_json[i]["date_added"] = date.strftime("%m/%d/%Y")
            df_json[i].pop("Date added")
            logger.debug(type(df_json[i]["date_added"]))
        except:
            logger.debug("This is not a timestamp")
    logger.debug(df_json)
    # df_json.sort(key=get_my_key(sorting))
    if sorting == "urgency":
        return_json = sorted(df_json,key=lambda i:i[sorting], reverse=True)
    else:
        return_json = sorted(df_json,key=lambda i:i[sorting])
    return return_json

