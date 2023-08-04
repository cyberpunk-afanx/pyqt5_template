import sys
import os

def createTemplate():
    temp_import = ''
    temp_class = ''
    temp_init = ''
    temp_main = ''
    temp_run = ''

    os.system("pyuic5 " + sys.argv[1] + " -o " + sys.argv[1][:len(sys.argv[1])-3] +".py")
    
    temp_import += 'import sys\nimport os\n' + 'from PyQt5 import QtWidgets\n'
    temp_import += "import " + sys.argv[1][:len(sys.argv[1])-3] + "\n\n"
    temp_class += 'class ExampleApp(QtWidgets.QMainWindow, ' + sys.argv[1][:len(sys.argv[1])-3] +'.Ui_MainWindow):\n'
    temp_init += '    def __init__(self):\n'
    temp_init += '        super().__init__()\n'
    temp_init += '        self.setupUi(self)\n\n'
    temp_main += 'def main():\n'
    temp_main += '    app = QtWidgets.QApplication(sys.argv)\n'
    temp_main += '    window = ExampleApp()\n'
    temp_main += '    window.show()\n'
    temp_main += '    app.exec_()\n\n'
    temp_run += 'if __name__ == \'__main__\':\n'
    temp_run += '    main()'

    file = open(sys.argv[3], 'w')
    file.write(temp_import+temp_class+temp_init+temp_main+temp_run)
    file.close()

def error(err):
    if(err == 0):
        print('usage: pytmplt design.ui -o main.py')
    elif(err == 1):
        print('[missed] -o\toutput')
    elif(err == 2):
        print('[missed] have to usage .ui file')
    exit(-1)

def main():
    if(len(sys.argv) - 1 == 0):
        error(0)
    else:  
        if('.ui' in sys.argv[1]):
            if(sys.argv[2] == '-o'):
                createTemplate()
            else:
                error(1)
        else:
            error(2)


if __name__ == '__main__':
    main()


