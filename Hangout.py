#This is the main game file
#import
from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from ursina.shaders.lit_with_shadows_shader import lit_with_shadows_shader
from ursinanetworking import *
import sys

Client = UrsinaNetworkingClient("127.0.0.1", 8000)
Easy = EasyUrsinaNetworkingClient(Client)

app = Ursina()

player = FirstPersonController()

Sky()

ground = Entity(model="plane", collider="mesh", scale=(100, 1, 100), texture="grass", shader=lit_with_shadows_shader)

def input(key):
    if key == "escape":
        sys.exit(0)
    
    if held_keys["shift"]:
        player.speed = 20
    else:
        player.speed = 10

@Client.event
def onConnectionEstablished():
    print("Connected!")

def update():
    Easy.process_net_events()

app.run()