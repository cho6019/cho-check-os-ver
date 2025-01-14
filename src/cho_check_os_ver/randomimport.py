import random
#from check_os_ver.hi import hi as hi1
#from hj_check_os_version.hi import hi as hi2
#from jacob_os_version_check.hi import hi as hi3
#from lucas_check_os_ver.hi import hi as hi4
#from stundrg_check_os_ver.hi import hi as hi5
#from nunininu_check_os_ver.hi import hi as hi6
#from seo-check-os-version.hi import hi as hi7

def pick():
    a = random.randint(1, 7)


    match a:
        case 1:
            print("hi1")
            from check_os_ver.hi import hi as hi1
            return(hi1())
        case 2:
            print("hi2")
            from hj_check_os_version.hi import hi as hi2
            return(hi2())
        case 3:
            print("hi3")
            from jacob_os_version_check.hi import hi as hi3
            return(hi3())
        case 4:
            print("hi4")
            from lucas_check_os_ver.hi import hi as hi4
            return(hi4())
        case 5:
            print("hi5")
            from stundrg_check_os_ver.hi import hi as hi5
            return(hi5())
        case 6:
            print("hi6")
            from nunininu_check_os_ver.hi import hi as hi6
            return(hi6())
    #elif a==7:
        #A=hi7()
