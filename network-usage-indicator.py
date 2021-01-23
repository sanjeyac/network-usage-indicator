import signal
from gi.repository import Gtk as gtk
from gi.repository import AppIndicator3 as appindicator
import logging
import threading
import time
import subprocess
import os


APPINDICATOR_ID = 'data-usage'
WAIT = 60 #waiting time in seconds
icon_file = "/icon-white-64.png"
running = True


def set_label(indicator):
    output = subprocess.getoutput("vnstat --oneline")
    data = output.split(";")
    indicator.set_label(data[5],"")

def listener(indicator):
    set_label(indicator)
    while(running):
        time.sleep(WAIT)
        set_label(indicator)
        #print(data[5])

def build_menu():
    menu = gtk.Menu()
    item_quit = gtk.MenuItem('Quit')
    item_quit.connect('activate', quit)
    menu.append(item_quit)
    running = False
    menu.show_all()
    return menu

def quit(source):
    gtk.main_quit()


# MAIN 
if __name__ == "__main__":

    # get starting data
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    dir_path = os.path.dirname(os.path.realpath(__file__))
    icon_image = dir_path + icon_file
    print("icon image: "+icon_image)
    
    # setup indicator
    indicator = appindicator.Indicator.new(APPINDICATOR_ID, icon_image, appindicator.IndicatorCategory.SYSTEM_SERVICES)
    indicator.set_status(appindicator.IndicatorStatus.ACTIVE)
    indicator.set_menu(build_menu())
    
    # data reading thread
    x = threading.Thread(target=listener, args=(indicator,), daemon=True)
    x.start()
    
    # start gtk
    gtk.main()
