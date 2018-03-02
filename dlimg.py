#Pour lancer le script faire : "python dlimg.py exemple.JSON"

import urllib
import json
import os, errno
import sys

with open(sys.argv[1]) as json_data:
    d = json.load(json_data)
    #A changer en fonction du path ou on enregistre les images
    path = "/home/oguerisck/Documents/TER/fishbase/tmp/images/full"
    for obj in d:
        name = json.dumps(obj['taxonomy'][0]).replace('"','').replace(' ','-')
        url = json.dumps(obj['image_urls'][0])
        print(name)
        print(url)
        exDir = True
        pathLetter = path + "/" + name[0]
        try:
            os.makedirs(pathLetter)
        except OSError as e:
            if e.errno != errno.EEXIST:
                raise


        pathFish = pathLetter + "/" + name
        try:
            os.makedirs(pathFish)
        except OSError as e:
            exDir = False
            print("Poisson deja traite")
            if e.errno != errno.EEXIST:
                raise

        if exDir :
            #Sauvegarde l'image, renvoie une erreur sinon
            testfile = urllib.URLopener()
            try :
                testfile.retrieve(url.replace('"',''), pathFish+"/fish")
            except IOError, e:
                print(e)
