'''
This script includes utils for nifti files.
@Can Zhao (volcanofly@gmail.com), Nov. 2019
'''

import nibabel as nib
import os
import numpy as np
class util_nifti():
	def __init__(self):
		super(util_nifti, self).__init__()

	def nifti_filenameSplit(self,filepath):
		# Split nifti filename, return (dir,filename,ext)
		# e.g. filepath: /home/happyface/happybrain.nii
		# 	   return ('/home/happyface', 'happybrain', '.nii')
		# if ext is not '.nii' or '.nii.gz', it will give an error message.
		head_tail = os.path.split(filepath)
		dir_file = head_tail[0]
		filenameList = head_tail[1].split('.')
		if filenameList[-1]=='nii':
			filename='.'.join(filenameList[:-1])
			ext='.nii'
			return dir_file, filename, ext
		elif filenameList[-1]=='gz' and filenameList[-2]=='nii':
			filename='.'.join(filenameList[:-2])
			ext='.nii.gz'
			return dir_file, filename, ext
		else:
			ValueError('filepath has be to .nii or .nii.gz')

	def read_nifti(self,filepath,to_canonicalBool=False):
		# read nifti file, return data and affine matrix
		img_obj = nib.load(filepath)
		if to_canonicalBool:
			img_obj = nib.as_closest_canonical(img_obj)
		img = img_obj.get_data()
		affine = img_obj.affine
		return img,affine

	def flip_nifti(self,inpath, outpath, axis=0):
		# flip along one axis
		assert axis in [0,1,2]
		img_obj = nib.load(inpath)
		img = img_obj.get_data()
		img_flip = nib.orientations.flip_axis(img,axis)
		img_obj = nib.Nifti1Image(img_flip,affine = img_obj.affine)
		nib.save(img_obj,outpath)

	def save_nifti(self,img,affine,outpath):
		img_obj = nib.Nifti1Image(img, affine = affine)
		nib.save(img_obj,outpath)

	def to_canonical(self,inpath, outpath):
		# flip image to canonical view
		img_obj = nib.load(inpath)
		canonical_img_obj = nib.as_closest_canonical(img_obj)
		nib.save(canonical_img_obj,outpath)

	def find_resolution(self,filepath):
		img_obj = nib.load(filepath)
		hdr = img_obj.header
		affineM = hdr.get_base_affine()
		x = abs(affineM[0][0])
		y = abs(affineM[1][1])
		z = abs(affineM[2][2])
		return [x,y,z]

	def create_allOneImg(self,infilepath,outfilepath):
		img,affine = self.read_nifti(infilepath,to_canonicalBool=False)
		img = np.ones(shape = img.shape)
		img_obj = nib.Nifti1Image(img, affine = affine)
		nib.save(img_obj,outfilepath)
