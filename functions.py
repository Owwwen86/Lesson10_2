# -*- coding: cp1251 -*-
import json
from Candidate import Candidate


def load_candidates(filename):
    """�������, ������� �������� ������ �� �����"""
    with open(filename, encoding='utf-8') as json_file:
        data = json.load(json_file)
    return data


def get_all(dates):
    """�������, ������� ������� ���� ����������"""
    arr = []
    for item in dates:
        candidate = Candidate(item['pk'], item['name'], item['picture'], item['position'], item['skills'])
        arr.append(candidate)
    return arr


def get_by_pk(pk, arr):
    """�������, ������� ������ ��������� �� pk"""
    for item in arr:
        if item.pk == pk:
            return item


def get_by_skill(skill_name, data):
    """�������, ������������ ���������� �� ������"""
    arr = []
    for item in data:
        skills_old = item.skills.split(',')
        skills = [skill.strip().lower() for skill in skills_old]
        for i in range(0, len(skills)):
            if skill_name.lower() == skills[i]:
                arr.append(item)
    return arr
