from PySide.QtGui import *
from PySide.QtCore import *
#import threading
import webview

import os
import mss
import mss.tools
import sys
import pygame
import sqlite3
from multiprocessing import Process
#from PySide.QtNetwork import *
#from PySide.QtWebKit import *
from PySide.phonon import Phonon
#from PySide.QtMultimedia import *
import qdarkstyle
#from PySide.QtNetwork import QNetworkRequest, QNetworkAccessManager
#from PySide.QtNetwork import QNetworkAccessManager, QNetworkRequest, QNetworkReply

class Form(QMainWindow):

    def __init__(self, parent=None):
        super(Form, self).__init__(parent)
        self.setGeometry(50,50,500, 500)
        self.setWindowTitle(('media'))
        self.filename = ''
        dial = QDial()
        dial.setNotchesVisible(True)

        self.home()

    def home(self):
        import sqlite3
        conn = sqlite3.connect('user.db')
        c = conn.cursor()
        c.execute('CREATE TABLE IF NOT EXISTS user(name TEXT, password TEXT)')
        c.execute('SELECT * FROM user')
        names = c.fetchall()

        self.labs = QLabel(self)
        #self.labs.setText(str(names[-4:-1]))
        self.pygamebtn = QPushButton(self, 'pygame')
        self.pygamebtn.clicked.connect(self.openpygame)
        self.labs.move(20, 20)
        self.labs.resize(300,300)

        self.line = QLineEdit(self)
        self.line.resize(200, 40)

        self.line2 = QLineEdit(self)
        self.line2.resize(200, 40)

        self.lab1 = QLabel('Name', self)
        self.lab1.move(100, 80)

        self.lab2 = QLabel('Password', self)
        self.lab2.move(100, 180)

        self.line2.move(100,100)
        self.line.move(100, 200)
# -------------------------------------------
        self.btn2 = QPushButton('Submit', self)




        self.btn2.clicked.connect(self.insert)
        self.btn2.move(200,300)
#-------------------------------------------
        self.btn3 = QPushButton('Login', self)
        self.btn3.clicked.connect(self.close)
        self.btn3.clicked.connect(self.fucky)
        self.btn3.move(100, 0)
        self.show()

#-------------------------------------------------
    def openpygame(self):

        self.pruns()

    def pruns(self):
        pygame.init()
        display_width = 800
        display_height = 600
        black = (0,0,0)
        white = (255,255,255)
        red = (255,0,0)
        gameDisplay = pygame.display.set_mode((800,600))
        pygame.display.set_caption('A bit Racey')
        clock = pygame.time.Clock()
        carImg = pygame.image.load('')
        crashed = False
        while not crashed:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    crashed = True
                print(event)
            pygame.display.update()
            clock.tick(60)
        pygame.quit()

    def insert(self):
        import sqlite3
        conn = sqlite3.connect('user.db')
        c = conn.cursor()
        c.execute('CREATE TABLE IF NOT EXISTS user(name TEXT, password TEXT)')
        c.execute('INSERT INTO user(name, password) VALUES (?, ?)', ((self.line.text()), (self.line2.text())))
        if len(self.line.text()) > 5 and len(self.line2.text()) > 5:
            conn.commit()
            self.msg2 = QMessageBox(self)
            self.msg2.setText('You are all set. We added you!')
            self.msg2.show()
            self.line.setText('')
            self.line2.setText('')
        else:
            self.msg = QMessageBox(self)
            self.msg.setText('Nope')
            self.msg.setDetailedText('Both fields have to be longer than 3 letters!')
            self.msg.show()


    def fucky(self):
        dials = dia()
        dials.exec_()

class dia(QDialog):
    filename = ''
    def __init__(self, parent=None):
        super(dia, self).__init__(parent)
        self.setWindowTitle('second title')
        self.setGeometry(50, 50, 500, 500)


        self.layout = QFormLayout()
        self.fhome()

    def fhome(self):

        self.lines = QLineEdit()
        self.lines.resize(30,30)
        self.lines2 = QLineEdit()
        lab = QLabel('Name')
        lab2 = QLabel('Password')
        btn = QPushButton('Create Account')
        self.layout.addWidget(lab)
        self.layout.addWidget(self.lines)
        self.layout.addWidget((lab2))

        self.layout.addWidget(self.lines2)
        btn2 = QPushButton('Submit')
        self.layout.addWidget(btn2)
        self.layout.addWidget(btn)



        btn.clicked.connect(self.someshit)
        btn.clicked.connect(self.close)


        btn2.clicked.connect(self.logins)
        #btn2.clicked.connect(self.close)





        self.setLayout(self.layout)
    def someshit(self):
        self.close()
        form = Form()
        form.exec_()
        print('ok')


    def logins(self):

        import sqlite3
        conn = sqlite3.connect('user.db')
        c = conn.cursor()
        c.execute('CREATE TABLE IF NOT EXISTS user(name TEXT, password TEXT)')
        c.execute('SELECT * FROM user WHERE (name) = (?) and password = (?)', (str(self.lines2.text()), str(self.lines.text())))
        ok = c.fetchall()
        if str(self.lines2.text()) and str(self.lines.text()) in str(ok):
            self.close()
            plays = mplayer()
            mplayer.exec_()
            self.lines2.setText('hi')
            self.lines.setText('hi')

class mplayer(QMainWindow):

    def __init__(self, parent=None):
        super(mplayer, self).__init__(parent)
        self.filename = None
        self.totalz = 100
        self.newwindows()
    def newwindows(self):
        import glob


        self.setWindowTitle('Media')
        action = QAction('text', self)
        self.actions = action.setStatusTip('check')
        self.setGeometry(100,50,1000,1000)
        self.tool = QMenuBar(self)

        self.okay = self.tool.addMenu('okay')
        self.okay2 = self.tool.addMenu('okay')
        self.okay.addAction(action)

        self.setWindowIcon(QIcon('C:/Users/fish/Downloads/nice/icons8-sunday-50.png'))
        #'''''''\



        #self.layout = QVBoxLayout(self)
        #self.browser = QWebView(self)

        '''damnit = "http://www.google.com/"
        self.fucks = self.browser.load(QUrl(damnit))

        self.browser.move(500,100)
        self.browser.resize(500,500)'''
        dir = ''
        self.btnss = QPushButton('open file', self)
        self.btns2 = QPushButton('pause', self)
        self.btns3 = QPushButton('play', self)
        self.btns3.clicked.connect(self.played)
        self.btns2.clicked.connect(self.paused)
        self.btnss.move(100, 350)
        self.btns2.move(100,400)
        self.btns3.move(100,450)


        self.btnss.clicked.connect(self.fhile)




        path = self.filename
        print(self.filename)

        self.media = Phonon.MediaObject(self)
        self.video = Phonon.VideoWidget(self)
        self.video.setMinimumSize(400, 400)
        self.audio = Phonon.AudioOutput(Phonon.VideoCategory, self)
        Phonon.createPath(self.media, self.audio)
        Phonon.createPath(self.media, self.video)
        self.media.setCurrentSource(Phonon.MediaSource(path))
        self.media.play()
        self.video.show()
# -------------------------------------------
        self.btns4 = QPushButton('Full Screen', self)
        self.btns4.move(400, 0)
        self.btns4.clicked.connect(self.enlarged)
# -------------------------------------------




        # -------------------------------------------
        self.slider = Phonon.VolumeSlider(self)
        self.slider.setAudioOutput(self.audio)
        self.slider.move(250,50)
        self.slider.resize(250,50)

        self.seekk = Phonon.SeekSlider(self)
        self.seekk.setMediaObject(self.media)
        self.seekk.move(200,550)
        self.seekk.resize(350,150)
        self.video.move(200,200)
# -------------------------------------------
        #self.view = QListView(self)
        #self.view.move(600,100)
        #self.view.resize(100,100)
        lists = glob.glob('C:/Users/fish/Downloads/*.WMV') + glob.glob('C:/Users/fish/Downloads/*.mp4') + glob.glob('C:/Users/fish/Downloads/*.flv')
        self.newview = QListWidget(self)
        self.newview.resize(300,300)
        self.newview.move(600,300)
        for item in lists:

            self.okay = QListWidgetItem('okay')
            self.okay.setData(Qt.UserRole, str(item))
            self.newview.addItem(self.okay)

            #self.newview.setValue(item)
# -------------------------------------------


        self.newview.clicked.connect(self.listfunc)
        #self.smodel = QStandardItemModel(self)


# -------------------------------------------
        #self.setKey(QShortcut(Qt.Key_Escape, self))
        # self.act.setKey(QKeySequence('Alt+Enter'))
        #self.act.activated.connect(self.efullscreen)

        print(lists)
        #self.line = QTextEdit(self)
        #self.line.resize(25,25)
        #self.line.resize(25,25)
        #self.line.move(100,100)
        #self.line = QLineEdit(self)
        #self.line.resize(300,30)
        #self.line.move(600,70)
# -------------------------------------------
        self.naved = QPushButton('browser', self)
        self.naved.clicked.connect(self.nav)


# -------------------------------------------
        self.btned = QPushButton('Random Photo', self)
        self.btned.move(100, 300)
        self.btned.clicked.connect(self.check)
# -------------------------------------------
        self.show()
        print(path)

        if path == None:
            self.lab = QLabel(self)
            paths = 'C:/Users/fish/Desktop/pexels-photo.jpg'
            self.img = QPixmap(paths)
            self.lab.setPixmap(paths)
            self.lab.move(200, 175)
            self.lab.resize(400, 400)
            self.lab.show()


        else:
            paths = ''

            self.lab.resize(10, 10)
            self.lab.move(10,10)



    def check(self):
        import glob
        import random
        self = QDialog()
        lab = QLabel()
        okay = glob.glob('C:/Users/fish/Desktop/jamimages/*.jpg')
        img = random.choice(okay)
        QPixmap()
        #img = QPixmap('C:/Users/fish/Pictures/2.jpg')
        lab.setPixmap(img)
        self.setGeometry(200, 200, 200, 200)
        new = QVBoxLayout()
        btn = QPushButton('check')
        new.addWidget((btn))
        new.addWidget(lab)
        self.setLayout(new)
        self.exec_()
    def enlarged(self, arg=0):
        '''arg = QDialog()


        #self.video.resize(1000,1000)
        arg.media = Phonon.MediaObject(arg)
        arg.video = Phonon.VideoWidget(arg)
        arg.video.setMinimumSize(400, 400)
        arg.audio = Phonon.AudioOutput(Phonon.VideoCategory, arg)
        Phonon.createPath(arg.media, arg.audio)
        Phonon.createPath(arg.media, arg.video)
        arg.media.setCurrentSource(Phonon.MediaSource(self.filename))

        arg.media.play()
        arg.video.resize(1300,1000)
        arg.show()
        arg.exec_()'''
        self.video.enterFullScreen()

    def efullscreen(self):
        self.video.exitFullScreen()
        print('hi')
    def listfunc(self):
        print(self.newview.currentItem().text())

        self.filename = self.newview.currentItem().data(Qt.UserRole)
        print(self.filename)
        self.close()

        self.newwindows()
    def paused(self):
        self.media.pause()
    def played(self):
        self.media.play()
    def fhile(self):
        dir = ''
        self.fileobj = QFileDialog.getOpenFileName(self, 'open file dialog', dir=dir)
        print(type(self.fileobj))
        print(self.fileobj)
        self.filename = self.fileobj[0]
        #file = open(filename, 'r')
        #read = file.read()
        #print(read)
        self.close()
        self.newwindows()
    def nav(self):
        self.close()

        okay = webB()

        okay.exec_()


class webB(QMainWindow):

    def __init__(self, parent=None):
        super(webB, self).__init__(parent)
        args = self
        args = self




        self.browser(args)
    def navtomov(self):
        self.close()
        webview.destroy_window()
        newvar = mplayer()
        newvar.exec_()

    def browser(self, args):
        #self.setWindowFlags(Qt.SplashScreen | Qt.WindowStaysOnTopHint)
        self.setWindowFlags(Qt.WindowStaysOnTopHint)
        self.btned = QPushButton('Open Browser', self)
        self.btned.move(200,199)
        self.labeled = QLabel('Browser Control Pannel', self)
        self.labeled.move(100,50)
        self.labeled.resize(300,30)
        self.setGeometry(0,0,400,250)
        self.setWindowTitle('Browser')
        trash = lambda: exit()
        self.openlink = QPushButton('exit', self)
        self.openlink.clicked.connect(trash)

        self.BBtn = QPushButton('Open Browser')
        self.navbtn = QPushButton('Media player', self)
        self.navbtn.move(100,0)

        self.navbtn.clicked.connect(self.navtomov)

        #-------- add new url
        self.addUrl = QLineEdit(self)
        self.urlbtn = QPushButton('enter', self)
        self.urlbtn.move(0,95)
        self.addUrl.move(100,100)
        self.addUrl.resize(280,25)
        t = lambda: self.newurl(args)

        self.urlbtn.clicked.connect(t)

        #--------
        #self.browsers = QWebView(self)
        #self.browsers.settings().setAttribute(QWebSettings.PluginsEnabled, True)
        '''QWebSettings.globalSettings().setAttribute(QWebSettings.PluginsEnabled, True)
        damnit = "https://www.google.com"
        self.fucks = QNetworkRequest(QUrl(damnit))
        self.reply = self.get(self.fucks)'''
        #self.browsers.move(500, 100)
        #self.browsers.resize(500, 500)
        #self.view = QWebView(self)
        '''s = ("""<iframe width="560" height="315" src="https://www.youtube.com/embed/NuIAYHVeFYs" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>""")

        self.view.setHtml(s, QUrl('https://youtube.com'))
        self.view.move(200,200)
        self.view.resize(400,400)'''
        url='https://www.bing.com'

        '''self.t = QProcess(self)

        self.t.setProcessChannelMode(QProcess.MergedChannels)
        self.t.readyReadStandardOutput.connect(self.get_current_ur)
        QProcess.start(self.t)'''
        #QtConcurrent.run(self, self.get_current_ur)
        self.imgBtn = QPushButton('add images', self)
        self.imgBtn.move(100,199)
        self.imgBtn.clicked.connect(self.checking2)
        self.vidbtn = QPushButton('add to video', self)
        self.vidbtn.clicked.connect(self.checking)
        self.vidbtn.move(0,199)
        #------------
        self.viewBtn = QPushButton('View Links', self)
        self.viewBtn.move(200,0)
        self.viewBtn.clicked.connect(self.displayTab)


        self.filebtns1 = QPushButton('Photo dir', self)
        self.filebtns1.clicked.connect(self.file2)


        self.filebtns1.move(300,199)

        #------------



        args.thread = AThread()

        #------------

        #args.thread.finished.connect(args.thread.run)
        #args.thread.start()
        g = lambda: self.launches(args)
        self.btned.clicked.connect(g)
        self.launches(args)
        conn = sqlite3.connect('user.db')
        c = conn.cursor()
        c.execute('CREATE TABLE IF NOT EXISTS webstuffs(links TEXT, videos TEXT, photos TEXT, vidname TEXT, photoname TEXT, vidimg TEXT, imgimg TEXT)')
        c.execute('SELECT * FROM webstuffs')
        tex = c.fetchall()
        self.labb = QLabel(self)
        try:
            self.labb.setText(str(tex[-1]))
        except:
            pass
        self.labb.resize(500,500)
        self.labb.move(0,300)

        #self.nameit = QLineEdit(self)
        #self.nameit.move(50,100)
        #self.photot = QLineEdit(self)
        #self.photot.move(50,200)


        self.show()
        #print(AThread.var.get_current_url())


        '''runnable = Runnable()
        QThreadPool.globalInstance().start(runnable)
        background
        '''

        '''objThread = QThread()
        obj = SomeObject()
        obj.moveToThread(objThread)

        objThread.started.connect(obj.long_running)
        #objThread.finished.connect(app.exit)
        objThread.start()'''
    def file2(self):
        dir = ''
        self.fileobj2 = QFileDialog.getExistingDirectory(self, 'open file dialog', dir=dir)
        conn = sqlite3.connect('system info.db')
        c = conn.cursor()
        c.execute('CREATE TABLE IF NOT EXISTS dir(screenshots TEXT)')
        c.execute('INSERT INTO dir(screenshots) VALUES (?)', [self.fileobj2])
        print(self.fileobj2)
        conn.commit()
        #c.execute('SELECT * FROM dir')
        #checks = c.fetchall()
        #print(checks)
        #print(self.fileobj2)


    def launches(self, args):
        #thread = AThread()
        #thread.finished.connect(thread.run)
        args.thread.start()

    def checking(self):
        '''conn = sqlite3.connect('user.db')
        c = conn.cursor()
        c.execute('CREATE TABLE IF NOT EXISTS webstuffs(links TEXT, videos TEXT, photos TEXT)')
        c.executer('INSERT INTO webstuffs(videos) VALUES (?)', (self.browser.ur(),))
        conn.commit()

        print(self.browser.url())'''

        #print(ok)
        ok = webview.get_current_url()
        if len(str(ok)) > 1:

            print('fuck her!')





            text, self.oktext = QInputDialog.getText(self, 'Input Dialog', 'Name of the link:')

            #self.msg.show()
            #elf.tbox.show()
            conn = sqlite3.connect('system info.db')
            c = conn.cursor()
            c.execute('SELECT * FROM dir')
            checks = c.fetchall()
            print(str(checks[-1]))
            for var in checks[-1]:
                varg = str(var) + '/' + str(text)

            with mss.mss() as sct:
                filename = sct.shot(mon=-1, output=str(varg))
                print(filename)

                print(str(text))
                conn = sqlite3.connect('user.db')
                c = conn.cursor()
                c.execute('CREATE TABLE IF NOT EXISTS webstuffs(links TEXT, videos TEXT, photos TEXT, vidname TEXT, photoname TEXT, vidimg TEXT, imgimg TEXT)')
                c.execute('INSERT INTO webstuffs(videos, vidname, vidimg) VALUES (?, ?, ?)', (str(ok), str(text), str(filename)))
                conn.commit()
                print(varg)
                print(ok)
                print(text)
                self.show()



    def checking2(self, varg='C:/new/fullscreen.png'):
        '''conn = sqlite3.connect('user.db')
        c = conn.cursor()
        c.execute('CREATE TABLE IF NOT EXISTS webstuffs(links TEXT, videos TEXT, photos TEXT)')
        c.executer('INSERT INTO webstuffs(videos) VALUES (?)', (self.browser.ur(),))
        conn.commit()

        print(self.browser.url())'''

        #print(ok)


        ok = webview.get_current_url()
        if len(str(ok)) > 1:

            print('fuck her!')
            conn = sqlite3.connect('user.db')
            c = conn.cursor()




            text2, self.oktext2 = QInputDialog.getText(self, 'Input Dialog', 'Name of the photo link:')

            #self.msg.show()
            #elf.tbox.show()

            conn = sqlite3.connect('system info.db')
            c = conn.cursor()
            c.execute('SELECT * FROM dir')
            checks = c.fetchall()
            print(str(checks[-1]))
            for var in checks[-1]:
                varg = str(var) + '/' + str(text2)

            with mss.mss() as sct:
                filename = sct.shot(mon=-1, output=str(varg))
                print(filename)
                # sct.save()
                # print(filename)

                print(str(text2))
                conn = sqlite3.connect('user.db')
                c = conn.cursor()
                c.execute('CREATE TABLE IF NOT EXISTS webstuffs(links TEXT, videos TEXT, photos TEXT, vidname TEXT, photoname TEXT, vidimg TEXT, imgimg TEXT)')
                c.execute('INSERT INTO webstuffs(photos, photoname, imgimg) VALUES (?, ?, ?)', (str(ok), str(text2), str(filename)))
                conn.commit()
                self.show()



    def newurl(self, args):

        webview.load_url(str(self.addUrl.text()))
        #args.thread.start()

    def get_current_ur(self):
        import webview
        from time import sleep

        webview.create_window(title='ok', url='https://www.bing.com', width=600, height=600, resizable=False,
                              fullscreen=False, min_size=(200, 100), strings={}, confirm_quit=False,
                              background_color='#FFF')

        print(webview.get_current_url())

    def displayTab(self):
        self.close()
        webview.destroy_window()
        views = DisplayB()
        views.show()
        views.exec_()


class DisplayB(QMainWindow):

    def __init__(self, parent=None):
        super(DisplayB, self).__init__(parent)
        self.video()

    def video(self):
        self.tabss = QTabWidget(self)
        self.tabss.resize(1000,1000)
        #self.tabss2 = QTabBar(self)
        self.setGeometry(100,100,1000,1000)
        self.setWindowTitle('Links')
        self.firsttab = QWidget()
        self.firsttab2 = QWidget()
        self.firsttab3 = QWidget()

        self.tabss.addTab(self.firsttab, 'Show Video')

        self.tabss.addTab(self.firsttab2, 'Show Images')
        self.tabss.addTab(self.firsttab3, 'Show Other')
        layout = QVBoxLayout()
        self.t1btn = QSystemTrayIcon(self)
        conn = sqlite3.connect('user.db')
        c = conn.cursor()
        c.execute('SELECT videos FROM webstuffs WHERE videos NOT NULL')
        links = c.fetchall()
        print(links)
        conn.close()
        conn = sqlite3.connect('user.db')
        c = conn.cursor()
        c.execute('SELECT vidimg FROM webstuffs WHERE vidimg NOT NULL')
        screenshots = c.fetchall()
        print(screenshots)
        c.execute('SELECT vidname FROM webstuffs WHERE vidname NOT NULL')
        vname = c.fetchall()
        print(vname)
        self.list = QListWidget()
        self.list.move(200,200)
        for newvars in screenshots:

            for self.itemname, something, counts in zip(links, newvars, vname):
                counts = QListWidgetItem(str(self.itemname))
                print(counts)

                counts.setData(Qt.UserRole, str(something))
                self.list.addItem(counts)
            self.list.setMaximumSize(900,200)

            layout.addWidget(self.list)

        self.firsttab.setLayout(layout)




        #----image
        layout2 = QVBoxLayout()
        conn.close()
        conn = sqlite3.connect('user.db')
        c = conn.cursor()
        c.execute('SELECT photos FROM webstuffs WHERE photos NOT NULL')
        imglinks = c.fetchall()
        conn.close()
        print(imglinks)
        conn = sqlite3.connect('user.db')
        c = conn.cursor()
        c.execute('SELECT imgimg FROM webstuffs WHERE imgimg NOT NULL')
        imgshots = c.fetchall()
        conn.close()

        print(imgshots)
        conn = sqlite3.connect('user.db')
        c = conn.cursor()
        c.execute('SELECT photoname FROM webstuffs WHERE photoname NOT NULL')
        aname = c.fetchall()
        conn.close()
        print(aname)
        self.list2 = QListWidget()
        self.list2.move(400, 400)
        for newvar in imgshots:

            for self.itemname2, something2, self.baname in zip(imglinks, newvar, aname):
                self.baname = QListWidgetItem(str(self.itemname2))
                print(self.itemname2)

                self.baname.setData(Qt.UserRole, str(something2))
                self.list2.addItem(self.baname)
            layout2.addWidget(self.list2)
        try:
            self.labed = QLabel()
            self.labed.setPixmap(self.okay)


            layout2.addWidget(self.labed)
        except:
            pass
        self.list2.setMaximumSize(900, 200)
        self.firsttab2.setLayout(layout2)
        self.list.clicked.connect(self.printcheck)
        self.list2.clicked.connect(self.printcheck2)

    def printcheck2(self):
        self.printvar2 = self.list2.currentItem().data(Qt.UserRole)
        print(self.printvar2)
        print(self.list2.currentItem().text())
        self.okay = str(self.printvar2)
        self.labed = QLabel()
        self.labed.setPixmap(self.okay)
        print(self.okay)

        self.labed.show()
        print(self.okay)





    def printcheck(self):
        self.printvar = self.list.currentItem().data(Qt.UserRole)
        print(self.printvar)
        print(self.list.currentItem().text())
        okay = str(self.printvar)
        self.labed = QLabel()
        self.labed.setPixmap(okay)
        print(okay)

        self.labed.show()
        print(okay)

class SomeObject(QObject):

    #finished = pyqtSignal()

    def long_running(self):
        from time import sleep
        count = 0
        '''while count < 30:
            sleep(1)
            print("B Increasing")
            count += 1
        self.finished.emit()'''

class Runnable(QRunnable):

    def run(self):
        from time import sleep
        webB.get_current_ur
        count = 0
        while count < 5:
            sleep(1)
            print("A Increasing")
            count += 1



class rpygame():

    def pruns(self):
        pygame.init()
        gameDisplay = pygame.display.set_mode((800,600))
        pygame.display.set_caption('window caption')
        clock = pygame.time.Clock()
        carImg = pygame.image.load('C:/Users/fish/Downloads/nice/icons8-sunday-50.png')

        crashed = False
        while not crashed:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    crashed = True
                print(event)
            pygame.display.update()
            clock.tick(60)
        #pygame.quit()
        #quit()

class AThread(QThread):
    var = 0
    def run(self):

        import webview
        from time import sleep

        webview.create_window(title='ok', url='https://www.bing.com', width=800, height=600, resizable=True,
                              fullscreen=False, min_size=(200, 100), strings={}, confirm_quit=False,
                              background_color='#FFF')
        AThread.var = webview
        #print(webview.get_current_url())
        '''while count < 5:
            #time.sleep(1)
            print("A Increasing")
            count += 1'''



'''pygame.init()
s=pygame.Surface((640,480))
s.fill((64,128,192,224))
pygame.draw.circle(s,(255,255,255,255),(100,100),50)'''



app = QApplication(sys.argv)
app.setStyleSheet(qdarkstyle.load_stylesheet_pyside())
#w=MainWindow(s)
#w.show()
form = Form()
form.show()
app.exec_()