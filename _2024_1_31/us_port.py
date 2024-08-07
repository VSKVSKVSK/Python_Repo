# -*- coding: utf-8 -*-
from core.genservice import GenService, CallHandler
import requests
import json
##############################################################################
# Constants and Variables and Classes
# 服务挂载http://111.231.32.99:8008/service/load
##############################################################################

class Service(GenService):
    # 成员列表
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.port_list = list(range(8190, 8200))

    @CallHandler.route("/port/available")
    def _available(self, data:dict):
        sql_statement = "select port from instance;"
        used = self.sql_run(sql_statement, True)
        for used_port in used:
            if used_port["port"] in self.port_list:
                self.port_list.remove(used_port["port"])
        return self.port_list
        
    def sql_run(self, sql:str, is_query:bool):
        response = requests.post(
            url="http://localhost:8050/sql/run",
            json={"sql":sql, "is_query":is_query},
            headers={"Content-Type":"application/json"}
        )
        return json.loads(response.text)

    @CallHandler.route("/port/list")
    def _list(self, data:dict):
        return self.port_list
    
    @CallHandler.route("/port/push")
    def _push(self, data:dict):
        # 检查data字典是否具有port字段
        if not "port" in data:
            return False
        # 端口存在则归还失败
        port = data["port"]
        if port in self.port_list:
            return False
        # 否则归还成功
        else:
            self.port_list.append(port)
            return True

    # 索要端口号，空参数默认返回port_list第一个端口号，若需要特定端口号可指定
    @CallHandler.route("/port/pop")
    def _pop(self, data:dict):
        # 如果可用端口为空，返回0
        if len(self.port_list) == 0:
            return 0
        # 1. 默认空参数返回第一个可用端口
        if not "port" in data:
            port = self.port_list[0]
            self.port_list.pop(0)
            return port
        # 2. 指定端口索要
        else:
            port = data["port"]
            if port in self.port_list:
                self.port_list.remove(port)
                return port
            else:
                # 索取端口不存在，返回0
                return 0
        