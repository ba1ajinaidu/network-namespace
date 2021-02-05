import re

def split_string(string):
    #r = re.sub(r'(?<=\d)(?=\D)|(?<=\D)(?=\d)', r' ', string).split()
    r = re.split(r'((\[0-9].[0-9])|([a-zA-Z]+))',string)
    #r = re.
    return r

def delay_type():
    test='85.76ms'
    result=split_string(test)
    delay =['s','sec','secs','ms','msec','msecs','us','usec','usecs']
    
    print(result)
    if(result[0].replace('.','',1).isdigit()):
        if(result[1] in delay):
            print("continue normally")
            
        else:
            print("please provide a proper unit")
            
    else:
        print("usage 85ms")
        
def bandwidth_type():
    test1='85mbit'
    result1=split_string(test1)
    bandwidth =['bit','kbit','kibit','mbit','mibit','gbit','gibit','tbit','tibit','bps','kbps','kibps','mbps','mibps','gbps','gibps','tbps','tibps']
    
    print(result1)
    if(result1[0].replace('.','',1).isdigit()):
        if(result1[1] in bandwidth):
            print("continue normally")
            
        else:
            print("Please provide a proper unit(type)")
            
    else:
        print("usage 85mbit")

delay_type()
bandwidth_type()
