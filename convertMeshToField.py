'''
Created by Suriya on 1st June, 2024

The idea is to extrapolate a 3D Mesh into a 4D Radiance Field
So that we can apply effects and operation in the higher dimension

Steps - 
1. Mesh to Point Cloud
2. Point Cloud to SDF
3. SDF to NeRF

Other way - Think about converting Mesh to Structured Point Cloud Data
'''

import torch
import kaolin as kal
import os
from pytorch3d.io import IO
from pytorch3d.structures import Pointclouds

def filter_invalid_faces(vertices, faces):
    num_vertices = vertices.shape[0]
    valid_faces = (faces < num_vertices).all(dim=1)
    return faces[valid_faces]

def convert_mesh_to_pointcloud(meshPath: str) -> str:
    surfaceMesh = kal.io.gltf.import_mesh(meshPath)
    print(surfaceMesh)
    verticesBatched = surfaceMesh.vertices.unsqueeze(0)
    
    points, _ = kal.ops.mesh.sample_points(verticesBatched, surfaceMesh.faces, num_samples=1000000)
    # Assuming 'point_cloud' is a tensor of shape (N, 3) where N is the number of points.
    exportPath = os.path.dirname(meshPath)+'/pointCloud.ply'
    IO().save_pointcloud(Pointclouds(points), exportPath)
    return exportPath

if __name__ == "__main__":
    convert_mesh_to_pointcloud('..\\3D Models\\cybertruck_from_tesla\\scene.gltf')