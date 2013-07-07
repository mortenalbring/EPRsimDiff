import glob
import os

files = glob.glob("*.epr");
print(len(files))

fullArray = [];

for j in range(1,len(files)) :

    filename = files[j];

    print(filename)
    
    fid = open(filename,'r')

    
    field = [];
    absorption = [];
    epr = [];

    for line in fid:
        x,y = line.split();
        field.append(float(x));
        absorption.append(float(y));

    fid.close()

    i = 1

    for i in range(1,len(field)) :
        v = (absorption[i] - absorption[i-1]) / (field[i] - field[i-1])
        epr.append(v)


    eprmax = max(epr)

    eprnorm = [x/eprmax for x in epr]


    outfile = os.path.splitext(filename)[0] + ".csv";
    fout = open(outfile,'w')
    fout.write("Field")
    fout.write(",")
    fout.write("Intensity")
    fout.write("\n")

    
    for i in range(0,len(field)-1) :
        fout.write(str(field[i]))
        fout.write(",")
        fout.write(str(eprnorm[i]))
        fout.write("\n")


    fout.close()

    fullArray.append(eprnorm)


outfile = "fullArray.csv"
fout = open(outfile,'w')

fout.write("Field,")
for j in range(1,len(files)) :
    filename = files[j];
    fout.write(files[j]);
    fout.write(",")

fout.write("\n")

for i in range(0,len(field)-1) :
    fout.write(str(field[i]))
    fout.write(",")
    for array in fullArray :
        fout.write(str(array[i]))
        fout.write(",")
    fout.write("\n")

fout.close()

        
    




    




    


    

    
    


    
