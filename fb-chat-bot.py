from fbchat import Client, log, _graphql
from fbchat.models import *
import json
import random
import wolframalpha
import requests
import time
import math
import sqlite3
from bs4 import BeautifulSoup
import os
import concurrent.futures
from difflib import SequenceMatcher, get_close_matches



class ChatBot(Client):

    def onMessage(self, mid=None, author_id=None, message_object=None, thread_id=None, thread_type=ThreadType.USER, **kwargs):
        try:
            msg = str(message_object).split(",")[15][14:-1]

            if ("//video.xx.fbcdn" in msg):
                msg = msg

            else:
                msg = str(message_object).split(",")[19][20:-1]
        except:
            try:
                msg = (message_object.text).lower()
                print(msg)
            except:
                pass
        def sendMsg():
            if (author_id != self.uid):
                self.send(Message(text=reply), thread_id=thread_id,
                          thread_type=thread_type)

        def sendQuery():
            self.send(Message(text=reply), thread_id=thread_id,
                      thread_type=thread_type)
        if(author_id == self.uid):
            pass
        else:
            try:
                conn = sqlite3.connect("messages.db")
                c = conn.cursor()
                c.execute("""
                CREATE TABLE IF NOT EXISTS "{}" (
                    mid text PRIMARY KEY,
                    message text NOT NULL
                );

                """.format(str(author_id).replace('"', '""')))

                c.execute("""

                INSERT INTO "{}" VALUES (?, ?)

                """.format(str(author_id).replace('"', '""')), (str(mid), msg))
                conn.commit()
                conn.close()
            except:
                pass

        #def searchFiles(self):
         #   query = " ".join(msg.split()[2:])
          #  file_urls = []
           # url = "https://filepursuit.p.rapidapi.com/"

            #querystring = {"q": query, "filetype": msg.split()[1]}

            #headers = {
             #   'x-rapidapi-host': "filepursuit.p.rapidapi.com",
              #  'x-rapidapi-key': "801ba934d6mshf6d2ea2be5a6a40p188cbejsn09635ee54c45"
            #}

            #response = requests.request(
             #   "GET", url, headers=headers, params=querystring)

            #response = json.loads(response.text)
            #file_contents = response["files_found"]
            #try:
             #   for file in random.sample(file_contents, 10):
              #      file_url = file["file_link"]
               #     file_name = file["file_name"]
                #    self.send(Message(text=f'{file_name}\n Link: {file_url}'),
                 #             thread_id=thread_id, thread_type=ThreadType.USER)
            #except:
             #   for file in file_contents:
              #      file_url = file["file_link"]
               #     file_name = file["file_name"]
                #    self.send(Message(text=f'{file_name}\n Link: {file_url}'),
                 #             thread_id=thread_id, thread_type=ThreadType.USER)

       
        try:
            if("search pdfiiixxd" in msg):
                searchFiles(self)
            elif("download youtubiiixdde" in msg):
                headers = {
                    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
                link = "".join(msg.split()[-3:])
                yt_url = link
                print("yt", yt_url)
                try:
                    yt_url = yt_url.replace(
                        "youtu.be/", "www.youtube.com/watch?v=")
                except:
                    pass
                #yt_url = yt_url.replace("youtube", "clipmega")
                #url = requests.get(yt_url, headers=headers)
                #soup = BeautifulSoup(url.text, "html.parser")
                #link = soup.select(".btn-group > a")
                #link = link[0]
                #link = str(link)
                #indx = link.find("href=")
                #indx_l = link.find("extension=mp4")
                #link = link[indx+6:indx_l+13].replace("amp;", "")
                #link = link.replace(" ", "%20")
                #final_link = link
                #print("final", final_link)
                #self.sendRemoteFiles(
                 #   file_urls=final_link, message=None, thread_id=thread_id, thread_type=thread_type)
            #elif("sarkojouch imakojouge" in msg):
             #   imageSearch(self, msg)

            #elif("prokojougram tkojouo" in msg):
             #   programming_solution(self, msg)
            #elif("trakojounslate" in msg):
             #   reply = translator(self, msg, msg.split()[-1])

                #sendQuery()
            elif "weakojouther okojouf" in msg:
                indx = msg.index("weathkojouer okojouf")
                query = msg[indx+11:]
                reply = weather(query)
                sendQuery()
            elif "corokojouna okojouf" in msg:
                corona_details(msg.split()[2])
            elif ("calckojouulus" in msg):
                stepWiseCalculus(" ".join(msg.split(" ")[1:]))
            elif ("algekojoubra" in msg):
                stepWiseAlgebra(" ".join(msg.split(" ")[1:]))
            elif ("qkojouuery" in msg):
                stepWiseQueries(" ".join(msg.split(" ")[1:]))

            elif "fikojound" in msg:
                app_id = "Y98QH3-24PWX83VGA"
                client = wolframalpha.Client(app_id)
                query = msg.split()[1:]
                res = client.query(' '.join(query))
                answer = next(res.results).text
                reply = f'Answer: {answer.replace("sqrt", "√")}'
                sendQuery()

            elif ("searkojouch ukojouser" in msg or "seakojourch frikojoukojouend" in msg):
                searchForUsers(self)

            elif("mkojouute convekojoursation" in msg):
                try:
                    self.muteThread(mute_time=-1, thread_id=author_id)
                    reply = "xd 🔕"
                    sendQuery()
                except:
                    pass
            elif ("t3riii mkb" in msg):
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "M=^ 🐧 K 😛 3 '-,-' L@^ 🐧 D ^8^3 '-,-' 7 😃 !!(=p=)C^H=^()^ ❤ '-,-' UD K 😛 3 '-,-' ^8^^ 🐧 C^H=3 '-,-' 7 😃 3 '-,-' R!!(=+=) M=^ 🐧 K 😛 3 '-,-' ^8^H^()^ ❤ '-,-' XD3 '-,-' K 😛 ^()^ ❤ '-,-' 🦈 [__----------]] ❤ 😃 🦈 (Y) ❤ [[(#_L3G3ND_F4DD3B44ZZ__#_M9RK_0WN__FIIR3 ❤ :-0 (Y) ❤ p"
                sendMsg()
                time.sleep(60)
                reply = "❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ❤ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) ♥ 😃 😈 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_ H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) 🐧 (Y) (Y) 🐧 😈 #TH3_L3GEND_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M9RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = ":P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3 :P <3  (( M9RK 099 FIIR33 )) :D (Y) (Y) "
                sendMsg()
                time.sleep(60)
                reply = "[[ :) '' #PRIY99NSH+ TIIY9 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <('') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<('') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
            
    

        except Exception as e:
            print(e)

        self.markAsDelivered(author_id, thread_id)

    def onMessageUnsent(self, mid=None, author_id=None, thread_id=None, thread_type=None, ts=None, msg=None):

        if(author_id == self.uid):
            pass
        else:
            try:
                conn = sqlite3.connect("messages.db")
                c = conn.cursor()
                c.execute("""
                SELECT * FROM "{}" WHERE mid = "{}"
                """.format(str(author_id).replace('"', '""'), mid.replace('"', '""')))

                fetched_msg = c.fetchall()
                conn.commit()
                conn.close()
                unsent_msg = fetched_msg[0][1]

                if("//video.xx.fbcdn" in unsent_msg):

                    if(thread_type == ThreadType.USER):
                       
                        self.send(Message(text=reply), thread_id=thread_id,
                                  thread_type=thread_type)
                        self.sendRemoteFiles(
                            file_urls=unsent_msg, message=None, thread_id=thread_id, thread_type=ThreadType.USER)
                    elif(thread_type == ThreadType.GROUP):
                        user = self.fetchUserInfo(f"{author_id}")[
                            f"{author_id}"]
                        username = user.name.split()[0]
                        #reply = f"{username} just unsent a video"
                        self.send(Message(text=reply), thread_id=thread_id,
                                  thread_type=thread_type)
                        self.sendRemoteFiles(
                            file_urls=unsent_msg, message=None, thread_id=thread_id, thread_type=ThreadType.GROUP)
                elif("//scontent.xx.fbc" in unsent_msg):

                    if(thread_type == ThreadType.USER):
                       
                        self.send(Message(text=reply), thread_id=thread_id,
                                  thread_type=thread_type)
                        self.sendRemoteFiles(
                            file_urls=unsent_msg, message=None, thread_id=thread_id, thread_type=ThreadType.USER)
                    elif(thread_type == ThreadType.GROUP):
                        user = self.fetchUserInfo(f"{author_id}")[
                            f"{author_id}"]
                        username = user.name.split()[0]
                        #reply = f"{username} just unsent an image"
                        self.send(Message(text=reply), thread_id=thread_id,
                                  thread_type=thread_type)
                        self.sendRemoteFiles(
                            file_urls=unsent_msg, message=None, thread_id=thread_id, thread_type=ThreadType.GROUP)
                #else:
                 #   if(thread_type == ThreadType.USER):
                  #      reply = f"You just unsent a message:\n{unsent_msg} "
                   #     self.send(Message(text=reply), thread_id=thread_id,
                    #              thread_type=thread_type)
                    #elif(thread_type == ThreadType.GROUP):
                     #   user = self.fetchUserInfo(f"{author_id}")[
                      #      f"{author_id}"]
                       # username = user.name.split()[0]
                        #reply = f"{username} just unsent a message:\n{unsent_msg}"
                        #self.send(Message(text=reply), thread_id=thread_id,
                            #      thread_type=thread_type)

            except:
                pass

    #def onColorChange(self, mid=None, author_id=None, nSUW4R K3 P1LL3 :Dew_color=None, thread_id=None, thread_type=ThreadType.USER, **kwargs):
     #   reply = "You changed the theme ✌️😎"
      #  self.send(Message(text=reply), thread_id=thread_id,
       #           thread_type=thread_type

    #def onEmojiChange(self, mid=None, author_id=None, new_color=None, thread_id=None, thread_type=ThreadType.USER, **kwargs):
     #   reply = "You changed the emoji 😎. Great!"
      #  self.send(Message(text=reply), thread_id=thread_id,
       #           thread_type=thread_type)

    #def onImageChange(self, mid=None, author_id=None, new_color=None, thread_id=None, thread_type=ThreadType.USER, **kwargs):
     #   reply = "This image looks nice. 💕🔥
      #  self.send(Message(text=reply), thread_id=thread_id,
       #           thread_type=thread_type)

    #def onNicknameChange(self, mid=None, author_id=None, new_nickname=None, thread_id=None, thread_type=ThreadType.USER, **kwargs):
     #   reply = f"You just changed the nickname to {new_nickname} But why? 😁🤔😶"
      #  self.send(Message(text=reply), thread_id=thread_id,
       #           thread_type=thread_type)

    #def onReactionRemoved(self, mid=None, author_id=None, thread_id=None, thread_type=ThreadType.USER, **kwargs):
     #   reply = "You just removed reaction from the message."
      #  self.send(Message(text=reply), thread_id=thread_id,
       #           thread_type=thread_type)

    #def onCallStarted(self, mid=None, caller_id=None, is_video_call=None, thread_id=None, thread_type=None, ts=None, metadata=None, msg=None, ** kwargs):
     #   reply = "You just started a call 📞🎥"
      #  self.send(Message(text=reply), thread_id=thread_id,
       #           thread_type=thread_type)

    #def onCallEnded(self, mid=None, caller_id=None, is_video_call=None, thread_id=None, thread_type=None, ts=None, metadata=None, msg=None, ** kwargs):
     #   reply = "Bye 👋🙋‍"
      #  self.send(Message(text=reply), thread_id=thread_id,
       #           thread_type=thread_type)

    #def onUserJoinedCall(mid=None, joined_id=None, is_video_call=None,
     #                    thread_id=None, thread_type=None, **kwargs):
      #  reply = f"New user with user_id {joined_id} has joined a call"
       # self.send(Message(text=reply), thread_id=thread_id,
        #          thread_type=thread_type


cookies = {
    "sb": "xasyYmAoy1tRpMGYvLxgkHBF",
    "fr": "0NxayJuewRHQ30OX3.AWVJwIYNh0Tt8AJv6kSwDamhkoM.BiMrVd.Iu.AAA.0.0.BiMtVZ.AWXMVaiHrpQ",
    "c_user": "100061804071519",
    "datr": "xasyYs51GC0Lq5H5lvXTl5zA",
    "xs": "10%3AjOfnvsZ3MOB5bw%3A2%3A1666967565%3A-1%3A7714"
}


client = ChatBot("",
                 "", session_cookies=cookies)
print(client.isLoggedIn())

try:
    client.listen()
except:
    time.sleep(3)
    client.listen()
