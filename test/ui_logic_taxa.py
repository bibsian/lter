from PyQt4 import QtGui
from collections import OrderedDict
import class_inputhandler as ini
import class_modelviewpandas as view
import ui_dialog_taxa as uitax
import ui_logic_preview as tprev
import class_helpers as hlp

class TaxaDialog(QtGui.QDialog, uitax.Ui_Dialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.facade = None
        # Place holders for user inputs
        self.taxalned = {}
        self.taxackbox = {}
        self.taxacreate = {}
        self.available = None
        self.null = None
        # Place holder: Data Model/ Data model view
        self.taxamodel = None
        self.viewEdit = view.PandasTableModelEdit
        # Placeholders: Data tables
        self.taxatable = None
        # Placeholder: Director (table builder), log
        self.taxadirector = None
        self._log = None
        # Placeholder for maindata Orms
        self.taxaorms = {}
        # Actions
        self.btnTaxasubmit.clicked.connect(self.submit_change)
        self.btnSaveClose.clicked.connect(self.submit_change)
        self.btnCancel.clicked.connect(self.close)

        # Update boxes/preview box
        self.message = QtGui.QMessageBox
        self.error = QtGui.QErrorMessage()
        self.preview = tprev.TablePreview()

    def submit_change(self):
        '''
        Method to take user input for the taxa
        dialog box, pass the information to the user facade,
        create the taxa table, and then rename colums
        as necessary.
        '''
        sender = self.sender()
        self.taxalned = OrderedDict((
            ('sppcode', self.lnedSppCode.text().strip()),
            ('kingdom', self.lnedKingdom.text().strip()),
            ('phylum', self.lnedPhylum.text().strip()),
            ('clss', self.lnedClass.text().strip()),
            ('order', self.lnedOrder.text().strip()),
            ('family', self.lnedFamily.text().strip()),
            ('genus', self.lnedGenus.text().strip()),
            ('species', self.lnedSpp.text().strip())
        ))
        # Log input (put in after test)
        self.facade._colinputlog['taxainfo'] = self.taxalned

        self.taxackbox = OrderedDict((
            ('sppcode', self.ckSppCode.isChecked()),
            ('kingdom', self.ckKingdom.isChecked()),
            ('phylum', self.ckPhylum.isChecked()),
            ('clss', self.ckClass.isChecked()),
            ('order', self.ckOrder.isChecked()),
            ('family', self.ckFamily.isChecked()),
            ('genus', self.ckGenus.isChecked()),
            ('species', self.ckSpp.isChecked())
        ))
        self.taxacreate = {
            'taxacreate': self.ckCreateTaxa.isChecked()
        }

        self.available = [
            x for x,y in zip(
                list(self.taxalned.keys()), list(
                    self.taxackbox.values()))
            if y is True
        ]

        self.taxaini = ini.InputHandler(
            name='taxainfo',
            tablename='taxatable',
            lnedentry=hlp.extract(self.taxalned, self.available),
            checks=self.taxacreate
        )

        self.facade.input_register(self.taxaini)
        self.facade.create_log_record('taxatable')
        self._log = self.facade._tablelog['taxatable']

        try:
            print('about to make taxa table')
            self.taxadirector = self.facade.make_table('taxainfo')
            assert self.taxadirector._availdf is not None
        except Exception as e:
            print(str(e))
            self._log.debug(str(e))
            self.error.showMessage(
                'Column(s) not identified')
            raise AttributeError('Column(s) not identified')

        self.taxatable = self.taxadirector._availdf.copy()
        self.taxamodel = self.viewEdit(self.taxatable)

        if sender is self.btnTaxasubmit:
            self.preview.tabviewPreview.setModel(self.taxamodel)
            self.preview.show()

        elif sender is self.btnSaveClose:
            hlp.write_column_to_log(
                self.taxalned, self._log, 'taxatable')                
            # Log input (put in after test)
            self.facade.push_tables['taxatable'] = self.taxatable
            self.close()