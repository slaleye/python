towrite='<?php \n return [  \n \'index\' => "content",\n \'index\' => "content",\n \'index\' => "content",\n \'index\' => "content",\n \'index\' => "content",\n \'index\' => "content",\n \'index\' => "content",\n \'index\' => "content",\n \'index\' => "content" \n];'
with open("langresource.txt") as f:
        for line in f:
            data= line.rstrip('\n')
            fname=data+'.php'
            if fname != ".php":
                with open(fname, "w") as f1:
                    f1.write(towrite)

print "done"
