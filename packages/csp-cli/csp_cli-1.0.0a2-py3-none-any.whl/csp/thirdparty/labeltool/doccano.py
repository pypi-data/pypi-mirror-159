#!/usr/bin/env python
# encoding: utf-8
"""
# @Time    : 2022/7/05 08:52
# @Author  : liny
# @Site    :
# @File    : doccano.py
# @Software: IDEA
# @python version: 3.7.4
"""
from csp.common.docker_server import DockerServer

class doccano:
    # 镜像版本号，默认值
    def_version = "1.0"
    # 镜像容器端口，默认值
    def_port = "8000"
    # 镜像容器内端口，默认值
    def_c_port = "8000"
    # 镜像名称，默认值
    def_name = "doccano"
    # 镜像启动参数，默认值
    def_username = "admin"
    def_email = "admin@example.com"
    def_password = "admin"

    def __init__(self, version=None, port=None, name=None, c_port=None, c_name=None, reload=True, d_username=None, d_email=None, d_password=None):
        self.version = self.def_version
        self.port = self.def_port
        self.name = self.def_name
        self.c_port = self.def_c_port
        self.d_username = self.def_username
        self.d_email = self.def_email
        self.d_password = self.def_password

        if version:
            self.version = version
        if port:
            self.port = port
        if name:
            self.name = name
        if c_port:
            self.c_port = c_port
        if d_username:
            self.d_username = d_username
        if d_email:
            self.d_email = d_email
        if d_password:
            self.d_password = d_password

        self.c_param = '-e "ADMIN_USERNAME=' + self.d_username + '" -e "ADMIN_EMAIL=' + self.d_email + '" -e "ADMIN_PASSWORD=' + self.d_password + '"'
        self.server = DockerServer(name=self.name, version=self.version, port=self.port, c_name=c_name, c_param=self.c_param, c_port=self.c_port, reload=reload)
        #self.server.start()

    def start(self):
        self.server.start()
        print("==============doccano==============")
        print("http://127.0.0.1:" + self.port)
        print("username:" + self.d_username)
        print("password:" + self.d_password)
        print("==============end==================")

    def stop(self):
        self.server.stop();

if __name__ == '__main__':
    print("start doccano")
    doccano = doccano()
    #doccano.start()
    doccano.stop()