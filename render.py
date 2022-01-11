#py -3.9 -m pip install
import pyrender
import trimesh
import numpy as np

def show(obj, wire=False):
    #r = pyrender.OffscreenRenderer(viewport_width=640, viewport_height=480, point_size=1.0)
    shape_trimesh = trimesh.load(obj)
    mesh = pyrender.Mesh.from_trimesh(shape_trimesh, wireframe=wire)
    scene = pyrender.Scene()
    pl = pyrender.PointLight(color=[1.0, 1.0, 1.0], intensity=2.0)
    scene.add(mesh)
    scene.add(pl)
    flags = pyrender.RenderFlags.SKIP_CULL_FACES
    #r.render(scene, flags = flags)
    pyrender.Viewer(scene, use_raymond_lighting = True, cull_faces = False)

#show("generationTest5.obj")
#show("out.obj")