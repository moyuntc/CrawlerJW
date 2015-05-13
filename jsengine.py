from config import *
import subprocess
import sys

#filename = "cached/"+sys.argv[1]
def read_web(url):
    try:
        phantom_call = PHANTOM_JS_BIN+"./phantomjs"
        jsengine = "jsengine.js"
        final_call = phantom_call+" "+jsengine+" "+url
        #subprocess.call(final_call,shell=True)
        p = subprocess.Popen(final_call,shell=True,stdout=subprocess.PIPE).communicate()[0]
        return p
    except:
        return "ERROR"
