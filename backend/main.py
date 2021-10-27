import eel
from middle.mid import *

if __name__ == '__main__':
    eel.init('front')
    eel.start('index.html', mode="chrome", size=(760, 760))