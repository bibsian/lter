#! /usr/bin/env python
from pandas import read_sql
from collections import namedtuple
from poplerGUI.logiclayer.datalayer import config as orm

all = ['Merger']

class Merger(object):
    '''
    Class to help with table building that requires
    querying the database for primary keys that were
    autogenerated
    '''

    tabletuple = namedtuple(
        'TableData', 'orm pkey filterer identifier')

    def __init__(self, globalid):
        self.globalid = globalid
        self.tableq = {
            'maintable': self.tabletuple(
                orm.Maintable,
                orm.Maintable.lter_proj_site,
                orm.Maintable.siteid,
                orm.Maintable.metarecordid  
            ),
            'taxatable': self.tabletuple(
                orm.Taxatable,
                orm.Taxatable.taxaid,
                orm.Taxatable.lter_proj_site,
                None
            )
        }

    def query_database(self, tablename, tablefilterlist, qraw=None):
        '''
        General method to query the database tables
        by indexing primary keys and filerting results
        with a instance specific list of filters (tablefilter)
        '''
        table = self.tableq[tablename]
        session = orm.Session()
        if tablename == 'maintable':
            query = (
                session.query(table.orm).
                order_by(table.pkey).
                filter(table.filterer.in_(tablefilterlist)).
                filter(table.identifier == self.globalid)
            )
        elif tablename == 'taxatable':
            query = (
                session.query(table.orm).
                order_by(table.pkey).
                filter(table.filterer.in_(tablefilterlist))
            )
        session.close()
        querydf = read_sql(
            query.statement, query.session.bind)
        if qraw is True:
            return query
        else:
            return querydf