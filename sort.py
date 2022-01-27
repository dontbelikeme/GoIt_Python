# -*- coding: utf-8 -*-
import glob
import os
import pathlib
import shutil
from sys import argv
from os import path

folder = []
ignore_list = ['./images', './videos', './documents', './audio', './archives']
home_dir = pathlib.Path.home()
name, path_dir = argv


def del_empty_dirs(path):
    for d in os.listdir(path):
        a = os.path.join(path, d)
        if os.path.isdir(a):
            del_empty_dirs(a)
            if not os.listdir(a):
                os.rmdir(a)

def move_files(pa):
    filename = glob.glob(pa)

    for file_old in filename:
    
        file_new = normalize(file_old, legend)

        if file_old != file_new:
            os.rename(file_old, file_new)

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
                   
def normalize (letter, dic):
    for i, j in dic.items():
        letter = letter.replace(i, j)
    return letter

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
    'а':'a',
    'б':'b',
    'в':'v',
    'г':'g',
    'д':'d',
    'е':'e',
    'ё':'yo',
    'ж':'zh',
    'з':'z',
    'и':'i',
    'й':'y',
    'к':'k',
    'л':'l',
    'м':'m',
    'н':'n',
    'о':'o',
    'п':'p',
    'р':'r',
    'с':'s',
    'т':'t',
    'у':'u',
    'ф':'f',
    'х':'h',
    'ц':'c',
    'ч':'ch',
    'ш':'sh',
    'щ':'shch',
    'ъ':'y',
    'ы':'y',
    'ь':"'",
    'э':'e',
    'ю':'yu',
    'я':'ya',

    'А':'A',
    'Б':'B',
    'В':'V',
    'Г':'G',
    'Д':'D',
    'Е':'E',
    'Ё':'Yo',
    'Ж':'Zh',
    'З':'Z',
    'И':'I',
    'Й':'Y',
    'К':'K',
    'Л':'L',
    'М':'M',
    'Н':'N',
    'О':'O',
    'П':'P',
    'Р':'R',
    'С':'S',
    'Т':'T',
    'У':'U',
    'Ф':'F',
    'Х':'H',
    'Ц':'Ts',
    'Ч':'Ch',
    'Ш':'Sh',
    'Щ':'Shch',
    'Ъ':'Y',
    'Ы':'Y',
    'Ь':"'",
    'Э':'E',
    'Ю':'Yu',
    'Я':'Ya',
    }

for i in os.walk(path_dir):
    folder.append(i)
    
for address, dirs, files in folder:
    if address.endswith('images') or address.endswith('videos') or address.endswith('documents') or address.endswith('audio') or address.endswith('archives'):
            continue
    for file in files:
        x = address+'/'+file
        move_files(x)
        
del_empty_dirs(path_dir)    

                                      