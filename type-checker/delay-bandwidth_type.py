import re

def split_string(string):
    #r = re.sub(r'(?<=\d)(?=\D)|(?<=\D)(?=\d)', r' ', string).split()
    r = re.split(r'((\[0-9].[0-9])|([a-zA-Z]+))',string)
    #r = re.
    res = None if len(r)==1 else r
    return res

def delay_type():
    test='85.76ms'
    result=split_string(test)
    delay =['s','sec','secs','ms','msec','msecs','us','usec','usecs']
    
    print(result)
    
    if(result!= None):
        if(result[0].replace('.','',1).isdigit()):
            if(result[1] in delay):
                print("continue normally")
            
            else:
                print("please provide a proper unit")
            
        else:
            print("usage 85ms")
            
    else:
            print("no unit was passed along with delay")
        
def bandwidth_type():
    test1='85'
    result1=split_string(test1)
    bandwidth =['bit','kbit','kibit','mbit','mebit','gbit','gibit','tbit','tebit','bps','kbps','kibps','mbps','mebps','gbps','gibps','tbps','tebps']
    
    print(result1)
    if(result1 != None):
        if(result1[0].replace('.','',1).isdigit()):
            if(result1[1] in bandwidth):
                print("continue normally")
            
            else:
                print("Please provide a proper unit(type)")
            
        else:
            print("usage 85mbit")
            
    else:
        print("no unit was passed along with bandwidth")

delay_type()
bandwidth_type()
