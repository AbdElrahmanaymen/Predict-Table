from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QDialog, QFrame, QLabel, QLineEdit
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import pyqtSlot, QRect
import sys
import gui
from H import Ui_Form
import Li, Na, K, Rb, Cs, Fr, Be, Mg, Ca, Sr, Ba, Ra, Sc, Y, Ti, Zr, Hf, Rf, V, Nb, Ta, Db, Cr, Mo, W, Sg, Mn, Tc, Re, Re, Bh, Fe, Ru, Os, Hs, Co, Rh, Ir, Mt, Ni, Pd, Pt, Cu, Ag, Au, Zn
class mainDialog(QDialog , gui.Ui_Dialog):
    def __init__(self, parent=None):
        super(mainDialog, self).__init__(parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.on_click)
        self.pushButton_2.clicked.connect(self.on_click2)
        self.pushButton_3.clicked.connect(self.on_click3)
        self.pushButton_4.clicked.connect(self.on_click4)
        self.pushButton_5.clicked.connect(self.on_click5)
        self.pushButton_6.clicked.connect(self.on_click6)
        self.pushButton_7.clicked.connect(self.on_click7)
        self.pushButton_9.clicked.connect(self.on_click8)
        self.pushButton_10.clicked.connect(self.on_click9)
        self.pushButton_11.clicked.connect(self.on_click10)
        self.pushButton_12.clicked.connect(self.on_click11)
        self.pushButton_13.clicked.connect(self.on_click12)
        self.pushButton_15.clicked.connect(self.on_click13)
        self.pushButton_16.clicked.connect(self.on_click14)
        self.pushButton_17.clicked.connect(self.on_click15)
        self.pushButton_21.clicked.connect(self.on_click16)
        self.pushButton_22.clicked.connect(self.on_click17)
        self.pushButton_23.clicked.connect(self.on_click18)
        self.pushButton_24.clicked.connect(self.on_click19)
        self.pushButton_25.clicked.connect(self.on_click20)
        self.pushButton_26.clicked.connect(self.on_click21)
        self.pushButton_27.clicked.connect(self.on_click22)
        self.pushButton_28.clicked.connect(self.on_click23)
        self.pushButton_44.clicked.connect(self.on_click24)
        self.pushButton_45.clicked.connect(self.on_click25)
        self.pushButton_46.clicked.connect(self.on_click26)
        self.pushButton_47.clicked.connect(self.on_click27)
        self.pushButton_48.clicked.connect(self.on_click28)
        self.pushButton_49.clicked.connect(self.on_click29)
        self.pushButton_50.clicked.connect(self.on_click30)
        self.pushButton_51.clicked.connect(self.on_click31)
        self.pushButton_52.clicked.connect(self.on_click32)
        self.pushButton_54.clicked.connect(self.on_click33)
        self.pushButton_55.clicked.connect(self.on_click34)
        self.pushButton_59.clicked.connect(self.on_click35)
        self.pushButton_61.clicked.connect(self.on_click36)
        self.pushButton_65.clicked.connect(self.on_click37)
        self.pushButton_66.clicked.connect(self.on_click38)
        self.pushButton_71.clicked.connect(self.on_click39)
        self.pushButton_72.clicked.connect(self.on_click40)
        self.pushButton_75.clicked.connect(self.on_click41)
        self.pushButton_79.clicked.connect(self.on_click42)
        self.pushButton_85.clicked.connect(self.on_click44)
        self.pushButton_89.clicked.connect(self.on_click45)
        self.pushButton_90.clicked.connect(self.on_click46)
        self.pushButton_94.clicked.connect(self.on_click47)


        self.dialog = H_info(self)
        self.dialog2 = Li_info(self)
        self.dialog3 = Na_info(self)
        self.dialog4 = K_info(self)
        self.dialog5 = Rb_info(self)
        self.dialog6 = Cs_info(self)
        self.dialog7 = Fr_info(self)
        self.dialog8 = Be_info(self)
        self.dialog9 = Mg_info(self)
        self.dialog10 = Ca_info(self)
        self.dialog11 = Sr_info(self)
        self.dialog12 = Ba_info(self)
        self.dialog13 = Ra_info(self)
        self.dialog14 = Sc_info(self)
        self.dialog15 = Y_info(self)
        self.dialog16 = Ti_info(self)
        self.dialog17 = Zr_info(self)
        self.dialog18 = Hf_info(self)
        self.dialog19 = Rf_info(self)
        self.dialog20 = V_info(self)
        self.dialog21 = Nb_info(self)
        self.dialog22 = Ta_info(self)
        self.dialog23 = Db_info(self)
        self.dialog24 = Cr_info(self)
        self.dialog25 = Mo_info(self)
        self.dialog26 = W_info(self)
        self.dialog27 = Sg_info(self)
        self.dialog28 = Mn_info(self)
        self.dialog29 = Tc_info(self)
        self.dialog30 = Re_info(self)
        self.dialog31 = Bh_info(self)
        self.dialog32 = Fe_info(self)
        self.dialog33 = Ru_info(self)
        self.dialog34 = Os_info(self)
        self.dialog35 = Hs_info(self)
        self.dialog36 = Co_info(self)
        self.dialog37 = Rh_info(self)
        self.dialog38 = Ir_info(self)
        self.dialog39 = Mt_info(self)
        self.dialog40 = Ni_info(self)
        self.dialog41 = Pd_info(self)
        self.dialog42 = Pt_info(self)
        self.dialog44 = Cu_info(self)
        self.dialog45 = Ag_info(self)
        self.dialog46 = Au_info(self)
        self.dialog47 = Zn_info(self)


    @pyqtSlot()
    def on_click(self):
        print('PyQt5 button click')
        self.dialog.exec_()

    def on_click2(self):
        print('PyQt5 button click')
        self.dialog2.exec_()

    def on_click3(self):
        print('PyQt5 button click')
        self.dialog3.exec_()

    def on_click4(self):
        print('PyQt5 button click')
        self.dialog4.exec_()

    def on_click5(self):
        print('PyQt5 button click')
        self.dialog5.exec_()

    def on_click6(self):
        print('PyQt5 button click')
        self.dialog6.exec_()

    def on_click7(self):
        print('PyQt5 button click')
        self.dialog7.exec_()

    def on_click8(self):
        print('PyQt5 button click')
        self.dialog8.exec_()

    def on_click9(self):
        print('PyQt5 button click')
        self.dialog9.exec_()

    def on_click10(self):
        print('PyQt5 button click')
        self.dialog10.exec_()

    def on_click11(self):
        print('PyQt5 button click')
        self.dialog11.exec_()

    def on_click12(self):
        print('PyQt5 button click')
        self.dialog12.exec_()

    def on_click13(self):
        print('PyQt5 button click')
        self.dialog13.exec_()

    def on_click14(self):
        print('PyQt5 button click')
        self.dialog14.exec_()

    def on_click15(self):
        print('PyQt5 button click')
        self.dialog15.exec_()

    def on_click16(self):
        print('PyQt5 button click')
        self.dialog16.exec_()

    def on_click17(self):
        print('PyQt5 button click')
        self.dialog17.exec_()

    def on_click18(self):
        print('PyQt5 button click')
        self.dialog18.exec_()

    def on_click19(self):
        print('PyQt5 button click')
        self.dialog19.exec_()

    def on_click20(self):
        print('PyQt5 button click')
        self.dialog20.exec_()

    def on_click21(self):
        print('PyQt5 button click')
        self.dialog21.exec_()

    def on_click22(self):
        print('PyQt5 button click')
        self.dialog22.exec_()

    def on_click23(self):
        print('PyQt5 button click')
        self.dialog23.exec_()

    def on_click24(self):
        print('PyQt5 button click')
        self.dialog24.exec_()

    def on_click25(self):
        print('PyQt5 button click')
        self.dialog25.exec_()

    def on_click26(self):
        print('PyQt5 button click')
        self.dialog26.exec_()

    def on_click27(self):
        print('PyQt5 button click')
        self.dialog27.exec_()

    def on_click28(self):
        print('PyQt5 button click')
        self.dialog28.exec_()

    def on_click29(self):
        print('PyQt5 button click')
        self.dialog29.exec_()

    def on_click30(self):
        print('PyQt5 button click')
        self.dialog30.exec_()

    def on_click31(self):
        print('PyQt5 button click')
        self.dialog31.exec_()

    def on_click32(self):
        print('PyQt5 button click')
        self.dialog32.exec_()

    def on_click33(self):
        print('PyQt5 button click')
        self.dialog33.exec_()

    def on_click34(self):
        print('PyQt5 button click')
        self.dialog34.exec_()

    def on_click35(self):
        print('PyQt5 button click')
        self.dialog35.exec_()

    def on_click36(self):
        print('PyQt5 button click')
        self.dialog36.exec_()

    def on_click37(self):
        print('PyQt5 button click')
        self.dialog37.exec_()

    def on_click38(self):
        print('PyQt5 button click')
        self.dialog38.exec_()

    def on_click39(self):
        print('PyQt5 button click')
        self.dialog39.exec_()

    def on_click40(self):
        print('PyQt5 button click')
        self.dialog40.exec_()

    def on_click41(self):
        print('PyQt5 button click')
        self.dialog41.exec_()

    def on_click42(self):
        print('PyQt5 button click')
        self.dialog42.exec_()

    def on_click44(self):
        print('PyQt5 button click')
        self.dialog44.exec_()

    def on_click45(self):
        print('PyQt5 button click')
        self.dialog45.exec_()

    def on_click46(self):
        print('PyQt5 button click')
        self.dialog46.exec_()

    def on_click47(self):
        print('PyQt5 button click')
        self.dialog47.exec_()

class H_info(QDialog):
    def __init__(self, parent=None):
        super(H_info, self).__init__(parent)
        label = QLabel(self)
        label.setGeometry(QRect(550, 10, 90, 90))
        pixmap = QPixmap('img.jpg')
        pixmap = pixmap.scaledToWidth(90)
        label.setPixmap(pixmap)
        self.ui = Ui_Form()
        self.ui.setupUi(self)


class Li_info(QDialog):
    def __init__(self, parent=None):
        super(Li_info, self).__init__(parent)
        label = QLabel(self)
        label.setGeometry(QRect(550, 10, 90, 90))
        pixmap = QPixmap('img2.jpg')
        pixmap = pixmap.scaledToWidth(85)
        label.setPixmap(pixmap)
        self.ui = Li.Ui_Form()
        self.ui.setupUi(self)

class Na_info(QDialog):
    def __init__(self, parent=None):
        super(Na_info, self).__init__(parent)
        label = QLabel(self)
        label.setGeometry(QRect(550, 10, 90, 90))
        pixmap = QPixmap('img3.jpg')
        pixmap = pixmap.scaledToWidth(90)
        label.setPixmap(pixmap)
        self.ui = Na.Ui_Form()
        self.ui.setupUi(self)

class Zn_info(QDialog):
    def __init__(self, parent=None):
        super(Zn_info, self).__init__(parent)
        label = QLabel(self)
        label.setGeometry(QRect(550, 10, 90, 90))
        pixmap = QPixmap('img3.jpg')
        pixmap = pixmap.scaledToWidth(90)
        label.setPixmap(pixmap)
        self.ui = Zn.Ui_Form()
        self.ui.setupUi(self)

class K_info(QDialog):
    def __init__(self, parent=None):
        super(K_info, self).__init__(parent)
        label = QLabel(self)
        label.setGeometry(QRect(550, 10, 90, 90))
        pixmap = QPixmap('img4.jpg')
        pixmap = pixmap.scaledToWidth(90)
        pixmap = pixmap.scaledToHeight(90)
        label.setPixmap(pixmap)
        self.ui = K.Ui_Form()
        self.ui.setupUi(self)

class Rb_info(QDialog):
    def __init__(self, parent=None):
        super(Rb_info, self).__init__(parent)
        label = QLabel(self)
        label.setGeometry(QRect(550, 10, 90, 90))
        pixmap = QPixmap('img5.jpg')
        pixmap = pixmap.scaledToWidth(90)
        label.setPixmap(pixmap)
        self.ui = Rb.Ui_Form()
        self.ui.setupUi(self)

class Cs_info(QDialog):
    def __init__(self, parent=None):
        super(Cs_info, self).__init__(parent)
        label = QLabel(self)
        label.setGeometry(QRect(550, 10, 90, 90))
        pixmap = QPixmap('img6.jpg')
        pixmap = pixmap.scaledToWidth(90)
        label.setPixmap(pixmap)
        self.ui = Cs.Ui_Form()
        self.ui.setupUi(self)

class Fr_info(QDialog):
    def __init__(self, parent=None):
        super(Fr_info, self).__init__(parent)
        label = QLabel(self)
        label.setGeometry(QRect(550, 10, 90, 90))
        pixmap = QPixmap('img7.jpg')
        pixmap = pixmap.scaledToWidth(90)
        label.setPixmap(pixmap)
        self.ui = Fr.Ui_Form()
        self.ui.setupUi(self)

class Be_info(QDialog):
    def __init__(self, parent=None):
        super(Be_info, self).__init__(parent)
        label = QLabel(self)
        label.setGeometry(QRect(550, 10, 90, 90))
        pixmap = QPixmap('img8.jpg')
        pixmap = pixmap.scaledToWidth(80)
        label.setPixmap(pixmap)
        self.ui = Be.Ui_Form()
        self.ui.setupUi(self)

class Mg_info(QDialog):
    def __init__(self, parent=None):
        super(Mg_info, self).__init__(parent)
        label = QLabel(self)
        label.setGeometry(QRect(550, 10, 90, 90))
        pixmap = QPixmap('img9.jpg')
        pixmap = pixmap.scaledToWidth(90)
        label.setPixmap(pixmap)
        self.ui = Mg.Ui_Form()
        self.ui.setupUi(self)

class Ca_info(QDialog):
    def __init__(self, parent=None):
        super(Ca_info, self).__init__(parent)
        label = QLabel(self)
        label.setGeometry(QRect(550, 10, 90, 90))
        pixmap = QPixmap('img10.jpg')
        pixmap = pixmap.scaledToWidth(90)
        label.setPixmap(pixmap)
        self.ui = Ca.Ui_Form()
        self.ui.setupUi(self)

class Sr_info(QDialog):
    def __init__(self, parent=None):
        super(Sr_info, self).__init__(parent)
        label = QLabel(self)
        label.setGeometry(QRect(550, 10, 95, 95))
        pixmap = QPixmap('img11.jpg')
        pixmap = pixmap.scaledToWidth(95)
        label.setPixmap(pixmap)
        self.ui = Sr.Ui_Form()
        self.ui.setupUi(self)

class Ba_info(QDialog):
    def __init__(self, parent=None):
        super(Ba_info, self).__init__(parent)
        label = QLabel(self)
        label.setGeometry(QRect(550, 10, 90, 90))
        pixmap = QPixmap('img12.jpg')
        pixmap = pixmap.scaledToWidth(90)
        label.setPixmap(pixmap)
        self.ui = Ba.Ui_Form()
        self.ui.setupUi(self)

class Ra_info(QDialog):
    def __init__(self, parent=None):
        super(Ra_info, self).__init__(parent)
        label = QLabel(self)
        label.setGeometry(QRect(550, 10, 90, 90))
        pixmap = QPixmap('img13.jpg')
        pixmap = pixmap.scaledToWidth(90)
        label.setPixmap(pixmap)
        self.ui = Ra.Ui_Form()
        self.ui.setupUi(self)

class Sc_info(QDialog):
    def __init__(self, parent=None):
        super(Sc_info, self).__init__(parent)
        label = QLabel(self)
        label.setGeometry(QRect(550, 10, 90, 90))
        pixmap = QPixmap('img14.jpg')
        pixmap = pixmap.scaledToWidth(90)
        label.setPixmap(pixmap)
        self.ui = Sc.Ui_Form()
        self.ui.setupUi(self)

class Y_info(QDialog):
    def __init__(self, parent=None):
        super(Y_info, self).__init__(parent)
        label = QLabel(self)
        label.setGeometry(QRect(550, 10, 90, 90))
        pixmap = QPixmap('img15.jpg')
        pixmap = pixmap.scaledToWidth(90)
        label.setPixmap(pixmap)
        self.ui = Y.Ui_Form()
        self.ui.setupUi(self)

class Ti_info(QDialog):
    def __init__(self, parent=None):
        super(Ti_info, self).__init__(parent)
        label = QLabel(self)
        label.setGeometry(QRect(550, 10, 90, 90))
        pixmap = QPixmap('img16.jpg')
        pixmap = pixmap.scaledToWidth(90)
        label.setPixmap(pixmap)
        self.ui = Ti.Ui_Form()
        self.ui.setupUi(self)

class Zr_info(QDialog):
    def __init__(self, parent=None):
        super(Zr_info, self).__init__(parent)
        label = QLabel(self)
        label.setGeometry(QRect(550, 10, 90, 90))
        pixmap = QPixmap('img17.jpg')
        pixmap = pixmap.scaledToWidth(90)
        label.setPixmap(pixmap)
        self.ui = Zr.Ui_Form()
        self.ui.setupUi(self)

class Hf_info(QDialog):
    def __init__(self, parent=None):
        super(Hf_info, self).__init__(parent)
        label = QLabel(self)
        label.setGeometry(QRect(550, 10, 90, 90))
        pixmap = QPixmap('img18.jpg')
        pixmap = pixmap.scaledToWidth(90)
        label.setPixmap(pixmap)
        self.ui = Hf.Ui_Form()
        self.ui.setupUi(self)

class Rf_info(QDialog):
    def __init__(self, parent=None):
        super(Rf_info, self).__init__(parent)
        label = QLabel(self)
        label.setGeometry(QRect(550, 10, 90, 90))
        pixmap = QPixmap('img19.jpg')
        pixmap = pixmap.scaledToWidth(90)
        label.setPixmap(pixmap)
        self.ui = Rf.Ui_Form()
        self.ui.setupUi(self)

class V_info(QDialog):
    def __init__(self, parent=None):
        super(V_info, self).__init__(parent)
        label = QLabel(self)
        label.setGeometry(QRect(550, 10, 90, 90))
        pixmap = QPixmap('img20.jpg')
        pixmap = pixmap.scaledToWidth(90)
        label.setPixmap(pixmap)
        self.ui = V.Ui_Form()
        self.ui.setupUi(self)

class Nb_info(QDialog):
    def __init__(self, parent=None):
        super(Nb_info, self).__init__(parent)
        label = QLabel(self)
        label.setGeometry(QRect(550, 10, 90, 90))
        pixmap = QPixmap('img21.jpg')
        pixmap = pixmap.scaledToWidth(90)
        label.setPixmap(pixmap)
        self.ui = Nb.Ui_Form()
        self.ui.setupUi(self)

class Ta_info(QDialog):
    def __init__(self, parent=None):
        super(Ta_info, self).__init__(parent)
        label = QLabel(self)
        label.setGeometry(QRect(550, 10, 90, 90))
        pixmap = QPixmap('img22.jpg')
        pixmap = pixmap.scaledToWidth(90)
        label.setPixmap(pixmap)
        self.ui = Ta.Ui_Form()
        self.ui.setupUi(self)

class Db_info(QDialog):
    def __init__(self, parent=None):
        super(Db_info, self).__init__(parent)
        label = QLabel(self)
        label.setGeometry(QRect(550, 10, 90, 90))
        pixmap = QPixmap('img23.jpg')
        pixmap = pixmap.scaledToWidth(90)
        label.setPixmap(pixmap)
        self.ui = Db.Ui_Form()
        self.ui.setupUi(self)

class Cr_info(QDialog):
    def __init__(self, parent=None):
        super(Cr_info, self).__init__(parent)
        label = QLabel(self)
        label.setGeometry(QRect(550, 10, 90, 90))
        pixmap = QPixmap('img24.jpg')
        pixmap = pixmap.scaledToWidth(90)
        label.setPixmap(pixmap)
        self.ui = Cr.Ui_Form()
        self.ui.setupUi(self)

class Mo_info(QDialog):
    def __init__(self, parent=None):
        super(Mo_info, self).__init__(parent)
        label = QLabel(self)
        label.setGeometry(QRect(550, 10, 90, 90))
        pixmap = QPixmap('img25.jpg')
        pixmap = pixmap.scaledToWidth(90)
        label.setPixmap(pixmap)
        self.ui = Mo.Ui_Form()
        self.ui.setupUi(self)

class W_info(QDialog):
    def __init__(self, parent=None):
        super(W_info, self).__init__(parent)
        label = QLabel(self)
        label.setGeometry(QRect(550, 10, 90, 90))
        pixmap = QPixmap('img26.jpg')
        pixmap = pixmap.scaledToWidth(90)
        label.setPixmap(pixmap)
        self.ui = W.Ui_Form()
        self.ui.setupUi(self)

class Sg_info(QDialog):
    def __init__(self, parent=None):
        super(Sg_info, self).__init__(parent)
        label = QLabel(self)
        label.setGeometry(QRect(550, 10, 90, 90))
        pixmap = QPixmap('img27.jpg')
        pixmap = pixmap.scaledToWidth(90)
        label.setPixmap(pixmap)
        self.ui = Sg.Ui_Form()
        self.ui.setupUi(self)

class Mn_info(QDialog):
    def __init__(self, parent=None):
        super(Mn_info, self).__init__(parent)
        label = QLabel(self)
        label.setGeometry(QRect(550, 10, 90, 90))
        pixmap = QPixmap('img28.jpg')
        pixmap = pixmap.scaledToWidth(90)
        label.setPixmap(pixmap)
        self.ui = Mn.Ui_Form()
        self.ui.setupUi(self)

class Tc_info(QDialog):
    def __init__(self, parent=None):
        super(Tc_info, self).__init__(parent)
        label = QLabel(self)
        label.setGeometry(QRect(550, 10, 90, 90))
        pixmap = QPixmap('img29.jpg')
        pixmap = pixmap.scaledToWidth(90)
        label.setPixmap(pixmap)
        self.ui = Tc.Ui_Form()
        self.ui.setupUi(self)

class Re_info(QDialog):
    def __init__(self, parent=None):
        super(Re_info, self).__init__(parent)
        label = QLabel(self)
        label.setGeometry(QRect(550, 10, 90, 90))
        pixmap = QPixmap('img30.jpg')
        pixmap = pixmap.scaledToWidth(90)
        label.setPixmap(pixmap)
        self.ui = Re.Ui_Form()
        self.ui.setupUi(self)

class Bh_info(QDialog):
    def __init__(self, parent=None):
        super(Bh_info, self).__init__(parent)
        label = QLabel(self)
        label.setGeometry(QRect(550, 10, 90, 90))
        pixmap = QPixmap('img31.jpg')
        pixmap = pixmap.scaledToWidth(90)
        label.setPixmap(pixmap)
        self.ui = Bh.Ui_Form()
        self.ui.setupUi(self)

class Fe_info(QDialog):
    def __init__(self, parent=None):
        super(Fe_info, self).__init__(parent)
        label = QLabel(self)
        label.setGeometry(QRect(550, 10, 90, 90))
        pixmap = QPixmap('img32.jpg')
        pixmap = pixmap.scaledToWidth(90)
        label.setPixmap(pixmap)
        self.ui = Fe.Ui_Form()
        self.ui.setupUi(self)

class Ru_info(QDialog):
    def __init__(self, parent=None):
        super(Ru_info, self).__init__(parent)
        label = QLabel(self)
        label.setGeometry(QRect(550, 10, 90, 90))
        pixmap = QPixmap('img33.jpg')
        pixmap = pixmap.scaledToWidth(90)
        label.setPixmap(pixmap)
        self.ui = Ru.Ui_Form()
        self.ui.setupUi(self)

class Os_info(QDialog):
    def __init__(self, parent=None):
        super(Os_info, self).__init__(parent)
        label = QLabel(self)
        label.setGeometry(QRect(550, 10, 90, 90))
        pixmap = QPixmap('img34.jpg')
        pixmap = pixmap.scaledToWidth(90)
        label.setPixmap(pixmap)
        self.ui = Os.Ui_Form()
        self.ui.setupUi(self)

class Hs_info(QDialog):
    def __init__(self, parent=None):
        super(Hs_info, self).__init__(parent)
        label = QLabel(self)
        label.setGeometry(QRect(550, 10, 90, 90))
        pixmap = QPixmap('img35.jpg')
        pixmap = pixmap.scaledToWidth(90)
        label.setPixmap(pixmap)
        self.ui = Hs.Ui_Form()
        self.ui.setupUi(self)

class Co_info(QDialog):
    def __init__(self, parent=None):
        super(Co_info, self).__init__(parent)
        label = QLabel(self)
        label.setGeometry(QRect(550, 10, 90, 90))
        pixmap = QPixmap('img36.jpg')
        pixmap = pixmap.scaledToWidth(90)
        label.setPixmap(pixmap)
        self.ui = Co.Ui_Form()
        self.ui.setupUi(self)

class Rh_info(QDialog):
    def __init__(self, parent=None):
        super(Rh_info, self).__init__(parent)
        label = QLabel(self)
        label.setGeometry(QRect(550, 10, 90, 90))
        pixmap = QPixmap('img37.jpg')
        pixmap = pixmap.scaledToWidth(90)
        label.setPixmap(pixmap)
        self.ui = Rh.Ui_Form()
        self.ui.setupUi(self)

class Ir_info(QDialog):
    def __init__(self, parent=None):
        super(Ir_info, self).__init__(parent)
        label = QLabel(self)
        label.setGeometry(QRect(550, 10, 90, 90))
        pixmap = QPixmap('img38.jpg')
        pixmap = pixmap.scaledToWidth(90)
        label.setPixmap(pixmap)
        self.ui = Ir.Ui_Form()
        self.ui.setupUi(self)

class Mt_info(QDialog):
    def __init__(self, parent=None):
        super(Mt_info, self).__init__(parent)
        label = QLabel(self)
        label.setGeometry(QRect(550, 10, 90, 90))
        pixmap = QPixmap('img39.jpg')
        pixmap = pixmap.scaledToWidth(90)
        label.setPixmap(pixmap)
        self.ui = Mt.Ui_Form()
        self.ui.setupUi(self)

class Ni_info(QDialog):
    def __init__(self, parent=None):
        super(Ni_info, self).__init__(parent)
        label = QLabel(self)
        label.setGeometry(QRect(550, 10, 90, 90))
        pixmap = QPixmap('img40.jpg')
        pixmap = pixmap.scaledToWidth(90)
        label.setPixmap(pixmap)
        self.ui = Ni.Ui_Form()
        self.ui.setupUi(self)

class Pd_info(QDialog):
    def __init__(self, parent=None):
        super(Pd_info, self).__init__(parent)
        label = QLabel(self)
        label.setGeometry(QRect(550, 10, 90, 90))
        pixmap = QPixmap('img40.jpg')
        pixmap = pixmap.scaledToWidth(90)
        label.setPixmap(pixmap)
        self.ui = Pd.Ui_Form()
        self.ui.setupUi(self)

class Pt_info(QDialog):
    def __init__(self, parent=None):
        super(Pt_info, self).__init__(parent)
        label = QLabel(self)
        label.setGeometry(QRect(550, 10, 90, 90))
        pixmap = QPixmap('img40.jpg')
        pixmap = pixmap.scaledToWidth(90)
        label.setPixmap(pixmap)
        self.ui = Pt.Ui_Form()
        self.ui.setupUi(self)

class Cu_info(QDialog):
    def __init__(self, parent=None):
        super(Cu_info, self).__init__(parent)
        label = QLabel(self)
        label.setGeometry(QRect(550, 10, 90, 90))
        pixmap = QPixmap('img40.jpg')
        pixmap = pixmap.scaledToWidth(90)
        label.setPixmap(pixmap)
        self.ui = Cu.Ui_Form()
        self.ui.setupUi(self)

class Ag_info(QDialog):
    def __init__(self, parent=None):
        super(Ag_info, self).__init__(parent)
        label = QLabel(self)
        label.setGeometry(QRect(550, 10, 90, 90))
        pixmap = QPixmap('img40.jpg')
        pixmap = pixmap.scaledToWidth(90)
        label.setPixmap(pixmap)
        self.ui = Ag.Ui_Form()
        self.ui.setupUi(self)

class Au_info(QDialog):
    def __init__(self, parent=None):
        super(Au_info, self).__init__(parent)
        label = QLabel(self)
        label.setGeometry(QRect(550, 10, 90, 90))
        pixmap = QPixmap('img40.jpg')
        pixmap = pixmap.scaledToWidth(90)
        label.setPixmap(pixmap)
        self.ui = Au.Ui_Form()
        self.ui.setupUi(self)


app = QApplication(sys.argv)
form = mainDialog()
form.show()
app.exec_()