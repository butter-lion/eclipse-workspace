'''
Created on 2018年5月6日

@author: zhang
'''
import os,sys    
from core.main import run_server
from core import data

BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_PATH)

run_server()