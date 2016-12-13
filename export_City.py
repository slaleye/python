import csv
#towrite='(NULL,"country","city","","","",NULL,NULL),'
towrite='array("country_code" =>"cc","city" => "ct"),'
with open("city/in.txt") as f:
    with open("city/out-seed.sql", "w") as f1:
        for line in f:
            #split line into sequence 
            data= line.rstrip('\n').split(",")
            #grades.append(lists[i].rstrip('\n').split(','))
            s0=towrite
            s1= s0.replace("cc", data[0].upper()).replace("ct", data[2])+'\n'
            
            f1.write(s1)

print "done"
            
