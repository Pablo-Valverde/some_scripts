import ctypes, sys
from time import sleep

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if is_admin():
    print("Admin")
else:
    print("Not Admin")
sleep(5)
sys.exit()