import csv,os

def opencsv(file):
    f= open(file,'r',encoding = 'utf-8')
    reader = csv.reader(f)
    output = []
    for i in reader:
        print(i)
        output.append(i)
        
    f.close()
    return output


def writecsv(file,list):
    with open(file,'w',newline="") as f:
        a = csv.writer(f,delimiter = ',')
        a.writerows(list)

def switch(listname):
    for i in listname:
        for j in i:
            try: 
                i[i.index(j)]=float(re.sub(',','',j))
            except:
                pass
    return listname