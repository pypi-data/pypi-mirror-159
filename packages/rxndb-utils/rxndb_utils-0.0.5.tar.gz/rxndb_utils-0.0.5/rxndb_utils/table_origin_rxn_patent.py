#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2022/7/18 14:17
# @Author  : zhangbc0315@outlook.com
# @File    : table_origin_rxn_patent.py
# @Software: PyCharm

import json


from rxndb_utils.db_base import DBBase


class TableOriginRxnPatent:

    def __init__(self, db_base: DBBase):
        self._db_base = db_base
        self._cols = ['rid', 'source', 'rxn_smi', 'reactants', 'products', 'spectators', 'actions']

    def get_rxn_by_rid(self, rid: int):
        rxns = list(self._db_base.get_data_iter('origin.rxn_patent', self._cols, f'rid={rid}'))
        if len(rxns) == 0:
            return None
        rxn = rxns[0]
        self._reset_rxn(rxn)
        return rxn

    def get_rxns_by_rid_range(self, min_rid: int, max_rid: int):
        rxns = list(self._db_base.get_data_iter('origin.rxn_patent', self._cols,
                                                f'rid>={min_rid} and rid<{max_rid}'))
        rxns = [self._reset_rxn(rxn) for rxn in rxns]
        return rxns

    def get_all_rxns(self):
        for rxn in self._db_base.get_data_iter('origin.rxn_patent', self._cols, None):
            self._reset_rxn(rxn)
            yield rxn

    @classmethod
    def _reset_rxn(cls, rxn):
        rxn['source'] = json.loads(rxn['source'].replace('""', '"')[1:-1])
        cls._reset_rxn_with_key(rxn, 'reactants')
        cls._reset_rxn_with_key(rxn, 'products')
        cls._reset_rxn_with_key(rxn, 'spectators')
        cls._reset_rxn_with_key(rxn, 'actions')
        return rxn

    @classmethod
    def _reset_rxn_with_key(cls, rxn, key):
        if rxn[key] != '[]':
            rxn[key] = json.loads(rxn[key].replace('""', '"')[1:-1])
        else:
            rxn[key] = []


if __name__ == "__main__":
    dbb = DBBase('114.214.205.122', 1684, 'rxndb', 'postgres', '65zm]+7[d1Kb')
    torp = TableOriginRxnPatent(dbb)
    print(torp.get_rxn_by_rid(3))
