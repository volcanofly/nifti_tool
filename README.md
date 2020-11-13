
# nifti_tool

This is a tool to read and save nifti files with nibabel in python.
We often worry that the nifti files we read have different orientations.
The solution is simply, reorient them all to canonical view.
This tool can do this, you won't need to worry it will ruin the header.

- To read an nifti image:

nib_obj = util_nifti()

img,affine = nib_obj.read_nifti(in_file)

- To read an nifti image in canonical view:

img,affine = nib_obj.read_nifti(in_file,to_canonicalBool=True)

- To find_resolution of an nifti image:

resolution_xyz_list = nib_obj.find_resolution(in_file)
