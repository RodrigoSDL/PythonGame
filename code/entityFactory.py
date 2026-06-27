#!/usr/bin/python
# -*- coding: utf-8 -*-
import random

from code.background import Background
from code.const import WINDOW_WIDTH, WINDOW_HEIGHT
from code.enemy import Enemy
from code.Player import Player


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str, position=(0, 0)):
        match entity_name:
            case 'Level1bg':
                list_bg = []
                for i in range(5):
                    list_bg.append(Background(f'Level1bg{i}', (0, 0)))
                    list_bg.append(Background(f'Level1bg{i}', (WINDOW_WIDTH, 0)))
                return list_bg
            case 'Level2bg':
                list_bg = []
                for i in range(7):
                    list_bg.append(Background(f'Level2bg{i}', (0, 0)))
                    list_bg.append(Background(f'Level2bg{i}', (WINDOW_WIDTH, 0)))
                return list_bg
            case 'Level3bg':
                list_bg = []
                for i in range(5):
                    list_bg.append(Background(f'Level3bg{i}', (0, 0)))
                    list_bg.append(Background(f'Level3bg{i}', (WINDOW_WIDTH, 0)))
                return list_bg
            case 'Player1':
                return Player('Player1', (10, WINDOW_HEIGHT / 2 - 30))
            case 'Player2':
                return Player('Player2', (10, WINDOW_HEIGHT / 2 + 30))
            case 'Enemy1':
                return Enemy('Enemy1', (WINDOW_WIDTH + 10, random.randint(30, WINDOW_HEIGHT - 30)))
            case 'Enemy2':
                return Enemy('Enemy2', (WINDOW_WIDTH + 10, random.randint(30, WINDOW_HEIGHT - 30)))
