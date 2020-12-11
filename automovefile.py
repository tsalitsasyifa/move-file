import shutil
from glob import glob
from time import sleep
import os


# scanning where to extract
def mv(dirs, formats):
    for file in dirs:
        shutil.move(file, os.path.join(root_dest_dir, formats))




# scanning dir path
def name():
    print("\tAuto Move File Pogram")
    print()
    print('=====================================')
    print("Anggota Kelompok: ")
    print("1. Nicholas  Raditya Nakevin Sagala")
    print("Absen 17")
    print("2. Tsalitsa Syifa 'Ufuadi")
    print("Absen 24")
    print('=====================================')
    print()

    

    global root_base_dir
    global root
    global root_dest_dir
    global dest
    root = input("Masukan Path Asal Untuk File/Folder: ")
    dest = input("Masukan Path Destinasi Untuk File/Folder: ")
    root_base_dir = r"%s" % root
    root_dest_dir = r"%s" % dest
  

# scanning file type

    
    txt = glob("%s\*.txt" % root_base_dir)
    jpg = glob("%s\*.jpg" % root_base_dir)
    word = glob("%s\*.doc" % root_base_dir)
    word2 = glob("%s\*.docx" % root_base_dir)
    pdf = glob("%s\*.pdf" % root_base_dir)
    png = glob("%s\*.png" % root_base_dir)
    rar = glob("%s\*.rar" % root_base_dir)
    zip = glob("%s\*.zip" % root_base_dir)
    sevenz = glob("%s\*.7z" % root_base_dir)
    exe = glob("%s\*.exe" % root_base_dir)
    py = glob("%s\*.py" % root_base_dir)
    mp3 = glob("%s\*.mp3" % root_base_dir)
    wav = glob("%s\*.wav" % root_base_dir)
    mp4 = glob("%s\*.mp4" % root_base_dir)
    iso = glob("%s\*.iso" % root_base_dir)
    flv = glob("%s\*.flv" % root_base_dir)
    mkv = glob("%s\*.mkv" % root_base_dir)
    csv = glob("%s\*.csv" % root_base_dir)
    xml = glob("%s\*.xml" % root_base_dir)
    apk = glob("%s\*.apk" % root_base_dir)
    bat = glob("%s\*.bat" % root_base_dir)
    bmp = glob("%s\*.bmp" % root_base_dir)
    gif = glob("%s\*.gif" % root_base_dir)
    ico = glob("%s\*.ico" % root_base_dir)
    html = glob("%s\*.html" % root_base_dir)
  



# Moving file

    print()
    print("\tScanning...")
    sleep(2)
    print("\tAnalyzing...")
    sleep(1)
    print("\tSemua File Siap Dipindahkan")
    print()
    user = input("Pindahkan File Dari %s ? (y/n): " % root)
    print()
    if user == 'y' or user == 'Y':
        sleep(0.5)
        print("\tMemindahkan File...")
        mv(txt, 'txt')
        mv(jpg, 'jpg')
        mv(word, 'word')
        mv(word2, 'word2')
        mv(pdf, 'pdf')
        mv(png, 'png')
        mv(rar, 'rar')
        mv(zip, 'zip')
        mv(sevenz, 'sevenz')
        mv(exe, 'exe')
        mv(py, 'py')
        mv(mp3, 'mp3')
        mv(wav, 'wav')
        mv(mp4, 'mp4')
        mv(iso, 'iso')
        mv(flv, 'flv')
        mv(mkv, 'mkv')
        mv(csv, 'csv')
        mv(xml, 'xml')
        mv(apk, 'apk')
        mv(bat, 'bat')
        mv(bmp, 'bmp')
        mv(gif, 'gif')
        mv(ico, 'ico')
        mv(html, 'html')
        sleep(1)
        print("\tPengecekan File Kembali...")
        sleep(0.5)
        print()
        print("\t\tFile Berhasil Dipindahkan")
        name()
    else:
        name()


# Accessing program
name()


        
    
    
    

                    
            
    

