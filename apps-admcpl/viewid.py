print("#######################")
print("#                     #")
print("# View All Data Admin #")
print("#                     #")
print("#######################")
print(" ")
api = ("http://localhost/Restapi/restapi.php?fiture=viewadm&id=")
ide = raw_input("Admin ID: ")

link = "{}{}".format(api, ide)

import webbrowser

webbrowser.open(link)
execfile('main.py')