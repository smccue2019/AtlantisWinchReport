#!/usr/bin/env python3

import sys, signal
from PyQt5.QtCore import QCoreApplication, QTimer
#from PyQt5.QtGui import QMainWindow
from PyQt5.QtWidgets import QMainWindow,QApplication
#from PyQt5 import uic
from winchDisplayUI import Ui_MainWindow
from sjm_pkg.udp_receiver import UDPreceiver 

signal.signal(signal.SIGINT, signal.SIG_DFL)

class winch_display(QMainWindow):

    def __init__(self, udp_port, parent=None):
        QMainWindow.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setWindowTitle("Atlantis Winch Report")
        
        self.udpr = UDPreceiver(udp_port)

        self.udpr.new_winch.connect(self.on_new_winch)
        self.ui.quitButton.clicked.connect(self.on_quit_button)

    def on_new_winch(self, tension, payout, payout_rate):
        self.ui.gb1_text_display.setText(tension)
        self.ui.gb2_text_display.setText(payout)
        self.ui.gb3_text_display.setText(payout_rate)

    def on_quit_button(self):
        QCoreApplication.exit()

def sigint_handler(*args):
    sys.stderr.write('\r')
    QApplication.quit()

if __name__ == '__main__':

    qapp = QApplication(sys.argv)

    signal.signal(signal.SIGINT, sigint_handler)

    my_udp_port = 55801
    
#    try:
#        exec("./udp_receiver.py")
#    except Exception as e:
#        print("error opening or running ./udp_receiver.py", e)



    # hack to allow closing from the keyboard using sigint handler above
    timer = QTimer()
    timer.start(500)
    timer.timeout.connect(lambda: None)

    thisguy = winch_display(my_udp_port)

    thisguy.show()

    sys.exit(qapp.exec_())
