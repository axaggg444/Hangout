#This is the Hangout file
#import
import ursinanetworking
from ursinanetworking import *

Server = UrsinaNetworkingServer("127.0.0.1", 8000)
Easy = EasyUrsinaNetworkingServer(Server)

@Server.event
def onClientConnected(Client):
    print(Client, "has connected.")
    Easy.create_replicated_variable(
        f"player_{Client}",
        {"id" : Client, "position" : (0, 0, 0) }
    )

@Server.event
def onClientDisconnected(Client):
    print(Client, "has disconnected.")

@Server.event
def UpdatePos(Client, NewPos):
    Easy.update_replicated_variable_by_name(Client, NewPos)

@Server.event
def NewPos(Client, Content):
    Server.broadcast(Client, Content)

@Server.event
def MyPosition(Client, NewPos):
    Easy.update_replicated_variable_by_name(f"player_{Client}", "position", NewPos)

while True:
    Easy.process_net_events()