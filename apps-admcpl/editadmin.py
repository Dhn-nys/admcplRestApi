print("#######################")
print("#                     #")
print("#   Edit Data Admin   #")
print("#                     #")
print("#######################")
print(" ")

word1 = ("http://localhost/Restapi/restapi.php?fiture=editadm&nm_adm=")
name = raw_input("Change Name : ")

word2 = ("&pwd_adm=")
psw = raw_input("Change Password : ")

word3 = ("&tgl=")
date = raw_input("Change Date [Exampe YYYY-MM-DD]: ")

word4 = ("&id=")
ide = raw_input("ID Admin: ")

link = "{}{}{}{}{}{}{}{}".format(word1, name, word2, psw, word3, date, word4, ide)

import webbrowser

webbrowser.open(link)
execfile('main.py')