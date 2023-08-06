#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2022/7/9 21:23
# @Author  : zbc@mail.ustc.edu.cn
# @File    : table_mol.py
# @Software: PyCharm


from rxndb_utils.db_base import DBBase


class TableMol:

    def __init__(self, db_base: DBBase):
        self._db_base = db_base
        self._cols = ['mid', 'smiles', 'inchi']
        self._table_name = 'base.mol'

    def add_mol(self, smiles, inchi, mid: int = None, commit: bool = True):
        if mid is None:
            sql = f"insert into {self._table_name} (smiles, inchi) values ('{smiles}', '{inchi}')"
        else:
            sql = f"insert into {self._table_name} (mid, smiles, inchi) values ({mid}, '{smiles}', '{inchi}')"
        self._db_base.exec(sql, commit)

    def commit(self):
        self._db_base.commit()


if __name__ == "__main__":
    pass
