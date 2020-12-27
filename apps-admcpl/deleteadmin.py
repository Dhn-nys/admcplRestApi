print("#######################")
print("#                     #")
print("#   Delete Data Admin #")
print("#                     #")
print("#######################")
print(" ")
api = ("http://localhost/Restapi/restapi.php?fiture=dltadm&id=")
ide = raw_input("Admin ID: ")

link = "{}{}".format(api, ide)

import webbrowser

webbrowser.open(link)
execfile('main.py')