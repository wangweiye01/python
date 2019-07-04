#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def describe_pet(pet_name, animal_type='dog'):
    """显示宠物的信息"""
    print("\nI hava a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet('wangwang')
describe_pet(pet_name='wangwang')
describe_pet(animal_type='cat', pet_name='miaomiao')