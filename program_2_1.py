import math

def intToDigit(integer, digit_number = 4): #this function takes an integer and returns
    return str(integer).zfill(digit_number)


#MyXMP is for individual xmp files
class MyXMP: 
    
    def __init__(self, number = 0, exposure = 0, temp = 6000, tint = 8):
        self.name = "DSC_" + intToDigit(number) + ".xmp"
        self.exposure = exposure
        self.temp = temp
        self.tint = tint
    
    def __repr__(self):
        return self.getData()
    
    def getNumber(self):
        number = int(self.name[4:-4])
        return number
    
    def getName(self):
        return self.name
    
    def getData(self):
        data = ""
        data += self.name + ":\t" + str(self.exposure) + "\t" + str(self.temp) + "\t" + str(self.tint)
        return data
    
    
    
    def setName(self, number): #setName changes the name according to the number inputed
        self.name = "DSC_" + intToDigit(number) + ".xmp"
    
    def setExposure(self, newData): #setExposure takes in new xmp exposure data as a string and reassigns the data
        startData = newData.find("crs:Exposure2012=\"") + 18
        endData = newData.find("\"\n", startData)
        self.exposure = float(newData[startData:endData])
    
    def setTemp(self, newData): #setExposure takes in new xmp exposure data as a string and reassigns the data
        startData = newData.find("crs:Temperature=\"") + 17
        endData = newData.find("\"\n", startData)
        self.temp = float(newData[startData:endData])
    
    def setTint(self, newData): #setExposure takes in new xmp exposure data as a string and reassigns the data
        startData = newData.find("crs:Tint=\"") + 10
        endData = newData.find("\"\n", startData)
        self.tint = float(newData[startData:endData])
    
    def setData(self, newData): #setData takes in new xmp data as a string and reassigns the data
        self.setExposure(newData)
        self.setTemp(newData)
        self.setTint(newData)
    
    
    
    def writeXMP(self, template): #writeXMP returns a string that can be written to a .xmp file
        startExposureData = template.find("crs:Exposure2012=\"") + 18
        endExposureData = template.find("\"\n", startExposureData) - 1
        data = template[:startExposureData] + str(self.exposure) + template[endExposureData:]
        
        startTempData = template.find("crs:Temperature=\"") + 17
        endTempData = template.find("\"\n", startTempData)
        data = template[:startTempData] + str(self.temp) + template[endTempData:]
        
        startTintData = template.find("crs:Tint=\"") + 10
        endTintData = template.find("\"\n", startTintData)
        data = template[:startTintData] + str(self.tint) + template[endTintData:]
        
        return data
    
    
#MyXMPList is for lists or groups of xmp files
class MyXMPList:
    
    def __init__(self, firstXMP, lastXMP):
        self.firstXMP = firstXMP #first and last XMP will be MyXMP objects
        self.lastXMP = lastXMP
        
    def length(self):
        return (self.lastXMP.getNumber - self.firstXMP.getNumber)





templateXMP = "./source/DSC_0830.xmp"
f = open(templateXMP, 'r')
template = f.read()
f.close()

x = MyXMP()
x.setData(template)
print(x)








#
#
#
#### Parameters ###
#
#template_file = "./source/DSC_0830.xmp"
#first_file = "DSC_0830.xmp"
#last_file = "DSC_0952.xmp"
#
##Exposure
#first_exposure = -1.05
#last_exposure = 1.7
#
##White balance
#first_temp = 6000
#last_temp = 6000
#
#first_tint = 8
#last_tint = 8
#
#
#### End Parameters ###
#
#
#def intToDigit(integer, digit_number = 4): #this function takes an integer and returns
#    string = str(integer)                     #a string with the correct number of digits
#    if digit_number < len(string):
#        return False
#    there_yet = False
#    power = 1
#    while there_yet == False:
#        if integer < 10**power:
#            string = "0"*(digit_number - power ) + string
#            there_yet = True
#            return string
#        else:
#            power += 1
#
#
##find total number of pictures
#first_picture = int(first_file[4:][:-4])    # chop off "DSC_" and ".xmp"
#last_picture = int(last_file[4:][:-4])      # chop off "DSC_" and ".xmp"
#number_pictures = last_picture - first_picture
#
#
## Copy template file as template_data
#f = open( template_file ,'r')
#template_data = f.read()
#f.close()
#
#
##make white balance custom
#template_data.replace("crs:WhiteBalance=\"As Shot\"", "crs:WhiteBalance=\"Custom\""
#
#
##remove exposure data from template ###PROBLEM AREA###
#name_start = template_data.find( "crs:Exposure2012=\"" )
#data_start = name_start + 18 #18 is the number of characters in "crs:Exposure2012=\""
#data_end = template_data.find( "\"\n", data_start ) - 1
#template_data = template_data[:data_start] + template_data[data_end + 1:] #removes exposure data from template
#print(template_data[data_start - 100:data_start + 100]) #for debugging purposes
#
#exposure = first_exposure
#delta_exposure = ( last_exposure - first_exposure ) / float(number_pictures)
#
#for picture in range(number_pictures + 1):
#    picture_number = picture + first_picture
#
#    new_data = template_data.replace("crs:Exposure2012=\"\"","crs:Exposure2012=\"" + str(exposure) + "\"")
#    print("picture number:\t" + str(picture_number) + "\t" + str(exposure))
#    filename = "DSC_" + intToDigit( picture_number ) + ".xmp"
#    newfile = open( "./output/" + filename, 'w' )
#    newfile.write( new_data )
#    newfile.close()
#
#    exposure += delta_exposure
#
#
#print("process completed :)")
#
