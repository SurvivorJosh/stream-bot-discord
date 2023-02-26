import os
try:
    from fymjosh import Client, Status
    
except:
    os,system('pip install fymjosh')

token = input("Token?: ")
stream_name = input("Stream Name?: ")
stream_url = input("Stream URL?: ")

client = Client(Status.streaming(stream_name, stream_url))
client.run(token)
