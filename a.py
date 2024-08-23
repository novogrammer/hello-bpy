import bpy
# import shutil

# blender_bin = shutil.which("blender")
# if blender_bin:
#   print("Found:", blender_bin)
#   bpy.app.binary_path = blender_bin
# else:
#   print("Unable to find blender!")

bpy.app.binary_path = "/Applications/Blender.app/Contents/MacOS/Blender"

# print(bpy.data.objects)
# print(bpy.data.objects['Cube'])
print(bpy.data.objects[0].name)