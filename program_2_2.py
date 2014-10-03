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
        data = template
        startExposureData = data.find("crs:Exposure2012=\"") + 18
        endExposureData = data.find("\"\n", startExposureData)
        print(self.exposure)
        data = data[:startExposureData] + str(self.exposure) + data[endExposureData:]
        
        startTempData = data.find("crs:Temperature=\"") + 17
        endTempData = data.find("\"\n", startTempData)
        data = data[:startTempData] + str(self.temp) + data[endTempData:]
        
        startTintData = data.find("crs:Tint=\"") + 10
        endTintData = data.find("\"\n", startTintData)
        data = data[:startTintData] + str(self.tint) + data[endTintData:]
        
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

x = MyXMP(102,.25,60000,10)
print(x)
newData = x.writeXMP(template)

newfile = x.name
f = open(newfile, 'w')
f.write(newData)