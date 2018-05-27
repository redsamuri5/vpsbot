# -*- coding: utf-8 -*-

import ASUL
from ASUL.lib.curve.ttypes import *
from datetime import datetime
# https://kaijento.github.io/2017/05/19/web-scraping-youtube.com/
import time,random,sys,json,codecs,threading,glob,requests,urllib

cl = ASUL.LINE()
cl.login(qr=True)
#cl.login(token="Ekvgz2Nht8TZmlZCyP6.xxD+zgW3gaYtM/L6PqLWLG.66vfknBfN3kwpXVAYkzt2QRuS+qMx+vXyqJUk4rNONE=")
cl.loginResult()

print u"login success"
reload(sys)
sys.setdefaultencoding('utf-8')

KAC=[cl]
mid = cl.getProfile().mid
admsa = "ua1cb6e845fe8f2646fe8a5c5911841fa"
admin = "ua1cb6e845fe8f2646fe8a5c5911841fa"

            elif msg.text in ["Mention","แทค"]:
                group = cl.getGroup(msg.to)
                k = len(group.members)//100
                for j in xrange(k+1):
                    msg = Message(to=msg.to)
                    txt = u''
                    s=0
                    d=[]
                    for i in group.members[j*100 : (j+1)*100]:
                        d.append({"S":str(s), "E" :str(s+8), "M":i.mid})
                        s += 9
                        txt += u'@Krampus\n'
                    msg.text = txt
                    msg.contentMetadata = {u'MENTION':json.dumps({"MENTIONEES":d})}
                    cl.sendMessage(msg) 
