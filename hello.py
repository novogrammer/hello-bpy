import bpy
from pathlib import Path

bpy.app.binary_path = "/Applications/Blender.app/Contents/MacOS/Blender"

# 画像ファイルのパス
image_path = str(Path("./input/hello.png").resolve())

output_path = str(Path("./output/output.jpg").resolve())

output_debug_path = str(Path("./output/debug.blend").resolve())

# アクティブなオブジェクトを取得
obj = bpy.context.active_object

# 不要なマテリアルを削除 (必要に応じて)
obj.data.materials.clear()

# マテリアルを作成
mat = bpy.data.materials.new(name="ImageMaterial")
if mat is None:
    print("Error: Material creation failed.")
    exit(1)
obj.data.materials.append(mat)

# ノードを作成
mat.use_nodes = True
nodes = mat.node_tree.nodes
principled_bsdf = nodes.get("Principled BSDF")

# 画像テクスチャノードを作成
image_texture = nodes.new('ShaderNodeTexImage')
image_texture.image = bpy.data.images.load(image_path)

# ノードを接続
links = mat.node_tree.links
links.new(image_texture.outputs['Color'], principled_bsdf.inputs['Base Color'])

# レンダー設定
bpy.context.scene.render.engine = 'CYCLES'
bpy.context.scene.render.filepath = output_path
bpy.context.scene.render.image_settings.file_format = 'JPEG'
bpy.context.scene.render.image_settings.quality = 95

# レンダー実行
bpy.ops.render.render(write_still=True)

# ファイルを保存
bpy.ops.wm.save_mainfile(filepath=output_debug_path)

