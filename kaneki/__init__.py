
import os, time, sys

try:
    import websocket
except:
    os.system("pip install websocket")
    
try:
    import requests
    
except:
    os.system("pip install requests")
    
try:
    import threading
except:
    os.system("pip install threading")
    
try:
    import json
except:
    print("COULD NOT IMPOET JSON")

try:
    import logging
except:
    os.system("pip install logging")


logging.basicConfig(
    level=logging.INFO,
    format="\033[38;5;196m[\033[0m%(asctime)s.%(msecs)03d\033[38;5;196m] \033[0m%(message)s\033[0m",
    datefmt="%H:%M:%S"
)

class Status:
    

    def streaming(stream_name:str, atream_url:str):
        return {
            "name": stream_name,
            "type": 1,
            "url": atream_url
        }

    def playing(game_name:str):
        return {
            "name": game_name,
            "type": 0,
        
        }       
    def watching(movie_name:str):
        return {
            "name": movie_name,
            "type": 3,
            
        }
        
    def listening(song_name:str):
        return {
            "name": song_name,
            "type": 2,
           
        }
        
        
class ImproperTokenError(Exception):
    def __init__(self, message="Improper Token has Been Passed"):
        self.message = message
        super().__init__(self.message)
    pass
        
class Client:
    def __init__(self, jsrp):
        self.token = ""
        self.jsrp = jsrp
        self.ws = websocket.WebSocket()
     
    
     
    def run(self, token:str):
        self.token = token
        r = requests.get(f"https://discord.com/api/v10/users/@me", headers={"Authorization": self.token})
        if r.status_code == 200:
            logging.info("token : {self.token}")
            
        elif r.status_code == 401:
            raise ImproperTokenError
            
        
        self.ws.connect("wss://gateway.discord.gg/?v=8&encoding=json")
        res = self.ws.recv()
        h = json.loads(res)
        heartbeat = int(h["d"]["heartbeat_interval"])
        
        self.ws.send(json.dumps({"op": 2, "d": {"token": self.token, "properties": {"$os": sys.platform, "$browser": "Discord", "$device": "desktop"}, "presence": {"game": self.jsrp, "status": "online", "since": 0, "afk": False}}, "s": None, "t": None}))
        
        beats = {"op": 1, "d": None}
        while True:
            self.ws.send(json.dumps(beats))
            time.sleep(heartbeat / 1000)
            
    
 

