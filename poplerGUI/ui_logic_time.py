#! /usr/bin/env python
from PyQt4 import QtGui
from poplerGUI import class_inputhandler as ini
from poplerGUI import class_modelviewpandas as view
from poplerGUI import ui_dialog_time as uitime
from poplerGUI import ui_logic_preview as tprev
from poplerGUI.logiclayer import class_helpers as hlp
from poplerGUI.logiclayer import class_timeparse as tmpa
from logiclayer.datalayer import config as orm

class TimeDialog(QtGui.QDialog, uitime.Ui_Dialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.facade = None

        # Place holders for user inputs
        self.timelned = {}
        # Place holder: Data Model/ Data model view
        self.timemodel = None
        self.viewEdit = view.PandasTableModelEdit
        # Placeholders: Data tables
        self.timetable = None
        # Placeholder for maindata Orms
        self.timeorms = {}
        # Actions
        self.btnPreview.clicked.connect(self.submit_change)
        self.btnSaveClose.clicked.connect(self.submit_change)
        self.btnCancel.clicked.connect(self.close)

        # Update boxes/preview box
        self.message = QtGui.QMessageBox
        self.error = QtGui.QErrorMessage()
        self.preview = tprev.TablePreview()

    def submit_change(self):
        sender = self.sender()
        self.timelned = {
            'dayname': self.lnedDay.text(),
            'dayform': self.cboxDay.currentText(),
            'monthname': self.lnedMonth.text(),
            'monthform': self.cboxMonth.currentText(),
            'yearname': self.lnedYear.text(),
            'yearform': self.cboxYear.currentText(),
            'jd': self.ckJulian.isChecked(),
            'mspell': self.ckMonthSpelling.isChecked()
        }

        # Input handler
        self.timeini = ini.InputHandler(
            name='timeinfo', tablename='timetable',
            lnedentry=self.timelned)
        self.facade.input_register(self.timeini)

        # Initiating time parser class
        self.timetable = tmpa.TimeParse(
            self.facade._data, self.timelned)

        # Logger
        self.facade.create_log_record('timetable')
        self._log = self.facade._tablelog['timetable']            

        try:
            # Calling formater method
            timeview =self.timetable.formater()
        except Exception as e:
            print(str(e))
            self._log.debug(str(e))
            self.error.showMessage(
                'Could not format dates - ' +
                'Check entries for errors'
            )
            raise ValueError(
                'Could not format dates - ' +
                'Check entries for errors')
        self.facade._valueregister['sitelevels']

        if sender is self.btnPreview:
            timeview = timeview.applymap(str)
            self.timemodel = self.viewEdit(timeview)
            self.preview.tabviewPreview.setModel(self.timemodel)
            self.preview.show()

        elif sender is self.btnSaveClose:
            hlp.write_column_to_log(
                self.timelned, self._log, 'timetable'
            )
            try:
                timeview
                orm.convert_types(timeview, orm.rawtypes)
                self.facade.push_tables['timetable'] = (
                    timeview)
                assert timeview is not None
            except Exception as e:
                print(str(e))
                self._log.debug(str(e))
                self.error.showMessage(
                    'Could not convert data to integers')
                raise TypeError(
                    'Could not convert data to integers')
            self.close()