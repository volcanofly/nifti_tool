# nifti_tool

# To read an nifti image:
nib_obj = util_nifti()
img,affine = nib_obj.read_nifti(in_file)

# To read an nifti image in canonical view:
img,affine = nib_obj.read_nifti(in_file,to_canonicalBool=True)

# To find_resolution of an nifti image:
resolution_xyz_list = nib_obj.find_resolution(in_file)
