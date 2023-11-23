from ww_db import SQLITE
import json
from datetime import datetime
from PIL import Image
db = SQLITE('ww/db_ww.sqlite3')
posts = SQLITE("ww/db_ww_posts.sqlite3")
"""      
что надо сделать:
новости
"""
path = r"C:\Users\mxm20\my_projects\ww_w\ww\mainapp\media\p88913212.png"
idorder = '2023-10-13T11:50:24.410166' # sasha reselfdb > поменятб
username = "MetraMax"
print(f"{username.encode('UTF-8')}")
posts.create("views", "TEXT")
# {idnews: [author, zag, desk, created_time, viewscount] 
# admin + chat_id = {admin: admincreated_at: date, avatar: image, users: [users], messages: [[datetime, msg, author, changed], [datetime, msg, author,changed]]}