#!usr/bin/env python
import pytest
import pandas as pd
import abc
import sys, os
sys.path.append(os.path.realpath(os.path.dirname(__file__)))
import class_inputhandler as ini
import class_userfacade as face
from class_helpers import *

@pytest.fixture
def AbstractTableBuilder():
    class AbstractTableBuilder(object):
        '''
        Abstrac class that will be used to implement
        a builder design pattern with all the tables that
        must be concatenated
        '''
        __meta__ = abc.ABCMeta

        # List of column names within each table of the database
        climaterawtable = {
            'columns': [
                'title', 'stationid', 'year', 'month', 'day',
                # temp
                'avetempobs', 'avetempmeasure',
                'mintempobs', 'mintempmeasure',
                'maxtempobs', 'maxtempmeasure',
                # precip
                'aveprecipobs', 'aveprecipmeasure',
                'minprecipobs', 'minprecipmeasure',
                'maxprecipobs', 'maxprecipmeasure',
                # wind
                'avewindobs', 'avewindmeasure',
                'minwindobs', 'minwindmeasure',
                'maxwindobs', 'maxwindmeasure',
                # light
                'avelightobs', 'avelightmeasure',
                'minlightobs', 'minlightmeasure',
                'maxlightobs', 'maxlightmeasure',
                # water temp
                'avewatertempobs', 'avewatertempmeasure',
                'minwatertempobs', 'minwatertempmeasure',
                'maxwatertempobs', 'maxwatertempmeasure',
                # ph
                'avephobs', 'avephmeasure',
                'minphobs', 'minphmeasure',
                'maxphobs', 'maxphmeasure',
                # cond
                'avecondobs', 'avecondmeasure',
                'mincondobs', 'mincondmeasure',
                'maxcondobs', 'maxcondmeasure',
                # turbidity
                'aveturbidityobs', 'aveturbiditymeasure',
                'minturbidityobs', 'minturbiditymeasure',
                'maxturbidityobs', 'maxturbiditymeasure',
                # other
                'covariates'],
            'time': True,
            'cov': True,
            'depend': False
        }
        stationtable = {
            'columns': ['lterid', 'lat', 'lng', 'descript'],
            'time': False,
            'cov': False,
            'depend': False
        }
        sitetable = {
            'columns': ['lterid','siteid', 'lat', 'lng', 'descript'],
            'time': False,
            'cov': False,
            'depend': False
        }
        
        maintable = {
            'columns': [
                'metarecordid', 'title', 'samplingunits',
                'samplingprotocol', 'structured', 'studystartyr',
                'studyendyr', 'siteid',
                'sitestartyr', 'siteendyr', 'samplefreq', 'totalobs',
                'studytype', 'community', 'uniquetaxaunits',
                # Spatial repliaction attributes
                'sp_rep1_ext', 'sp_rep1_ext_units', 'sp_rep1_label',
                'sp_rep1_uniquelevels',
                'sp_rep2_ext', 'sp_rep2_ext_units', 'sp_rep2_label',
                'sp_rep2_uniquelevels',
                'sp_rep3_ext', 'sp_rep3_ext_units', 'sp_rep3_label',
                'sp_rep3_uniquelevels',
                'sp_rep4_ext', 'sp_rep4_ext_units', 'sp_rep4_label',
                'sp_rep4_uniquelevels',
                'authors', 'authors_contact', 'metalink', 'knbid'],
            'time': False,
            'cov': False,
            'depend': True
        }
        taxatable = {
            'columns': [
                'projid', 'sppcode', 'kingdom', 'phylum', 'clss',
                'order','family', 'genus', 'species', 'authority'],
            'time': False,
            'cov': False,
            'depend': False
        }
        rawtable = {
            'columns': [
                'taxaid', 'projid', 'year', 'month', 'day',
                'spt_rep1', 'spt_rep2', 'spt_rep3', 'spt_rep4',
                'structure', 'individ', 'unitobs', 'covariates'],
            'time': True,
            'cov': True ,
            'depend': False
        }

        tabledict = {
            'climaterawtable': climaterawtable,
            'stationtable': stationtable,
            'sitetable': sitetable,
            'maintable': maintable,
            'taxatable': taxatable,
            'rawtable': rawtable
        }

        def get_table_name(self):
            return self._inputs.tablename

        def get_columns(self):
            return self.tabledict[
                self._inputs.tablename]['columns']

        def get_available_columns(self):
            return list(self._inputs.lnedentry.values())
        
        def get_null_columns(self):
            availcol = list(self._inputs.lnedentry.keys())
            allcol = self.tabledict[
                self._inputs.tablename]['columns']
            return [x for x in allcol if x not in availcol]

        def get_time_status(self):
            return  self.tabledict[
                self._inputs.tablename]['time']

        @abc.abstractmethod
        def get_time_data(self):
            pass
        
        def get_cov_status(self):
            return self.tabledict[
                self._inputs.tablename]['cov']

        @abc.abstractmethod
        def get_cov_data(self):
            pass

        
        def get_dependent_status(self):
            return self.tabledict[
                self._inputs.tablename]['depend']
        
        @abc.abstractmethod
        def get_merged_foreign_data(self):
            pass

        @abc.abstractmethod
        def get_dataframe(self):
            pass
            
    return AbstractTableBuilder

@pytest.fixture
def SiteTableBuilder(AbstractTableBuilder):
    class SiteTableBuilder(AbstractTableBuilder):
        '''
        Concrete table builder implementation: Site
        Note, no get methods because there is no
        alternate informatoin needed
        '''

        def get_dataframe(self, dataframe, acols, nullcols, dbcol):
            try:
                assert acols is not None
            except Exception as e:
                print(str(e))
                raise AssertionError('Columns names not set')
            try:
                assert dataframe is not None
            except Exception as e:
                print(str(e))
                raise AssertionError('Raw dataframe not set')
            if 'lterid' in dbcol:
                dbcol.remove('lterid')
            else:
                pass
            if 'lterid' in nullcols:
                nullcols.remove('lterid')
            else:
                pass
            uniquesubset = dataframe[acols]
            nullsubset = produce_null_df(
                ncols=len(nullcols),
                colnames=nullcols,
                dflength=len(uniquesubset),
                nullvalue='NaN')
            
            concat =  pd.concat(
                [uniquesubset, nullsubset], axis=1).reset_index(
                    drop=True)
            final = concat.drop_duplicates().reset_index(drop=True) 
            final.columns =dbcol
            return final
        
    return SiteTableBuilder


@pytest.fixture
def DatabaseTable():
    class DatabaseTable:
        def __init__(self):
            self._name = None
            self._cols = None
            self._null = None
            self._availcols = None
            self._availdf = None
            self._time = None
            self._timedf = None
            self._cov = None
            self._covdf = None
            self._depend = None
            self._dependdf = None
            self._foreigndf = None

        def set_table_name(self, tablename):
            self._name = tablename

        def set_columns(self, colnames):
            self._cols = colnames

        def set_available_columns(self, acols):
            self._availcols = acols
        
        def set_null_columns(self, nullcol):
            self._null = nullcol

        def set_dataframe(self, availdf):
            self._availdf = availdf
            
        def set_time_status(self, timebool):
            self._time = timebool

        def set_cov_status(self, covbool):
            self._cov = covbool

        def set_dependent_status(self, dependitems):
            self._depend = dependitems



    return DatabaseTable


@pytest.fixture
def TableDirector(DatabaseTable):

    class TableDirector:
        '''Constructs database tables'''
        _inputs = None
        _name = None
        _builder = None
        _rawdata = None
        def set_user_input(self, userinputcls):
            try:
                self._inputs = userinputcls
            except Exception as e:
                print(str(e))
                raise AttributeError('Incorrect user input class')

        def set_builder(self, builder):
            self._builder = builder
            try:
                assert self._inputs is not None
            except Exception as e:
                print(str(e))
                raise AssertionError('User input not set')

            self._builder._inputs = self._inputs

        def set_data(self, dataframe):
            self._rawdata = dataframe
            try:
                assert self._rawdata is not None
            except Exception as e:
                print(str(e))
                raise AssertionError('Data not set')

        def get_database_table(self):
            ''' Initiates a concrete table class'''
            dbtable = DatabaseTable()
            try:
                assert self._builder is not None
            except Exception as e:
                print(str(e))
                raise AttributeError('Builder type not set')
            
            # ---Starts build process--- #
            # Table name
            table = self._builder.get_table_name()
            dbtable.set_table_name(table)

            columns = self._builder.get_columns()
            dbtable.set_columns(columns)

            acolumns = self._builder.get_available_columns()
            dbtable.set_available_columns(acolumns)
            
            nullcol = self._builder.get_null_columns()
            dbtable.set_null_columns(nullcol)

            adata = self._builder.get_dataframe(
                self._rawdata, acolumns, nullcol, columns)
            dbtable.set_dataframe(adata)
            
            time = self._builder.get_time_status()
            dbtable.set_time_status(time)

            cov = self._builder.get_cov_status()
            dbtable.set_cov_status(cov)

            dep = self._builder.get_dependent_status()
            dbtable.set_dependent_status(dep)
            
            return dbtable

    return TableDirector

@pytest.fixture
def user_input():
    lned = {'siteid': 'SITE'}
    user_input = ini.InputHandler(
        name='siteinfo', tablename='sitetable', lnedentry=lned)
    return user_input

@pytest.fixture
def df():
    return pd.read_csv('raw_data_test.csv')
    
def test_build(SiteTableBuilder, TableDirector, user_input, df):
    '''
    Testing builder classes
    '''
    facade = face.Facade()
    facade.input_register(user_input)
    face_input = facade._inputs[user_input.name]
    assert (isinstance(face_input, ini.InputHandler)) is True

    sitetable = SiteTableBuilder()
    assert (isinstance(sitetable, SiteTableBuilder)) is True

    director = TableDirector()
    assert (isinstance(director, TableDirector)) is True
    director.set_user_input(face_input)
    director.set_builder(sitetable)
    director.set_data(df)

    sitetab = director.get_database_table()
    showsite = sitetab._availdf
    assert (isinstance(showsite, pd.DataFrame)) is True
    
def test_error_builds(SiteTableBuilder, TableDirector, user_input):
    pass
