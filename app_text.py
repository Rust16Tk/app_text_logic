#проба чтения текста с файла с расширением txt
import eel


@eel.expose
def text_open(self):
    f = open('', 'r')
    
    
    


eel.init("web")
eel.start("main.html", size=(500, 700))