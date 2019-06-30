import time,subprocess,os
os.system("clear")

normal = "\033[0;37;40m" #normal
miring = "\033[3;37;40m" #miring

#text warna
abu = "\033[1;30;40m" #abu abu
merah = "\033[1;31;40m" #merah
hijau = "\033[1;32;40m" #hijau
kuning = "\033[1;33;40m" #kuning
biru = "\033[1;34;40m" #biru
pink = "\033[1;35;40m" #pink
birumuda = "\033[1;36;40m" #birumuda
putih = "\033[1;37;40m" #putih


print
print putih+"                                                ["+kuning+" Tool - Facebook "+putih+"]"
print putih+"               ( ) > Termux                                         "
print putih+"              (   )                "+merah+"?????????????????????????????????"
print putih+"             (     )               "+merah+"??"+kuning+" Author : Mr. Achmad         "+hijau+"?? "
print putih+"           _(       )_             "+merah+"??"+kuning+" Contact WA : 085608035292   "+hijau+"??"
print putih+"          [ INDONESIA ]            "+hijau+"?????????????????????????????????"+normal
print "____________________________________________________________________"
print "_____________________"+biru+"Selamat_Datang_ya_Bangsat"+putih+"______________________"
print

                 

print(merah+"[!]"+kuning+" Mohon maaf trial gratis sudah berakhir")
print(merah+"[!]"+kuning+" Silahkan membeli fitur premium untuk tool-night.")
print(merah+"[!]"+kuning+" Pilih y untuk langsung menghubungi administrator (whatsapp)")
print
f=raw_input(putih+"[!] beli? y/n):").lower()
if f =="y":
    subprocess.check_output(
								["am","start",
				"https://api.whatsapp.com/send?phone=6285608035292&text=hello%20admin%20saya%20ingin%20membeli%20tool - Night%20premium%20Seharga%2020k"])
exit("[!] terimakasih atas jawaban anda.")
    
#s=subprocess.Popen(["git","pull"],
#    stdout=subprocess.PIPE)
#time.sleep(2)