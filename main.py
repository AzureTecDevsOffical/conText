import npyscreen, fs_utils, os, argparse, signal

parser = argparse.ArgumentParser(prog='context', description='Edit files in your console.', epilog='(c) 2025 AzureTecDevs  |  Updated: 1-1-2025')
parser.add_argument('--file', '-f', help='file to open by default')
args = parser.parse_args()

def handler(signum, frame):
    exit(code=0)
signal.signal(signal.SIGINT, handler)

class MainScreen(npyscreen.FormBaseNewWithMenus):
    def create(self):
        self.title = self.add(npyscreen.FixedText, value='new', color='LABEL')
        self.menu1 = self.new_menu('Menu')
        self.editor = self.add(npyscreen.MultiLineEdit, value = '''''')
        self.menu1.addItem('Open', onSelect=self.spawn_file_dialog, shortcut='^O')
        self.menu1.addItem('Save as', onSelect=self.spawn_file_dialog_save, shortcut='^N')
        self.menu1.addItem('Save', onSelect=self.spawn_file_dialog_savecur, shortcut='^S')
        self.menu1.addItem('Exit', onSelect=self.exitg, shortcut='^C')
        if not args.file == None:
            self.open_file(args.file)
    
    def exitg(self):
        print('Exit')
        exit(code=0)

    def spawn_file_dialog(self):
        selected_file = npyscreen.selectFile(confirm_if_exists=False)
        self.editor.value = fs_utils.openFile(selected_file)
        self.title.value = selected_file
    
    def open_file(self, file):
        selected_file = os.path.abspath(file)
        self.editor.value = fs_utils.openFile(selected_file)
        self.title.value = selected_file
    
    def spawn_file_dialog_save(self):
        selected_file = npyscreen.selectFile(confirm_if_exists=False)
        fs_utils.writeFile(selected_file, self.editor.value)
        self.title.value = selected_file
    
    def spawn_file_dialog_savecur(self):
        fs_utils.writeFile(self.title.value, self.editor.value)

class MyApplication(npyscreen.NPSAppManaged):
    def onStart(self):
        self.addForm('MAIN', MainScreen, name='conText 0.1.0')

if __name__ == '__main__':
    TestApp = MyApplication().run()
