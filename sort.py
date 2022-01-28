# -*- coding: utf-8 -*-
import glob
import os
import pathlib
import shutil
from sys import argv
from os import path

folder = []
home_dir = pathlib.Path.home()
name, path_dir = argv

images = ['.jpeg','.png','.jpg','.svg']
video = ['.avi','.mp4','.mov','.mkv']
documents = ['.doc','.docx','.txt','.pdf','.xlsx','.pptx']
music = ['.mp3','.ogg','.wav','.amr']
archives = ['.zip','.gz','.tar','.rar']

img_location = ('./images')
vid_location = ('./videos')
doc_location = ('./documents')
mus_location = ('./audio')
arc_location = ('./archives/')

location_dirs = [img_location, vid_location, doc_location, mus_location, arc_location]

def del_empty_dirs(path):
    for d in os.listdir(path):
        a = os.path.join(path, d)
        if os.path.isdir(a):
            del_empty_dirs(a)
            if not os.listdir(a):
                os.rmdir(a)

def make_dirs(location):
    os.makedirs(location)

def move_files(pa):
    filename = glob.glob(pa)
    for files in filename:
       os.rename(files, normalize(files,legend))

    filename = glob.glob(pa)
    
    for file in filename:
        
            
        if os.path.splitext(file)[1] in images:
            if(path.exists(img_location)):
                shutil.move(file,img_location)
            else:
                os.makedirs(img_location)
                shutil.move(file,img_location)
        if os.path.splitext(file)[1] in video:
            if(path.exists(vid_location)):
                shutil.move(file,vid_location)
            else:
                os.makedirs(vid_location)
                shutil.move(file,vid_location)
        if os.path.splitext(file)[1] in documents:
            if(path.exists(doc_location)):
                shutil.move(file,doc_location)
            else:
                os.makedirs(doc_location)
                shutil.move(file,doc_location)
        if os.path.splitext(file)[1] in music:
            if(path.exists(mus_location)):
                shutil.move(file,mus_location)
            else:
                os.makedirs(mus_location)
                shutil.move(file,mus_location)
        if os.path.splitext(file)[1] in archives:
            if(path.exists(arc_location)):
                shutil.unpack_archive(file, './archives/' + os.path.splitext(os.path.basename(file))[0] + '/')
                shutil.move(file, arc_location)
            else:
                os.makedirs(arc_location)
                shutil.unpack_archive(file,'./archives/' + os.path.splitext(os.path.basename(file))[0] + '/')
                shutil.move(file, arc_location)
                   
def normalize (some_string, dic):
    n_string = some_string.translate(dic)
    return n_string

legend = {
    '~':'_',
    '@':'_',
    '#':'_',
    '$':'_',
    '%':'_',
    '^':'_',
    '-':'_',
    ' ':'_',
    '(':'_',
    ')':'_',
    '{':'_',
    '}':'_',
    ',':'',
    ord('а'):'a',
    ord('б'):'b',
    ord('в'):'v',
    ord('г'):'g',
    ord('д'):'d',
    ord('е'):'e',
    ord('ё'):'yo',
    ord('ж'):'zh',
    ord('з'):'z',
    ord('и'):'i',
    ord('й'):'y',
    ord('к'):'k',
    ord('л'):'l',
    ord('м'):'m',
    ord('н'):'n',
    ord('о'):'o',
    ord('п'):'p',
    ord('р'):'r',
    ord('с'):'s',
    ord('т'):'t',
    ord('у'):'u',
    ord('ф'):'f',
    ord('х'):'h',
    ord('ц'):'c',
    ord('ч'):'ch',
    ord('ш'):'sh',
    ord('щ'):'shch',
    ord('ъ'):'y',
    ord('ы'):'y',
    ord('ь'):"'",
    ord('э'):'e',
    ord('ю'):'yu',
    ord('я'):'ya',

    ord('А'):'A',
    ord('Б'):'B',
    ord('В'):'V',
    ord('Г'):'G',
    ord('Д'):'D',
    ord('Е'):'E',
    ord('Ё'):'Yo',
    ord('Ж'):'Zh',
    ord('З'):'Z',
    ord('И'):'I',
    ord('Й'):'Y',
    ord('К'):'K',
    ord('Л'):'L',
    ord('М'):'M',
    ord('Н'):'N',
    ord('О'):'O',
    ord('П'):'P',
    ord('Р'):'R',
    ord('С'):'S',
    ord('Т'):'T',
    ord('У'):'U',
    ord('Ф'):'F',
    ord('Х'):'H',
    ord('Ц'):'Ts',
    ord('Ч'):'Ch',
    ord('Ш'):'Sh',
    ord('Щ'):'Shch',
    ord('Ъ'):'Y',
    ord('Ы'):'Y',
    ord('Ь'):"'",
    ord('Э'):'E',
    ord('Ю'):'Yu',
    ord('Я'):'Ya',
    }

for locations in location_dirs:
    make_dirs(locations)

for i in os.walk(path_dir):
    folder.append(i)
    
for address, dirs, files in folder:
    for file in files:
        x = address+'/'+file
        move_files(x)
        
del_empty_dirs(path_dir)    

                                      