#!/usr/bin/python
# -*- coding:utf-8 -*-

from flask import Blueprint, request
from iceCon import ice_con
import json
import Ice
# Ice.loadSlice("./ice-sqlite.ice")
Ice.loadSlice("/code/tool/configTool/ice-sqlite.ice")
import YKArea

yk_blu = Blueprint('yk', __name__)


# 查找(遥控属性)
@yk_blu.route('/yk_data', methods=['POST'])
def get_yk_property_send():
    stationId = request.form.get("stationId")
    station = json.loads(stationId)
    DataCommand = ice_con()
    status, result = DataCommand.RPCGetYKProperty(station)
    ykproperty = []
    for i in range(len(result)):
        ykproperty.append({"ID": result[i].ID, "name": result[i].name,
                           "describe": result[i].describe, "ASDU": result[i].ASDU,
                           "wordPos": result[i].wordPos, "bitPos": result[i].bitPos,
                           "bitLength": result[i].bitLength, "EnablePoint": result[i].EnablePoint,
                           "EnableValue": result[i].EnableValue, "address": result[i].address})
    return json.dumps(ykproperty)


# 添加、修改(遥控属性)
@yk_blu.route('/set_yk', methods=['POST'])
def set_yk_property():
    DataCommand = ice_con()
    stationId = request.form.get("stationId")
    station = json.loads(stationId)
    newyk = request.form.get("data")
    YkProperty = json.loads(newyk)
    ykp = []
    for i in range(len(YkProperty)):
        ykp.append(json.loads(YkProperty[i]))
    ykproperty = []
    for j in range(len(ykp[1])):
        ID = ykp[0][j]
        name = ykp[1][j]
        describe = ykp[2][j]
        ASDU = ykp[3][j]
        wordPos = ykp[4][j]
        bitPos = ykp[5][j]
        bitLength = ykp[6][j]
        EnablePoint = ykp[7][j]
        EnableValue = ykp[8][j]
        address = ykp[9][j]
        if ID == "":
            ID = 1000
        if name == "":
            name = "请添加遥控名称"
        if describe == "":
            describe = "请描述遥控"
        if ASDU == "":
            ASDU = 0
        if wordPos == "":
            wordPos = 0
        if bitPos == "":
            bitPos = 0
        if bitLength == "":
            bitLength = 1
        if EnablePoint == "":
            EnablePoint = 0
        if EnableValue == "":
            EnableValue = 0
        if address == "":
            address = "0"
        ykpstruct = YKArea.DxPropertyYK(int(ID), name.encode("utf-8"),
                                        describe.encode("utf-8"), int(ASDU),
                                        int(wordPos), int(bitPos),
                                        int(bitLength), int(EnablePoint),
                                        int(EnableValue), address.encode("utf-8"))
        ykproperty.append(ykpstruct)
    DataCommand.RPCSetYKProperty(station, ykproperty)
    return '保存成功!'


# 删除(遥控属性)
@yk_blu.route('/delete_yk', methods=['POST'])
def delete_yk_data():
    DataCommand = ice_con()
    stationId = request.form.get("stationId")
    station = json.loads(stationId)
    ykIDs = request.form.get("ids")
    yk_IDs = json.loads(ykIDs)
    pIDs = []
    for i in range(len(yk_IDs)):
        pIDs.append(long(yk_IDs[i]))
    DataCommand.RPCDelYKProperty(station, pIDs)
    return '删除成功!'