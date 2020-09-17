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

file = "/usr/src/app/doc/demo.xlsx"
def get_statusnj():  # noqa: E501
    """Get all status at Paterson

     # noqa: E501


    :rtype: List[StatusInfo]
    """

    # file = "C:/Users/ENGINEERING-FLN1/Documents/Automation/Projects/software_ws/demo_shared_drive/demo.xlsx"
    
    df = pd.read_excel(file, sheet_name='NJ')

    result = df.to_json(orient="records")
    df_json = json.loads(result)

    for i in range(len(df_json)):
        try:
            timestamp = df_json[i]["Due"]/1000
            df_json[i]["Due"] = datetime.fromtimestamp(timestamp).isoformat()
        except:
            logger.debug("This is not a timestamp")
    logger.debug(df_json)
    return df_json


def get_statusva():  # noqa: E501
    """Get all status at Richmond

     # noqa: E501


    :rtype: List[StatusInfo]
    """
    
    df = pd.read_excel(file, sheet_name='VA')
    result = df.to_json(orient="records")
    df_json = json.loads(result)

    for i in range(len(df_json)):
        try:
            timestamp = df_json[i]["Due"]/1000
            df_json[i]["Due"] = datetime.fromtimestamp(timestamp).isoformat()
        except:
            logger.debug("This is not a timestamp")
    logger.debug(df_json)
    return df_json

