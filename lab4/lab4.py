import httplib
import urllib
import time
key = "AT68QYQ94MQEWXL3"  # Put your API Key here
def labpi():
    while True:
        
        temp = "Group: L3-T-3" 
        temp2 = "harshilverma@cmail.ca"
        temp3 = "b"
        params = urllib.urlencode({'field1': temp, 'field2': temp2, 'field3': temp3,  'key':key }) 
        headers = {"Content-typZZe": "application/x-www-form-urlencoded","Accept": "text/plain"}
        conn = httplib.HTTPConnection("api.thingspeak.com:80")
        try:
            conn.request("POST", "/update", params, headers)
            response = conn.getresponse()
            print (temp)
            print (temp2)
            print (temp3)
            print (response.status, response.reason)
            data = response.read()
            conn.close()
        except:
            print ("connection failed")
        break
if __name__ == "__main__":
        while True:
                labpi()