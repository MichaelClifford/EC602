from os import listdir
import re
from skimage.io import imread
import numpy as np
import hashlib


def make_transforms(img):

    #change hash libs to just standard hash
    transform_list = []
    
    transform_list.append(hashlib.sha256(bytes(img)).hexdigest())
    
    turn_0_mirror = img[::1,::-1]
    turn_0_mirror_hash = hashlib.sha256(bytes(turn_0_mirror)).hexdigest()
    transform_list.append(turn_0_mirror_hash)

    turn_90 = np.transpose(img[::-1,])
    turn_90_hash = hashlib.sha256(bytes(turn_90)).hexdigest()
    transform_list.append(turn_90_hash)
                
    turn_90_mirror = np.transpose(img)
    turn_90_mirror_hash = hashlib.sha256(bytes(turn_90_mirror)).hexdigest()
    transform_list.append(turn_90_mirror_hash)

    turn_180 = img[::-1,::-1]
    turn_180_hash = hashlib.sha256(bytes(turn_180)).hexdigest()
    transform_list.append(turn_180_hash)
                
                
    turn_180_mirror = img[::-1]
    turn_180_mirror_hash = hashlib.sha256(bytes(turn_180_mirror)).hexdigest()
    transform_list.append(turn_180_mirror_hash)

    turn_270 = np.transpose(img[::1,::-1])
    turn_270_hash = hashlib.sha256(bytes(turn_270)).hexdigest()
    transform_list.append(turn_270_hash)
                
                
    turn_270_mirror = np.transpose(img[::-1,::-1])
    turn_270_mirror_hash = hashlib.sha256(bytes(turn_270_mirror)).hexdigest()
    transform_list.append(turn_270_mirror_hash)

    
    return frozenset(transform_list)

def main():
    
    # get image file names
    files = []
    for file in listdir():
        if file.endswith(".png"):
            files.append(file)
    
    # read in images and compare to existing
    
    Answer_List = {}
    
    for png in files:
        img = 1-imread(png,as_grey=True) # read an inverse gray scale image
        x = np.nonzero(img) # identify colored sqaures
        img = img[min(x[0]):max(x[0])+1,min(x[1]):max(x[1])+1] # crop image to region of interest
        shape = make_transforms(img)
        if shape in Answer_List.keys():
            Answer_List[shape].append(png)
        else:
            Answer_List[shape] = [png]

        
    # Order the matches appropriately
    
    
    ORDER = []
    regex = re.compile(r'\d+')

    for i in Answer_List.keys():
        ORDER.append(Answer_List[i])
        
  
    for j in range(len(ORDER)):
        for k in range(len(ORDER[j])):
            num = regex.findall(ORDER[j][k])
            num = int(num[0])
            ORDER[j][k] = (num,ORDER[j][k])
            

    To_write = sorted(ORDER)

    for t in range(len(To_write)):
        To_write[t] = sorted(To_write[t])

    To_write = sorted(To_write)
    

    # write to file 
    with open("answersTEST.txt", "w") as text_file:
        for l in range(len(To_write)):
            for m in range(len(To_write[l])):
                if m == len(To_write[l])-1:
                    text_file.write(To_write[l][m][1])
                else:
                    text_file.write(To_write[l][m][1]+ " ")
            text_file.write("\n")

    has = open('answersTEST.txt','r')
    h = has.read()
    done = hashlib.sha256(bytes(h,'utf-8')).hexdigest()
    has.close()

    print(done)
    return done
    
    
if __name__ == '__main__':
    main()
