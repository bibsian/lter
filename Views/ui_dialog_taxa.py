# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/bibsian/Desktop/git/database-development/Views/ui_dialog_taxa.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(976, 693)
        Dialog.setStyleSheet(_fromUtf8(".QLabel{\n"
"    background: None;\n"
"    padding: 0px;\n"
"    margin: 0px;\n"
"}\n"
".QComboBox {\n"
"    border: 1px solid gray;\n"
"    border-radius: 7px;\n"
"    padding: 2px;\n"
"    padding-left: 15px;\n"
"    background: #EEEEEE;\n"
"}\n"
".QFrame, .QWidget{\n"
"    border-radius: 7;\n"
"    background: white;\n"
"}    \n"
"\n"
"\n"
"\n"
".QLineEdit{\n"
"    padding: 1px;\n"
"    border-style: solid;\n"
"    border: 1px solid black;\n"
"    border-radius: 8px;\n"
"    margin: 0px;\n"
"}\n"
"\n"
".QPushButton {\n"
"    color: black;\n"
"    background: #EEEEEE;\n"
"    border-width: 1px;\n"
"    border-color: black;\n"
"    border-style: solid;\n"
"    border-radius: 7;\n"
"    margin-top: 0px;\n"
"    margin-left: 5px;\n"
"    margin-right:5px;    \n"
"    padding-left: 5px;\n"
"    padding-right: 5px;\n"
"    padding-top: 3px;\n"
"    padding-bottom: 3px;\n"
"}\n"
"\n"
"\n"
""))
        self.verticalLayout_6 = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.verticalLayout_5 = QtGui.QVBoxLayout()
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.frame = QtGui.QFrame(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.frame)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem = QtGui.QSpacerItem(13, 335, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        spacerItem1 = QtGui.QSpacerItem(378, 5, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem1)
        self.groupBox = QtGui.QGroupBox(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox.setFont(font)
        self.groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.ckCreateTaxa = QtGui.QCheckBox(self.groupBox)
        self.ckCreateTaxa.setObjectName(_fromUtf8("ckCreateTaxa"))
        self.verticalLayout.addWidget(self.ckCreateTaxa)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.formLayout_16 = QtGui.QFormLayout()
        self.formLayout_16.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_16.setObjectName(_fromUtf8("formLayout_16"))
        self.lnedSubclass = QtGui.QLineEdit(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lnedSubclass.sizePolicy().hasHeightForWidth())
        self.lnedSubclass.setSizePolicy(sizePolicy)
        self.lnedSubclass.setObjectName(_fromUtf8("lnedSubclass"))
        self.formLayout_16.setWidget(2, QtGui.QFormLayout.SpanningRole, self.lnedSubclass)
        self.ckSubclass = QtGui.QCheckBox(self.groupBox)
        self.ckSubclass.setObjectName(_fromUtf8("ckSubclass"))
        self.formLayout_16.setWidget(1, QtGui.QFormLayout.LabelRole, self.ckSubclass)
        self.gridLayout.addLayout(self.formLayout_16, 1, 3, 1, 1)
        self.formLayout_9 = QtGui.QFormLayout()
        self.formLayout_9.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_9.setObjectName(_fromUtf8("formLayout_9"))
        self.ckSubphylum = QtGui.QCheckBox(self.groupBox)
        self.ckSubphylum.setObjectName(_fromUtf8("ckSubphylum"))
        self.formLayout_9.setWidget(0, QtGui.QFormLayout.LabelRole, self.ckSubphylum)
        self.lnedSubphylum = QtGui.QLineEdit(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lnedSubphylum.sizePolicy().hasHeightForWidth())
        self.lnedSubphylum.setSizePolicy(sizePolicy)
        self.lnedSubphylum.setObjectName(_fromUtf8("lnedSubphylum"))
        self.formLayout_9.setWidget(1, QtGui.QFormLayout.SpanningRole, self.lnedSubphylum)
        self.gridLayout.addLayout(self.formLayout_9, 1, 2, 1, 1)
        self.formLayout_14 = QtGui.QFormLayout()
        self.formLayout_14.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_14.setObjectName(_fromUtf8("formLayout_14"))
        self.ckSubdivision = QtGui.QCheckBox(self.groupBox)
        self.ckSubdivision.setObjectName(_fromUtf8("ckSubdivision"))
        self.formLayout_14.setWidget(0, QtGui.QFormLayout.LabelRole, self.ckSubdivision)
        self.lnedSubdivision = QtGui.QLineEdit(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lnedSubdivision.sizePolicy().hasHeightForWidth())
        self.lnedSubdivision.setSizePolicy(sizePolicy)
        self.lnedSubdivision.setObjectName(_fromUtf8("lnedSubdivision"))
        self.formLayout_14.setWidget(1, QtGui.QFormLayout.LabelRole, self.lnedSubdivision)
        self.gridLayout.addLayout(self.formLayout_14, 0, 1, 1, 1)
        self.formLayout_10 = QtGui.QFormLayout()
        self.formLayout_10.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_10.setObjectName(_fromUtf8("formLayout_10"))
        self.ckSubkingdom = QtGui.QCheckBox(self.groupBox)
        self.ckSubkingdom.setObjectName(_fromUtf8("ckSubkingdom"))
        self.formLayout_10.setWidget(0, QtGui.QFormLayout.LabelRole, self.ckSubkingdom)
        self.lnedSubkingdom = QtGui.QLineEdit(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lnedSubkingdom.sizePolicy().hasHeightForWidth())
        self.lnedSubkingdom.setSizePolicy(sizePolicy)
        self.lnedSubkingdom.setObjectName(_fromUtf8("lnedSubkingdom"))
        self.formLayout_10.setWidget(1, QtGui.QFormLayout.SpanningRole, self.lnedSubkingdom)
        self.gridLayout.addLayout(self.formLayout_10, 1, 0, 1, 1)
        self.formLayout_15 = QtGui.QFormLayout()
        self.formLayout_15.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_15.setObjectName(_fromUtf8("formLayout_15"))
        self.ckSuperphylum = QtGui.QCheckBox(self.groupBox)
        self.ckSuperphylum.setObjectName(_fromUtf8("ckSuperphylum"))
        self.formLayout_15.setWidget(0, QtGui.QFormLayout.LabelRole, self.ckSuperphylum)
        self.lnedSuperphylum = QtGui.QLineEdit(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lnedSuperphylum.sizePolicy().hasHeightForWidth())
        self.lnedSuperphylum.setSizePolicy(sizePolicy)
        self.lnedSuperphylum.setObjectName(_fromUtf8("lnedSuperphylum"))
        self.formLayout_15.setWidget(1, QtGui.QFormLayout.SpanningRole, self.lnedSuperphylum)
        self.gridLayout.addLayout(self.formLayout_15, 0, 2, 1, 1)
        self.formLayout_13 = QtGui.QFormLayout()
        self.formLayout_13.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_13.setObjectName(_fromUtf8("formLayout_13"))
        self.lnedDivision = QtGui.QLineEdit(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lnedDivision.sizePolicy().hasHeightForWidth())
        self.lnedDivision.setSizePolicy(sizePolicy)
        self.lnedDivision.setObjectName(_fromUtf8("lnedDivision"))
        self.formLayout_13.setWidget(1, QtGui.QFormLayout.SpanningRole, self.lnedDivision)
        self.ckDivision = QtGui.QCheckBox(self.groupBox)
        self.ckDivision.setObjectName(_fromUtf8("ckDivision"))
        self.formLayout_13.setWidget(0, QtGui.QFormLayout.FieldRole, self.ckDivision)
        self.gridLayout.addLayout(self.formLayout_13, 2, 1, 1, 1)
        self.formLayout_11 = QtGui.QFormLayout()
        self.formLayout_11.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_11.setObjectName(_fromUtf8("formLayout_11"))
        self.lnedInfrakingdom = QtGui.QLineEdit(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lnedInfrakingdom.sizePolicy().hasHeightForWidth())
        self.lnedInfrakingdom.setSizePolicy(sizePolicy)
        self.lnedInfrakingdom.setObjectName(_fromUtf8("lnedInfrakingdom"))
        self.formLayout_11.setWidget(2, QtGui.QFormLayout.SpanningRole, self.lnedInfrakingdom)
        self.ckInfrakingdom = QtGui.QCheckBox(self.groupBox)
        self.ckInfrakingdom.setObjectName(_fromUtf8("ckInfrakingdom"))
        self.formLayout_11.setWidget(1, QtGui.QFormLayout.LabelRole, self.ckInfrakingdom)
        self.gridLayout.addLayout(self.formLayout_11, 2, 0, 1, 1)
        self.formLayout_2 = QtGui.QFormLayout()
        self.formLayout_2.setObjectName(_fromUtf8("formLayout_2"))
        self.ckKingdom = QtGui.QCheckBox(self.groupBox)
        self.ckKingdom.setObjectName(_fromUtf8("ckKingdom"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.LabelRole, self.ckKingdom)
        self.lnedKingdom = QtGui.QLineEdit(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lnedKingdom.sizePolicy().hasHeightForWidth())
        self.lnedKingdom.setSizePolicy(sizePolicy)
        self.lnedKingdom.setObjectName(_fromUtf8("lnedKingdom"))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.SpanningRole, self.lnedKingdom)
        self.gridLayout.addLayout(self.formLayout_2, 0, 0, 1, 1)
        self.formLayout_5 = QtGui.QFormLayout()
        self.formLayout_5.setObjectName(_fromUtf8("formLayout_5"))
        self.lnedOrder = QtGui.QLineEdit(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lnedOrder.sizePolicy().hasHeightForWidth())
        self.lnedOrder.setSizePolicy(sizePolicy)
        self.lnedOrder.setObjectName(_fromUtf8("lnedOrder"))
        self.formLayout_5.setWidget(2, QtGui.QFormLayout.SpanningRole, self.lnedOrder)
        self.ckOrder = QtGui.QCheckBox(self.groupBox)
        self.ckOrder.setObjectName(_fromUtf8("ckOrder"))
        self.formLayout_5.setWidget(1, QtGui.QFormLayout.LabelRole, self.ckOrder)
        self.gridLayout.addLayout(self.formLayout_5, 2, 3, 1, 1)
        self.formLayout_3 = QtGui.QFormLayout()
        self.formLayout_3.setObjectName(_fromUtf8("formLayout_3"))
        self.ckPhylum = QtGui.QCheckBox(self.groupBox)
        self.ckPhylum.setObjectName(_fromUtf8("ckPhylum"))
        self.formLayout_3.setWidget(0, QtGui.QFormLayout.LabelRole, self.ckPhylum)
        self.lnedPhylum = QtGui.QLineEdit(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lnedPhylum.sizePolicy().hasHeightForWidth())
        self.lnedPhylum.setSizePolicy(sizePolicy)
        self.lnedPhylum.setObjectName(_fromUtf8("lnedPhylum"))
        self.formLayout_3.setWidget(1, QtGui.QFormLayout.SpanningRole, self.lnedPhylum)
        self.gridLayout.addLayout(self.formLayout_3, 2, 2, 1, 1)
        self.formLayout_4 = QtGui.QFormLayout()
        self.formLayout_4.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_4.setObjectName(_fromUtf8("formLayout_4"))
        self.lnedClass = QtGui.QLineEdit(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lnedClass.sizePolicy().hasHeightForWidth())
        self.lnedClass.setSizePolicy(sizePolicy)
        self.lnedClass.setObjectName(_fromUtf8("lnedClass"))
        self.formLayout_4.setWidget(2, QtGui.QFormLayout.SpanningRole, self.lnedClass)
        self.ckClass = QtGui.QCheckBox(self.groupBox)
        self.ckClass.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.ckClass.setObjectName(_fromUtf8("ckClass"))
        self.formLayout_4.setWidget(1, QtGui.QFormLayout.LabelRole, self.ckClass)
        self.gridLayout.addLayout(self.formLayout_4, 0, 3, 1, 1)
        self.formLayout_12 = QtGui.QFormLayout()
        self.formLayout_12.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_12.setObjectName(_fromUtf8("formLayout_12"))
        self.ckSuperdivision = QtGui.QCheckBox(self.groupBox)
        self.ckSuperdivision.setObjectName(_fromUtf8("ckSuperdivision"))
        self.formLayout_12.setWidget(0, QtGui.QFormLayout.LabelRole, self.ckSuperdivision)
        self.lnedSuperdivision = QtGui.QLineEdit(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lnedSuperdivision.sizePolicy().hasHeightForWidth())
        self.lnedSuperdivision.setSizePolicy(sizePolicy)
        self.lnedSuperdivision.setObjectName(_fromUtf8("lnedSuperdivision"))
        self.formLayout_12.setWidget(1, QtGui.QFormLayout.SpanningRole, self.lnedSuperdivision)
        self.gridLayout.addLayout(self.formLayout_12, 1, 1, 1, 1)
        self.formLayout_6 = QtGui.QFormLayout()
        self.formLayout_6.setObjectName(_fromUtf8("formLayout_6"))
        self.ckFamily = QtGui.QCheckBox(self.groupBox)
        self.ckFamily.setObjectName(_fromUtf8("ckFamily"))
        self.formLayout_6.setWidget(0, QtGui.QFormLayout.LabelRole, self.ckFamily)
        self.lnedFamily = QtGui.QLineEdit(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lnedFamily.sizePolicy().hasHeightForWidth())
        self.lnedFamily.setSizePolicy(sizePolicy)
        self.lnedFamily.setObjectName(_fromUtf8("lnedFamily"))
        self.formLayout_6.setWidget(1, QtGui.QFormLayout.SpanningRole, self.lnedFamily)
        self.gridLayout.addLayout(self.formLayout_6, 0, 4, 1, 1)
        self.formLayout_7 = QtGui.QFormLayout()
        self.formLayout_7.setObjectName(_fromUtf8("formLayout_7"))
        self.lnedGenus = QtGui.QLineEdit(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lnedGenus.sizePolicy().hasHeightForWidth())
        self.lnedGenus.setSizePolicy(sizePolicy)
        self.lnedGenus.setObjectName(_fromUtf8("lnedGenus"))
        self.formLayout_7.setWidget(2, QtGui.QFormLayout.SpanningRole, self.lnedGenus)
        self.ckGenus = QtGui.QCheckBox(self.groupBox)
        self.ckGenus.setObjectName(_fromUtf8("ckGenus"))
        self.formLayout_7.setWidget(1, QtGui.QFormLayout.LabelRole, self.ckGenus)
        self.gridLayout.addLayout(self.formLayout_7, 1, 4, 1, 1)
        self.formLayout_8 = QtGui.QFormLayout()
        self.formLayout_8.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_8.setObjectName(_fromUtf8("formLayout_8"))
        self.lnedSpp = QtGui.QLineEdit(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lnedSpp.sizePolicy().hasHeightForWidth())
        self.lnedSpp.setSizePolicy(sizePolicy)
        self.lnedSpp.setObjectName(_fromUtf8("lnedSpp"))
        self.formLayout_8.setWidget(3, QtGui.QFormLayout.SpanningRole, self.lnedSpp)
        self.ckSpp = QtGui.QCheckBox(self.groupBox)
        self.ckSpp.setObjectName(_fromUtf8("ckSpp"))
        self.formLayout_8.setWidget(2, QtGui.QFormLayout.FieldRole, self.ckSpp)
        self.gridLayout.addLayout(self.formLayout_8, 2, 4, 1, 1)
        self.formLayout_17 = QtGui.QFormLayout()
        self.formLayout_17.setContentsMargins(-1, -1, 5, -1)
        self.formLayout_17.setObjectName(_fromUtf8("formLayout_17"))
        self.lnedCommonname = QtGui.QLineEdit(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lnedCommonname.sizePolicy().hasHeightForWidth())
        self.lnedCommonname.setSizePolicy(sizePolicy)
        self.lnedCommonname.setObjectName(_fromUtf8("lnedCommonname"))
        self.formLayout_17.setWidget(2, QtGui.QFormLayout.SpanningRole, self.lnedCommonname)
        self.ckCommonname = QtGui.QCheckBox(self.groupBox)
        self.ckCommonname.setObjectName(_fromUtf8("ckCommonname"))
        self.formLayout_17.setWidget(1, QtGui.QFormLayout.FieldRole, self.ckCommonname)
        self.gridLayout.addLayout(self.formLayout_17, 3, 1, 1, 1)
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.ckSppCode = QtGui.QCheckBox(self.groupBox)
        self.ckSppCode.setObjectName(_fromUtf8("ckSppCode"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.ckSppCode)
        self.lnedSppCode = QtGui.QLineEdit(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lnedSppCode.sizePolicy().hasHeightForWidth())
        self.lnedSppCode.setSizePolicy(sizePolicy)
        self.lnedSppCode.setObjectName(_fromUtf8("lnedSppCode"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.SpanningRole, self.lnedSppCode)
        self.gridLayout.addLayout(self.formLayout, 3, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_3.addWidget(self.groupBox)
        spacerItem2 = QtGui.QSpacerItem(13, 5, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem2)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        spacerItem3 = QtGui.QSpacerItem(13, 335, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        self.verticalLayout_5.addWidget(self.frame)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.btnTaxasubmit = QtGui.QPushButton(Dialog)
        self.btnTaxasubmit.setObjectName(_fromUtf8("btnTaxasubmit"))
        self.horizontalLayout_3.addWidget(self.btnTaxasubmit)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem4)
        self.btnSaveClose = QtGui.QPushButton(Dialog)
        self.btnSaveClose.setObjectName(_fromUtf8("btnSaveClose"))
        self.horizontalLayout_3.addWidget(self.btnSaveClose)
        self.btnCancel = QtGui.QPushButton(Dialog)
        self.btnCancel.setObjectName(_fromUtf8("btnCancel"))
        self.horizontalLayout_3.addWidget(self.btnCancel)
        self.verticalLayout_5.addLayout(self.horizontalLayout_3)
        self.verticalLayout_6.addLayout(self.verticalLayout_5)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.ckCreateTaxa, self.ckKingdom)
        Dialog.setTabOrder(self.ckKingdom, self.lnedKingdom)
        Dialog.setTabOrder(self.lnedKingdom, self.ckSubdivision)
        Dialog.setTabOrder(self.ckSubdivision, self.lnedSubdivision)
        Dialog.setTabOrder(self.lnedSubdivision, self.ckSuperphylum)
        Dialog.setTabOrder(self.ckSuperphylum, self.lnedSuperphylum)
        Dialog.setTabOrder(self.lnedSuperphylum, self.ckClass)
        Dialog.setTabOrder(self.ckClass, self.lnedClass)
        Dialog.setTabOrder(self.lnedClass, self.ckFamily)
        Dialog.setTabOrder(self.ckFamily, self.lnedFamily)
        Dialog.setTabOrder(self.lnedFamily, self.ckSubkingdom)
        Dialog.setTabOrder(self.ckSubkingdom, self.lnedSubkingdom)
        Dialog.setTabOrder(self.lnedSubkingdom, self.ckSuperdivision)
        Dialog.setTabOrder(self.ckSuperdivision, self.lnedSuperdivision)
        Dialog.setTabOrder(self.lnedSuperdivision, self.ckSubphylum)
        Dialog.setTabOrder(self.ckSubphylum, self.lnedSubphylum)
        Dialog.setTabOrder(self.lnedSubphylum, self.ckSubclass)
        Dialog.setTabOrder(self.ckSubclass, self.lnedSubclass)
        Dialog.setTabOrder(self.lnedSubclass, self.ckGenus)
        Dialog.setTabOrder(self.ckGenus, self.lnedGenus)
        Dialog.setTabOrder(self.lnedGenus, self.ckInfrakingdom)
        Dialog.setTabOrder(self.ckInfrakingdom, self.lnedInfrakingdom)
        Dialog.setTabOrder(self.lnedInfrakingdom, self.ckDivision)
        Dialog.setTabOrder(self.ckDivision, self.lnedDivision)
        Dialog.setTabOrder(self.lnedDivision, self.ckPhylum)
        Dialog.setTabOrder(self.ckPhylum, self.lnedPhylum)
        Dialog.setTabOrder(self.lnedPhylum, self.ckOrder)
        Dialog.setTabOrder(self.ckOrder, self.lnedOrder)
        Dialog.setTabOrder(self.lnedOrder, self.ckSpp)
        Dialog.setTabOrder(self.ckSpp, self.lnedSpp)
        Dialog.setTabOrder(self.lnedSpp, self.ckSppCode)
        Dialog.setTabOrder(self.ckSppCode, self.lnedSppCode)
        Dialog.setTabOrder(self.lnedSppCode, self.ckCommonname)
        Dialog.setTabOrder(self.ckCommonname, self.lnedCommonname)
        Dialog.setTabOrder(self.lnedCommonname, self.btnTaxasubmit)
        Dialog.setTabOrder(self.btnTaxasubmit, self.btnSaveClose)
        Dialog.setTabOrder(self.btnSaveClose, self.btnCancel)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Taxonomic Information", None))
        self.groupBox.setTitle(_translate("Dialog", "Identify Taxa Information", None))
        self.ckCreateTaxa.setText(_translate("Dialog", "Create Taxonomic Labels", None))
        self.ckSubclass.setText(_translate("Dialog", "Subclass", None))
        self.ckSubphylum.setText(_translate("Dialog", "Subphylum", None))
        self.ckSubdivision.setText(_translate("Dialog", "Subdivision", None))
        self.ckSubkingdom.setText(_translate("Dialog", "Subkingdom", None))
        self.ckSuperphylum.setText(_translate("Dialog", "Superphylum", None))
        self.ckDivision.setText(_translate("Dialog", "Division", None))
        self.ckInfrakingdom.setText(_translate("Dialog", "Infrakingdom", None))
        self.ckKingdom.setText(_translate("Dialog", "Kingom", None))
        self.ckOrder.setText(_translate("Dialog", "Order", None))
        self.ckPhylum.setText(_translate("Dialog", "Phylum", None))
        self.ckClass.setText(_translate("Dialog", "Class", None))
        self.ckSuperdivision.setText(_translate("Dialog", "Superdivision", None))
        self.ckFamily.setText(_translate("Dialog", "Family", None))
        self.ckGenus.setText(_translate("Dialog", "Genus", None))
        self.ckSpp.setText(_translate("Dialog", "Species Name", None))
        self.ckCommonname.setText(_translate("Dialog", "Common Name", None))
        self.ckSppCode.setText(_translate("Dialog", "Species Code", None))
        self.btnTaxasubmit.setText(_translate("Dialog", "Preview", None))
        self.btnSaveClose.setText(_translate("Dialog", "Save && Close", None))
        self.btnCancel.setText(_translate("Dialog", "Cancel", None))
