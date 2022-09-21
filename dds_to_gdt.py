import os, sys
from PIL import Image

normal_map_extensions = ["_n", "_nrm", "_nml", "_norm", "_normal"]
specular_map_extensions = ["_s", "_spec", "_specular"]
color_map_extensions = ["_c", "_col", "_color", "_colour"]

asphalt = ["_asphalt", "asphalt_"]
bark = ["_bark", "bark_"]
brick = ["_brick", "brick_"]
carpet = ["_carpet", "carpet_"]
cloth = ["_cloth", "cloth_"]
concrete = ["_concrete", "concrete_"]
dirt = ["_dirt", "dirt_"]
flesh = ["_flesh", "flesh_"]
foliage = ["_foliage", "foliage_"]
glass = ["_glass", "glass_", "_window", "window_"]
grass = ["_grass", "grass_"]
gravel = ["_gravel", "gravel_"]
metal = ["_metal", "metal_"]
mud = ["_mud", "mud_"]
paper = ["_paper", "paper_"]
plaster = ["_plaster", "plaster_"]
rock = ["_rock", "rock_"]
sand = ["_sand", "sand_"]
snow = ["_snow", "snow_"]
water = ["_water", "water_"]
wood = ["_wood", "wood_"]

def has_transparency(img):
    if img.info.get("transparency", None) is not None:
        return True
    if img.mode == "P":
        transparent = img.info.get("transparency", -1)
        for _, index in img.getcolors():
            if index == transparent:
                return True
    elif img.mode == "RGBA":
        extrema = img.getextrema()
        if extrema[3][0] < 255:
            return True

    return False

if not(len(sys.argv) == 3):
	print("Invalid arguments. Usage: " + sys.argv[0] + " path/to/dds/folder output.gdt")
	quit()

path = sys.argv[1]
f = open(sys.argv[2], "w")
f.write("{\n")
for index, file in enumerate(os.listdir(sys.argv[1])):
	if file.endswith(".dds"):
		if file.endswith(".dds"):
			normalmap_detected = 0
			specularmap_detected = 0
			for index2, texturemap in enumerate(normal_map_extensions):
				if(file.endswith(normal_map_extensions[index2] + ".dds")):
					normalmap_detected = 1
			
			for index2, texturemap in enumerate(specular_map_extensions):
				if(file.endswith(specular_map_extensions[index2] + ".dds")):
					specularmap_detected = 1
			
			if not(normalmap_detected) and not(specularmap_detected):
				normalmap_detected = 0
				normalmap_file = ""
				specularmap_detected = 0
				specularmap_file = ""
				colormap_file = file[0:(len(file) - 4)]
				
				for index2, texturemap in enumerate(color_map_extensions):
					if(file.endswith(color_map_extensions[index2] + ".dds")):
						colormap_file = file[0:(len(file) - (len(texturemap)) - 4)]
						break
				
				for index2, texturemap in enumerate(normal_map_extensions):
					for index3, texture in enumerate(os.listdir(sys.argv[1])):
						if(texture in (colormap_file + normal_map_extensions[index2] + ".dds")):
							normalmap_detected = 1
							normalmap_file = texture
				
				for index2, texturemap in enumerate(specular_map_extensions):
					for index3, texture in enumerate(os.listdir(sys.argv[1])):
						if(texture in (colormap_file + specular_map_extensions[index2] + ".dds")):
							specularmap_detected = 1
							specularmap_file = texture
				
				f.write("\t\"" + colormap_file + "\" ( \"material.gdf\" )\n")
				f.write("\t{\n")
				f.write("\t\t\"materialType\" \"world phong\"\n")
				f.write("\t\t\"usage\" \"tools\"\n")
				f.write("\t\t\"colorMap\" \"texture_assets\\\\" + os.path.basename(path) + "\\\\" + file + "\"\n")
				
				if(normalmap_detected):
					f.write("\t\t\"normalMap\" \"texture_assets\\\\" + os.path.basename(path) + "\\\\" + normalmap_file + "\"\n")
				
				if(specularmap_detected):
					f.write("\t\t\"specColorMap\" \"texture_assets\\\\" + os.path.basename(path) + "\\\\" + specularmap_file + "\"\n")
				
				surfaceType = "<none>"
				while(1):
					if(any(substring in file for substring in asphalt)):
						surfaceType = "asphalt"
						break
					if(any(substring in file for substring in bark)):
						surfaceType = "bark"
						break
					if(any(substring in file for substring in brick)):
						surfaceType = "brick"
						break
					if(any(substring in file for substring in carpet)):
						surfaceType = "carpet"
						break
					if(any(substring in file for substring in cloth)):
						surfaceType = "cloth"
						break
					if(any(substring in file for substring in concrete)):
						surfaceType = "concrete"
						break
					if(any(substring in file for substring in flesh)):
						surfaceType = "flesh"
						break
					if(any(substring in file for substring in foliage)):
						surfaceType = "foliage"
						break
					if(any(substring in file for substring in glass)):
						surfaceType = "glass"
						break
					if(any(substring in file for substring in grass)):
						surfaceType = "grass"
						break
					if(any(substring in file for substring in gravel)):
						surfaceType = "gravel"
						break
					if(any(substring in file for substring in metal)):
						surfaceType = "metal"
						break
					if(any(substring in file for substring in mud)):
						surfaceType = "mud"
						break
					if(any(substring in file for substring in paper)):
						surfaceType = "paper"
						break
					if(any(substring in file for substring in plaster)):
						surfaceType = "plaster"
						break
					if(any(substring in file for substring in rock)):
						surfaceType = "rock"
						break
					if(any(substring in file for substring in sand)):
						surfaceType = "sand"
						break
					if(any(substring in file for substring in snow)):
						surfaceType = "snow"
						break
					if(any(substring in file for substring in water)):
						surfaceType = "water"
						break
					if(any(substring in file for substring in wood)):
						surfaceType = "wood"
						break
					if(any(substring in file for substring in dirt)):
						surfaceType = "dirt"
						break
					break
				
				f.write("\t\t\"surfaceType\" \"" + surfaceType + "\"\n")
				
				img = Image.open(sys.argv[1] + "\\" + file)
				if(has_transparency(img)):
					f.write("\t\t\"blendFunc\" \"Blend\"\n")
				
				f.write("\t}\n")

f.write("}\n")
f.close()