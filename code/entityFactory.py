#!/usr/bin/python
# -*- coding: utf-8 -*-
from code.background import Background
from code.const import WINDOW_WIDTH


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str, position=(0,0)):
        match entity_name:
            case'Fase_A_':
                list_bg = []
                for i in range(1,5):
                    list_bg.append(Background(f'Fase_A_{i}', (0, 0)))
                    list_bg.append(Background(f'Fase_A_{i}', (WINDOW_WIDTH, 0)))
                return list_bg


