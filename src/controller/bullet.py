from pygame import math
from copy import deepcopy

from environment import variables as gvar
from environment.instances import window, keyboard

from classes.entity import Entity
from .player import player

bullet_mtx = []

bullet_vel = math.Vector2(0)
player_can_shoot = True
player_cooldown = gvar.PLAYER_COOLDOWN


def run():
    global bullet_mtx
    global bullet_vel
    global player_can_shoot
    global player_cooldown

    # DEFAULT
    bullet_vel.update(0)
    # PLAYER SHOOT
    if player_can_shoot == False and player_cooldown >= 0:
        player_cooldown -= 5
    if player_cooldown <= 0:
        player_can_shoot = True
        player_cooldown = gvar.PLAYER_COOLDOWN

    if keyboard.key_pressed("a") and keyboard.key_pressed("d") == False and player_can_shoot == True:
        bullet_vel.x = -1
    if keyboard.key_pressed("d") and keyboard.key_pressed("a") == False and player_can_shoot == True:
        bullet_vel.x = 1
    if keyboard.key_pressed("w") and keyboard.key_pressed("s") == False and player_can_shoot == True:
        bullet_vel.y = -1
    if keyboard.key_pressed("s") and keyboard.key_pressed("w") == False and player_can_shoot == True:
        bullet_vel.y = 1

    if bullet_vel != math.Vector2(0):
        bullet_vel.normalize_ip()
        bullet_vel *= gvar.BULLET_VELOCITY
        bullet_mtx.append(player.shoot(
            "./src/assets/actors/bullet/bullet.png", 1, deepcopy(bullet_vel)))
        player_can_shoot = False

    if len(bullet_mtx) != 0:
        print(bullet_mtx[0].velocity)
        for bullet in bullet_mtx:
            bullet.update()
            bullet.render()
