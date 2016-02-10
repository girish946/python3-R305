from R305 import generateHeader, header, address


identifire = {1:"command packet",
              2: "data packet",
              7:"acknokedge packet",
              8:"end of data packte"}

confirmation_codes = {0:"operation success",
                      1:"error while reciving packet",
                      0x0a:"failed to combine character files"}




def parse(s):
    recived_header = s[:2]
    recived_address = s[2:6]
    recived_id = s[6]
    recived_length = s[7:9]
    recived_c_code = s[9]
    recived_c_sum = s[10:11]
    if( header == [int(c) for c in recived_header]):
        if( address == [int(c) for c in recived_address]):

            print ("address and header ok")
            
            #print hex(ord(recived_id))
            #print int(ord(recived_id))
            #print identifire

            print(identifire[int(recived_id) ])

            #print ([hex(ord(c)) for c in recived_length])

            print (confirmation_codes[int(recived_c_code)])
            return confirmation_codes[int(recived_c_code)]
            
    return "ok"



def getHeader():
        return generateHeader()+[0x01, 0x00, 0x03, 0x05, 0x00, 0x09]
