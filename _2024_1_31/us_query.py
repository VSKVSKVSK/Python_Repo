# -*- coding: utf-8 -*-
from core.genservice import GenService, CallHandler
import requests
import json
##############################################################################
# Constants and Variables and Classes
# 服务挂载http://111.231.32.99:8008/service/load
##############################################################################

class Service(GenService):
    @CallHandler.route("/sql/query")
    def _query(self, data:dict):
        table = data["table"]
        sql_statement = "select * from {};".format(table)
        body = self.sql_run(sql_statement, True)
        return body
    
    def sql_run(self, sql:str, is_query: bool):
        response = requests.post(
            url="http://localhost:8050/sql/run",
            json={"sql":sql, "is_query":is_query},
            headers={"Content-Type":"application/json"}
        )
        return json.loads(response.text)