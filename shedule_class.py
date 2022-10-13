from watchdog.events import FileSystemEventHandler
def get_name(a):
        a = a.split("\\")
        a = a[len(a) - 1].split(".")
        return a[0]
def print_letters(a):
    for i in a:
        if(i.lower()=='a' or i.lower()=='e' or i.lower()=='i' or i.lower()=='o' or i.lower()=='u' or i.lower()=='y' or i.lower()=='i' or i.lower()=='а' or i.lower()=='е' or i.lower()=='ё' or i.lower()=='и' or i.lower()=='о' or i.lower()=='у'  or i.lower()=='ы' or i.lower()=='э' or i.lower()=='ю' or i.lower()=='я'):
            print(i.lower())
        else:
            print(i.upper())
class FileShedule(FileSystemEventHandler):
    def __init__(self, file_path) -> None:
        self._file_path = file_path
    def on_created(self, event):
        print_letters(get_name(event.src_path))