# -*- coding: utf-8 -*-
"""
@Author: HuangJianYi
@Date: 2021-07-22 10:59:39
@LastEditTime: 2022-01-24 10:14:47
@LastEditors: HuangJianYi
@Description: 
"""
#此文件由rigger自动生成
from seven_framework.mysql import MySQLHelper
from seven_framework.base_model import *
from seven_cloudapp_frame.models.cache_model import *


class UserAccountModel(CacheModel):
    def __init__(self, db_connect_key='db_cloudapp', sub_table=None, db_transaction=None, context=None):
        super(UserAccountModel, self).__init__(UserAccount, sub_table)
        self.db = MySQLHelper(config.get_value(db_connect_key))
        self.db_connect_key = db_connect_key
        self.db_transaction = db_transaction
        self.db.context = context

    #方法扩展请继承此类


class UserAccount:

    def __init__(self):
        super(UserAccount, self).__init__()
        self.id = 0  # id
        self.union_id = ""  # union_id
        self.open_id = ""  # open_id
        self.user_nick = ""  # 用户昵称
        self.user_nick_encrypt = ""  # 昵称加密值
        self.avatar = ""  # 头像
        self.user_state = 0  # 用户状态（0-正常，1-黑名单）
        self.full_name = ""  # 姓名
        self.telephone = ""  #电话号码
        self.certificate_type = 1  #证件类型(1身份证2军官证)
        self.certificate_no = "" #证件号码
        self.relieve_date = "1900-01-01 00:00:00"  # 解禁时间
        self.create_date = "1900-01-01 00:00:00"  # 创建时间
        self.modify_date = "1900-01-01 00:00:00"  # 修改时间

    @classmethod
    def get_field_list(self):
        return ['id', 'union_id', 'open_id', 'user_nick', 'user_nick_encrypt', 'avatar', 'user_state','full_name','telephone','certificate_type','certificate_no', 'relieve_date', 'create_date', 'modify_date']

    @classmethod
    def get_primary_key(self):
        return "id"

    def __str__(self):
        return "user_account_tb"
