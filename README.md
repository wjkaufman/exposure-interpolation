# Exposure Interpolation

This python script is intended to make nice linear transitions between bright and dark frames of a time lapse by adjusting the exposure, temperature, and tint levels in the `.xmp` files.

The `interpolationController` class is used to interpolate between two given `.xmp` files (file paths are parameters for the interpolationController) and write `.xmp` files to a specified folder (also a parameter for the interpolationController).

## Helpful Information

For exposure: `crs:Exposure2012="[0]"`

For white balance: `crs:WhiteBalance="[Custom]"`
    temperature: `crs:Temperature="[6000]"`
    tint: `crs:Tint="[+8]"`
    
For raw file name: `crs:RawFileName="DSC_0011.NEF"`
