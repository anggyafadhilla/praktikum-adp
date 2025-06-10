import os
from termcolor import colored, cprint
os.system('cls')
nama=input("Masukkan nama : ")
umur=input("Masukkan umur : ")
def print_cake():

    lilin=colored("        i   i   i","red")
    print(lilin)
    print("        |   |   |")
    print("       ( ) ( ) ( )")

    print("        |   |   |")
    print("        |   |   |")

    la1=colored("     ***************",'yellow')
    print(la1)
    la2=colored("    *~~~~~~~~~~~~~~~*","red")
    print(la2)
    la3=colored("   *                 *","light_blue")
    print(la3)

    lt1=colored("   ===================","yellow")
    print(lt1)
    lt2=colored("  *                   *","light_blue")
    print(lt2)
    lt3=colored("  =====================","red")
    print(lt3)

    lb1=colored(" *                      *","light_blue")
    print(lb1)
    lb2=colored("*~~~~~~~~~~~~~~~~~~~~~~~~*",'red',"on_white")
    print(lb2)
    lb3=colored("==========================","yellow")
    print(lb3)

    ls=colored("##########################",'red','on_white')
    print(ls)

    print("\nSelamat Ulang Tahun yang ke "+umur+" "+ nama+"!")
print_cake()