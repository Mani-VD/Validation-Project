import re
class formcheck:
    def namevalidate(name):
        if len(name)>=4:
            if name.find(' ')!=-1:
                if  name.isalpha()==True and name[0].isupper()==True:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False
    def  mailvalidate(mail):
        if re.match('[^@]+@[^@]+\.[^@]+',mail):
            return True
        else:
            return False
    def phonevalidate(phone):
        if phone.isdigit()==True and len(phone)==10:
            return True
        else:
            return False
    def addressvalidate(address):
        if len(address)>6 and address.isdigit()==False:
            addresssplit=address.split(',')
            if len(addresssplit)>1:
                words=[word.isalpha() for word in addresssplit]
                if any(words)==True:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False
            
        
                
            
