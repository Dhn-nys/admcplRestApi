print("########################################")
print("#                                      #")
print("# ADMINISTRATOR CONTROL PANEL Ver.1.10 #")
print("#                                      #")
print("########################################")
print(" ")
print("########################################")
print("#   Keys  ||           Action          #")
print("#   1     ||  Open View All Data Admin #")
print("#   2     ||  Open View One Data Admin #")
print("#   3     ||  Add Data Admin           #")
print("#   4     ||  Edit Data Admin          #")
print("#   5     ||  Delete All Data Admin    #")
print("#   6     ||           Exit            #")
print("########################################")
print(" ")
pilih=raw_input("Select : ")
print ""
if pilih =='1':
      execfile('viewall.py')
elif pilih == '2':
      execfile('viewid.py')
elif pilih == '3':
      execfile('insertadmin.py')
elif pilih == '4':
      execfile('editadmin.py')
elif pilih == '5':
      execfile('deleteadmin.py')