#!/usr/bin/env python
# encoding: utf-8
"""
# @Time    : 2022/7/05 08:52
# @Author  : liny
# @Site    :
# @File    : labeltool_cli.py
# @Software: IDEA
# @python version: 3.7.4
"""
import click,os,zipfile
from csp.command.cli import csptools
from csp.thirdparty import doccano
from csp.thirdparty import DoccanoClient
# from urllib.parse import urljoin

# 一级命令 CSP ocr
@csptools.group("labeltool")
def labeltool():
    """
    csp labeltool Command line
    """

def doccano_init(url,username,password):   
    # path = 'luotuofeile'
    # URL_PATH = urljoin(url,path) 
    doccano_client = DoccanoClient(
        url,
        username,
        password
    ) 
    return doccano_client

def get_project_id(doccano_client,project_name):
    project_list = doccano_client.get_project_list() 
    for project in project_list['results']:
        if project_name == project['name']:
            return project['id']
    return -1

## doccano启动
@labeltool.command()
@click.option("-v", "--version", help="the version of server images", default=None)
@click.option("-p", "--port", help="the port for server container", default=None)
@click.option("-c", "--c_name", help="the container name", default=None)
@click.option('-r', is_flag=True, help="Re query image information.Indicates true when it appears")
@click.option("-u", "--username", help="The administrator account in doccano project is admin by default", default=None)
@click.option("-e", "--email", help="The contact mailbox of the administrator in doccano project, which defaults to admin@example.com", default=None)
@click.option("-p", "--password", help="The administrator login password in doccano project is password by default", default=None)
def doccano_start(version, port, c_name, r, username, email, password):
    client = doccano(version=version, port=port, c_name=c_name, reload=r, d_username=username, d_email=email, d_password=password);
    client.start()

## doccano停止
@labeltool.command()
@click.option("-v", "--version", help="the version of server images", default=None)
@click.option("-p", "--port", help="the port for server container", default=None)
@click.option("-c", "--c_name", help="the container name", default=None)
def doccano_stop(version, port, c_name):
    client = doccano(version=version, port=port, c_name=c_name);
    client.stop()

@labeltool.command() 
@click.option("--url","-u", help="doccano url eg.http://192.168.18.25:8001", default="http://192.168.18.25:8001",type=str) 
@click.option("--username","-u", help="doccano username eg.admin", default="admin",type=str) 
@click.option("--password","-p", help="doccano password eg.password", default="password",type=str)
@click.option("--data_dir","-d", help="doccano file path eg.data/", default="data/",type=str)
@click.option("--file_name","-f", help="doccano filename eg.doccano_ext.json", default="doccano_ext.json",type=str)
@click.option("--project_type","-p", help="project type eg.SequenceLabeling", default="SequenceLabeling",type=str)
@click.option("--project_name","-n", help="project name eg.test", default="test",type=str) 
def doccano_import(url,username,password,data_dir,file_name,project_type,project_name):
    '''
    doccano 三元组标注数据导入
    '''
    doccano_client = doccano_init(url,username,password)
    project_id = get_project_id(doccano_client,project_name)
    if project_id >= 0 :
        doccano_client.delete_project(project_id) 
    
    doccano_client.create_project(project_name, project_name, project_type)
    
    project_id = get_project_id(doccano_client,project_name)
    rs = doccano_client.post_doc_upload(project_id,file_name, data_dir)
    print(rs)   
    
@labeltool.command() 
@click.option("--url","-u", help="doccano url eg.192.168.18.25:8001", default="192.168.18.25:8001",type=str) 
@click.option("--username","-u", help="doccano username eg.admin", default="admin",type=str) 
@click.option("--password","-p", help="doccano password eg.password", default="password",type=str) 
@click.option("--project_name","-n", help="project name eg.test", default="test",type=str)
@click.option("--output_dir","-o", help="output dir eg.data/uie", default="data/uie",type=str)  
def doccano_export(url,username,password,project_name,output_dir):
    '''
    doccano 三元组标注数据导出
    '''
    doccano_client = doccano_init(url,username,password)
    project_id = get_project_id(project_name)
    if project_id >=0 : 
        result = doccano_client.get_doc_download(project_id)  
        output_file = os.path.join(output_dir,f'{project_id}.zip') 
        with open(output_file, 'wb') as f:
            for chunk in result.iter_content(chunk_size=8192): 
                f.write(chunk) 
        
        zfile = zipfile.ZipFile(output_file,'r') 
        for filename in zfile.namelist():  
            data = zfile.read(filename) 
            file = open(os.path.join(output_dir,filename), 'w+b') 
            file.write(data) 
            file.close() 
        print('output_file:',output_file)