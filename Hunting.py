import os
import sys

def read_motion(location_name):

    filename = os.path.join(sys.path[0], location_name+".motion.txt")
    open(filename,"r")

    b = []
    with open(filename, "r") as f:
        for line in f:
            b.append(line.strip())
   
    c=[]
    d=[]
    for x in b:
        c.append(x.split(","))
    
    for i in c:
        if i[2] == "detected":
            if i[0] not in d:
                d.append(i[0])
    return d

def read_emf(location_name):

    filename = os.path.join(sys.path[0], location_name+".emf.txt")
    open(filename,"r")
    

    a=[]
    e=[]
    sum = 0
    count = 0
    average = 0
    position = 0
    with open(filename, "r") as f:
        for line in f:
            a.append(line.strip("\n"))
        for x in a:
            if x.isdigit():
                sum = sum + int(x)
                count = count + 1
            
            else:

                if count >0:
                    average = sum / count
                if average > 3:
                    e.append(a[position-(count+1)])
                count = 0 
                sum = 0
            
            if position == len(a)-1:
                average = sum / count
                if average > 3:
                    e.append(a[position-(count)])
                
            position = position + 1
    return e

def is_valid_temp(val):
    w = ((val.strip("-")).split("."))[0]
    
    if w.isdigit():
        return True
    else:
        return False

def  read_temp(location_name):
    filename = os.path.join(sys.path[0], location_name+".temp.txt")
    open(filename,"r")

    l = []
    y = []
    pos = 0
    neg = 0
    rst = 0
    with open(filename, "r") as f:
        for line in f:
            l.append(line.strip("\n"))             
    for x in l:
        if is_valid_temp(x):
            rst=rst+1
            
            if float(x) < 0.00:
                neg = neg + 1
            elif neg < 5:
                neg = 0
        else:
            if neg >= 5:
                y.append(l[pos-rst-1])
            neg = 0
            rst = 0
        
        pos = pos + 1

    return y

def generate_report(location, motion, emf, temp):
    filename = os.path.join(sys.path[0],"ghost_report.ravensnest.txt")
    open(filename,"w")

    with open(filename, "a") as f:
        f.write("== Raven Ghost Hunting Society Haunting Report == \n\n")
        f.write("Location: " + str(location) + "\n\n")

    listo = [motion,emf,temp]
    ghosts = []
    with open(filename, "a") as f:
        for x in listo:
            for z in x:
                if (z in motion) and (z in emf) and (z in temp):
                    if ("Poltergeist in "+z) not in ghosts:
                        ghosts.append("Poltergeist in " + z)
                elif (z in motion ) and (z in emf):
                    if ("Oni in " +z) not in ghosts:
                        ghosts.append("Oni in " +z)
                elif (z in motion) and (z in temp):
                    if ( "Bansher in " + z) not in ghosts:
                        ghosts.append("Bansher in "+ z)
                elif (z in emf) and (z in temp):
                    if ("Phantom in "+ z) not in ghosts:
                        ghosts.append(("Phantom in "+ z))
        

        for x in ghosts:
            f.write(x)
            f.write("\n\n")

                

def main():
    location = "ravensnest"
    x = read_motion(location)
    y = read_emf(location)
    z = read_temp(location)
    generate_report(location, x, y, z)
    
    print(x,'\n')
    print(y,'\n')
    print(z,'\n')

main()