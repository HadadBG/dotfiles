#!/usr/bin/env python

import sys
import json
import subprocess

if (len(sys.argv) != 3):
    print ("Uso : jsonConcatener.py <Archivo Destino> <Archivo fuente>")
else:
    with open(sys.argv[2]) as src_json:
        dest_json = open(sys.argv[1],"r")            
        data_dest = json.load(dest_json)
        dest_json.close()
        data_src = json.load(src_json)
        data_dest.update(data_src)
        dest_json = open(sys.argv[1],"w")
        dest_json.write(json.dumps(data_dest))
        dest_json.close()
        print("Json Pegado Correctamente")
        process = subprocess.Popen(['/home/hadad/.config/nvim/plugged/vim-prettier/node_modules/.bin/prettier', sys.argv[1],"--write"],
                     stdout=subprocess.PIPE, 
                     stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()
        print(stdout.decode("utf-8")) 
        print(stderr.decode("utf-8"))

       # ~/.config/nvim/plugged/vim-prettier/node_modules/.bin/prettier
