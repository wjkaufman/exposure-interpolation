
### Parameters ###

template_file = "./source/DSC_0830.xmp"
first_file = "DSC_0830.xmp"
last_file = "DSC_0952.xmp"

#Exposure
first_exposure = -1.05
last_exposure = 1.7

#White balance
first_temp = 6000
last_temp = 6000

first_tint = 8
last_tint = 8


### End Parameters ###


def int_to_digit(integer, digit_number = 4): #this function takes an integer and returns
    string = str(integer)                     #a string with the correct number of digits
    if digit_number < len(string):
        return False
    there_yet = False
    power = 1
    while there_yet == False:
        if integer < 10**power:
            string = "0"*(digit_number - power ) + string
            there_yet = True
            return string
        else:
            power += 1



# Copy template file as template_data
f = open( template_file ,'r')
template_data = f.read()
f.close()

#make white balance custom
template_data.replace("crs:WhiteBalance=\"As Shot\"", "crs:WhiteBalance=\"Custom\"")

#find index of exposure
exposure_index = template_data.index("crs:Exposure2012=")
print("index:" + str(exposure_index))

#find total number of pictures
first_picture = int(first_file[4:][:-4])    # chop off "DSC_" and ".xmp"
last_picture = int(last_file[4:][:-4])      # chop off "DSC_" and ".xmp"
number_pictures = last_picture - first_picture


#remove exposure data from template ###PROBLEM AREA###
name_start = template_data.find( "crs:Exposure2012=\"" )
data_start = name_start + 18 #18 is the number of characters in "crs:Exposure2012=\""
data_end = template_data.find( "\"\n", data_start ) - 1
template_data = template_data[:data_start] + template_data[data_end + 1:] #removes exposure data from template
print(template_data[data_start - 100:data_start + 100]) #for debugging purposes

exposure = first_exposure
delta_exposure = ( last_exposure - first_exposure ) / float(number_pictures)

for picture in range(number_pictures + 1):
    picture_number = picture + first_picture

    new_data = template_data.replace("crs:Exposure2012=\"\"","crs:Exposure2012=\"" + str(exposure) + "\"")
    print("picture number:\t" + str(picture_number) + "\t" + str(exposure))
    filename = "DSC_" + int_to_digit( picture_number ) + ".xmp"
    newfile = open( "./output/" + filename, 'w' )
    newfile.write( new_data )
    newfile.close()

    exposure += delta_exposure


print("process completed :)")

