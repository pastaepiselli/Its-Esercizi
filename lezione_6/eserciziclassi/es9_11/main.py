from lezione_6.eserciziclassi.es9_11.module_users import *

popa = User('alessandro', 'popa', 'noj', 'popa@gmail.com')

cose = Privileges(['cosa', 'potete', 'fare'])


pier = Admin(popa, cose)

pier.user.describe_user()

pier.priviileges.show_privileges()