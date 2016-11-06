# Exposure Interpolation

This python script is intended to make nice linear transitions between bright and dark frames of a time lapse by adjusting the exposure, temperature, and tint levels in the `.xmp` files.

The `interpolationController` class is used to interpolate between two given `.xmp` files (file paths are parameters for the interpolationController) and write `.xmp` files to a specified folder (also a parameter for the interpolationController).
