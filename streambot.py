import kaneki
import asyncio

token = input("Token?: ")
stream_name = input("Stream Name?: ")
stream_url = input("Stream URL?: ")


client = kaneki.Client(kaneki.Status.streaming(stream_name, stream_url))
client.run(token)