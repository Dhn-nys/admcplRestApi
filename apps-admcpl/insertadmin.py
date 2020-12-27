print("#######################")
print("#                     #")
print("#    Add Data Admin   #")
print("#                     #")
print("#######################")
print(" ")

word1 = ("http://localhost/Restapi/restapi.php?fiture=insadm&nm_adm=")
name = raw_input("What your Name : ")

word2 = ("&pwd_adm=")
psw = raw_input("Password : ")

word3 = ("&tgl=")
date = raw_input("Date [Exampe YYYY-MM-DD]: ")

link = "{}{}{}{}{}{}".format(word1, name, word2, psw, word3, date)

import webbrowser

webbrowser.open(link)
execfile('main.py')