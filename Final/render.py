import pyrender
import trimesh
import numpy as np

def show(obj, wire=False):
    shape_trimesh = trimesh.load(obj)
    mesh = pyrender.Mesh.from_trimesh(shape_trimesh, wireframe=wire)
    scene = pyrender.Scene()
    pl = pyrender.PointLight(color=[1.0, 1.0, 1.0], intensity=2.0)
    scene.add(mesh)
    scene.add(pl)
    flags = pyrender.RenderFlags.SKIP_CULL_FACES
    pyrender.Viewer(scene, use_raymond_lighting = True, cull_faces = False)