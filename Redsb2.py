# -*- coding: utf-8 -*-
#redsamuri_Bot

import LINETCR
from LINETCR.lib.curve.ttypes import *
from datetime import datetime
from bs4 import BeautifulSoup
from threading import Thread
from googletrans import Translator
from gtts import gTTS
import time,random,sys,json,codecs,threading,glob,urllib,urllib2,urllib3,re,ast,os,subprocess,requests,tempfile

red = LINETCR.LINE()
red.login(token="EqbIkEGCAaTD0x9A6XO6.Lkg8ohUsFOz1yZrKJtfpHG.3h8BTM8ZNTrqucTDvmH+NqaBWswPi5cYHwGBDeShZ8g=")
red.loginResult()
print "\n=====[redbot Login]====="

reload(sys)
sys.setdefaultencoding('utf-8')


selfMessage ="""
╔═════════════════════════
║            ☆☞ S E L F ☜☆
╠═════════════════════════
╠➩〘Hi〙
╠➩〘Me〙
╠➩〘Mymid〙
╠➩〘Mid @〙
╠➩〘SearchID: (ID LINE)〙
╠➩〘Checkdate (DD/MM/YY)〙
╠➩〘Kalender〙
╠➩〘Steal contact〙
╠➩〘Pp @〙
╠➩〘Cover @〙
╠➩〘Auto like〙
╠➩〘Scbc Text〙
╠➩〘Cbc Text〙
╠➩〘Gbc Text〙
╠➩〘Getbio @〙
╠➩〘Getinfo @〙
╠➩〘Getname @〙
╠➩〘Getprofile @〙
╠➩〘Getcontact @〙
╠➩〘Getvid @〙
╠➩〘Friendlist〙
╠➩〘Micadd @〙
╠➩〘Micdel @〙
╠➩〘Miclist〙
╠═════════════════════════
║                 🚩By : Ŕèď 🚩
║    ✴ line.me/ti/p/~samuri5✴
╚═════════════════════════
"""

botMessage ="""
╔═════════════════════════
║             ☆☞ B O T ☜☆
╠═════════════════════════
╠➩〘Absen〙
╠➩〘Respon〙
╠➩〘Runtime〙
╠➩〘Mycopy @〙
╠➩〘Copycontact〙
╠➩〘Mybackup〙
╠➩〘Mybio (Text)〙
╠➩〘Myname (Text)〙
╠➩〘@bye〙
╠➩〘บาย〙
╠➩〘หา...〙
╠➩〘เงียบ〙
╠➩〘Bot on/off〙
╠═════════════════════════
║             🚩By : Ŕèď 🚩
║    ✴ line.me/ti/p/~samuri5✴
╚═════════════════════════
"""

mediaMessage ="""
╔═════════════════════════
║           ☆☞ M E D I A ☜☆
╠═════════════════════════
╠➩〘Gift〙
╠➩〘Gift1 @ s/d Gift10 @〙
╠➩〘Giftbycontact〙
╠➩〘Gif gore〙
╠➩〘Google: (Text)〙
╠➩〘Playstore NamaApp〙
╠➩〘Fancytext: Text〙
╠➩〘/musik Judul-Penyanyi〙
╠➩〘/lirik Judul-Penyanyi〙
╠➩〘/musrik Judul-Penyanyi〙
╠➩〘/ig UrsnameInstagram〙
╠➩〘Checkig UrsnameInstagram〙
╠➩〘/apakah Text (Kerang Ajaib)〙
╠➩〘/kapan Text (Kerang Ajaib)〙
╠➩〘/hari Text (Kerang Ajaib)〙
╠➩〘/berapa Text (Kerang Ajaib)〙
╠➩〘/berapakah Text〙
╠➩〘Youtubelink: Judul Video〙
╠➩〘Youtubevideo: Judul Video〙
╠➩〘Youtubesearch: Judul Video〙
╠➩〘Image NamaGambar〙
╠➩〘Say-id Text〙
╠➩〘Say-en Text〙
╠➩〘Say-jp Text〙
╠➩〘Image NamaGambar〙
╠➩〘Tr-id Text (Translate En Ke ID〙
╠➩〘Tr-en Text (Translate ID Ke En〙
╠➩〘Tr-th Text (Translate ID Ke Th〙
╠➩〘Id@en Text (Translate ID Ke En〙
╠➩〘Id@th Text (Translate ID Ke TH〙
╠➩〘En@id Text (Translate En Ke ID〙
╠═════════════════════════
║             🚩By : Ŕèď 🚩
║    ✴ line.me/ti/p/~samuri5✴
╚═════════════════════════
"""

groupMessage ="""
╔═════════════════════════
║           ☆☞ G R O U P ☜☆
╠═════════════════════════
╠➩〘Welcome〙
╠➩〘Say welcome〙
╠➩〘Invite creator〙
╠➩〘Setview〙
╠➩〘Viewseen〙
╠➩〘Gn: (NamaGroup)〙
╠➩〘Tag all〙
╠➩〘Recover〙
╠➩〘Cancel〙
╠➩〘Cancelall〙
╠➩〘Gcreator〙
╠➩〘Ginfo〙
╠➩〘Gurl〙
╠➩〘List group〙
╠➩〘Pict group: (NamaGroup)〙
╠➩〘Spam: (Text)〙
╠➩〘Add all〙
╠➩〘Kick: (Mid)〙
╠➩〘Invite: (Mid)〙
╠➩〘Invite〙
╠➩〘Memlist〙
╠➩〘Getgroup image〙
╠➩〘Urlgroup Image〙
╠═════════════════════════
║             🚩By : Ŕèď 🚩
║    ✴ line.me/ti/p/~samuri5✴
╚═════════════════════════
"""
jia = "ub5abe828cd964292195c3c59d6322033"

setMessage ="""
╔═════════════════════════
║              ☆☞ S E T ☜☆
╠═════════════════════════
╠➩〘Sambutan on/off〙
╠➩〘Mimic on/off〙
╠➩〘Url on/off〙
╠➩〘Alwaysread on/off〙
╠➩〘Sider on/off〙
╠➩〘Contact on/off〙
╠➩〘Sticker on〙
╠➩〘Simisimi on/off〙
╠═════════════════════════
║             🚩By : Ŕèď 🚩
║    ✴ line.me/ti/p/~samuri5✴
╚═════════════════════════
"""

creatorMessage ="""
╔═════════════════════════
║         ☆☞ C R E A T O R ☜☆
╠═════════════════════════
╠➩〘Crash〙
╠➩〘Kickall〙
╠➩〘Bc: (Text)〙
╠➩〘Join group: (NamaGroup〙
╠➩〘Leave group: (NamaGroup〙
╠➩〘Leave all group〙
╠➩〘Tag on/off〙
╠➩〘Bot restart〙
╠➩〘Turn off〙
╠═════════════════════════
║             🚩By : Ŕèď 🚩
║    ✴ line.me/ti/p/~samuri5✴
╚═════════════════════════
"""

adminMessage ="""
╔═════════════════════════
║            ☆☞ A D M I N ☜☆
╠═════════════════════════
╠➩〘Allprotect on/off〙
╠➩〘Ban〙
╠➩〘Unban〙
╠➩〘Ban @〙
╠➩〘Unban @〙
╠➩〘Ban list〙
╠➩〘Clear ban〙
╠➩〘Kill〙
╠➩〘Kick @〙
╠➩〘Set member: (Jumblah)〙
╠➩〘Ban group: (NamaGroup〙
╠➩〘Del ban: (NamaGroup〙
╠➩〘List ban〙
╠➩〘Kill ban〙
╠➩〘Glist〙
╠➩〘Glistmid〙
╠➩〘Details group: (Gid)〙
╠➩〘Cancel invite: (Gid)〙
╠➩〘Invitemeto: (Gid)〙
╠➩〘Acc invite〙
╠➩〘Removechat〙
╠➩〘Qr on/off〙
╠➩〘Autokick on/off〙
╠➩〘Autocancel on/off〙
╠➩〘Invitepro on/off〙
╠➩〘Join on/off〙
╠➩〘Joincancel on/off〙
╠➩〘Respon1 on/off〙
╠➩〘Respon2 on/off〙
╠➩〘Respon3 on/off〙
╠➩〘Responkick on/off〙
╠═════════════════════════
║             🚩By : Ŕèď 🚩
║    ✴ line.me/ti/p/~samuri5✴
╚═════════════════════════
"""

helpMessage ="""
╔═════════════════════════
║              ☆☞ H E L P ☜☆
╠═════════════════════════
╠➩〘Help self〙
╠➩〘Help bot〙
╠➩〘Help group〙
╠➩〘Help set〙
╠➩〘Help media〙
╠➩〘Help admin〙
╠➩〘Help creator〙
╠➩〘Owner〙
╠➩〘Pap owner〙
╠➩〘Speed〙
╠➩〘Speed test〙
╠➩〘Status〙
╠═════════════════════════
║             🚩By : Ŕèď 🚩
║    ✴ line.me/ti/p/~samuri5✴
╚═════════════════════════
"""


KAC=[red]
mid = red.getProfile().mid
Bots=[mid,"u94a1bc387b927e86756334648d314f86","u5b35c9714ca359616335efed888537a8","ube52b8931eee2e15a1b689377e3e5637","u1aedef8b888ae108d96bacbc5054e679","u99cde2e2a4a4b11bfd4cc418913e8986","u1865fbab05ea885ca7bd481ec35c9a1d","u46a050ebcc66a90b47fae6256547cc53","u656b0ca994a1c9b462f9feb6f5ae3177","ub5abe828cd964292195c3c59d6322033"]
Creator=["u94a1bc387b927e86756334648d314f86","u5b35c9714ca359616335efed888537a8","ube52b8931eee2e15a1b689377e3e5637","u1aedef8b888ae108d96bacbc5054e679","u99cde2e2a4a4b11bfd4cc418913e8986","u1865fbab05ea885ca7bd481ec35c9a1d","u46a050ebcc66a90b47fae6256547cc53","u656b0ca994a1c9b462f9feb6f5ae3177","ub5abe828cd964292195c3c59d6322033"]
admin=["u685f98d0edab398bbbc0bcfdf0a33be1","u94a1bc387b927e86756334648d314f86","u5b35c9714ca359616335efed888537a8","ube52b8931eee2e15a1b689377e3e5637","u1aedef8b888ae108d96bacbc5054e679","u99cde2e2a4a4b11bfd4cc418913e8986","u1865fbab05ea885ca7bd481ec35c9a1d","u46a050ebcc66a90b47fae6256547cc53","u656b0ca994a1c9b462f9feb6f5ae3177","ub5abe828cd964292195c3c59d6322033","uc360193fd87f05f352673cadbd9f2947","u3a737b8dc7135de09ceb6741c46d709f","ub2a4ba24b217b1bd64336a8a8cca11a1","uecdd917f87c7a68b90fe3055cd79fb48","ub4aee366a1b1607f7201b788843f1876"]

contact = red.getProfile()
backup1 = red.getProfile()
backup1.displayName = contact.displayName
backup1.statusMessage = contact.statusMessage                        
backup1.pictureStatus = contact.pictureStatus

responsename = red.getProfile().displayName


wait = {
    "LeaveRoom":True,
    "Bot":True,
    "AutoJoin":False,
    "AutoJoinCancel":False,
    "memberscancel":30,
    "Members":1,
    "AutoCancel":False,
    "AutoKick":False,
    'pap':{},
    'invite':{},
    'steal':{},
    'gift':{},
    'copy':{},    
    'likeOn':{},
    'detectMention':False,
    'detectMention2':True,
    'detectMention3':False,
    'kickMention':False,  
    'sticker':False,  
    'timeline':True,
    "Timeline":True,
    "comment":"Bot Auto Like ©By : Ŕèď\nContact Me : 👉 line.me/ti/p/~samuri5.",    
    "commentOn":True,
    "commentBlack":{},
    "message":"Thx For Add Me (^_^)\nInvite Me To Your Group ヘ(^_^)ヘ",    
    "blacklist":{},
    "wblacklist":False,
    "dblacklist":False,
    "Qr":False,
    "Contact":False,
    "Sambutan":False,
    "inviteprotect":False,    
    "alwaysRead":False,    
    "Sider":{},
    "Simi":{},    
    "lang":"JP",
    "BlGroup":{}
}

settings = {
    "simiSimi":{}
    }
    
cctv = {
    "cyduk":{},
    "point":{},
    "sidermem":{}
}    

wait2 = {
    "readPoint":{},
    "readMember":{},
    "setTime":{},
    "ROM":{}
    }
    
mimic = {
    "copy":False,
    "copy2":False,
    "status":False,
    "target":{}
    }    

setTime = {}
setTime = wait2['setTime']
mulai = time.time() 

def download_page(url):
    version = (3,0)
    cur_version = sys.version_info
    if cur_version >= version:     
        import urllib,request    
        try:
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
            req = urllib,request.Request(url, headers = headers)
            resp = urllib,request.urlopen(req)
            respData = str(resp.read())
            return respData
        except Exception as e:
            print(str(e))
    else:                        
        import urllib2
        try:
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
            req = urllib2.Request(url, headers = headers)
            response = urllib2.urlopen(req)
            page = response.read()
            return page
        except:
            return"Page Not found"


def _images_get_next_item(s):
    start_line = s.find('rg_di')
    if start_line == -1:    
        end_quote = 0
        link = "no_links"
        return link, end_quote
    else:
        start_line = s.find('"class="rg_meta"')
        start_content = s.find('"ou"',start_line+90)
        end_content = s.find(',"ow"',start_content-90)
        content_raw = str(s[start_content+6:end_content-1])
        return content_raw, end_content


def _images_get_all_items(page):
    items = []
    while True:
        item, end_content = _images_get_next_item(page)
        if item == "no_links":
            break
        else:
            items.append(item)      
            time.sleep(0.1)        
            page = page[end_content:]
    return items
    
def waktu(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    return '%02d Jam %02d Menit %02d Detik' % (hours, mins, secs)      
    
def cms(string, commands): #/XXX, >XXX, ;XXX, ^XXX, %XXX, $XXX...
    tex = ["+","@","/",">",";","^","%","$","＾","サテラ:","サテラ:","サテラ：","サテラ："]
    for texX in tex:
        for command in commands:
            if string ==command:
                return True
    return False    

def upload_tempimage(client):
     '''
         Upload a picture of a kitten. We don't ship one, so get creative!
     '''
     config = {
         'album': album,
         'name':  'bot auto upload',
         'title': 'bot auto upload',
         'description': 'bot auto upload'
     }

     print("Uploading image... ")
     image = client.upload_from_path(image_path, config=config, anon=False)
     print("Done")
     print()

     return image
     
def sendAudio(self, to_, path):
       M = Message()
       M.text = None
       M.to = to_
       M.contentMetadata = None
       M.contentPreview = None
       M.contentType = 3
       M_id = self._client.sendMessage(0,M).id
       files = {
             'file': open(path,  'rb'),
       }
    
def sendMessage(to, text, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes.from_ = to, profile.mid
    mes.text = text
    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1
    
def sendImage(self, to_, path):
      M = Message(to=to_, text=None, contentType = 1)
      M.contentMetadata = None
      M.contentPreview = None
      M2 = self._client.sendMessage(0,M)
      M_id = M2.id
      files = {
         'file': open(path, 'rb'),
      }
      params = {
         'name': 'media',
         'oid': M_id,
         'size': len(open(path, 'rb').read()),
         'type': 'image',
         'ver': '1.0',
      }
      data = {
         'params': json.dumps(params)
      }
      r = self.post_content('https://obs-sg.line-apps.com/talk/m/upload.nhn', data=data, files=files)
      if r.status_code != 201:
         raise Exception('Upload image failure.')
      return True


def sendImageWithURL(self, to_, url):
      path = '%s/pythonLine-%i.data' % (tempfile.gettempdir(), randint(0, 9))
      r = requests.get(url, stream=True)
      if r.status_code == 200:
         with open(path, 'w') as f:
            shutil.copyfileobj(r.raw, f)
      else:
         raise Exception('Download image failure.')
      try:
         self.sendImage(to_, path)
      except:
         try:
            self.sendImage(to_, path)
         except Exception as e:
            raise e

def sendAudioWithURL(self, to_, url):
        path = self.downloadFileWithURL(url)
        try:
            self.sendAudio(to_, path)
        except Exception as e:
            raise Exception(e)

def sendAudioWithUrl(self, to_, url):
        path = '%s/pythonLine-%1.data' % (tempfile.gettempdir(), randint(0, 9))
        r = requests.get(url, stream=True, verify=False)
        if r.status_code == 200:
           with open(path, 'w') as f:
              shutil.copyfileobj(r.raw, f)
        else:
           raise Exception('Download audio failure.')
        try:
            self.sendAudio(to_, path)
        except Exception as e:
            raise e
            
def downloadFileWithURL(self, fileUrl):
        saveAs = '%s/pythonLine-%i.data' % (tempfile.gettempdir(), randint(0, 9))
        r = self.get_content(fileUrl)
        if r.status_code == 200:
            with open(saveAs, 'wb') as f:
                shutil.copyfileobj(r.raw, f)
            return saveAs
        else:
            raise Exception('Download file failure.')
            
def summon(to, nama):
    aa = ""
    bb = ""
    strt = int(14)
    akh = int(14)
    nm = nama
    for mm in nm:
      akh = akh + 2
      aa += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(mm)+"},"""
      strt = strt + 6
      akh = akh + 4
      bb += "\xe2\x95\xa0 @x \n"
    aa = (aa[:int(len(aa)-1)])
    msg = Message()
    msg.to = to
    msg.text = "\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\n"+bb+"\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90"
    msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+aa+']}','EMTVER':'4'}
    print "[Command] Tag All"
    try:
       red.sendMessage(msg)
    except Exception as error:
       print error          
                        
       

def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)


def bot(op):
    try:

        if op.type == 0:
            return

        if op.type == 5:
           if wait["autoAdd"] == True:
              red.findAndAddContactsByMid(op.param1)
              if(wait["message"]in[""," ","\n",None]):
                pass
              else:
                red.sendText(op.param1,str(wait["message"]))


        if op.type == 55:
	    try:
	      group_id = op.param1
	      user_id=op.param2
	      subprocess.Popen('echo "'+ user_id+'|'+str(op.createdTime)+'" >> dataSeen/%s.txt' % group_id, shell=True, stdout=subprocess.PIPE, )
	    except Exception as e:
	      print e
	      
        if op.type == 55:
                try:
                    if cctv['cyduk'][op.param1]==True:
                        if op.param1 in cctv['point']:
                            Name = nadya.getContact(op.param2).displayName
#                            Name = summon(op.param2)
                            if Name in cctv['sidermem'][op.param1]:
                                pass
                            else:
                                cctv['sidermem'][op.param1] += "\n• " + Name
                                if " " in Name:
                                    nick = Name.split(' ')
                                    if len(nick) == 2:
                                        red.sendText(op.param1, "Haii " + "☞ " + Name + " ☜" + "\nแอบกันตำมอย. . .\nออกมาคุยบ้างจิ (-__-)   ")
                                        time.sleep(0.2)
                                        summon(op.param1,[op.param2])
                                    else:
                                        red.sendText(op.param1, "Haii " + "☞ " + Name + " ☜" + "\nนี่กะอีกคนอ่านอย่างเดียว. . .\nคุยคับคุย (-__-)   ")
                                        time.sleep(0.2)
                                        summon(op.param1,[op.param2])
                                else:
                                    red.sendText(op.param1, "Haii " + "☞ " + Name + " ☜" + "\nคือหยังบ่ออกมาเว้ากันละ???\nห้วย...   ")
                                    time.sleep(0.2)
                                    summon(op.param1,[op.param2])
                        else:
                            pass
                    else:
                        pass
                except:
                    pass

        else:
            pass    	      
	      

        if op.type == 22:
            red.leaveRoom(op.param1)

        if op.type == 21:
            red.leaveRoom(op.param1)


        if op.type == 13:
	    print op.param3
            if op.param3 in mid:
		if op.param2 in Creator:
		    red.acceptGroupInvitation(op.param1)

		    
	    if mid in op.param3:	        
                if wait["AutoJoinCancel"] == True:
		    G = red.getGroup(op.param1)
                    if len(G.members) <= wait["memberscancel"]:
                        red.acceptGroupInvitation(op.param1)
                        red.sendText(op.param1,"Maaf " + red.getContact(op.param2).displayName + "\nMember Kurang Dari 30 Orang\nUntuk Info, เป็นคำสั่งสำหรับ Owner นะต็ะ!!")
                        red.leaveGroup(op.param1)                        
		    else:
                        red.acceptGroupInvitation(op.param1)
			red.sendText(op.param1,"☆ใช้คำสั่งนี้ ☞Help☜ ในการเรียกดูคำสั่งทั้งหมด☆\n☆ขอบคุณที่เชิญเข้ากลุ่มคับ ^_^ ☆")
                        		    
 
	    if mid in op.param3:
                if wait["AutoJoin"] == True:
		    G = red.getGroup(op.param1)
                    if len(G.members) <= wait["Members"]:
                        red.rejectGroupInvitation(op.param1)
		    else:
                        red.acceptGroupInvitation(op.param1)
			red.sendText(op.param1,"☆ใช้คำสั่งนี้ ☞Help☜ ในการเรียกดูคำสั่งทั้งหมด☆\n☆ขอบคุณที่เชิญเข้ากลุ่มคับ ^_^ ☆")
	    else:
                if wait["AutoCancel"] == True:
		    if op.param3 in Bots:
			pass
		    else:
                        red.cancelGroupInvitation(op.param1, [op.param3])
		else:
		    if op.param3 in wait["blacklist"]:
			red.cancelGroupInvitation(op.param1, [op.param3])
			red.sendText(op.param1, "Blacklist Detected")
		    else:
			pass
			
        if op.type == 13:
            if op.param2 not in Creator:
             if op.param2 not in admin:
              if op.param2 not in Bots:
                if op.param2 in Creator:
                 if op.param2 in admin:
                  if op.param2 in Bots:
                    pass
                elif wait["inviteprotect"] == True:
                    wait ["blacklist"][op.param2] = True
                    red.cancelGroupInvitation(op.param1,[op.param3])
                    red.kickoutFromGroup(op.param1,[op.param2])
                    if op.param2 not in Creator:
                     if op.param2 not in admin:
                      if op.param2 not in Bots:
                        if op.param2 in Creator:
                         if op.param2 in admin:
                          if op.param2 in Bots:
                            pass

        if op.type == 19:
		if wait["AutoKick"] == True:
		    try:
			if op.param3 in Creator:
			 if op.param3 in admin:
			  if op.param3 in Bots:
			      pass
		         if op.param2 in Creator:
		          if op.param2 in admin:
		           if op.param2 in Bots:
		               pass
		           else:
		               red.kickoutFromGroup(op.param1,[op.param2])
		               if op.param2 in wait["blacklist"]:
		                   pass
		        else:
			    red.inviteIntoGroup(op.param1,[op.param3])
		    except:
		        try:
			    if op.param2 not in Creator:
			        if op.param2 not in admin:
			            if op.param2 not in Bots:
                                        red.kickoutFromGroup(op.param1,[op.param2])
			    if op.param2 in wait["blacklist"]:
			        pass
			    else:
			        red.inviteIntoGroup(op.param1,[op.param3])
		        except:
			    print ("client Kick regulation or Because it does not exist in the group\ngid=["+op.param1+"]\nmid=["+op.param2+"]")
                        if op.param2 in wait["blacklist"]:
                            pass
                        else:
			    if op.param2 in Creator:
			        if op.param2 in admin:
			            if op.param2 in Bots:
			              pass
			    else:
                                wait["blacklist"][op.param2] = True
		    if op.param2 in wait["blacklist"]:
                        pass
                    else:
		        if op.param2 in Creator:
		            if op.param2 in admin:
		                if op.param2 in Bots:
			             pass
		        else:
                            wait["blacklist"][op.param2] = True
		else:
		    pass


                if mid in op.param3:
                    if op.param2 in Creator:
                      if op.param2 in Bots:
                        pass
                    try:
                        red.kickoutFromGroup(op.param1,[op.param2])
			red.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
			    red.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client Kick regulation or Because it does not exist in the group\ngid=["+op.param1+"]\nmid=["+op.param2+"]")
                        if op.param2 in wait["blacklist"]:
                            pass
                        else:
			    if op.param2 in Bots:
			        pass
                    if op.param2 in wait["blacklist"]:
                        pass
                    else:
		        if op.param2 in Bots:
			    pass
		        else:
                            wait["blacklist"][op.param2] = True

 
                if Creator in op.param3:
                  if admin in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        red.kickoutFromGroup(op.param1,[op.param2])
			red.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
			    if op.param2 not in Bots:
                                red.kickoutFromGroup(op.param1,[op.param2])
			    if op.param2 in wait["blacklist"]:
			        pass
			    else:
			        red.inviteIntoGroup(op.param1,[op.param3])
                        except:
                            print ("client Kick regulation or Because it does not exist in the group\ngid=["+op.param1+"]\nmid=["+op.param2+"]")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True
                    red.inviteIntoGroup(op.param1,[op.param3])
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True


        if op.type == 11:
            if wait["Qr"] == True:
		if op.param2 in Creator:
		 if op.param2 in admin:
		  if op.param2 in Bots:
		   pass		
		else:
                    red.kickoutFromGroup(op.param1,[op.param2])
            else:
                pass


        if op.type == 17:
          if wait["Sambutan"] == True:
            if op.param2 in Creator:
                return
            ginfo = red.getGroup(op.param1)
            contact = red.getContact(op.param2)
            image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
            red.sendText(op.param1,"Hallo " + red.getContact(op.param2).displayName + "\nWelcome To ☞ " + str(ginfo.name) + " ☜" + "\nBudayakan Cek Note\nDan Semoga Betah Disini ^_^")
            c = Message(to=op.param1, from_=None, text=None, contentType=13)
            c.contentMetadata={'mid':op.param2}
            red.sendMessage(c)  
            red.sendImageWithURL(op.param1,image)
            d = Message(to=op.param1, from_=None, text=None, contentType=7)
            d.contentMetadata={
                                    "STKID": "13269548",
                                    "STKPKGID": "1329191",
                                    "STKVER": "1" }                
            red.sendMessage(d)             
            print "MEMBER JOIN TO GROUP"

        if op.type == 15:
          if wait["Sambutan"] == True:
            if op.param2 in Creator:
                return
            red.sendText(op.param1,"Good Bye " + red.getContact(op.param2).displayName +  "\nSee You Next Time . . . (p′︵‵。) 🤗")
            d = Message(to=op.param1, from_=None, text=None, contentType=7)
            d.contentMetadata={
                                    "STKID": "13269542",
                                    "STKPKGID": "1329191",
                                    "STKVER": "1" }                
            red.sendMessage(d)                  
            print "MEMBER HAS LEFT THE GROUP"
            
        if op.type == 26:
            msg = op.message
            
            if msg.from_ in mimic["target"] and mimic["status"] == True and mimic["target"][msg.from_] == True:
                    text = msg.text
                    if text is not None:
                        red.sendText(msg.to,text)             
            
            
            if msg.to in settings["simiSimi"]:
                if settings["simiSimi"][msg.to] == True:
                    if msg.text is not None:
                        text = msg.text
                        r = requests.get("http://api.ntcorp.us/chatbot/v1/?text=" + text.replace(" ","+") + "&key=beta1.nt")
                        data = r.text
                        data = json.loads(data)
                        if data['status'] == 200:
                            if data['result']['result'] == 100:
                                red.sendText(msg.to,data['result']['response'].encode('utf-8'))

            if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["kickMention"] == True:
                     contact = red.getContact(msg.from_)
                     cName = contact.displayName
                     balas = ["กวนดีนัก" + cName + "\nสมน้ำหน้า! 555+, Byee!!!"]
                     ret_ = random.choice(balas)                     
                     name = re.findall(r'@(\w+)', msg.text)
                     mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                     mentionees = mention['MENTIONEES']
                     for mention in mentionees:
                           if mention['M'] in Bots:
                                  red.sendText(msg.to,ret_)
                                  red.kickoutFromGroup(msg.to,[msg.from_])
                                  break                              
                              
            if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["detectMention"] == True:
                     contact = red.getContact(msg.from_)
                     cName = contact.displayName
                     balas = ["Dont Tag!! Me",cName + " จะแทคทำไมมิทราบ?",cName + " แทคบ่อยๆเดะจับทำเมีย -..-","หยุดแทคสักพัก", cName + " มาพบรักที่หลังแชท?","😎😎😎\nคับ มีไรคับ " + cName, "ยังไม่ว่าง เดี๋ยวมาตอบนะ " + cName, "ไม่อยู่ ไปทำธุระ " + cName + "?", "อ่ะ เอาอีกแระ " + cName + "?","ป๊าาาด " + cName + " คุณนายคับ จะแทค, ทำไมคับ!"]
                     ret_ = random.choice(balas)
                     name = re.findall(r'@(\w+)', msg.text)
                     mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                     mentionees = mention['MENTIONEES']
                     for mention in mentionees:
                           if mention['M'] in Bots:
                                  red.sendText(msg.to,ret_)
                                  break   
                              
            if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["detectMention2"] == True:          
                    contact = red.getContact(msg.from_)
                    cName = contact.displayName
                    balas = ["แทคไม่เลิก เดะจับตีเข่า มีธุระไร ทักมาส.ต " + cName + " เข้าใจบ่!"]
                    ret_ = random.choice(balas)
                    name = re.findall(r'@(\w+)', msg.text)
                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                    mentionees = mention['MENTIONEES']
                    for mention in mentionees:
                           if mention['M'] in Bots:
                                  red.sendText(msg.to,ret_)
                                  msg.contentType = 7   
                                  msg.text = None
                                  msg.contentMetadata = {
                                                       "STKID": "20001316",
                                                       "STKPKGID": "1582380",
                                                       "STKVER": "1" }
                                  red.sendMessage(msg)                                
                                  break
                              
            if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["detectMention3"] == True:          
                    contact = red.getContact(msg.from_)
                    cName = contact.displayName
                    balas = ["อุต๊ะ " + cName + ", แทคไม่เลิก..สงสัยอยากโดน🌚!"]
                    balas1 = "เอาเบอร์ไป 0946345913. . ."
                    ret_ = random.choice(balas)
                    image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                    name = re.findall(r'@(\w+)', msg.text)
                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                    mentionees = mention['MENTIONEES']
                    for mention in mentionees:
                           if mention['M'] in Bots:
                                  red.sendText(msg.to,ret_)
                                  red.sendText(msg.to,balas1)
                                  red.sendImageWithURL(msg.to,image)
                                  msg.contentType = 7   
                                  msg.text = None
                                  msg.contentMetadata = {
                                                       "STKID": "11764508",
                                                       "STKPKGID": "6641",
                                                       "STKVER": "1" }
                                  red.sendMessage(msg)                                
                                  break  
                                  
        if op.type == 25:
            msg = op.message                                  
                              
            if msg.text in ["Bot on"]:
                wait["Bot"] = True
                red.sendText(msg.to,"เปิดระบบบอทแล้ว")  

        if op.type == 25:
          if wait["Bot"] == True:    
            msg = op.message
            
            
            if msg.contentType == 7:
              if wait["sticker"] == True:
                msg.contentType = 0
                stk_id = msg.contentMetadata['STKID']
                stk_ver = msg.contentMetadata['STKVER']
                pkg_id = msg.contentMetadata['STKPKGID']
                filler = "『 Sticker Check 』\nSTKID : %s\nSTKPKGID : %s\nSTKVER : %s\n『 Link 』\nline://shop/detail/%s" % (stk_id,pkg_id,stk_ver,pkg_id)
                red.sendText(msg.to, filler)
                wait["sticker"] = False
            else:
                pass              

            if wait["alwaysRead"] == True:
                if msg.toType == 0:
                    red.sendChatChecked(msg.from_,msg.id)
                else:
                    red.sendChatChecked(msg.to,msg.id)
                    
                    
            if msg.contentType == 16:
                if wait['likeOn'] == True:
                     url = msg.contentMetadata["postEndUrl"]
                     red.like(url[25:58], url[66:], likeType=1005)
                     red.comment(url[25:58], url[66:], wait["comment"])
                     red.sendText(msg.to,"Like Success")                     
                     wait['likeOn'] = False


            if msg.contentType == 13:
                if wait["wblacklist"] == True:
		    if msg.contentMetadata["mid"] not in admin:
                        if msg.contentMetadata["mid"] in wait["blacklist"]:
                            red.sendText(msg.to,"Sudah")
                            wait["wblacklist"] = False
                        else:
                            wait["blacklist"][msg.contentMetadata["mid"]] = True
                            wait["wblacklist"] = False
                            red.sendText(msg.to,"Ditambahkan")
		    else:
			red.sendText(msg.to,"Admin Detected~")
			

                elif wait["dblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        del wait["blacklist"][msg.contentMetadata["mid"]]
                        red.sendText(msg.to,"Terhapus")
                        wait["dblacklist"] = False

                    else:
                        wait["dblacklist"] = False
                        red.sendText(msg.to,"Tidak Ada Black List")
            
                    
 
                elif wait["Contact"] == True:
                     msg.contentType = 0
                     red.sendText(msg.to,msg.contentMetadata["mid"])
                     if 'displayName' in msg.contentMetadata:
                         contact = red.getContact(msg.contentMetadata["mid"])
                         try:
                             cu = red.channel.getCover(msg.contentMetadata["mid"])
                         except:
                             cu = ""
                         red.sendText(msg.to,"Nama:\n" + msg.contentMetadata["displayName"] + "\n\nMid:\n" + msg.contentMetadata["mid"] + "\n\nStatus:\n" + contact.statusMessage + "\n\nPhoto Profile:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n\nPhoto Cover:\n" + str(cu))
                     else:
                         contact = red.getContact(msg.contentMetadata["mid"])
                         try:
                             cu = red.channel.getCover(msg.contentMetadata["mid"])
                         except:
                             cu = ""
                         red.sendText(msg.to,"Nama:\n" + msg.contentMetadata["displayName"] + "\n\nMid:\n" + msg.contentMetadata["mid"] + "\n\nStatus:\n" + contact.statusMessage + "\n\nPhoto Profile:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n\nPhoto Cover:\n" + str(cu))


 
            elif msg.text == "Ginfo":
                if msg.toType == 2:
                    ginfo = red.getGroup(msg.to)
                    try:
                        gCreator = ginfo.creator.displayName
                    except:
                        gCreator = "Error"
                    if wait["lang"] == "JP":
                        if ginfo.invitee is None:
                            sinvitee = "0"
                        else:
                            sinvitee = str(len(ginfo.invitee))
                        if ginfo.preventJoinByTicket == True:
                            u = "close"
                        else:
                            u = "open"
                        red.sendText(msg.to,"[Group name]\n" + str(ginfo.name) + "\n\n[Gid]\n" + msg.to + "\n\n[Group creator]\n" + gCreator + "\n\n[Profile status]\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus + "\n\nMembers:" + str(len(ginfo.members)) + "members\nPending:" + sinvitee + "people\nURL:" + u + "it is inside")
                    else:
                        red.sendText(msg.to,"[group name]\n" + str(ginfo.name) + "\n[gid]\n" + msg.to + "\n[group creator]\n" + gCreator + "\n[profile status]\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus)
                else:
                    if wait["lang"] == "JP":
                        red.sendText(msg.to,"Can not be used outside the group")
                    else:
                        red.sendText(msg.to,"Not for use less than group")
                        

 
            elif msg.text is None:
                return
 
            elif msg.text in ["Creator","Owner"]:
                msg.contentType = 13
                msg.contentMetadata = {'mid':"ub5abe828cd964292195c3c59d6322033"}
                red.sendMessage(msg)
		red.sendText(msg.to,"ผู้สร้าง คือ คนนี้ (^_^)")

 

	    elif msg.text in ["Group creator","Gcreator","gcreator"]:
		ginfo = nadya.getGroup(msg.to)
		gCreator = ginfo.creator.mid
                msg.contentType = 13
                msg.contentMetadata = {'mid': gCreator}
                red.sendMessage(msg)
		red.sendText(msg.to,"Itu Yang Buat Grup Ini")
 

                
            elif msg.contentType == 16:
                if wait["Timeline"] == True:
                    msg.contentType = 0
                    msg.text = "post URL\n" + msg.contentMetadata["postEndUrl"]
                    red.sendText(msg.to,msg.text)

            
            if msg.contentType == 13:
                if wait["steal"] == True:
                    _name = msg.contentMetadata["displayName"]
                    copy = msg.contentMetadata["mid"]
                    groups = red.getGroup(msg.to)
                    pending = groups.invitee
                    targets = []
                    for s in groups.members:
                        if _name in s.displayName:
                            print "[Target] Stealed"
                            break                             
                        else:
                            targets.append(copy)
                    if targets == []:
                        pass
                    else:
                        for target in targets:
                            try:
                                red.findAndAddContactsByMid(target)
                                contact = red.getContact(target)
                                cu = red.channel.getCover(target)
                                path = str(cu)
                                image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                                red.sendText(msg.to,"Nama :\n" + contact.displayName + "\n\nMid :\n" + msg.contentMetadata["mid"] + "\n\nBio :\n" + contact.statusMessage)
                                red.sendText(msg.to,"Profile Picture " + contact.displayName)
                                red.sendImageWithURL(msg.to,image)
                                red.sendText(msg.to,"Cover " + contact.displayName)
                                red.sendImageWithURL(msg.to,path)
                                wait["steal"] = False
                                break
                            except:
                                    pass


            if msg.contentType == 13:
                if wait["gift"] == True:
                    _name = msg.contentMetadata["displayName"]
                    copy = msg.contentMetadata["mid"]
                    groups = red.getGroup(msg.to)
                    pending = groups.invitee
                    targets = []
                    for s in groups.members:
                        if _name in s.displayName:
                            print "[Target] Gift"
                            break                             
                        else:
                            targets.append(copy)
                    if targets == []:
                        pass
                    else:
                        for target in targets:
                            try:
                                red.sendText(msg.to,"Gift Sudah Terkirim!")
                                msg.contentType = 9
                                msg.contentMetadata= {'PRDTYPE': 'STICKER',
                                                         'STKVER': '1',
                                                         'MSGTPL': '1',
                                                         'STKPKGID': '1296261'}
                                msg.to = target
                                msg.text = None
                                red.sendMessage(msg)
                                wait['gift'] = False
                                break
                            except:
                                     msg.contentMetadata = {'mid': target}
                                     wait["gift"] = False
                                     break

            if msg.contentType == 13:
                if wait["copy"] == True:
                    _name = msg.contentMetadata["displayName"]
                    copy = msg.contentMetadata["mid"]
                    groups = red.getGroup(msg.to)
                    targets = []
                    for s in groups.members:
                        if _name in s.displayName:
                            print "[Target] Copy"
                            break                             
                        else:
                            targets.append(copy)
                    if targets == []:
                        red.sendText(msg.to, "Not Found...")
                        pass
                    else:
                        for target in targets:
                            try:
                                red.CloneContactProfile(target)
                                red.sendText(msg.to, "Copied (^_^)")
                                wait['copy'] = False
                                break
                            except:
                                     msg.contentMetadata = {'mid': target}
                                     wait["copy"] = False
                                     break


            if msg.contentType == 13:
                if wait['invite'] == True:
                     _name = msg.contentMetadata["displayName"]
                     invite = msg.contentMetadata["mid"]
                     groups = red.getGroup(msg.to)
                     pending = groups.invitee
                     targets = []
                     for s in groups.members:
                         if _name in s.displayName:
                             red.sendText(msg.to, _name + " Berada DiGrup Ini")
                         else:
                             targets.append(invite)
                     if targets == []:
                         pass
                     else:
                         for target in targets:
                             try:
                                 red.findAndAddContactsByMid(target)
                                 red.inviteIntoGroup(msg.to,[target])
                                 red.sendText(msg.to,"Invite " + _name)
                                 wait['invite'] = False
                                 break                              
                             except:             
                                      red.sendText(msg.to,"Limit Invite")
                                      wait['invite'] = False
                                      break
                                  
 
            elif msg.text in ["Key creator","help creator","Help creator"]:
                red.sendText(msg.to,creatorMessage)

            elif msg.text in ["Key group","help group","Help group"]:
                red.sendText(msg.to,groupMessage)

            elif msg.text in ["Key","help","Help"]:
                red.sendText(msg.to,helpMessage)

            elif msg.text in ["Key self","help self","Help self"]:
                red.sendText(msg.to,selfMessage)

            elif msg.text in ["Key bot","help bot","Help bot"]:
                red.sendText(msg.to,botMessage)

            elif msg.text in ["Key set","help set","Help set"]:
                red.sendText(msg.to,setMessage)

            elif msg.text in ["Key media","help media","Help media"]:
                red.sendText(msg.to,mediaMessage)
                
            elif msg.text in ["Key admin","help admin","Help admin"]:
                red.sendText(msg.to,adminMessage)               
                

 
            elif msg.text in ["List group"]:
                    gid = red.getGroupIdsJoined()
                    h = ""
		    jml = 0
                    for i in gid:
		        gn = red.getGroup(i).name
                        h += "♦【%s】\n" % (gn)
		        jml += 1
                    red.sendText(msg.to,"=======[List Group]=======\n"+ h +"\nTotal Group: "+str(jml))
 
	    elif "Ban group: " in msg.text:
		grp = msg.text.replace("Ban group: ","")
		gid = red.getGroupIdsJoined()
		if msg.from_ in admin:
		    for i in gid:
		        h = red.getGroup(i).name
			if h == grp:
			    wait["BlGroup"][i]=True
			    red.sendText(msg.to, "Success Ban Group : "+grp)
			else:
			    pass
		else:
		    red.sendText(msg.to, "Khusus red")
 
            elif msg.text in ["List ban","List ban group"]:
		if msg.from_ in admin:
                    if wait["BlGroup"] == {}:
                        red.sendText(msg.to,"ขอรับ..นายท่าน")
                    else:
                        mc = ""
                        for gid in wait["BlGroup"]:
                            mc += "-> " +red.getGroup(gid).name + "\n"
                        red.sendText(msg.to,"===[Ban Group]===\n"+mc)
		else:
		    red.sendText(msg.to, "คำสั่ง Admin")
 
	    elif msg.text in ["Del ban: "]:
		if msg.from_ in admin:
		    ng = msg.text.replace("Del ban: ","")
		    for gid in wait["BlGroup"]:
		        if red.getGroup(gid).name == ng:
			    del wait["BlGroup"][gid]
			    red.sendText(msg.to, "Success del ban "+ng)
		        else:
			    pass
		else:
		    red.sendText(msg.to, "คำสั่ง red")
 
            elif "Join group: " in msg.text:
		ng = msg.text.replace("Join group: ","")
		gid = red.getGroupIdsJoined()
		try:
		    if msg.from_ in Creator:
                        for i in gid:
                            h = red.getGroup(i).name
		            if h == ng:
		                red.inviteIntoGroup(i,[Creator])
			        red.sendText(msg.to,"Success Join To ["+ h +"] Group")
			    else:
			        pass
		    else:
		        red.sendText(msg.to,"Khusus red")
		except Exception as e:
		    red.sendText(msg.to, str(e))
 
	    elif "Leave group: " in msg.text:
		ng = msg.text.replace("Leave group: ","")
		gid = red.getGroupIdsJoined()
		if msg.from_ in Creator:
                    for i in gid:
                        h = red.getGroup(i).name
		        if h == ng:
			    red.sendText(i,"Bot Di Paksa Keluar Oleh Owner!")
		            red.leaveGroup(i)
			    red.sendText(msg.to,"Success Left ["+ h +"] group")
			else:
			    pass
		else:
		    red.sendText(msg.to,"Khusus red")
 
	    elif "Leave all group" == msg.text:
		gid = red.getGroupIdsJoined()
                if msg.from_ in Creator:
		    for i in gid:
			red.sendText(i,"Bot Di Paksa Keluar Oleh Owner!")
		        red.leaveGroup(i)
		    red.sendText(msg.to,"Success Leave All Group")
		else:
		    red.sendText(msg.to,"Khusus red")
		   

            elif "Pict group: " in msg.text:
                saya = msg.text.replace('Pict group: ','')
                gid = red.getGroupIdsJoined()
                for i in gid:
                    h = red.getGroup(i).name
                    gna = red.getGroup(i)
                    if h == saya:
                        red.sendImageWithURL(msg.to,"http://dl.profile.line.naver.jp/"+ gna.pictureStatus)		    
		    
 
            elif msg.text in ["cancelall","Cancelall"]:
                if msg.toType == 2:
                    X = red.getGroup(msg.to)
                    if X.invitee is not None:
                        gInviMids = [contact.mid for contact in X.invitee]
                        red.cancelGroupInvitation(msg.to, gInviMids)
                    else:
                        red.sendText(msg.to,"ปฏิเสธคำเชิญทั้งหมดแล้ว")
                else:
                    red.sendText(msg.to,"ไม่มีสมาชิกที่ค้างเชิญในกลุ่มนี้")
 
            elif msg.text in ["Ourl","Url on"]:
                if msg.toType == 2:
                    X = red.getGroup(msg.to)
                    X.preventJoinByTicket = False
                    red.updateGroup(X)
                    red.sendText(msg.to,"เปิดลิ้ง รับทราบ")
                else:
                    red.sendText(msg.to,"ลิ้งค์กลุ่มเปิดอยู่แล้ว")
 
            elif msg.text in ["Curl","Url off"]:
                if msg.toType == 2:
                    X = red.getGroup(msg.to)
                    X.preventJoinByTicket = True
                    red.updateGroup(X)
                    red.sendText(msg.to,"ปิดลิ้งค์ รับทราบ")

                else:
                    red.sendText(msg.to,"ลิ้งค์กลุ่มนี้ปิดอยู่แล้ว")
 
            elif msg.text in ["Join on","Autojoin on"]:
		if msg.from_ in admin:
                    wait["AutoJoin"] = True
                    wait["AutoJoinCancel"] = False
                    red.sendText(msg.to,"เปิดการเข้าร่วมกลุ่มอัตโนมัติ")
		else:
		    red.sendText(msg.to,"Klusus red")

            elif msg.text in ["Join off","Autojoin off"]:
		if msg.from_ in admin:
                    wait["AutoJoin"] = False
                    red.sendText(msg.to,"ปิดการเข้าร่วมกลุ่มอัตโนมัติ")
		else:
		    red.sendText(msg.to,"Khusus red")
		    
		    
            elif msg.text in ["Joincancel on","Autojoincancel on"]:
		if msg.from_ in admin:
                    wait["AutoJoinCancel"] = True
                    wait["AutoJoin"] = False
                    red.sendText(msg.to,"ไม่อนุยาติให้ยกเลิกคำเชิญ")
		else:
		    red.sendText(msg.to,"Khusus red")

            elif msg.text in ["Joincancel off","Autojoincancel off"]:
		if msg.from_ in admin:
                    wait["AutoJoinCancel"] = False
                    red.sendText(msg.to,"อนุญาติให้ยกเลิกคำเชิญได้")
		else:
		    red.sendText(msg.to,"Khusus red")		    
		    
 
            elif msg.text in ["Respon1 on"]:
		if msg.from_ in admin:
                    wait["detectMention"] = True
                    wait["detectMention2"] = False
                    wait["detectMention3"] = False
                    wait["kickMention"] = False
                    red.sendText(msg.to,"Auto Respon1 เปิด")
		else:
		    red.sendText(msg.to,"Khusus red")

            elif msg.text in ["Respon1 off"]:
		if msg.from_ in admin:
                    wait["detectMention"] = False
                    red.sendText(msg.to,"Auto Respon1 ปิด")
		else:
		    red.sendText(msg.to,"Khusus red")	
		    
		    
            elif msg.text in ["Respon2 on"]:
		if msg.from_ in admin:
                    wait["detectMention"] = False
                    wait["detectMention2"] = True
                    wait["detectMention3"] = False
                    wait["kickMention"] = False
                    red.sendText(msg.to,"Auto Respon2 เปิด")
		else:
		    red.sendText(msg.to,"Khusus Red")
            elif msg.text in ["Respon2 off"]:
		if msg.from_ in admin:
                    wait["detectMention2"] = False
                    red.sendText(msg.to,"Auto Respon2 ปิด")
		else:
		    red.sendText(msg.to,"Khusus red")	
		    

            elif msg.text in ["Respon3 on"]:
		if msg.from_ in admin:
                    wait["detectMention"] = False
                    wait["detectMention2"] = False
                    wait["detectMention3"] = True
                    wait["kickMention"] = False
                    red.sendText(msg.to,"Auto Respon3 เปิด")
		else:
		    red.sendText(msg.to,"Khusus red")

            elif msg.text in ["Respon3 off"]:
		if msg.from_ in admin:
                    wait["detectMention3"] = False
                    red.sendText(msg.to,"Auto Respon3 ปิด")
		else:
		    red.sendText(msg.to,"Khusus red")	
		    
 
            elif msg.text in ["Responkick on"]:
		if msg.from_ in admin:
                    wait["kickMention"] = True  
                    wait["detectMention"] = False
                    wait["detectMention2"] = False
                    wait["detectMention3"] = False                    
                    red.sendText(msg.to,"Auto Respon Kick เปิด")
		else:
		    red.sendText(msg.to,"Khusus red")

            elif msg.text in ["Responkick off"]:
		if msg.from_ in admin:
                    wait["kickMention"] = False                    
                    red.sendText(msg.to,"Auto Respon Kick ปิด")
		else:
		    red.sendText(msg.to,"Khusus red")			  
		    
 
	    elif msg.text in ["Autocancel on"]:
	     if msg.from_ in admin:	        
                wait["AutoCancel"] = True
                red.sendText(msg.to,"Auto Cancel เปิด")
		print wait["AutoCancel"]
	     else:
		    red.sendText(msg.to,"Khusus red")		

	    elif msg.text in ["Autocancel off"]:
	     if msg.from_ in admin:	        
                wait["AutoCancel"] = False
                red.sendText(msg.to,"Auto Cancel ปิด")
		print wait["AutoCancel"]
	     else:
		    nadya.sendText(msg.to,"Khusus red")	
		    

	    elif msg.text in ["Invitepro on"]:
	     if msg.from_ in admin:	        
                wait["inviteprotect"] = True
                red.sendText(msg.to,"Invite Protect เปิด")
		print wait["inviteprotect"]
	     else:
		    red.sendText(msg.to,"Khusus red")		

	    elif msg.text in ["Invitepro off"]:
	     if msg.from_ in admin:	        
                wait["inviteprotect"] = False
                red.sendText(msg.to,"Invite Protect ปิด")
		print wait["inviteprotect"]
	     else:
		    red.sendText(msg.to,"Khusus red")		    

	    elif "Qr on" in msg.text:
	     if msg.from_ in admin:	        
	        wait["Qr"] = True
	    	red.sendText(msg.to,"QR Protect เปิด")
	     else:
		    red.sendText(msg.to,"Khusus red")	    	

	    elif "Qr off" in msg.text:
	     if msg.from_ in admin:	        
	    	wait["Qr"] = False
	    	red.sendText(msg.to,"Qr Protect ปิด")
	     else:
		    red.sendText(msg.to,"Khusus red")	    	

                        

	    elif "Autokick on" in msg.text:
	     if msg.from_ in admin:	 	        
		     wait["AutoKick"] = True
		     red.sendText(msg.to,"เปิดระบบ Auto Kick")
	     else:
	        red.sendText(msg.to,"Khusus red")	     

	    elif "Autokick off" in msg.text:
	     if msg.from_ in admin:	 	        
		     wait["AutoKick"] = False
		     red.sendText(msg.to,"ปิดระบบ Auto Kick")
	     else:
	        red.sendText(msg.to,"Khusus red")	     


            elif msg.text in ["Allprotect on"]:
		if msg.from_ in admin:
                    wait["AutoCancel"] = True
                    wait["inviteprotect"] = True                   
                    wait["AutoKick"] = True
                    wait["Qr"] = True
                    red.sendText(msg.to,"เปิดระบบป้องกันทั้งหมดแล้ว")
		else:
		    red.sendText(msg.to,"Khusus red")

            elif msg.text in ["Allprotect off"]:
		if msg.from_ in admin:
                    wait["AutoCancel"] = False
                    wait["inviteprotect"] = False                    
                    wait["AutoKick"] = False
                    wait["Qr"] = False
                    red.sendText(msg.to,"ปิดระบบป้องกันทั้งหมดแล้ว")
		else:
		    red.sendText(msg.to,"Khusus red")


            elif msg.text in ["K on","Contact on"]:
                wait["Contact"] = True
                red.sendText(msg.to,"เปิดอ่าน คท")

            elif msg.text in ["K off","Contact off"]:
                wait["Contact"] = False
                red.sendText(msg.to,"ปิดอ่าน คทแล้ว")
                

            elif msg.text in ["Alwaysread on"]:
                wait["alwaysRead"] = True
                red.sendText(msg.to,"เปิดระบบอ่านทั้งหมด")

            elif msg.text in ["Alwaysread off"]:
                wait["alwaysRead"] = False
                red.sendText(msg.to,"ปิดนะบบอ่านทั้งหมดแล้ว")                


            elif msg.text in ["Sambutan on"]:
                if wait["Sambutan"] == True:
                    if wait["lang"] == "JP":
                        red.sendText(msg.to,"Sambutan เปิดヾ(*´∀｀*)ﾉ")
                else:
                    wait["Sambutan"] = True
                    if wait["lang"] == "JP":
                        red.sendText(msg.to,"เปิดแล้วヽ(´▽｀)/")

            elif msg.text in ["Sambutan off"]:
                if wait["Sambutan"] == False:
                    if wait["lang"] == "JP":
                        red.sendText(msg.to,"ปิดระบบ Sambutan(　＾∇＾)")
                else:
                    wait["Sambutan"] = False
                    if wait["lang"] == "JP":
                        red.sendText(msg.to,"ปิดแล้ว(p′︵‵。)")
                        
                        
            elif "Sider on" in msg.text:
                try:
                    del cctv['point'][msg.to]
                    del cctv['sidermem'][msg.to]
                    del cctv['cyduk'][msg.to]
                except:
                    pass
                cctv['point'][msg.to] = msg.id
                cctv['sidermem'][msg.to] = ""
                cctv['cyduk'][msg.to]=True
                wait["Sider"] = True
                red.sendText(msg.to,"เปิดระบบจับคนแอบ")
                
            elif "Sider off" in msg.text:
                if msg.to in cctv['point']:
                    cctv['cyduk'][msg.to]=False
                    wait["Sider"] = False
                    red.sendText(msg.to, "ปิดระบบจับคนแอบแล้ว")
                else:
                    red.sendText(msg.to, "ดูได้ที่การตั้งค่า")                         


            elif msg.text in ["Status"]:
                md = ""
		if wait["Sambutan"] == True: md+="╠➩✔️ Sambutan : On\n"
		else:md+="╠➩❌ Sambutan : Off\n"
		if wait["AutoJoin"] == True: md+="╠➩✔️ Auto Join : On\n"
                else: md +="╠➩❌ Auto Join : Off\n"
		if wait["AutoJoinCancel"] == True: md+="╠➩✔️ Auto Join Cancel : On\n"
                else: md +="╠➩❌ Auto Join Cancel : Off\n"                
		if wait["Contact"] == True: md+="╠➩✔️ Info Contact : On\n"
		else: md+="╠➩❌ Info Contact : Off\n"
                if wait["AutoCancel"] == True:md+="╠➩✔️ Auto Cancel : On\n"
                else: md+= "╠➩❌ Auto Cancel : Off\n"
                if wait["inviteprotect"] == True:md+="╠➩✔️ Invite Protect : On\n"
                else: md+= "╠➩❌ Invite Protect : Off\n"                
		if wait["Qr"] == True: md+="╠➩✔️ Qr Protect : On\n"
		else:md+="╠➩❌ Qr Protect : Off\n"
		if wait["AutoKick"] == True: md+="╠➩✔️ Auto Kick : On\n"
		else:md+="╠➩❌ Auto Kick : Off\n"
		if wait["alwaysRead"] == True: md+="╠➩✔️ Always Read : On\n"
		else:md+="╠➩❌ Always Read: Off\n"
		if wait["detectMention"] == True: md+="╠➩✔️ Auto Respon1 : On\n"
		else:md+="╠➩❌ Auto Respon1 : Off\n"		
		if wait["detectMention2"] == True: md+="╠➩✔️ Auto Respon2 : On\n"
		else:md+="╠➩❌ Auto Respon2 : Off\n"	
		if wait["detectMention3"] == True: md+="╠➩✔️ Auto Respon3 : On\n"
		else:md+="╠➩❌ Auto Respon3 : Off\n"			
		if wait["kickMention"] == True: md+="╠➩✔️ Auto Respon Kick : On\n"
		else:md+="╠➩❌ Auto Respon Kick : Off\n"				
		if wait["Sider"] == True: md+="╠➩✔️ Auto Sider : On\n"
		else:md+="╠➩❌ Auto Sider: Off\n"	
		if wait["Simi"] == True: md+="╠➩✔️ Simisimi : On\n"
		else:md+="╠➩❌ Simisimi: Off\n"		
                red.sendText(msg.to,"╔═════════════════════════\n""║           ☆☞ S T A T U S ☜☆\n""╠═════════════════════════\n"+md+"╚═════════════════════════")


            elif msg.text in ["Gift","gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '5'}
                msg.text = None
                red.sendMessage(msg)
                
                
            elif "Gift1 " in msg.text:
                       msg.contentType = 13
                       nk0 = msg.text.replace("Gift1 ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = red.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
                                    red.sendText(msg.to,_name + " Check Your Gift")
                                    msg.contentType = 9
                                    msg.contentMetadata= {'PRDTYPE': 'STICKER',
                                                         'STKVER': '1',
                                                         'MSGTPL': '1',
                                                         'STKPKGID': '1380280'}
                                    msg.to = target
                                    msg.text = None
                                    red.sendMessage(msg)
                                except:
                                    msg.contentMetadata = {'mid': target}

            elif "Gift2 " in msg.text:
                       msg.contentType = 13
                       nk0 = msg.text.replace("Gift2 ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = red.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
                                    red.sendText(msg.to,_name + " Check Your Gift")
                                    msg.contentType = 9
                                    msg.contentMetadata= {'PRDTYPE': 'STICKER',
                                                         'STKVER': '1',
                                                         'MSGTPL': '2',
                                                         'STKPKGID': '1360738'}
                                    msg.to = target
                                    msg.text = None
                                    red.sendMessage(msg)
                                except:
                                    msg.contentMetadata = {'mid': target}

            elif "Gift3 " in msg.text:
                       msg.contentType = 13
                       nk0 = msg.text.replace("Gift3 ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = red.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
                                    red.sendText(msg.to,_name + " Check Your Gift")
                                    msg.contentType = 9
                                    msg.contentMetadata= {'PRDTYPE': 'STICKER',
                                                         'STKVER': '1',
                                                         'MSGTPL': '3',
                                                         'STKPKGID': '1395389'}
                                    msg.to = target
                                    msg.text = None
                                    red.sendMessage(msg)
                                except:
                                    msg.contentMetadata = {'mid': target}

            elif "Gift4 " in msg.text:
                       msg.contentType = 13
                       nk0 = msg.text.replace("Gift4 ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = red.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
                                    red.sendText(msg.to,_name + " Check Your Gift")
                                    msg.contentType = 9
                                    msg.contentMetadata= {'PRDTYPE': 'STICKER',
                                                         'STKVER': '1',
                                                         'MSGTPL': '4',
                                                         'STKPKGID': '1329191'}
                                    msg.to = target
                                    msg.text = None
                                    red.sendMessage(msg)
                                except:
                                    msg.contentMetadata = {'mid': target}

            elif "Gift5 " in msg.text:
                       msg.contentType = 13
                       nk0 = msg.text.replace("Gift5 ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = red.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
                                    red.sendText(msg.to,_name + " Check Your Gift")
                                    msg.contentType = 9
                                    msg.contentMetadata= {'PRDTYPE': 'STICKER',
                                                         'STKVER': '1',
                                                         'MSGTPL': '1',
                                                         'STKPKGID': '9057'}
                                    msg.to = target
                                    msg.text = None
                                    red.sendMessage(msg)
                                except:
                                    msg.contentMetadata = {'mid': target}

            elif "Gift6 " in msg.text:
                       msg.contentType = 13
                       nk0 = msg.text.replace("Gift6 ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = nadya.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
                                    red.sendText(msg.to,_name + " Check Your Gift")
                                    msg.contentType = 9
                                    msg.contentMetadata= {'PRDTYPE': 'STICKER',
                                                         'STKVER': '1',
                                                         'MSGTPL': '2',
                                                         'STKPKGID': '9167'}
                                    msg.to = target
                                    msg.text = None
                                    red.sendMessage(msg)
                                except:
                                    msg.contentMetadata = {'mid': target}

            elif "Gift7 " in msg.text:
                       msg.contentType = 13
                       nk0 = msg.text.replace("Gift7 ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = red.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
                                    red.sendText(msg.to,_name + " Check Your Gift")
                                    msg.contentType = 9
                                    msg.contentMetadata= {'PRDTYPE': 'STICKER',
                                                         'STKVER': '1',
                                                         'MSGTPL': '3',
                                                         'STKPKGID': '7334'}
                                    msg.to = target
                                    msg.text = None
                                    red.sendMessage(msg)
                                except:
                                    msg.contentMetadata = {'mid': target}

            elif "Gift8 " in msg.text:
                       msg.contentType = 13
                       nk0 = msg.text.replace("Gift8 ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = red.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
                                    red.sendText(msg.to,_name + " Check Your Gift")
                                    msg.contentType = 9
                                    msg.contentMetadata= {'PRDTYPE': 'STICKER',
                                                         'STKVER': '1',
                                                         'MSGTPL': '1',
                                                         'STKPKGID': '1380280'}
                                    msg.to = target
                                    msg.text = None
                                    red.sendMessage(msg)
                                except:
                                    msg.contentMetadata = {'mid': target}

            elif "Gift9 " in msg.text:
                       msg.contentType = 13
                       nk0 = msg.text.replace("Gift9 ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = red.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
                                    red.sendText(msg.to,_name + " Check Your Gift")
                                    msg.contentType = 9
                                    msg.contentMetadata= {'PRDTYPE': 'STICKER',
                                                         'STKVER': '1',
                                                         'MSGTPL': '4',
                                                         'STKPKGID': '1405277'}
                                    msg.to = target
                                    msg.text = None
                                    red.sendMessage(msg)
                                except:
                                    msg.contentMetadata = {'mid': target}

            elif "Gift10 " in msg.text:
                       msg.contentType = 13
                       nk0 = msg.text.replace("Gift10 ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = red.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
                                    red.sendText(msg.to,_name + " Check Your Gift")
                                    msg.contentType = 9
                                    msg.contentMetadata= {'PRDTYPE': 'STICKER',
                                                         'STKVER': '1',
                                                         'MSGTPL': '1',
                                                         'STKPKGID': '1296261'}
                                    msg.to = target
                                    msg.text = None
                                    red.sendMessage(msg)
                                except:
                                    msg.contentMetadata = {'mid': target}


            elif msg.text.lower() in ["ตลก","ติ๊ก1","หัวเราะ","ขำ"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '100',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                red.sendMessage(msg)

            elif msg.text.lower() in ["555+","555","ติ๊ก2"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '10',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                red.sendMessage(msg)

            elif msg.text.lower() in ["ติ๊ก3"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '9',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                red.sendMessage(msg)

            elif msg.text.lower() in ["ติ๊ก4","เธอ","ตะเอง"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '7',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                red.sendMessage(msg)

            elif msg.text.lower() in ["ติ๊ก5","hadeuh","hadeh"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '6',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                red.sendMessage(msg)

            elif msg.text.lower() in ["please","pliss","ติ๊ก5","ขอร้อง"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '4',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                red.sendMessage(msg)

            elif msg.text.lower() in ["haa","haaa","ติ๊ก6"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '3',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                red.sendMessage(msg)

            elif msg.text.lower() in ["lucu","เศร้า","ติ๊ก7"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '110',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                red.sendMessage(msg)

            elif msg.text.lower() in ["hmm","ติ๊ก8"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '101',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                red.sendMessage(msg)

            elif msg.text.lower() in ["ติ๊ก9"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '1',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                red.sendMessage(msg)

            elif msg.text.lower() in ["ติ๊ก10"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '2',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                red.sendMessage(msg)

            elif msg.text.lower() in ["ติ๊ก11","imut"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '5',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                red.sendMessage(msg)

            elif msg.text.lower() in ["ติ๊ก12","ชิว"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '11',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                red.sendMessage(msg)

            elif msg.text.lower() in ["ติ๊ก13"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '8',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                red.sendMessage(msg)

            elif msg.text.lower() in ["ok","oke","okay","ติ๊ก14"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '13',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                red.sendMessage(msg)

            elif msg.text.lower() in ["mantab","ติ๊ก15"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '14',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                red.sendMessage(msg)

            elif msg.text.lower() in ["ติ๊ก16"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '15',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                red.sendMessage(msg)

            elif msg.text.lower() in ["ติ๊ก17"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '16',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                red.sendMessage(msg)

            elif msg.text.lower() in ["woi","ติ๊ก18"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '102',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                red.sendMessage(msg)

            elif msg.text.lower() in ["ติ๊ก19"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '104',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                red.sendMessage(msg)
                

            elif "tag all" == msg.text.lower():
                 group = red.getGroup(msg.to)
                 nama = [contact.mid for contact in group.members]
                 nm1, nm2, nm3, nm4, nm5, jml = [], [], [], [], [], len(nama)
                 if jml <= 100:
                    summon(msg.to, nama)
                 if jml > 100 and jml < 200:
                    for i in range(0, 99):
                        nm1 += [nama[i]]
                    summon(msg.to, nm1)
                    for j in range(100, len(nama)-1): 
                        nm2 += [nama[j]]
                    summon(msg.to, nm2)                 
                 if jml > 200 and jml < 300:
                    for i in range(0, 99):
                        nm1 += [nama[i]]
                    summon(msg.to, nm1)
                    for j in range(100, 199):
                        nm2 += [nama[j]]
                    summon(msg.to, nm2)
                    for k in range(200, len(nama)-1):
                        nm3 += [nama[k]]
                    summon(msg.to, nm3)
                 if jml > 300  and jml < 400:
                    for i in range(0, 99):
                        nm1 += [nama[i]]
                    summon(msg.to, nm1)
                    for j in range(100, 199):
                        nm2 += [nama[j]]
                    summon(msg.to, nm2)
                    for k in range(200, 299):
                        nm3 += [nama[k]]
                    summon(msg.to, nm3)
                    for l in range(300, len(nama)-1):
                    	nm4 += [nama[l]]
                    summon(msg.to, nm4)
                 if jml > 400  and jml < 500:
                    for i in range(0, 99):
                        nm1 += [nama[i]]
                    summon(msg.to, nm1)
                    for j in range(100, 199):
                        nm2 += [nama[j]]
                    summon(msg.to, nm2)
                    for k in range(200, 299):
                        nm3 += [nama[k]]
                    summon(msg.to, nm3)
                    for l in range(300, 399):
                        nm4 += [nama[l]]
                    summon(msg.to, nm4)
                    for m in range(400, len(nama)-1):
                        nm5 += [nama[m]]
                    summon(msg.to, nm5)
                 if jml > 500:
                     print "Terlalu Banyak Men 500+"
                 cnt = Message()
                 cnt.text = "Jumlah:\n" + str(jml) +  " Members"
                 cnt.to = msg.to
                 red.sendMessage(cnt)
                 
            elif "tagall" == msg.text.lower():
                 group = red.getGroup(msg.to)
                 nama = [contact.mid for contact in group.members]
                 nm1, nm2, nm3, nm4, nm5, jml = [], [], [], [], [], len(nama)
                 if jml <= 100:
                    summon(msg.to, nama)
                 if jml > 100 and jml < 200:
                    for i in range(0, 99):
                        nm1 += [nama[i]]
                    summon(msg.to, nm1)
                    for j in range(100, len(nama)-1): 
                        nm2 += [nama[j]]
                    summon(msg.to, nm2)                 
                 if jml > 200 and jml < 300:
                    for i in range(0, 99):
                        nm1 += [nama[i]]
                    summon(msg.to, nm1)
                    for j in range(100, 199):
                        nm2 += [nama[j]]
                    summon(msg.to, nm2)
                    for k in range(200, len(nama)-1):
                        nm3 += [nama[k]]
                    summon(msg.to, nm3)
                 if jml > 300  and jml < 400:
                    for i in range(0, 99):
                        nm1 += [nama[i]]
                    summon(msg.to, nm1)
                    for j in range(100, 199):
                        nm2 += [nama[j]]
                    summon(msg.to, nm2)
                    for k in range(200, 299):
                        nm3 += [nama[k]]
                    summon(msg.to, nm3)
                    for l in range(300, len(nama)-1):
                    	nm4 += [nama[l]]
                    summon(msg.to, nm4)
                 if jml > 400  and jml < 500:
                    for i in range(0, 99):
                        nm1 += [nama[i]]
                    summon(msg.to, nm1)
                    for j in range(100, 199):
                        nm2 += [nama[j]]
                    summon(msg.to, nm2)
                    for k in range(200, 299):
                        nm3 += [nama[k]]
                    summon(msg.to, nm3)
                    for l in range(300, 399):
                        nm4 += [nama[l]]
                    summon(msg.to, nm4)
                    for m in range(400, len(nama)-1):
                        nm5 += [nama[m]]
                    summon(msg.to, nm5)
                 if jml > 500:
                     print "Terlalu Banyak Men 500+"
                 cnt = Message()
                 cnt.text = "Jumlah:\n" + str(jml) +  " Members"
                 cnt.to = msg.to
                 red.sendMessage(cnt)                 


            elif msg.text in ["Setview","Setpoint","Cctv","จับ"]:
                subprocess.Popen("echo '' > dataSeen/"+msg.to+".txt", shell=True, stdout=subprocess.PIPE)
                red.sendText(msg.to, "☆Checkpoint Checked☆")
                print "Setview"

            elif msg.text in ["Viewseen","Check","Ciduk","อ่าน"]:
	        lurkGroup = ""
	        dataResult, timeSeen, contacts, userList, timelist, recheckData = [], [], [], [], [], []
                with open('dataSeen/'+msg.to+'.txt','r') as rr:
                    contactArr = rr.readlines()
                    for v in xrange(len(contactArr) -1,0,-1):
                        num = re.sub(r'\n', "", contactArr[v])
                        contacts.append(num)
                        pass
                    contacts = list(set(contacts))
                    for z in range(len(contacts)):
                        arg = contacts[z].split('|')
                        userList.append(arg[0])
                        timelist.append(arg[1])
                    uL = list(set(userList))
                    for ll in range(len(uL)):
                        try:
                            getIndexUser = userList.index(uL[ll])
                            timeSeen.append(time.strftime("%H:%M:%S", time.localtime(int(timelist[getIndexUser]) / 1000)))
                            recheckData.append(userList[getIndexUser])
                        except IndexError:
                            conName.append('nones')
                            pass
                    contactId = nadya.getContacts(recheckData)
                    for v in range(len(recheckData)):
                        dataResult.append(contactId[v].displayName + ' ('+timeSeen[v]+')')
                        pass
                    if len(dataResult) > 0:
                        tukang = "╔═════════════════════════\n║         ☆☞ LIST VIEWERS ☜☆\n╠═════════════════════════\n╠➩"
                        grp = '\n╠➩ '.join(str(f) for f in dataResult)
                        total = '\n╠═════════════════════════\n╠➩ Total %i Viewers (%s)' % (len(dataResult), datetime.now().strftime('%H:%M:%S')) + "\n╚═════════════════════════"
                        red.sendText(msg.to, "%s %s %s" % (tukang, grp, total))
                        subprocess.Popen("echo '' > dataSeen/"+msg.to+".txt", shell=True, stdout=subprocess.PIPE)
                        red.sendText(msg.to, "☆Auto Checkpoint☆")                        
                    else:
                        red.sendText(msg.to, "☆Belum Ada Viewers☆")
                    print "Viewseen"


	    elif "Kick " in msg.text:
		if msg.from_ in admin:	        
		    if 'MENTION' in msg.contentMetadata.keys()!= None:
		        names = re.findall(r'@(\w+)', msg.text)
		        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
		        mentionees = mention['MENTIONEES']
		        print mentionees
		        for mention in mentionees:
			    red.kickoutFromGroup(msg.to,[mention['M']])

	    elif "Set member: " in msg.text:
		if msg.from_ in admin:	 	        
		    jml = msg.text.replace("Set member: ","")
		    wait["Members"] = int(jml)
		    red.sendText(msg.to, "Jumlah minimal member telah di set : "+jml)

	    elif "Add all" in msg.text:
		    thisgroup = nadya.getGroups([msg.to])
		    Mids = [contact.mid for contact in thisgroup[0].members]
		    mi_d = Mids[:33]
		    red.findAndAddContactsByMids(mi_d)
		    red.sendText(msg.to,"Success Add all")


            elif msg.text in ["Invite"]:
                wait["invite"] = True
                red.sendText(msg.to,"Send Contact")
                
                

            elif msg.text in ["Auto like"]:
                wait["likeOn"] = True
                red.sendText(msg.to,"Shere Post ที่ต้องการกดไลค์")                


            elif msg.text in ["Steal contact"]:
                wait["steal"] = True
                red.sendText(msg.to,"Send Contact")
                

            elif msg.text in ["Giftbycontact"]:
                wait["gift"] = True
                red.sendText(msg.to,"Send Contact") 
                
            elif msg.text in ["Copycontact"]:
                wait["copy"] = True
                red.sendText(msg.to,"Send Contact") 
                
            elif msg.text in ["Sticker on"]:
                wait["sticker"] = True
                red.sendText(msg.to,"Sticker ID Detect Already On.")  
                
            elif msg.text in ["Bot off"]:
                wait["Bot"] = False
                red.sendText(msg.to,"ปิดระบบบอทแล้วคับ")  

	    elif "Recover" in msg.text:
		thisgroup = nadya.getGroups([msg.to])
		Mids = [contact.mid for contact in thisgroup[0].members]
		mi_d = Mids[:33]
		red.createGroup("Recover", mi_d)
		red.sendText(msg.to,"Success recover")



            elif ("Gn: " in msg.text):
                if msg.toType == 2:
                    X = nadya.getGroup(msg.to)
                    X.name = msg.text.replace("Gn: ","")
                    red.updateGroup(X)
                else:
                    red.sendText(msg.to,"It can't be used besides the group.")

            elif "Kick: " in msg.text:
                midd = msg.text.replace("Kick: ","")
		if midd not in admin:
		    red.kickoutFromGroup(msg.to,[midd])
		else:
		    red.sendText(msg.to,"Admin Detected")

            elif "Invite: " in msg.text:
                midd = msg.text.replace("Invite: ","")
                red.findAndAddContactsByMid(midd)
                red.inviteIntoGroup(msg.to,[midd])

            elif "Invite creator" in msg.text:
                midd = "ub5abe828cd964292195c3c59d6322033"
                red.inviteIntoGroup(msg.to,[midd])

            elif msg.text in ["Welcome","welcome","Welkam","welkam","Wc","wc"]:
                gs = red.getGroup(msg.to)
                red.sendText(msg.to,"Selamat Datang Di "+ gs.name)
                msg.contentType = 7
                msg.contentMetadata={'STKID': '247',
                                    'STKPKGID': '3',
                                    'STKVER': '100'}
                msg.text = None
                red.sendMessage(msg)
 
            elif msg.text in ["เยส","เยสส","เยส..."]:
                gs = red.getGroup(msg.to)
                red.sendText(msg.to,"เห็นแล้วมันงึด")
                msg.contentType = 7
                msg.contentMetadata={'STKID': '121',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                red.sendMessage(msg)
                
            elif msg.text in ["เดะโดน","ว่าไงนะ","หา..."]:
                gs = red.getGroup(msg.to)
                red.sendText(msg.to,"เดะปัดเหนี่ยวเลย")
                msg.contentType = 7
                msg.contentMetadata={'STKID': '102',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                red.sendMessage(msg)
                
            elif msg.text in ["เงียบ","กริบ"]:
                gs = red.getGroup(msg.to)
                red.sendText(msg.to,"ป่าช้าชัดๆ")
                msg.contentType = 7
                msg.contentMetadata={'STKID': '113',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                red.sendMessage(msg)
                
            elif msg.text in ["บาย","ลาก่อน","ไปแระ"]:
                gs = red.getGroup(msg.to)
                red.sendText(msg.to,"แล้วเจอกันใหม่นะ😭😭")
                msg.contentType = 7
                msg.contentMetadata={'STKID': '42',
                                    'STKPKGID': '2',
                                    'STKVER': '100'}
                msg.text = None
                red.sendMessage(msg)

	    elif "Bc: " in msg.text:
		bc = msg.text.replace("Bc: ","")
		gid = red.getGroupIdsJoined()
		if msg.from_ in Creator:
		    for i in gid:
			red.sendText(i,"=======[BROADCAST]=======\n\n"+bc+"\n\nContact Me : line.me/ti/p/~samuri5")
		    red.sendText(msg.to,"Success BC BosQ")
		else:
		    red.sendText(msg.to,"Khusus Admin")

            elif msg.text in ["Cancel"]:
                gid = red.getGroupIdsInvited()
                for i in gid:
                    red.rejectGroupInvitation(i)
                red.sendText(msg.to,"All invitations have been refused")

            elif msg.text in ["Gurl"]:
                if msg.toType == 2:
                    x = red.getGroup(msg.to)
                    if x.preventJoinByTicket == True:
                        x.preventJoinByTicket = False
                        red.updateGroup(x)
                    gurl = red.reissueGroupTicket(msg.to)
                    red.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    if wait["lang"] == "JP":
                        red.sendText(msg.to,"Can't be used outside the group")
                    else:
                        red.sendText(msg.to,"Not for use less than group")


            elif msg.text in ["timeline"]:
		try:
                    url = red.activity(limit=5)
		    red.sendText(msg.to,url['result']['posts'][0]['postInfo']['postId'])
		except Exception as E:
		    print E

            elif msg.text in ["@bye","@Bye"]:
		    red.leaveGroup(msg.to)		    
		    

            elif msg.text in ["Absen"]:
		red.sendText(msg.to,"Hadir!!")


            elif msg.text.lower() in ["respon"]:
                red.sendText(msg.to,responsename)

            elif msg.text in ["Sp","Speed","speed"]:
                start = time.time()
                print("Speed")                
                elapsed_time = time.time() - start
		red.sendText(msg.to, "Progress...")
                red.sendText(msg.to, "%sseconds" % (elapsed_time))
                
            elif msg.text in ["Speed test"]:
                start = time.time()
                red.sendText(msg.to, "Progress...")
                elapsed_time = time.time() - start
                red.sendText(msg.to, "%sseconds" % (elapsed_time))                
 
            elif msg.text in ["Ban"]:
                if msg.from_ in admin:
                    wait["wblacklist"] = True
                    red.sendText(msg.to,"send contact")

            elif msg.text in ["Unban"]:
                if msg.from_ in admin:
                    wait["dblacklist"] = True
                    red.sendText(msg.to,"send contact")
 
            elif "Ban @" in msg.text:
                if msg.from_ in admin:
                  if msg.toType == 2:
                    print "@Ban by mention"
                    _name = msg.text.replace("Ban @","")
                    _nametarget = _name.rstrip('  ')
                    gs = red.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        red.sendText(msg.to,"Not found")
                    else:
                        for target in targets:
			    if target not in admin:
                                try:
                                    wait["blacklist"][target] = True
                                    f=codecs.open('st2__b.json','w','utf-8')
                                    json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                    red.sendText(msg.to,"Succes BosQ")
                                except:
                                    red.sendText(msg.to,"Error")
			    else:
				red.sendText(msg.to,"Admin Detected~")
 
            elif msg.text in ["Banlist","Ban list"]:
              if msg.from_ in admin:
                if wait["blacklist"] == {}:
                    red.sendText(msg.to,"ไม่มีรายการที่ถูกแบน")
                else:
                    mc = ""
                    for mi_d in wait["blacklist"]:
                        mc += "->" +red.getContact(mi_d).displayName + "\n"
                    red.sendText(msg.to,"===[Blacklist User]===\n"+mc)

 
            elif "Unban @" in msg.text:
                if msg.toType == 2:
                    print "@Unban by mention"
                if msg.from_ in admin:
                    _name = msg.text.replace("Unban @","")
                    _nametarget = _name.rstrip('  ')
                    gs = red.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        red.sendText(msg.to,"Not found")
                    else:
                        for target in targets:
                            try:
                                del wait["blacklist"][target]
                                f=codecs.open('st2__b.json','w','utf-8')
                                json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                red.sendText(msg.to,"Succes BosQ")
                            except:
                                red.sendText(msg.to,"Succes BosQ")
                                
                                
            elif msg.text.lower() == 'clear ban':
                if msg.from_ in admin:
                    wait["blacklist"] = {}
                    red.sendText(msg.to,"ヽ( ^ω^)ﾉ└ ❉Unbanned All Success❉ ┐") 

 
            elif msg.text in ["Kill ban"]:
		if msg.from_ in admin:
                    if msg.toType == 2:
                        group = red.getGroup(msg.to)
                        gMembMids = [contact.mid for contact in group.members]
                        matched_list = []
                        for tag in wait["blacklist"]:
                            matched_list+=filter(lambda str: str == tag, gMembMids)
                        if matched_list == []:
                            red.sendText(msg.to,"There was no blacklist user")
                            return
                        for jj in matched_list:
                            red.kickoutFromGroup(msg.to,[jj])
                        red.sendText(msg.to,"Blacklist emang pantas tuk di usir")
		else:
		    red.sendText(msg.to, "Khusus creator")
 
            elif msg.text in ["Kill"]:
                    if msg.toType == 2:
                      if msg.from_ in admin:
                        group = red.getGroup(msg.to)
                        gMembMids = [contact.mid for contact in group.members]
                        matched_list = []
                        for tag in wait["blacklist"]:
                            matched_list+=filter(lambda str: str == tag, gMembMids)
                        if matched_list == []:
                            red.sendText(msg.to,"Fuck You")
                            return
                        for jj in matched_list:
                            try:
                                red.kickoutFromGroup(msg.to,[jj])
                                print (msg.to,[jj])
                            except:
                                pass

 
            elif "Kickall" == msg.text:
		    if msg.from_ in Creator:
                     if msg.toType == 2:
                        print "Kick all member"
                        _name = msg.text.replace("Kickall","")
                        gs = red.getGroup(msg.to)
                        red.sendText(msg.to,"ลาก่อย~")
                        targets = []
                        for g in gs.members:
                            if _name in g.displayName:
                                targets.append(g.mid)
                        if targets == []:
                            red.sendText(msg.to,"Not found.")
                        else:
                            for target in targets:
				if target not in admin:
                                    try:
                                        red.kickoutFromGroup(msg.to,[target])
                                        print (msg.to,[g.mid])
                                    except Exception as e:
                                        red.sendText(msg.to,str(e))
			    red.inviteIntoGroup(msg.to, targets)
 

	    elif msg.text in ["Bot restart","Reboot"]:
		if msg.from_ in Creator:
		    red.sendText(msg.to, "Bot Has Been Restarted...")
		    restart_program()
		    print "@Restart"
		else:
		    red.sendText(msg.to, "No Access")
		    
            elif msg.text in ["Turn off"]: 
	        if msg.from_ in Creator:                
                 try:
                     import sys
                     sys.exit()
                 except:
                     pass 		    


            elif 'Crash' in msg.text:
              if msg.from_ in Creator:
                msg.contentType = 13
                msg.contentMetadata = {'mid': "RED,'"}
                red.sendMessage(msg)

 
            elif "Mycopy @" in msg.text:
                   print "[COPY] Ok"
                   _name = msg.text.replace("Mycopy @","")
                   _nametarget = _name.rstrip('  ')
                   gs = red.getGroup(msg.to)
                   targets = []
                   for g in gs.members:
                       if _nametarget == g.displayName:
                           targets.append(g.mid)
                   if targets == []:
                       red.sendText(msg.to, "Not Found...")
                   else:
                       for target in targets:
                            try:
                               red.CloneContactProfile(target)
                               red.sendText(msg.to, "Copied (^_^)")
                            except Exception as e:
                                print e

            elif msg.text in ["Mybackup"]:
                try:
                    red.updateDisplayPicture(backup1.pictureStatus)
                    red.updateProfile(backup1)
                    red.sendText(msg.to, "Done (^_^)")
                except Exception as e:
                    red.sendText(msg.to, str(e))

 
	    elif "/music " in msg.text:
					songname = msg.text.replace("/music ","")
					params = {"songname": songname}
					r = requests.get('http://ide.fdlrcn.com/workspace/yumi-apis/joox?' + urllib.urlencode(params))
					data = r.text
					data = json.loads(data)
					for song in data:
						abc = song[3].replace('https://','http://')
						red.sendText(msg.to, "Title : " + song[0] + "\nLength : " + song[1] + "\nLink download : " + song[4])
						red.sendText(msg.to, "Lagu " + song[0] + "\nSedang Di Prosses... Tunggu Sebentar ^_^ ")
						red.sendAudioWithURL(msg.to,abc)
						red.sendText(msg.to, "Selamat Mendengarkan Lagu " + song[0])
	
            elif '/lirik ' in msg.text.lower():
                try:
                    songname = msg.text.lower().replace('/lirik ','')
                    params = {'songname': songname}
                    r = requests.get('http://ide.fdlrcn.com/workspace/yumi-apis/joox?' + urllib.urlencode(params))
                    data = r.text
                    data = json.loads(data)
                    for song in data:
                        hasil = 'Lyric Lagu ('
                        hasil += song[0]
                        hasil += ')\n\n'
                        hasil += song[5]
                        red.sendText(msg.to, hasil)
                except Exception as wak:
                        red.sendText(msg.to, str(wak))
                        
	    elif "/musrik " in msg.text:
					songname = msg.text.replace("/musrik ","")
					params = {"songname": songname}
					r = requests.get('http://ide.fdlrcn.com/workspace/yumi-apis/joox?' + urllib.urlencode(params))
					data = r.text
					data = json.loads(data)
					for song in data:
						abc = song[3].replace('https://','http://')
						hasil = 'Lyric Lagu ('
						hasil += song[0]
						hasil += ')\n\n'
						hasil += song[5]
						red.sendText(msg.to, "Lagu " + song[0] + "\nSedang Di Prosses... Tunggu Sebentar ^_^ ")
						red.sendAudioWithURL(msg.to,abc)
						red.sendText(msg.to, "Title : " + song[0] + "\nLength : " + song[1] + "\nLink download : " + song[4] +"\n\n" + hasil)
						red.sendText(msg.to, "Selamat Mendengarkan Lagu " + song[0])
             
            
            
            elif "Fancytext: " in msg.text:
                    txt = msg.text.replace("Fancytext: ", "")
                    red.kedapkedip(msg.to,txt)
                    print "[Command] Kedapkedip"


            elif "cover @" in msg.text:
                if msg.toType == 2:
                    cover = msg.text.replace("cover @","")
                    _nametarget = cover.rstrip('  ')
                    gs = red.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        red.sendText(msg.to,"Not found")
                    else:
                        for target in targets:
                            try:
                                h = red.channel.getHome(target)
                                objId = h["result"]["homeInfo"]["objectId"]
                                red.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/myhome/c/download.nhn?userid=" + target + "&oid=" + objId)
                            except Exception as error:
                                print error
                                red.sendText(msg.to,"Upload image failed.")

            elif "Cover @" in msg.text:
                if msg.toType == 2:
                    cover = msg.text.replace("Cover @","")
                    _nametarget = cover.rstrip('  ')
                    gs = red.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        red.sendText(msg.to,"Not found")
                    else:
                        for target in targets:
                            try:
                                h = red.channel.getHome(target)
                                objId = h["result"]["homeInfo"]["objectId"]
                                red.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/myhome/c/download.nhn?userid=" + target + "&oid=" + objId)
                            except Exception as error:
                                print error
                                red.sendText(msg.to,"Upload image failed.")
                                
            elif "Cpp" in msg.text:
                if msg.from_ in admin:
                    path = "B612_20170830_112729.jpg"
                    red.sendText(msg.to,"Update PP :")
                    red.sendImage(msg.to,path)
                    red.updateProfilePicture(path)                                
                                
                                
            elif "pp @" in msg.text:
                if msg.toType == 2:
                    cover = msg.text.replace("pp @","")
                    _nametarget = cover.rstrip('  ')
                    gs = red.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        red.sendText(msg.to,"Not found")
                    else:
                        for target in targets:
                            try:
                                h = red.getContact(target)
                                red.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/" + h.pictureStatus)
                            except Exception as error:
                                print error
                                red.sendText(msg.to,"Upload image failed.")

            elif "Pp @" in msg.text:
                if msg.toType == 2:
                    cover = msg.text.replace("Pp @","")
                    _nametarget = cover.rstrip('  ')
                    gs = red.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        red.sendText(msg.to,"Not found")
                    else:
                        for target in targets:
                            try:
                                h = red.getContact(target)
                                red.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/" + h.pictureStatus)
                            except Exception as error:
                                print error
                                red.sendText(msg.to,"Upload image failed.")

            elif msg.text.lower() in ["pap owner","pap creator"]:
                                link = ["http://dl.profile.line-cdn.net/0hNPsZWL9WEX9OIz0lhyFuKHJmHxI5DRc3NkJaETwkRklqGwQoJkNbTGklHRo2G1B7cxFXH2NxSU03"]
                                pilih = random.choice(link)
                                red.sendImageWithURL(msg.to,pilih)

 
            elif "Spam: " in msg.text:
                  bctxt = msg.text.replace("Spam: ", "")
                  t = 10
                  while(t):
                    red.sendText(msg.to, (bctxt))
                    t-=1

            elif "Scbc " in msg.text:
                  bctxt = msg.text.replace("Scbc ", "")
                  orang = nadya.getAllContactIds()
                  t = 20
                  for manusia in orang:
                    while(t):
                      red.sendText(manusia, (bctxt))
                      t-=1

            elif "Cbc " in msg.text:
                  broadcasttxt = msg.text.replace("Cbc ", "") 
                  orang = nadya.getAllContactIds()
                  for manusia in orang:
                    red.sendText(manusia, (broadcasttxt))

 
            elif '/ig ' in msg.text.lower():
                try:
                    instagram = msg.text.lower().replace("/ig ","")
                    html = requests.get('https://www.instagram.com/' + instagram + '/?')
                    soup = BeautifulSoup(html.text, 'html.parser')
                    data = soup.find_all('meta', attrs={'property':'og:description'})
                    text = data[0].get('content').split()
                    data1 = soup.find_all('meta', attrs={'property':'og:image'})
                    text1 = data1[0].get('content').split()
                    tj = text1[0].replace("s150x150/","")
                    user = "Name: " + text[-2] + "\n"
                    user1 = "Username: " + text[-1] + "\n"
                    followers = "Followers: " + text[0] + "\n"
                    following = "Following: " + text[2] + "\n"
                    post = "Post: " + text[4] + "\n"
                    link = "Link: " + "https://www.instagram.com/" + instagram
                    detail = "========INSTAGRAM INFO ========\n"
                    details = "\n========INSTAGRAM INFO ========"
                    red.sendText(msg.to, detail + user + user1 + followers + following + post + link + details)
                    red.sendImageWithURL(msg.to, tj)
                except Exception as njer:
                	red.sendText(msg.to, str(njer))
                	
                	
            elif "Checkig " in msg.text:
                separate = msg.text.split(" ")
                user = msg.text.replace(separate[0] + " ","")
                if user.startswith("@"):
                    user = user.replace("@","")
                profile = "https://www.instagram.com/" + user
                with requests.session() as x:
                    x.headers['user-agent'] = 'Mozilla/5.0'
                    end_cursor = ''
                    for count in range(1, 999):
                        print('PAGE: ', count)
                        r = x.get(profile, params={'max_id': end_cursor})
                    
                        data = re.search(r'window._sharedData = (\{.+?});</script>', r.text).group(1)
                        j    = json.loads(data)
                    
                        for node in j['entry_data']['ProfilePage'][0]['user']['media']['nodes']: 
                            if node['is_video']:
                                page = 'https://www.instagram.com/p/' + node['code']
                                r = x.get(page)
                                url = re.search(r'"video_url": "([^"]+)"', r.text).group(1)
                                print(url)
                                red.sendVideoWithURL(msg.to,url)
                            else:
                                print (node['display_src'])
                                red.sendImageWithURL(msg.to,node['display_src'])
                        end_cursor = re.search(r'"end_cursor": "([^"]+)"', r.text).group(1)                	


            elif 'Youtubelink: ' in msg.text:
                try:
                    textToSearch = (msg.text).replace('Youtube ', "").strip()
                    query = urllib.quote(textToSearch)
                    url = "https://www.youtube.com/results?search_query=" + query
                    response = urllib2.urlopen(url)
                    html = response.read()
                    soup = BeautifulSoup(html, "html.parser")
                    results = soup.find(attrs={'class':'yt-uix-tile-link'})
                    red.sendText(msg.to,'https://www.youtube.com' + results['href'])
                except:
                    red.sendText(msg.to,"Could not find it")
                    
                    
            elif 'Youtubevideo: ' in msg.text:
                    try:
                        textToSearch = (msg.text).replace('Youtubevideo: ', "").strip()
                        query = urllib.quote(textToSearch)
                        url = "https://www.youtube.com/results?search_query=" + query
                        response = urllib2.urlopen(url)
                        html = response.read()
                        soup = BeautifulSoup(html, "html.parser")
                        results = soup.find(attrs={'class': 'yt-uix-tile-link'})
                        red.sendVideoWithURL(msg.to,'https://www.youtube.com' + results['href'])
                    except:
                        red.sendText(msg.to, "Could not find it")                    

 
            elif "Say-id " in msg.text:
                say = msg.text.replace("Say-id ","")
                lang = 'id'
                tts = gTTS(text=say, lang=lang)
                tts.save("hasil.mp3")
                red.sendAudio(msg.to,"hasil.mp3")

            elif "Say-en " in msg.text:
                say = msg.text.replace("Say-en ","")
                lang = 'en'
                tts = gTTS(text=say, lang=lang)
                tts.save("hasil.mp3")
                red.sendAudio(msg.to,"hasil.mp3")

            elif "Say-jp " in msg.text:
                say = msg.text.replace("Say-jp ","")
                lang = 'ja'
                tts = gTTS(text=say, lang=lang)
                tts.save("hasil.mp3")
                red.sendAudio(msg.to,"hasil.mp3")

            elif "Say welcome" in msg.text:
                gs = red.getGroup(msg.to)
                say = msg.text.replace("Say welcome","Selamat Datang Di "+ gs.name)
                lang = 'id'
                tts = gTTS(text=say, lang=lang)
                tts.save("hasil.mp3")
                red.sendAudio(msg.to,"hasil.mp3")


            elif msg.text.lower() in ["hi","hai","halo","hallo"]:
                    beb = "Hi สวัสดีคับ ทุกคน😘 " +red.getContact(msg.from_).displayName + " 􀸂􀆇starry heart􏿿"
                    red.sendText(msg.to,beb)



            elif "playstore " in msg.text.lower():
                tob = msg.text.lower().replace("playstore ","")
                red.sendText(msg.to,"Sedang Mencari...")
                red.sendText(msg.to,"Title : "+tob+"\nSource : Google Play\nLink : https://play.google.com/store/search?q=" + tob)
                red.sendText(msg.to,"Tuh Linknya Kak (^_^)")


            elif "Mid @" in msg.text:
                _name = msg.text.replace("Mid @","")
                _nametarget = _name.rstrip(' ')
                gs = red.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                        red.sendText(msg.to, g.mid)
                    else:
                        pass


            elif "Mybio " in msg.text:
                    string = msg.text.replace("Mybio ","")
                    if len(string.decode('utf-8')) <= 500:
                        profile = nadya.getProfile()
                        profile.statusMessage = string
                        red.updateProfile(profile)
                        red.sendText(msg.to,"Done")

            elif "Myname " in msg.text:
		if msg.from_ in Creator:
                    string = msg.text.replace("Myname ","")
                    if len(string.decode('utf-8')) <= 5000:
                        profile = nadya.getProfile()
                        profile.displayName = string
                        red.updateProfile(profile)
                        red.sendText(msg.to,"Done")



            elif msg.text.lower() in ["mymid","myid"]:
                middd = "Name : " +red.getContact(msg.from_).displayName + "\nMid : " +msg.from_
                red.sendText(msg.to,middd)

            elif msg.text.lower() in ["me"]:
                msg.contentType = 13
                msg.contentMetadata = {'mid': msg.from_}
                red.sendMessage(msg)

            elif "/apakah " in msg.text:
                apk = msg.text.replace("/apakah ","")
                rnd = ["Ya","Tidak","Bisa Jadi","Mungkin"]
                p = random.choice(rnd)
                lang = 'id'
                tts = gTTS(text=p, lang=lang)
                tts.save("hasil.mp3")
                red.sendAudio(msg.to,"hasil.mp3")
                
            elif "/hari " in msg.text:
                apk = msg.text.replace("/hari ","")
                rnd = ["Senin","Selasa","Rabu","Kamis","Jumat","Sabtu","Minggu"]
                p = random.choice(rnd)
                lang = 'id'
                tts = gTTS(text=p, lang=lang)
                tts.save("hasil.mp3")
                red.sendAudio(msg.to,"hasil.mp3")   


            elif "/berapa " in msg.text:
                apk = msg.text.replace("/berapa ","")
                rnd = ['10%','20%','30%','40%','50%','60%','70%','80%','90%','100%','0%']
                p = random.choice(rnd)
                lang = 'id'
                tts = gTTS(text=p, lang=lang)
                tts.save("hasil.mp3")
                red.sendAudio(msg.to,"hasil.mp3")
                
            elif "/berapakah " in msg.text:
                apk = msg.text.replace("/berapakah ","")
                rnd = ['1','2','3','4','5','6','7','8','9','10','Tidak Ada']
                p = random.choice(rnd)
                lang = 'id'
                tts = gTTS(text=p, lang=lang)
                tts.save("hasil.mp3")
                red.sendAudio(msg.to,"hasil.mp3")                

            elif "/kapan " in msg.text:
                apk = msg.text.replace("/kapan ","")
                rnd = ["kapan kapan","besok","satu abad lagi","Hari ini","Tahun depan","Minggu depan","Bulan depan","Sebentar lagi","Tidak Akan Pernah"]
                p = random.choice(rnd)
                lang = 'id'
                tts = gTTS(text=p, lang=lang)
                tts.save("hasil.mp3")
                red.sendAudio(msg.to,"hasil.mp3")

 
            elif msg.text in ["Simisimi on","Simisimi:on"]:
                settings["simiSimi"][msg.to] = True
                wait["Simi"] = True
                red.sendText(msg.to," Simisimi Di Aktifkan")
                
            elif msg.text in ["Simisimi off","Simisimi:off"]:
                settings["simiSimi"][msg.to] = False
                wait["Simi"] = False
                red.sendText(msg.to,"Simisimi Di Nonaktifkan")

 
            elif "Image " in msg.text:
                search = msg.text.replace("Image ","")
                url = 'https://www.google.com/search?espv=2&biw=1366&bih=667&tbm=isch&oq=kuc&aqs=mobile-gws-lite.0.0l5&q=' + search
                raw_html = (download_page(url))
                items = []
                items = items + (_images_get_all_items(raw_html))
                path = random.choice(items)
                print path
                try:
                    red.sendImageWithURL(msg.to,path)
                except:
                    pass
 
            elif "Youtubesearch: " in msg.text:
                    query = msg.text.replace("Youtube ","")
                    with requests.session() as s:
                        s.headers['user-agent'] = 'Mozilla/5.0'
                        url = 'http://www.youtube.com/results'
                        params = {'search_query': query}
                        r = s.get(url, params=params)
                        soup = BeautifulSoup(r.content, 'html.parser')
                        hasil = ""
                        for a in soup.select('.yt-lockup-title > a[title]'):
                            if '&list=' not in a['href']:
                                hasil += ''.join((a['title'],'\nUrl : http://www.youtube.com' + a['href'],'\n\n'))
                        red.sendText(msg.to,hasil)
                        print '[Command] Youtube Search'


 
            elif "Tr-id " in msg.text:
                isi = msg.text.replace("Tr-id ","")
                translator = Translator()
                hasil = translator.translate(isi, dest='id')
                A = hasil.text
                A = A.encode('utf-8')
                red.sendText(msg.to, A)

            elif "Tr-en " in msg.text:
                isi = msg.text.replace("Tr-en ","")
                translator = Translator()
                hasil = translator.translate(isi, dest='en')
                A = hasil.text
                A = A.encode('utf-8')
                red.sendText(msg.to, A)
                
            elif "Tr-th " in msg.text:
                isi = msg.text.replace("Tr-th ","")
                translator = Translator()
                hasil = translator.translate(isi, dest='th')
                A = hasil.text
                A = A.encode('utf-8')
                red.sendText(msg.to, A)                

            
            elif "Id@en" in msg.text:
                bahasa_awal = 'id'
                bahasa_tujuan = 'en'
                kata = msg.text.replace("Id@en ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                red.sendText(msg.to,"----Dari Indonesia----\n" + "" + kata + "\n\n----Ke Inggris----\n" + "" + result)


            elif "En@id" in msg.text:
                bahasa_awal = 'en'
                bahasa_tujuan = 'id'
                kata = msg.text.replace("En@id ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                red.sendText(msg.to,"----Dari Inggris----\n" + "" + kata + "\n\n----Ke Indonesia----\n" + "" + result)
                
            
            elif "Id@th" in msg.text:
                bahasa_awal = 'id'
                bahasa_tujuan = 'th'
                kata = msg.text.replace("Id@en ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                red.sendText(msg.to,"----Dari Indonesia----\n" + "" + kata + "\n\n----Ke Thailand----\n" + "" + result)
                
            
            elif "Th@id" in msg.text:
                bahasa_awal = 'th'
                bahasa_tujuan = 'id'
                kata = msg.text.replace("Id@en ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                red.sendText(msg.to,"----Dari Thailand----\n" + "" + kata + "\n\n----Ke Indonesia----\n" + "" + result)                
 
            elif msg.text in ["Friendlist"]:    
                contactlist = red.getAllContactIds()
                kontak = red.getContacts(contactlist)
                num=1
                msgs="═════════List Friend═════════"
                for ids in kontak:
                    msgs+="\n[%i] %s" % (num, ids.displayName)
                    num=(num+1)
                msgs+="\n═════════List Friend═════════\n\nTotal Friend : %i" % len(kontak)
                red.sendText(msg.to, msgs)

            elif msg.text in ["Memlist"]:   
                kontak = nadya.getGroup(msg.to)
                group = kontak.members
                num=1
                msgs="═════════List Member═�����═══════-"
                for ids in group:
                    msgs+="\n[%i] %s" % (num, ids.displayName)
                    num=(num+1)
                msgs+="\n═════════List Member═════════\n\nTotal Members : %i" % len(group)
                red.sendText(msg.to, msgs)

            

 
            elif "Getvid @" in msg.text:
                print "[Command]dp executing"
                _name = msg.text.replace("Getvid @","")
                _nametarget = _name.rstrip('  ')
                gs = red.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                    red.sendText(msg.to,"Contact not found")
                else:
                    for target in targets:
                        try:
                            contact = red.getContact(target)
                            path = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                            red.sendVideoWithURL(msg.to, path)
                        except Exception as e:
                            raise e
                print "[Command]dp executed"


            elif "Getgroup image" in msg.text:
                group = red.getGroup(msg.to)
                path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                red.sendImageWithURL(msg.to,path)

            elif "Urlgroup image" in msg.text:
                group = red.getGroup(msg.to)
                path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                red.sendText(msg.to,path)
 
            elif "Getname" in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                contact = red.getContact(key1)
                cu = red.channel.getCover(key1)
                try:
                    red.sendText(msg.to, "===[DisplayName]===\n" + contact.displayName)
                except:
                    red.sendText(msg.to, "===[DisplayName]===\n" + contact.displayName)


            elif "Getprofile" in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                contact = red.getContact(key1)
                cu = red.channel.getCover(key1)
                path = str(cu)
                image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                try:
                    red.sendText(msg.to,"Nama :\n" + contact.displayName + "\n\nBio :\n" + contact.statusMessage)
                    red.sendText(msg.to,"Profile Picture " + contact.displayName)
                    red.sendImageWithURL(msg.to,image)
                    red.sendText(msg.to,"Cover " + contact.displayName)
                    red.sendImageWithURL(msg.to,path)
                except:
                    pass


            elif "Getcontact" in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]                
                mmid = red.getContact(key1)
                msg.contentType = 13
                msg.contentMetadata = {"mid": key1}
                red.sendMessage(msg)

            elif "Getinfo" in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                contact = red.getContact(key1)
                cu = nadya.channel.getCover(key1)
                try:
                    red.sendText(msg.to,"Nama :\n" + contact.displayName + "\n\nMid :\n" + contact.mid + "\n\nBio :\n" + contact.statusMessage + "\n\nProfile Picture :\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n\nHeader :\n" + str(cu))
                except:
                    red.sendText(msg.to,"Nama :\n" + contact.displayName + "\n\nMid :\n" + contact.mid + "\n\nBio :\n" + contact.statusMessage + "\n\nProfile Picture :\n" + str(cu))


            elif "Getbio" in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                contact = red.getContact(key1)
                cu = red.channel.getCover(key1)
                try:
                    red.sendText(msg.to, "===[StatusMessage]===\n" + contact.statusMessage)
                except:
                    red.sendText(msg.to, "===[StatusMessage]===\n" + contact.statusMessage)


            elif msg.text.lower() == 'runtime':
                eltime = time.time() - mulai
                van = "Bot Sudah Berjalan Selama :\n"+waktu(eltime)
                red.sendText(msg.to,van)
                
                 
            elif "Checkdate " in msg.text:
                tanggal = msg.text.replace("Checkdate ","")
                r=requests.get('https://script.google.com/macros/exec?service=AKfycbw7gKzP-WYV2F5mc9RaR7yE3Ve1yN91Tjs91hp_jHSE02dSv9w&nama=ervan&tanggal='+tanggal)
                data=r.text
                data=json.loads(data)
                lahir = data["data"]["lahir"]
                usia = data["data"]["usia"]
                ultah = data["data"]["ultah"]
                zodiak = data["data"]["zodiak"]
                red.sendText(msg.to,"========== I N F O R M A S I ==========\n"+"Date Of Birth : "+lahir+"\nAge : "+usia+"\nUltah : "+ultah+"\nZodiak : "+zodiak+"\n========== I N F O R M A S I ==========")
                
   
            elif msg.text in ["Kalender","Time","Waktu"]:
                timeNow = datetime.now()
                timeHours = datetime.strftime(timeNow,"(%H:%M)")
                day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                inihari = datetime.today()
                hr = inihari.strftime('%A')
                bln = inihari.strftime('%m')
                for i in range(len(day)):
                    if hr == day[i]: hasil = hari[i]
                for k in range(0, len(bulan)):
                    if bln == str(k): bln = bulan[k-1]
                rst = hasil + ", " + inihari.strftime('%d') + " - " + bln + " - " + inihari.strftime('%Y') + "\nJam : [ " + inihari.strftime('%H:%M:%S') + " ]"
                red.sendText(msg.to, rst)                
                 
                
            elif "SearchID: " in msg.text:
                userid = msg.text.replace("SearchID: ","")
                contact = red.findContactsByUserid(userid)
                msg.contentType = 13
                msg.contentMetadata = {'mid': contact.mid}
                red.sendMessage(msg)
                
            elif "Searchid: " in msg.text:
                userid = msg.text.replace("Searchid: ","")
                contact = red.findContactsByUserid(userid)
                msg.contentType = 13
                msg.contentMetadata = {'mid': contact.mid}
                red.sendMessage(msg)       
                
                
            elif "removechat" in msg.text.lower():
                if msg.from_ in admin:
                    try:
                        red.removeAllMessages(op.param2)
                        print "[Command] Remove Chat"
                        red.sendText(msg.to,"Done")
                    except Exception as error:
                        print error
                        red.sendText(msg.to,"Error")      
                        
                        
            elif "Invitemeto: " in msg.text:
                if msg.from_ in admin:
                    gid = msg.text.replace("Invitemeto: ","")
                    if gid == "":
                        red.sendText(msg.to,"Invalid group id")
                    else:
                        try:
                            red.findAndAddContactsByMid(msg.from_)
                            red.inviteIntoGroup(gid,[msg.from_])
                        except:
                            red.sendText(msg.to,"Mungkin Saya Tidak Di Dalaam Grup Itu")


            elif msg.text in ["Glist"]:
                red.sendText(msg.to, "Tunggu Sebentar. . .")                    
                gid = red.getGroupIdsJoined()
                h = ""
                for i in gid:
                    h += "╠➩" + "%s\n" % (red.getGroup(i).name +" ~> ["+str(len(nadya.getGroup(i).members))+"]")
                red.sendText(msg.to,"╔═════════════════════════\n║          ☆☞ LIST GROUPS☜☆\n╠═════════════════════════\n" + h + "╠═════════════════════════" + "\n║ Total Groups =" +" ["+str(len(gid))+"]\n╚═════════════════════════")

            elif msg.text in ["Glistmid"]:   
                gruplist = red.getGroupIdsJoined()
                kontak = red.getGroups(gruplist)
                num=1
                msgs="═════════List GrupMid═════════"
                for ids in kontak:
                    msgs+="\n[%i] %s" % (num, ids.id)
                    num=(num+1)
                msgs+="\n═════════List GrupMid═════════\n\nTotal Grup : %i" % len(kontak)
                red.sendText(msg.to, msgs)



            elif "Google: " in msg.text:
                    a = msg.text.replace("Google: ","")
                    b = urllib.quote(a)
                    red.sendText(msg.to,"Sedang Mencari...")
                    red.sendText(msg.to, "https://www.google.com/" + b)
                    red.sendText(msg.to,"Itu Dia Linknya. . .")     


            elif "Details group: " in msg.text:
                if msg.from_ in admin:
                    gid = msg.text.replace("Details group: ","")
                    if gid in [""," "]:
                        red.sendText(msg.to,"Grup id tidak valid")
                    else:
                        try:
                            groups = nadya.getGroup(gid)
                            if groups.members is not None:
                                members = str(len(groups.members))
                            else:
                                members = "0"
                            if groups.invitee is not None:
                                pendings = str(len(groups.invitee))
                            else:
                                pendings = "0"
                            h = "[" + groups.name + "]\n -+GroupID : " + gid + "\n -+Members : " + members + "\n -+MembersPending : " + pendings + "\n -+Creator : " + groups.creator.displayName + "\n -+GroupPicture : http://dl.profile.line.naver.jp/" + groups.pictureStatus
                            red.sendText(msg.to,h)
                        except Exception as error:
                            red.sendText(msg.to,(error))
            
            elif "Cancel invite: " in msg.text:
                if msg.from_ in admin:
                    gids = msg.text.replace("Cancel invite: ","")
                    gid = red.getGroup(gids)
                    for i in gid:
                        if i is not None:
                            try:
                                red.rejectGroupInvitation(i)
                            except:
                                red.sendText(msg.to,"Error!")
                                break
                        else:
                            break
                    if gid is not None:
                        red.sendText(msg.to,"Berhasil tolak undangan dari grup " + gid.name)
                    else:
                        red.sendText(msg.to,"Grup tidak ditemukan")
            
            elif msg.text in ["Acc invite"]:
                if msg.from_ in admin:
                    gid = red.getGroupIdsInvited()
                    _list = ""
                    for i in gid:
                        if i is not None:
                            gids = nadya.getGroup(i)
                            _list += gids.name
                            red.acceptGroupInvitation(i)
                        else:
                            break
                    if gid is not None:
                        red.sendText(msg.to,"Berhasil terima semua undangan dari grup :\n" + _list)
                    else:
                        red.sendText(msg.to,"Tidak ada grup yang tertunda saat ini")  


            elif "Gif gore" in msg.text:
            	gif = ("https://media.giphy.com/media/l2JHVsQiOZrNMGzYs/giphy.gif","https://media.giphy.com/media/OgltQ2hbilzJS/200w.gif")
                gore = random.choice(gif)
                red.sendGifWithURL(msg.to,gore)
                

                
            elif ("Micadd " in msg.text):
                targets = []
                key = eval(msg.contentMetadata["MENTION"])
                key["MENTIONEES"][0]["M"]
                for x in key["MENTIONEES"]:
                    targets.append(x["M"])
                for target in targets:
                    try:
                        mimic["target"][target] = True
                        red.sendText(msg.to,"Target ditambahkan!")
                        break
                    except:
                        red.sendText(msg.to,"Fail !")
                        break
                    
            elif ("Micdel " in msg.text):
                targets = []
                key = eval(msg.contentMetadata["MENTION"])
                key["MENTIONEES"][0]["M"]
                for x in key["MENTIONEES"]:
                    targets.append(x["M"])
                for target in targets:
                    try:
                        del mimic["target"][target]
                        red.sendText(msg.to,"Target dihapuskan!")
                        break
                    except:
                        red.sendText(msg.to,"Fail !")
                        break
                    
            elif msg.text in ["Miclist"]:
                        if mimic["target"] == {}:
                            red.sendText(msg.to,"Nothing")
                        else:
                            mc = "Target Mimic User:\n"
                            for mi_d in mimic["target"]:
                                mc += "?? "+nadya.getContact(mi_d).displayName + "\n"
                            red.sendText(msg.to,mc)

            elif "Mimic target " in msg.text:
                        if mimic["copy"] == True:
                            siapa = msg.text.replace("Mimic target ","")
                            if siapa.rstrip(' ') == "me":
                                mimic["copy2"] = "me"
                                red.sendText(msg.to,"Mimic change to me")
                            elif siapa.rstrip(' ') == "target":
                                mimic["copy2"] = "target"
                                red.sendText(msg.to,"Mimic change to target")
                            else:
                                red.sendText(msg.to,"I dont know")
            
            elif "Mimic " in msg.text:
                cmd = msg.text.replace("Mimic ","")
                if cmd == "on":
                    if mimic["status"] == False:
                        mimic["status"] = True
                        red.sendText(msg.to,"Reply Message on")
                    else:
                        red.sendText(msg.to,"Sudah on")
                elif cmd == "off":
                    if mimic["status"] == True:
                        mimic["status"] = False
                        red.sendText(msg.to,"Reply Message off")
                    else:
                        red.sendText(msg.to,"Sudah off")



        if op.type == 59:
            print op


    except Exception as error:
        print error


while True:
    try:
        Ops = red.fetchOps(red.Poll.rev, 5)
    except EOFError:
        raise Exception("It might be wrong revision\n" + str(red.Poll.rev))

    for Op in Ops:
        if (Op.type != OpType.END_OF_OPERATION):
            red.Poll.rev = max(red.Poll.rev, Op.revision)
            bot(Op)

