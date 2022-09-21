# GDT-Generator
GDT generator for Call of Duty 2

This will create a GDT file for all DDS images in the folder you specify. Supports normal map and specular map alignment if textures are properly named. Same thing with surface types.

eg.  
nt_floor_carpet3.dds - Colour map, surfaceType = carpet  
nt_floor_carpet3_n.tga - Normal map, surfaceType = carpet  
nt_floor_carpet3_s.tga - Specular map, surfaceType = carpet  
  
Also, normal/specular maps should be the .TGA filetype.
  
Lastly alpha detection is applied to automatically flag textures as transparent.

Requires Python (Tested on version 3.7.9) and Pillow (pip install pillow).

Usage: .\dds_to_gdt.py path/to/dds/folder output.gdt
