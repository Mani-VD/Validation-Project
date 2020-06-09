#import section
import csv
import pandas as pd
from pptx import Presentation
import textract as extract
from PIL import Image as im
import PyPDF2
#code  section
class filecheck:
    def filevalidate(filetype,filedir):
        filetype=filetype.upper()
        filedirls=filedir.split('\\')
        filename=filedirls[len(filedirls)-1]
        filenamels=filename.split('.')

        if filetype=='TEXT':
            try:
                data=open(filedir,'r')
                lines=data.read()
                if type(lines) is str:
                    return True
            except:
                return False
        if filetype=='PDF':
            try:
                pdfFileObj = open(filedir, 'rb') 
                pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
                for x in range(pdfReader.numPages): 
                     pageObj = pdfReader.getPage(x) 
                pdfFileObj.close()
                return True
            except:
                return False
        if filetype=='IMAGE':
            try:
                img=im.open(filedir)
                width,height=img.size
                if width>50 and height>50:
                    return True
                else:
                    return False
            except:
                return False
        if filetype=='DOCUMENT':
            try:
                if filenamels[len(filenamels)-1].lower()=='docx' or filenamels[len(filenamels)-1].tolower()=='doc' or filenamels[len(filenamels)-1].tolower()=='rtf' or filenamels[len(filenamels)-1].tolower()=='odt' :
                    text=extract.process(filedir)
                    return True
                else:
                    return False
            except:
                return False
                
        if filetype=='SHEET':
            try:
                if filenamels[len(filenamels)-1].lower()=='xlsx' or filenamels[len(filenamels)-1].lower()=='xls'  :
                    data=pd.read_excel(filedir)
                    return True
                elif  filenamels[len(filenamels)-1].lower()=='csv':
                    data=pd.read_csv(filedir)
                    return True
                elif  filenamels[len(filenamels)-1].lower()=='ods':
                    data=pd.read_excel(filedir, engine="odf")
                    return True
                else:
                    return False
            except:
                return False
        if filetype=='PRESENTATION':
            try:
                if filenamels[len(filenamels)-1].lower()=='pptx':
                    file=open(filedir,'rb')
                    pst=Presentation(file)
                    file.close()
                    return True
                else:
                    return False
            except:
                return False
                    
                    
