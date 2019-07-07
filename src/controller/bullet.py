from math import exp, ceil
from pygame import math
from copy import deepcopy

from environment import variables as gvar
from environment.instances import window, keyboard, store

from classes.entity import Entity
from .player import player
from .enemy import enemy_mtx

bullet_mtx = []
bullet_vel = math.Vector2(0)
player_can_shoot = True
bullet_cooldown = gvar.BULLET_COOLDOWN


def reset():
    global bullet_mtx
    global bullet_vel
    global player_can_shoot
    global bullet_cooldown

    bullet_mtx.clear()
    bullet_vel = math.Vector2(0)
    player_can_shoot = True
    bullet_cooldown = gvar.BULLET_COOLDOWN

    store.dispatch("score", value=0)

def run():
    global bullet_mtx
    global bullet_vel
    global player_can_shoot
    global bullet_cooldown

    # DEFAULT
    bullet_vel.update(0)
    # PLAYER SHOOT
    if player_can_shoot == False and bullet_cooldown >= 0:
        bullet_cooldown -= 5
    if bullet_cooldown <= 0:
        player_can_shoot = True
        bullet_cooldown = gvar.BULLET_COOLDOWN

    if (
        keyboard.key_pressed("left")
        and keyboard.key_pressed("right") == False
        and player_can_shoot == True
    ):
        bullet_vel.x = -1
    if (
        keyboard.key_pressed("right")
        and keyboard.key_pressed("left") == False
        and player_can_shoot == True
    ):
        bullet_vel.x = 1
    if (
        keyboard.key_pressed("up")
        and keyboard.key_pressed("down") == False
        and player_can_shoot == True
    ):
        bullet_vel.y = -1
    if (
        keyboard.key_pressed("down")
        and keyboard.key_pressed("up") == False
        and player_can_shoot == True
    ):
        bullet_vel.y = 1

    if bullet_vel != math.Vector2(0):
        bullet_vel.normalize_ip()
        bullet_vel *= gvar.BULLET_VELOCITY
        bullet = store.get("player").shoot(
            "./src/assets/actors/bullet/bullet.png", 1, deepcopy(bullet_vel)
        )
        bullet_mtx.append(bullet)
        player_can_shoot = False

    # BULLET COLLISION
    for enemy in store.get("enemy_mtx"):
        for bullet in bullet_mtx:
            if bullet.collide(enemy):
                enemy.life -= store.get("player").strenght
                bullet_mtx.remove(bullet)
                if enemy.life <= 0:
                    store.get("enemy_mtx").remove(enemy)
                    if enemy.is_boss:
                        store.dispatch("score", lambda score: score + 200)
                    else:
                        aux_score = get_score(store.get("wave"))
                        store.dispatch("score", lambda score: score + aux_score)
    # DESTROY BULLET
    for bullet in bullet_mtx:
        if (
            bullet.animation.x >= gvar.WIDTH
            or bullet.animation.x <= 0
            or bullet.animation.y >= gvar.HEIGHT
            or bullet.animation.y <= 48
        ):
            bullet_mtx.remove(bullet)

    # DRAW
    if len(bullet_mtx) != 0:
        for bullet in bullet_mtx:
            bullet.update()
            bullet.render()


def get_score(x):
    if x <= 25:
        return ceil(0.85 * exp(0.16 * x))
    else:
        return 50
