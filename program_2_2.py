import math

def intToDigit(integer, digit_number = 4): #this function takes an integer and returns
    return str(integer).zfill(digit_number)


#MyXMP is for individual xmp files
class MyXMP: 
    
    def __init__(self, number = 0, exposure = 0, temp = 6000, tint = 0):
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
    
    
    
    
    def setAttribute(self, attributeName, newData): #attributeName would be "crs:Exposure2012=\"" for exposure
        startData = newData.find(attributeName) + len(attributeName)
        endData = newData.find("\"\n", startData)
        if (attributeName.find("Exposure") >= 0):
            self.exposure = float(newData[startData:endData])
        elif (attributeName.find("Temperature") >= 0):
            self.temp = float(newData[startData:endData])
        elif (attributeName.find("Tint") >= 0):
            self.tint = float(newData[startData:endData])
        elif (attributeName.find("RawFileName") >= 0):
            self.name = newData[startData:endData-4] + ".xmp"
    
    def setExposure(self, newData): #setExposure takes in new xmp exposure data as a string and reassigns the data
        self.setAttribute("crs:Exposure2012=\"", newData)
    
    def setTemp(self, newData): #setExposure takes in new xmp exposure data as a string and reassigns the data
        self.setAttribute("crs:Temperature=\"", newData)
    
    def setTint(self, newData): #setExposure takes in new xmp exposure data as a string and reassigns the data
        self.setAttribute("crs:Tint=\"", newData)
        
    def setName(self, newData):
        self.setAttribute("crs:RawFileName=\"", newData)
        
    def setData(self, newData): #setData takes in new xmp data as a string and reassigns the data
        self.setExposure(newData)
        self.setTemp(newData)
        self.setTint(newData)
        self.setName(newData)
        
    
    
    def writeXMP(self, template): #writeXMP returns a string that can be written to a .xmp file
        data = template
        startExposureData = data.find("crs:Exposure2012=\"") + 18
        endExposureData = data.find("\"\n", startExposureData)
        data = data[:startExposureData] + str(self.exposure) + data[endExposureData:]
        
        startTempData = data.find("crs:Temperature=\"") + 17
        endTempData = data.find("\"\n", startTempData)
        data = data[:startTempData] + str(self.temp) + data[endTempData:]
        
        startTintData = data.find("crs:Tint=\"") + 10
        endTintData = data.find("\"\n", startTintData)
        data = data[:startTintData] + str(self.tint) + data[endTintData:]
        
        startNameData = data.find("crs:RawFileName=\"") + 17
        endNameData = data.find("\"\n", startNameData)
        data = data[:startNameData] + str(self.name) + data[endNameData:]
        
        return data
    
    
#MyXMPList is for lists or groups of xmp files
class MyXMPList:
    
    def __init__(self, templatePath, firstXMP = MyXMP(), lastXMP = MyXMP()):
        self.firstXMP = firstXMP #first and last XMP will be MyXMP objects
        self.lastXMP = lastXMP
        f = open(templatePath, 'r')
        self.templateData = f.read()
        f.close()
    
    def __repr__(self):
        return str(self.firstXMP) + ":\t" + str(self.lastXMP)
    
    def getNumber(self):
        return (self.lastXMP.getNumber() - self.firstXMP.getNumber())
    
    def setData(self, filePath1, filePath2):
        f1 = open(filePath1, 'r')
        f2 = open(filePath2, 'r')
        data1 = f1.read()
        data2 = f2.read()
        f1.close()
        f2.close()
        
        self.firstXMP.setData(data1)
        self.lastXMP.setData(data2)
        
    def writeData(self, writePath): #writes a list of XMP's to the writePath (e.g. "./source/") that transition from firstXMP to lastXMP
        changeExposure = (self.lastXMP.exposure - self.firstXMP.exposure)/float(self.getNumber())
        print("changeExposure:\t", changeExposure)
        changeTemp = (self.lastXMP.temp - self.firstXMP.temp)/float(self.getNumber())
        print("changeTemp:\t", changeTemp)
        changeTint = (self.lastXMP.tint - self.firstXMP.tint)/float(self.getNumber())
        print("changeTint:\t", changeTint)
        
        print("firstXMP.exposure:\t", self.firstXMP.exposure)
        
        for i in range(self.getNumber()+1):
            newXMP = MyXMP(i+self.firstXMP.getNumber(), \
                           self.firstXMP.exposure + changeExposure*i, \
                           self.firstXMP.temp + changeTemp*i, \
                           self.firstXMP.tint + changeTint*i)
            
            data = newXMP.writeXMP(self.templateData)
            
            f = open(writePath + newXMP.name, 'w')
            f.write(data)
            f.close()
    

class InterpolationController:
    
    def __init__(self, file1Path, file2Path, writePath):
        self.XMPList = MyXMPList(file1Path) # I have no idea if this will work
        self.XMPList.setData(file1Path, file2Path)
        self.writePath = writePath
        
    def interpolateData(self):
        self.XMPList.writeData(self.writePath)



print("\nProgram is starting...\n")

controller = InterpolationController("./source/DSC_0001.xmp", "./source/DSC_0010.xmp", "./output/")
print("controller is initialized\n")
controller.interpolateData()
print("data interpolated\n")

print("Process is done\n")