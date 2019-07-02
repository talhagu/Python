
import requests
import datetime
from datetime import datetime ,timedelta
import csv
import re
#2 post requests , 9 get request->total 11 method
class Vehicle: #National Highway Trafic saftey administrator כמו משרד רישוי
    def __init__(self):  # can we have default constructor
        self.name=''
    def DecodeVINValuesBatch(self):
        url = 'https://vpic.nhtsa.dot.gov/api/vehicles/DecodeVINValuesBatch/'
        post_fields = {'format': 'json', 'data': '3GNDA13D76S000000;5XYKT3A12CG000000'}
        response = requests.post(url, data=post_fields)
        return response
    def InfoWMI(self,WMI):  # World Manufacturer Identifier (WMI)- 1FD FORD 1HG-Honda
        url = 'https://vpic.nhtsa.dot.gov/api/vehicles/DecodeVINValuesBatch//DecodeWMI/'
        post_fields = {'format': 'json', 'data': WMI}
        response = requests.post(url, data=post_fields)
        return response

    def GetModelsForMakeId(self,makeID): # makeID  440 example
        url = 'https://vpic.nhtsa.dot.gov/api/vehicles/GetModelsForMakeId/' + makeID
        get_fields = {'format': 'json'}
        response = requests.get(url, get_fields)
        return response
    def GetAllMakeIDRespository(self):# Get all the car name and makeidfrom repository
        url = 'https://vpic.nhtsa.dot.gov/api/vehicles/GetAllMakes'
        get_fields = {'format': 'json'}
        response = requests.get(url, get_fields)
        return response

    def GetMakeForManufacturer(self,manufactor):
        url = 'https://vpic.nhtsa.dot.gov/api//vehicles/GetMakeForManufacturer/'+manufactor
        get_fields = {'format': 'json'}
        response = requests.get(url, get_fields)
        return response

    def GetVehicleVariableList(self):  # hug method response more then 150 response
        url = 'https://vpic.nhtsa.dot.gov/api//vehicles/GetVehicleVariableList'
        get_fields = {'format': 'json'}
        response = requests.get(url, get_fields)
        return response

    def GetModelsForMakeYear(self, year,model):  #
        url = 'https://vpic.nhtsa.dot.gov/api/vehicles/GetModelsForMakeYear/make/'+model+'/modelyear/' + year
        get_fields = {'format': 'json'}
        response = requests.get(url, get_fields)
        return response

    def GetCanadianVehicleSpecifications(self, year,make):  #
        url = 'https://vpic.nhtsa.dot.gov/api/vehicles/GetCanadianVehicleSpecifications/?year='+year+'&make='+make
        get_fields = {'format': 'json'}
        response = requests.get(url, get_fields)
        return response

    def GetMakesForManufacturerAndYear(self, year,manufactorer):  #
        url = 'https://vpic.nhtsa.dot.gov/api/vehicles/GetMakesForManufacturerAndYear/'+manufactorer+'?year='+year
        get_fields = {'format': 'json'}
        response = requests.get(url, get_fields)
        return response

    #GetEquipmentPlantCodes

    def GetEquipmentPlantCodes(self, year,type):
        line='&reportType=all'
        url = 'https://vpic.nhtsa.dot.gov/api/vehicles/GetEquipmentPlantCodes?year='+year+'&equipmentType='+type+line
        get_fields = {'format': 'json'}
        response = requests.get(url, get_fields)
        return response

    # /vehicles/GetParts?type=565&fromDate=1/1/2015&toDate=5/5/2015&format=xml&page=1
    def GetParts(self, type, StartDate,EndDate):  #
        url = 'https://vpic.nhtsa.dot.gov/api/vehicles/GetParts?type='+type+'fromDate='+StartDate+'&toDate='+EndDate
        get_fields = {'format': 'json'}
        response = requests.get(url, get_fields)
        return response
#https://vpic.nhtsa.dot.gov/api/vehicles/GetSAEWMIsForManufacturer/hon?format=xml

    def GetSAEWMIsForManufacturer(self, manufactorer):  #manufactorer=non (nonda as example)
        url = 'https://vpic.nhtsa.dot.gov/api/vehicles/GetSAEWMIsForManufacturer/'+manufactorer
        get_fields = {'format': 'json'}
        response = requests.get(url, get_fields)
        return response
#https://vpic.nhtsa.dot.gov/api/vehicles/getallmanufacturers?format=XML
    def getallmanufacturers(self):  # manufactorer=non (honda as example)
        url = 'https://vpic.nhtsa.dot.gov/api/vehicles/getallmanufacturers'
        get_fields = {'format': 'json'}
        response = requests.get(url, get_fields)
        return response

    def getmanufacturerdetails(self,manufactor):  # manufactorer=honda (honda as example)
        url = 'https://vpic.nhtsa.dot.gov/api/vehicles/getmanufacturerdetails/'+manufactor
        get_fields = {'format': 'json'}
        response = requests.get(url, get_fields)
        return response


    def GetDatasetPeryear(self,year):  # hug method response more then 150 response
        url ='https://vpic.nhtsa.dot.gov/api/vehicles/GetModelsForMakeYear/make/honda/modelyear/'+year
        get_fields = {'format': 'json'}
        response = requests.get(url, get_fields)
        return response

    def WriteResonseToFile(self,filepath,requesttype,responsedict,linevalue,filter_only_header,filter_only_header_data,time_pars):
        # open up a csv (comma separated values) file to write data to
        need_filter=False
        if (filter_only_header)!='':
            need_filter=True
        with open(filepath + requesttype+'.csv', 'w',newline='') as file:
            # let w represent our file
            w = csv.writer(file)
            keys=[]
            values=[]
            filter_location=0
            found=False
            for item in responsedict:
                for key,value in item.items():
                    keys.append(key)
                    if key in time_pars:
                        #print(type(value))
                        if (value != None):
                            #print("value",value)
                            clean_text=re.search(r'\((.*?)\)',value).group(1)
                            #print("clean_text", clean_text)
                            time = clean_text.split("-")
                            input_int=float('-'+time[1])
                            if len(time)>2:
                                new_time = datetime(1970,1,1)+timedelta(seconds=(input_int / 10000)) - timedelta(hours=int(time[2][1]))
                            else:
                                input_int = int(time[0])
                                new_time = datetime.utcfromtimestamp(input_int / 1000) - timedelta(hours=int(time[1][1]))
                            values.append(new_time)
                        else:
                            values.append(new_time)
                    else:
                        values.append(value)
            header=sorted(set(keys))
            if (need_filter==True):
                for headerbame in header:
                    if (headerbame == filter_only_header and found == False):
                        found = True
                    if (found == False):
                        filter_location += 1
            w.writerow(header)
            count = 0
            line = []
            for data in values:
                if(count<linevalue):
                    line.append(data)
                    count+=1
                if(count==linevalue):
                    if (need_filter == True):
                        if (line[filter_location]==filter_only_header_data):
                            w.writerow(line)
                    else:
                        w.writerow(line)
                    count=0
                    line=[]
    print("finish saving data to csv file")

            #process_starttime = datetime.datetime.now()




##alsogood api-https://vpic.nhtsa.dot.gov/api/vehicles/getmanufacturerdetails/honda?format=XML





