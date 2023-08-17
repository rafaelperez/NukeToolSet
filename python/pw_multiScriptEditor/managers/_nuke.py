import os, sys, re
# import nuke
main = __import__('__main__')
ns = main.__dict__
exec ('import nuke') in ns
nuke = ns['nuke']
import nukescripts
from managers.nuke import nodes
nuke_nodes = dir(nodes)
from managers.completeWidget import contextCompleterClass

from Qt.QtGui import *
from Qt.QtWidgets import *
from Qt.QtCore import *

p = os.path.dirname(__file__).replace('\\','/')
if not p in sys.path:
    sys.path.insert(0, p)

from pw_multiScriptEditor import scriptEditor
try:
	from importlib import reload
except:
	pass
reload(scriptEditor)

# QT
qApp = QApplication.instance()

def getMainWindow():
    for widget in qApp.topLevelWidgets():
        if widget.metaObject().className() == 'Foundry::UI::DockMainWindow':
            return widget
qNuke = getMainWindow()

def show(panel=False):
    if panel:
        import pw_multiScriptEditor.scriptEditor
        nukescripts.panels.registerWidgetAsPanel("pw_multiScriptEditor.scriptEditor.scriptEditorClass", "Multi Script Editor", "pw_multi_script_editor")
    else:
        showWindow()


def showWindow():
    se = scriptEditor.scriptEditorClass(qNuke)
    se.runCommand('import nuke')
    se.show()


# add to menu.py
# Add to menu.py
# menubar = nuke.menu("Nuke")
# toolMenu = menubar.addMenu('&Tools')
# path = 'path/to/MultiScriptEditor_module'
# # example c:/nuke/python/lib
# if not path in sys.path:
#     sys.path.append(path)
#
# import pw_multiScriptEditor
# # add to menu
# toolMenu.addCommand("Multi Script Editor", "pw_multiScriptEditor.showNuke()")
# # create new pane
# pw_multiScriptEditor.showNuke(panel=True)


############ COMPLETER

def completer(line):
    # node types
    p1 = r"nuke\.createNode\(['\"](\w*)$"
    m = re.search(p1, line)# or re.search(p2, line)
    if m:
        name = m.group(1)
        l = len(name)
        if name:
            auto = [x for x in nuke_nodes if x.lower().startswith(name.lower())]
        else:
            auto = nuke_nodes
        return [contextCompleterClass(x, x[l:], True) for x in auto], None
    # exists nodes
    p3 = r"nuke\.toNode\(['\"](\w*)$"
    m = re.search(p3, line)
    if m:
        name = m.group(1)
        nuke.tprint(name)
        nodes = [x.name() for x in nuke.allNodes()] #recurseGroups=True
        if name:
            result = [x for x in nodes if x.lower().startswith(name.lower())]
        else:
            result = nodes
        l = len(name)
        return [contextCompleterClass(x, x[l:], True) for x in result], None
    return None, None

################  CONTEXT MENU

def contextMenu(parent):
    m = nukeContextMenu(parent)
    return m

class nukeContextMenu(QMenu):
    def __init__(self, parent):
        super(nukeContextMenu, self).__init__('Nuke')
        self.par = parent
        # a.setShortcut('Alt+Return')
        # a.setShortcutContext(Qt.ApplicationShortcut)
        self.addAction(QAction('Read PyScript Knob', parent, triggered=self.readPyScriptKnob))
        self.addAction(QAction('Save To PyScript Knob', parent, triggered=self.saveToKnob))
        self.addSeparator()
        self.addAction(QAction('From Selected', parent, triggered=self.nodeToCode))
        self.addAction(QAction('From Clipboard', parent, triggered=self.nodesFromClipboard))

    def nodeToCode(self):
        nodes = nuke.selectedNodes()
        names = [x.name() for x in nodes]
        result = '\n'.join(["nuke.toNode('%s')" % x for x in names])
        self.par.insertText(result)

    def getPyKnob(self, title):
        s = nuke.selectedNodes()
        if s:
            s = s[0]
            pyKnobs = [x for x in s.knobs().values() if x.Class() in ['PyScript_Knob','PythonCustomKnob']]
            if pyKnobs:
                result = {}
                for k in pyKnobs:
                    result[k.name()] = k
                if result:
                    dial = selectDialog(result.keys(), title)
                    if dial.exec_():
                        name = dial.list.currentItem().text()
                        knob = result[name]
                        return knob
            else:
                nuke.message('Python Knobs not found')
        else:
            nuke.message('Select one node')

    def readPyScriptKnob(self):
        knob = self.getPyKnob('Select Python Knob to Read')
        if knob:
            text = knob.value()
            self.par.tab.addNewTab(knob.node().name()+' | '+knob.name(), text)

    def saveToKnob(self):
        knob = self.getPyKnob('Select Python Knob to Save')
        if knob:
            text = self.par.tab.getCurrentText()
            knob.setValue(text)

    def nodesFromClipboard(self):
        nuke.tprint(str(self.par))
        text = QApplication.clipboard().text()
        nodes = []
        if text:
            for l in text.split('\n'):
                res = re.findall(r'name \w+$', l)
                if res:
                    name = res[0].split()[1]
                    nodes.append(name)
        for n in nodes:
            self.par.tab.addToCurrent('nuke.toNode("%s")\n' % n)

class selectDialog(QDialog):
    def __init__(self, items, title):
        super(selectDialog, self).__init__()
        self.setWindowTitle(title)
        self.setWindowFlags(Qt.Tool)
        self.list = QListWidget(self)
        self.list.setSelectionMode(QAbstractItemView.SingleSelection)
        self.ly = QVBoxLayout(self)
        self.setLayout(self.ly)
        self.ly.addWidget(self.list)

        self.btn = QPushButton('Select')
        self.ly.addWidget(self.btn)
        self.btn.clicked.connect(self.accept)
        for i in items:
            item = QListWidgetItem(i)
            item.setData(32, i)
            self.list.addItem(item)

    def closeEvent(self, *args, **kwargs):
        self.reject()
        super(selectDialog, self).closeEvent( *args, **kwargs)


