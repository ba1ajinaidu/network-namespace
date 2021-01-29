import re

def split(string):
    r = re.sub(r'(?<=\d)(?=\D)|(?<=\D)(?=\d)', r' ', string).split()
    return r

def delay_type():
    test='85ms'
    result=split(test)
    delay =['s','S','ms','us','ns','ps','as','fs']
    
    print(result)
    if(result[0].isdigit()):
        if(result[1] in delay):
            print("continue normally")
            
        else:
            print("please provide a proper unit")
            
    else:
        print("usage 85ms")
        
def bandwidth_type():
    test1='85Mbits'
    result1=split(test1)
    bandwidth =['bits','kbits','Kbits','mbits','Mbits','gbits','Gbits','bps','kbps','Kbps','mbps','Mbps','gbps','Gbps']
    
    print(result1)
    if(result1[0].isdigit()):
        if(result1[1] in bandwidth):
            print("continue normally")
            
        else:
            print("Please provide a proper unit(type)")
            
    else:
        print("usage 85mbits")

delay_type()
bandwidth_type()
