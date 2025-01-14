import random
from check_os_ver.hi import hi as hi1
from hj_check_os_version.hi import hi as hi2
from jacob_os_version_check.hi import hi as hi3
from lucas_check_os_ver.hi import hi as hi4
from stundrg_check_os_ver.hi import hi as hi5
from nunininu_check_os_ver.hi import hi as hi6
#from seo-check-os-version.hi import hi as hi7


a = random.randint(1, 8)

if a==1:
    A=hi1()
elif a==2:
    A=hi2()
elif a==3:
    A=hi3()
elif a==4:
    A=hi4()
elif a==5:
    A=hi5()
elif a==6:
    A=hi6()
#elif a==7:
    #A=hi7()

print(A)
