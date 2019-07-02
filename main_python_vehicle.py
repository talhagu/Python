

# #start with get WMi info
from VehicleAPI import Vehicle
import re
import datetime as datetime
import json

def removechar(data_dict):
    for item in data_dict:
        for x, y in item.items():
            if (y != None and type(y) == type('')):
                # print("val:",y)
                new_value = re.sub(r"</?p>", "", y)
                new_value1 = re.sub(r"</?li>", "", new_value)
                new_value2 = re.sub(r"</?ul>", "", new_value1)
                new_value3 = re.sub(r"</?br>", "", new_value2)
                item[x] = new_value3
    return data_dict

def coloumn_calc(data_dict):
    first_key=''
    count=0
    for item in data_dict:
        for x, y in item.items():
                if (first_key==''):#firts
                    count+=1
                    first_key=x
                elif (x==first_key):  #calc the coloumn
                    return count
                else:
                    count += 1

    return data_dict
# # #GetModelsForMakeId
model='440'  #ford WMi info
vehicle = Vehicle()
information=vehicle.GetModelsForMakeId(model)
response_dict=json.loads(information.text)
csvpath='d:\\pythonproject\\'
linevalue=4 #how many headers
filter_only_header=''
filter_only_header_data=''
vehicle.WriteResonseToFile(csvpath,'GetModelsForMakeId',response_dict['Results'],linevalue,filter_only_header,filter_only_header_data,[])
print("finish successfully GetModelsForMakeId")
# #
# # #GetVehicleVariableList
# # #regex
vehicle = Vehicle()
information=vehicle.GetVehicleVariableList()
response_dict=json.loads(information.text)
removechar(response_dict['Results'])  #regular expression
csvpath='d:\\pythonproject\\'
#linevalue=4 #how many headers
linevalue=coloumn_calc(response_dict['Results'])  #calcheaders
filter_only_header=''
filter_only_header_data=''
vehicle.WriteResonseToFile(csvpath,'GetVehicleVariableList',response_dict['Results'],linevalue,filter_only_header,filter_only_header_data,[])
print("finish successfully GetVehicleVariableList")
# #
# #
# # #GetEquipmentPlantCodes
vehicle = Vehicle()
# # #equipmentType
# # #1 Tires
# # #3 Brake Hoses
# # #13 Glazing
# # #16 Retread
type='1'
year='2015'
information=vehicle.GetEquipmentPlantCodes(year,type)
response_dict=json.loads(information.text)
csvpath='d:\\pythonproject\\'
#linevalue=9 #how many headers
linevalue=coloumn_calc(response_dict['Results'])  #calcheaders
filter_only_header='Status'  #filter only Active status 
filter_only_header_data='Active'
# #
# # #talh- can add filter only status open as example
vehicle.WriteResonseToFile(csvpath,'GetEquipmentPlantCodes',response_dict['Results'],linevalue,filter_only_header,filter_only_header_data,[])
print("finish successfully GetEquipmentPlantCodes")
# #
# # #GetSAEWMIsForManufacturer
# #
vehicle = Vehicle()
manufactorer='hon'
information=vehicle.GetSAEWMIsForManufacturer(manufactorer)
response_dict=json.loads(information.text)
csvpath='d:\\pythonproject\\'
linevalue=25 #how many headers
filter_only_header=''
filter_only_header_data=''
time_pars_lst=['CreationDate','ModificationDate']
vehicle.WriteResonseToFile(csvpath,'GetSAEWMIsForManufacturer',response_dict['Results'],linevalue,filter_only_header,filter_only_header_data,time_pars_lst)
print("finish successfully GetSAEWMIsForManufacturer")

#getallmanufacturers
vehicle = Vehicle()
information=vehicle.getallmanufacturers()
response_dict=json.loads(information.text)
filter_country= dict()
csvpath='d:\\pythonproject\\'
linevalue=5 #how many headers
filter_only_header ='Country'
filter_only_header_data="United States (USA)"

vehicle.WriteResonseToFile(csvpath,'getallmanufacturers',response_dict['Results'],linevalue,filter_only_header,filter_only_header_data,[])
print("finish successfully getallmanufacturers")
#
#
#

#getmanufacturerdetails
vehicle = Vehicle()
manufactor='honda'
information=vehicle.getmanufacturerdetails(manufactor)
response_dict=json.loads(information.text)
csvpath='d:\\pythonproject\\'
linevalue=25 #how many headers
#no filter
filter_only_header=''
filter_only_header_data=''
time_pars_lst=['LastUpdated','SubmittedOn']

vehicle.WriteResonseToFile(csvpath,'getmanufacturerdetails',response_dict['Results'],linevalue,filter_only_header,filter_only_header_data,time_pars_lst)
print("finish successfully getmanufacturerdetails")
