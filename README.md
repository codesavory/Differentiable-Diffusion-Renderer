# Differentiable-Diffusion-Renderer
Differentiable Renderer that allows to texture 3D models using Stable Diffusion

Pipeline - 
1. Sample 3D Mesh into Points Clouds
2. Convert 3D to 4D Radiance Field or SDF
3. Fetch textures using Stable Diffusion
4. Optimize textures using differentiable rendering
5. Extract 3D meshes using Marching Cubes