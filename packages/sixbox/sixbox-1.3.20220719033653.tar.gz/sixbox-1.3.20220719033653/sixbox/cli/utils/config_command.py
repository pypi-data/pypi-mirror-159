
import os, sys,io
from ruamel import yaml
import json
import uuid
from cwltool import main

import psutil
from .logger import log
from multiprocessing import Process, Lock

import time



###################################
# config相关
##################################




def read_channel():
    """
    获取config.yaml中的channel
    """
    config_path = os.environ['HOME'] + '/.sixbox/config.yaml'
    initialize_config()
    try:
        with open(config_path, encoding='utf-8') as f: # 读取config文件中的libPath
            content = yaml.load(f, Loader= yaml.RoundTripLoader)
            return content['channel']
    except:
        log.error("Your configuration is incorrect, run folowing command to the configuration:\n\tsixbox config info \n\t and set it up with command:\n\t sixbox config set ")
        sys.exit()


def getConfig():
    """
    读取config文件
    """
    config_path = os.environ['HOME'] + '/.sixbox/config.yaml'
    initialize_config()
    try:
        with open(config_path, encoding='utf-8') as f: 
            content = yaml.load(f, Loader= yaml.RoundTripLoader)
            return content
    except:
        log.error("Your configuration is incorrect, run folowing command to the configuration:\n\tsixbox config info \n\t and set it up with command:\n\t sixbox config set ")
        sys.exit()

def setConfig(config):
    """
    配置config文件
    """
    config_path = os.environ['HOME'] + '/.sixbox/config.yaml'

    try:
        with open(config_path, 'w', encoding="utf-8") as nf:
            yaml.dump(config, nf, Dumper= yaml.RoundTripDumper)
    except:
        log.error("Your configuration is incorrect, run folowing command to the configuration:\n\tsixbox config info \n\t and set it up with command:\n\t sixbox config set ")
        sys.exit()


def initialize_config():
    """
    初始化config.yaml
    
    """
    # TODO:  config 添加一个配置，用于指定其它路径的配置（比如当前用户支持使用其他用户安装的sixbox并调用CWLdb内的应用）
    config_path = os.environ['HOME'] + '/.sixbox/config.yaml'

    if os.path.exists(config_path):
        pass
        
    else:
        log.warning("Config.yaml for sixbox  could not be found, we are trying to initialize ... ")
        
        content = {
            'libPath': os.path.join(os.environ['HOME'], '.sixbox', 'lib'),
            'channel': 'https://www.sixoclock.net/api',
            'token': 'Fill in your token here'
        }
        
        os.makedirs(os.path.dirname(config_path), exist_ok=True)
        os.makedirs(content['libPath'], exist_ok=True)
        with open(config_path, 'w', encoding="utf-8") as nf:
            yaml.dump(content, nf, Dumper= yaml.RoundTripDumper)


# 默认导入配置
Config = getConfig()