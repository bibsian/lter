#! /usr/bin/env python
import sys
from pandas import read_csv

__all__ = ['MetaVerifier']

class MetaVerifier(object):
    """
    This is going to be a Singleton pattern i.e. 
    only one instance of this class will be created 
    in the whole program.

    Keyword Arguments
    -----------------
    idnumber: integer
    lterloc: string
    metaurl: string
    """

    if sys.platform == "darwin":
        metapath = (
        "/Users/bibsian/Desktop/git/database-development/poplerGUI/" +
        "Metadata_and_og_data/Cataloged_Data_Current_sorted.csv")

    elif sys.platform == "win32":
        metapath = (
        "C:\\Users\MillerLab\\Desktop\\database-development" +
        "\\poplerGUI\\Metadata_and_og_data\\Cataloged_Data_Current_sorted.csv")

    _meta = read_csv(metapath, encoding='iso-8859-11')

    def __init__(self,  inputclsinstance):
        self.idnumber = int(inputclsinstance.lnedentry['globalid'])
        self.lterloc = inputclsinstance.lnedentry['lter']
        self.metaurl = inputclsinstance.lnedentry['metaurl']


    def verify_entries(self):
        '''
        This method is going to be used to verify
        the user input into the program. Ensuring that
        all the parameter supplied match a given record
        in the metadata dataframe.
        '''
        if None in (self.idnumber, self.lterloc, self.metaurl):
            raise AttributeError(
                'Not all attributes have been set. Please enter' +
                'the globalid, lter location, and metadata url.')
        else:
            try:
                assert self.idnumber > 0
            except:
                raise AttributeError(
                    'Plese enter the globalid number.')

            try:

                assert (self._meta.loc[
                    self._meta['global_id']== self.idnumber][
                            'global_id'] == 
                        self.idnumber).bool() is True

                assert (self._meta.loc[
                    self._meta['global_id']== self.idnumber][
                        'lter'] ==
                        self.lterloc).bool() is True

                assert (self._meta.loc[
                    self._meta['global_id']== self.idnumber][
                            'site_metadata']
                        == self.metaurl).bool() is True

                return True
            except:
                raise LookupError(
                    "The verification attributes have not been set" +
                    " correctly. Please check values for the " +
                    "global_id, LTER location, and metadata url.")
