# Make all the necessary imports___________________________________________________________________________
import sys
import os
import numpy as np
import pandas as pd
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'batches')))
from experiments.sud.tanh_training.batches.__training_data import training_data
from experiments.sud.tanh_training.batches.__training_data import (nobl_fu, vymi_fu, pey_fu, xle_fu, vym_fu,
																   hdv_fu, glncy_fu, dgro_fu, vb_fu, jnk_fu,
																   hyg_fu, schd_fu, ixus_fu, djia_fu, lit_fu,
																   sphd_fu, iscf_fu, hscz_fu, hdef_fu, pcy_fu,
																   bndx_fu, smx_fu, hefa_fu, iyk_fu, usoi_fu,
																   xlf_fu, vfh_fu, kre_fu, iyf_fu, fncl_fu,
																   qqq_fu, spy_fu, vti_fu, itot_fu, xlk_fu,
																   xly_fu, xlv_fu, eem_fu, veu_fu)
# Format required NOBL entries___________________________________________________________________________
nobl_dat = nobl_fu(training_data)

# Daily change for NOBL batches 1 to 5
def nobl_batch_values(nobl_dat):
	nobl_open_stop = pd.DataFrame(nobl_dat)  # Define the value we are subtracting from
	nobl_open_start = pd.DataFrame(nobl_dat).shift(periods=1)  # Define the value we are subtracting
	nobl_stop = nobl_open_stop.to_numpy()  # Convert to array
	nobl_start = nobl_open_start.to_numpy()  # Convert to array
	nobl_start[np.isnan(nobl_start)] = np.mean(nobl_start[np.logical_not(np.isnan(nobl_start))])  # Remove NaN values
	nobl_change = nobl_stop - nobl_start  # Calculate difference
	nobl_change = np.transpose(nobl_change)  # Transpose so we calculate the per day change magnitude
	nobl_change_mag = np.linalg.norm(nobl_change, axis=0)  # Calculate the magnitude
	nobl_values = nobl_change_mag * nobl_change  # Calculate the data we will work with
	return nobl_values

# Retrieving formatted data
def nobl_batch_1_values():
	return nobl_batch_values(nobl_dat[0])

def nobl_batch_2_values():
	return nobl_batch_values(nobl_dat[1])

def nobl_batch_3_values():
	return nobl_batch_values(nobl_dat[2])

def nobl_batch_4_values():
	return nobl_batch_values(nobl_dat[3])

def nobl_batch_5_values():
	return nobl_batch_values(nobl_dat[4])

# Format required VYMI entries___________________________________________________________________________
vymi_dat = vymi_fu(training_data)

# Daily change for VYMI batches 1 to 5
def vymi_batch_values(vymi_dat):
	vymi_open_stop = pd.DataFrame(vymi_dat)  # Define the value we are subtracting from
	vymi_open_start = pd.DataFrame(vymi_dat).shift(periods=1)  # Define the value we are subtracting
	vymi_stop = vymi_open_stop.to_numpy()  # Convert to array
	vymi_start = vymi_open_start.to_numpy()  # Convert to array
	vymi_start[np.isnan(vymi_start)] = np.mean(vymi_start[np.logical_not(np.isnan(vymi_start))])  # Remove NaN values
	vymi_change = vymi_stop - vymi_start  # Calculate difference
	vymi_change = np.transpose(vymi_change)  # Transpose so we calculate the per day change magnitude
	vymi_change_mag = np.linalg.norm(vymi_change, axis=0)  # Calculate the magnitude
	vymi_values = vymi_change_mag * vymi_change  # Calculate the data we will work with
	return vymi_values

# Retrieving formatted data
def vymi_batch_1_values():
	return vymi_batch_values(vymi_dat[0])

def vymi_batch_2_values():
	return vymi_batch_values(vymi_dat[1])

def vymi_batch_3_values():
	return vymi_batch_values(vymi_dat[2])

def vymi_batch_4_values():
	return vymi_batch_values(vymi_dat[3])

def vymi_batch_5_values():
	return vymi_batch_values(vymi_dat[4])

# Format required PEY entries___________________________________________________________________________
pey_dat = pey_fu(training_data)

# Daily change for PEY batches 1 to 5
def pey_batch_values(pey_dat):
	pey_open_stop = pd.DataFrame(pey_dat)  # Define the value we are subtracting from
	pey_open_start = pd.DataFrame(pey_dat).shift(periods=1)  # Define the value we are subtracting
	pey_stop = pey_open_stop.to_numpy()  # Convert to array
	pey_start = pey_open_start.to_numpy()  # Convert to array
	pey_start[np.isnan(pey_start)] = np.mean(pey_start[np.logical_not(np.isnan(pey_start))])  # Remove NaN values
	pey_change = pey_stop - pey_start  # Calculate difference
	pey_change = np.transpose(pey_change)  # Transpose so we calculate the per day change magnitude
	pey_change_mag = np.linalg.norm(pey_change, axis=0)  # Calculate the magnitude
	pey_values = pey_change_mag * pey_change  # Calculate the data we will work with
	return pey_values

# Retrieving formatted data
def pey_batch_1_values():
	return pey_batch_values(pey_dat[0])

def pey_batch_2_values():
	return pey_batch_values(pey_dat[1])

def pey_batch_3_values():
	return pey_batch_values(pey_dat[2])

def pey_batch_4_values():
	return pey_batch_values(pey_dat[3])

def pey_batch_5_values():
	return pey_batch_values(pey_dat[4])

# Format required VYM entries___________________________________________________________________________
vym_dat = vym_fu(training_data)

# Daily change for VYM batches 1 to 5
def vym_batch_values(vym_dat):
	vym_open_stop = pd.DataFrame(vym_dat)  # Define the value we are subtracting from
	vym_open_start = pd.DataFrame(vym_dat).shift(periods=1)  # Define the value we are subtracting
	vym_stop = vym_open_stop.to_numpy()  # Convert to array
	vym_start = vym_open_start.to_numpy()  # Convert to array
	vym_start[np.isnan(vym_start)] = np.mean(vym_start[np.logical_not(np.isnan(vym_start))])  # Remove NaN values
	vym_change = vym_stop - vym_start  # Calculate difference
	vym_change = np.transpose(vym_change)  # Transpose so we calculate the per day change magnitude
	vym_change_mag = np.linalg.norm(vym_change, axis=0)  # Calculate the magnitude
	vym_values = vym_change_mag * vym_change  # Calculate the data we will work with
	return vym_values

# Retrieving formatted data
def vym_batch_1_values():
	return vym_batch_values(vym_dat[0])

def vym_batch_2_values():
	return vym_batch_values(vym_dat[1])

def vym_batch_3_values():
	return vym_batch_values(vym_dat[2])

def vym_batch_4_values():
	return vym_batch_values(vym_dat[3])

def vym_batch_5_values():
	return vym_batch_values(vym_dat[4])

# Format required HDV entries___________________________________________________________________________
hdv_dat = hdv_fu(training_data)

# Daily change for HDV batches 1 to 5
def hdv_batch_values(hdv_dat):
	hdv_open_stop = pd.DataFrame(hdv_dat)  # Define the value we are subtracting from
	hdv_open_start = pd.DataFrame(hdv_dat).shift(periods=1)  # Define the value we are subtracting
	hdv_stop = hdv_open_stop.to_numpy()  # Convert to array
	hdv_start = hdv_open_start.to_numpy()  # Convert to array
	hdv_start[np.isnan(hdv_start)] = np.mean(hdv_start[np.logical_not(np.isnan(hdv_start))])  # Remove NaN values
	hdv_change = hdv_stop - hdv_start  # Calculate difference
	hdv_change = np.transpose(hdv_change)  # Transpose so we calculate the per day change magnitude
	hdv_change_mag = np.linalg.norm(hdv_change, axis=0)  # Calculate the magnitude
	hdv_values = hdv_change_mag * hdv_change  # Calculate the data we will work with
	return hdv_values

# Retrieving formatted data
def hdv_batch_1_values():
	return hdv_batch_values(hdv_dat[0])

def hdv_batch_2_values():
	return hdv_batch_values(hdv_dat[1])

def hdv_batch_3_values():
	return hdv_batch_values(hdv_dat[2])

def hdv_batch_4_values():
	return hdv_batch_values(hdv_dat[3])

def hdv_batch_5_values():
	return hdv_batch_values(hdv_dat[4])

# Format required GLNCY entries___________________________________________________________________________
glncy_dat = glncy_fu(training_data)

# Daily change for GLNCY batches 1 to 5
def glncy_batch_values(glncy_dat):
	glncy_open_stop = pd.DataFrame(glncy_dat)  # Define the value we are subtracting from
	glncy_open_start = pd.DataFrame(glncy_dat).shift(periods=1)  # Define the value we are subtracting
	glncy_stop = glncy_open_stop.to_numpy()  # Convert to array
	glncy_start = glncy_open_start.to_numpy()  # Convert to array
	glncy_start[np.isnan(glncy_start)] = np.mean(glncy_start[np.logical_not(np.isnan(glncy_start))])  # Remove NaN values
	glncy_change = glncy_stop - glncy_start  # Calculate difference
	glncy_change = np.transpose(glncy_change)  # Transpose so we calculate the per day change magnitude
	glncy_change_mag = np.linalg.norm(glncy_change, axis=0)  # Calculate the magnitude
	glncy_values = glncy_change_mag * glncy_change  # Calculate the data we will work with
	return glncy_values

# Retrieving formatted data
def glncy_batch_1_values():
	return glncy_batch_values(glncy_dat[0])

def glncy_batch_2_values():
	return glncy_batch_values(glncy_dat[1])

def glncy_batch_3_values():
	return glncy_batch_values(glncy_dat[2])

def glncy_batch_4_values():
	return glncy_batch_values(glncy_dat[3])

def glncy_batch_5_values():
	return glncy_batch_values(glncy_dat[4])

# Format required XLE entries___________________________________________________________________________
xle_dat = xle_fu(training_data)

# Daily change for XLE batches 1 to 5
def xle_batch_values(xle_dat):
	xle_open_stop = pd.DataFrame(xle_dat)  # Define the value we are subtracting from
	xle_open_start = pd.DataFrame(xle_dat).shift(periods=1)  # Define the value we are subtracting
	xle_stop = xle_open_stop.to_numpy()  # Convert to array
	xle_start = xle_open_start.to_numpy()  # Convert to array
	xle_start[np.isnan(xle_start)] = np.mean(xle_start[np.logical_not(np.isnan(xle_start))])  # Remove NaN values
	xle_change = xle_stop - xle_start  # Calculate difference
	xle_change = np.transpose(xle_change)  # Transpose so we calculate the per day change magnitude
	xle_change_mag = np.linalg.norm(xle_change, axis=0)  # Calculate the magnitude
	xle_values = xle_change_mag * xle_change  # Calculate the data we will work with
	return xle_values

# Retrieving formatted data
def xle_batch_1_values():
	return xle_batch_values(xle_dat[0])

def xle_batch_2_values():
	return xle_batch_values(xle_dat[1])

def xle_batch_3_values():
	return xle_batch_values(xle_dat[2])

def xle_batch_4_values():
	return xle_batch_values(xle_dat[3])

def xle_batch_5_values():
	return xle_batch_values(xle_dat[4])

# Format required VB entries___________________________________________________________________________
vb_dat = vb_fu(training_data)

# Daily change for VB batches 1 to 5
def vb_batch_values(vb_dat):
	vb_open_stop = pd.DataFrame(vb_dat)  # Define the value we are subtracting from
	vb_open_start = pd.DataFrame(vb_dat).shift(periods=1)  # Define the value we are subtracting
	vb_stop = vb_open_stop.to_numpy()  # Convert to array
	vb_start = vb_open_start.to_numpy()  # Convert to array
	vb_start[np.isnan(vb_start)] = np.mean(vb_start[np.logical_not(np.isnan(vb_start))])  # Remove NaN values
	vb_change = vb_stop - vb_start  # Calculate difference
	vb_change = np.transpose(vb_change)  # Transpose so we calculate the per day change magnitude
	vb_change_mag = np.linalg.norm(vb_change, axis=0)  # Calculate the magnitude
	vb_values = vb_change_mag * vb_change  # Calculate the data we will work with
	return vb_values

# Retrieving formatted data
def vb_batch_1_values():
	return vb_batch_values(vb_dat[0])

def vb_batch_2_values():
	return vb_batch_values(vb_dat[1])

def vb_batch_3_values():
	return vb_batch_values(vb_dat[2])

def vb_batch_4_values():
	return vb_batch_values(vb_dat[3])

def vb_batch_5_values():
	return vb_batch_values(vb_dat[4])

# Format required JNK entries___________________________________________________________________________
jnk_dat = jnk_fu(training_data)

# Daily change for JNK batches 1 to 5
def jnk_batch_values(jnk_dat):
	jnk_open_stop = pd.DataFrame(jnk_dat)  # Define the value we are subtracting from
	jnk_open_start = pd.DataFrame(jnk_dat).shift(periods=1)  # Define the value we are subtracting
	jnk_stop = jnk_open_stop.to_numpy()  # Convert to array
	jnk_start = jnk_open_start.to_numpy()  # Convert to array
	jnk_start[np.isnan(jnk_start)] = np.mean(jnk_start[np.logical_not(np.isnan(jnk_start))])  # Remove NaN values
	jnk_change = jnk_stop - jnk_start  # Calculate difference
	jnk_change = np.transpose(jnk_change)  # Transpose so we calculate the per day change magnitude
	jnk_change_mag = np.linalg.norm(jnk_change, axis=0)  # Calculate the magnitude
	jnk_values = jnk_change_mag * jnk_change  # Calculate the data we will work with
	return jnk_values

# Retrieving formatted data
def jnk_batch_1_values():
	return jnk_batch_values(jnk_dat[0])

def jnk_batch_2_values():
	return jnk_batch_values(jnk_dat[1])

def jnk_batch_3_values():
	return jnk_batch_values(jnk_dat[2])

def jnk_batch_4_values():
	return jnk_batch_values(jnk_dat[3])

def jnk_batch_5_values():
	return jnk_batch_values(jnk_dat[4])

# Format required DGRO entries___________________________________________________________________________
dgro_dat = dgro_fu(training_data)

# Daily change for DGRO batches 1 to 5
def dgro_batch_values(dgro_dat):
	dgro_open_stop = pd.DataFrame(dgro_dat)  # Define the value we are subtracting from
	dgro_open_start = pd.DataFrame(dgro_dat).shift(periods=1)  # Define the value we are subtracting
	dgro_stop = dgro_open_stop.to_numpy()  # Convert to array
	dgro_start = dgro_open_start.to_numpy()  # Convert to array
	dgro_start[np.isnan(dgro_start)] = np.mean(dgro_start[np.logical_not(np.isnan(dgro_start))])  # Remove NaN values
	dgro_change = dgro_stop - dgro_start  # Calculate difference
	dgro_change = np.transpose(dgro_change)  # Transpose so we calculate the per day change magnitude
	dgro_change_mag = np.linalg.norm(dgro_change, axis=0)  # Calculate the magnitude
	dgro_values = dgro_change_mag * dgro_change  # Calculate the data we will work with
	return dgro_values

# Retrieving formatted data for DGRO
def dgro_batch_1_values():
	return dgro_batch_values(dgro_dat[0])

def dgro_batch_2_values():
	return dgro_batch_values(dgro_dat[1])

def dgro_batch_3_values():
	return dgro_batch_values(dgro_dat[2])

def dgro_batch_4_values():
	return dgro_batch_values(dgro_dat[3])

def dgro_batch_5_values():
	return dgro_batch_values(dgro_dat[4])


# Format required HYG entries___________________________________________________________________________
hyg_dat = hyg_fu(training_data)

# Daily change for HYG batches 1 to 5
def hyg_batch_values(hyg_dat):
	hyg_open_stop = pd.DataFrame(hyg_dat)  # Define the value we are subtracting from
	hyg_open_start = pd.DataFrame(hyg_dat).shift(periods=1)  # Define the value we are subtracting
	hyg_stop = hyg_open_stop.to_numpy()  # Convert to array
	hyg_start = hyg_open_start.to_numpy()  # Convert to array
	hyg_start[np.isnan(hyg_start)] = np.mean(hyg_start[np.logical_not(np.isnan(hyg_start))])  # Remove NaN values
	hyg_change = hyg_stop - hyg_start  # Calculate difference
	hyg_change = np.transpose(hyg_change)  # Transpose so we calculate the per day change magnitude
	hyg_change_mag = np.linalg.norm(hyg_change, axis=0)  # Calculate the magnitude
	hyg_values = hyg_change_mag * hyg_change  # Calculate the data we will work with
	return hyg_values

# Retrieving formatted data for HYG
def hyg_batch_1_values():
	return hyg_batch_values(hyg_dat[0])

def hyg_batch_2_values():
	return hyg_batch_values(hyg_dat[1])

def hyg_batch_3_values():
	return hyg_batch_values(hyg_dat[2])

def hyg_batch_4_values():
	return hyg_batch_values(hyg_dat[3])

def hyg_batch_5_values():
	return hyg_batch_values(hyg_dat[4])


# Format required SCHD entries___________________________________________________________________________
schd_dat = schd_fu(training_data)

# Daily change for SCHD batches 1 to 5
def schd_batch_values(schd_dat):
	schd_open_stop = pd.DataFrame(schd_dat)  # Define the value we are subtracting from
	schd_open_start = pd.DataFrame(schd_dat).shift(periods=1)  # Define the value we are subtracting
	schd_stop = schd_open_stop.to_numpy()  # Convert to array
	schd_start = schd_open_start.to_numpy()  # Convert to array
	schd_start[np.isnan(schd_start)] = np.mean(schd_start[np.logical_not(np.isnan(schd_start))])  # Remove NaN values
	schd_change = schd_stop - schd_start  # Calculate difference
	schd_change = np.transpose(schd_change)  # Transpose so we calculate the per day change magnitude
	schd_change_mag = np.linalg.norm(schd_change, axis=0)  # Calculate the magnitude
	schd_values = schd_change_mag * schd_change  # Calculate the data we will work with
	return schd_values

# Retrieving formatted data for SCHD
def schd_batch_1_values():
	return schd_batch_values(schd_dat[0])

def schd_batch_2_values():
	return schd_batch_values(schd_dat[1])

def schd_batch_3_values():
	return schd_batch_values(schd_dat[2])

def schd_batch_4_values():
	return schd_batch_values(schd_dat[3])

def schd_batch_5_values():
	return schd_batch_values(schd_dat[4])


# Format required IXUS entries___________________________________________________________________________
ixus_dat = ixus_fu(training_data)

# Daily change for IXUS batches 1 to 5
def ixus_batch_values(ixus_dat):
	ixus_open_stop = pd.DataFrame(ixus_dat)  # Define the value we are subtracting from
	ixus_open_start = pd.DataFrame(ixus_dat).shift(periods=1)  # Define the value we are subtracting
	ixus_stop = ixus_open_stop.to_numpy()  # Convert to array
	ixus_start = ixus_open_start.to_numpy()  # Convert to array
	ixus_start[np.isnan(ixus_start)] = np.mean(ixus_start[np.logical_not(np.isnan(ixus_start))])  # Remove NaN values
	ixus_change = ixus_stop - ixus_start  # Calculate difference
	ixus_change = np.transpose(ixus_change)  # Transpose so we calculate the per day change magnitude
	ixus_change_mag = np.linalg.norm(ixus_change, axis=0)  # Calculate the magnitude
	ixus_values = ixus_change_mag * ixus_change  # Calculate the data we will work with
	return ixus_values

# Retrieving formatted data for IXUS
def ixus_batch_1_values():
	return ixus_batch_values(ixus_dat[0])

def ixus_batch_2_values():
	return ixus_batch_values(ixus_dat[1])

def ixus_batch_3_values():
	return ixus_batch_values(ixus_dat[2])

def ixus_batch_4_values():
	return ixus_batch_values(ixus_dat[3])

def ixus_batch_5_values():
	return ixus_batch_values(ixus_dat[4])


# Format required DJIA entries___________________________________________________________________________
djia_dat = djia_fu(training_data)

# Daily change for DJIA batches 1 to 5
def djia_batch_values(djia_dat):
	djia_open_stop = pd.DataFrame(djia_dat)  # Define the value we are subtracting from
	djia_open_start = pd.DataFrame(djia_dat).shift(periods=1)  # Define the value we are subtracting
	djia_stop = djia_open_stop.to_numpy()  # Convert to array
	djia_start = djia_open_start.to_numpy()  # Convert to array
	djia_start[np.isnan(djia_start)] = np.mean(djia_start[np.logical_not(np.isnan(djia_start))])  # Remove NaN values
	djia_change = djia_stop - djia_start  # Calculate difference
	djia_change = np.transpose(djia_change)  # Transpose so we calculate the per day change magnitude
	djia_change_mag = np.linalg.norm(djia_change, axis=0)  # Calculate the magnitude
	djia_values = djia_change_mag * djia_change  # Calculate the data we will work with
	return djia_values

# Retrieving formatted data for DJIA
def djia_batch_1_values():
	return djia_batch_values(djia_dat[0])

def djia_batch_2_values():
	return djia_batch_values(djia_dat[1])

def djia_batch_3_values():
	return djia_batch_values(djia_dat[2])

def djia_batch_4_values():
	return djia_batch_values(djia_dat[3])

def djia_batch_5_values():
	return djia_batch_values(djia_dat[4])


# Format required LIT entries___________________________________________________________________________
lit_dat = lit_fu(training_data)

# Daily change for LIT batches 1 to 5
def lit_batch_values(lit_dat):
	lit_open_stop = pd.DataFrame(lit_dat)  # Define the value we are subtracting from
	lit_open_start = pd.DataFrame(lit_dat).shift(periods=1)  # Define the value we are subtracting
	lit_stop = lit_open_stop.to_numpy()  # Convert to array
	lit_start = lit_open_start.to_numpy()  # Convert to array
	lit_start[np.isnan(lit_start)] = np.mean(lit_start[np.logical_not(np.isnan(lit_start))])  # Remove NaN values
	lit_change = lit_stop - lit_start  # Calculate difference
	lit_change = np.transpose(lit_change)  # Transpose so we calculate the per day change magnitude
	lit_change_mag = np.linalg.norm(lit_change, axis=0)  # Calculate the magnitude
	lit_values = lit_change_mag * lit_change  # Calculate the data we will work with
	return lit_values

# Retrieving formatted data for LIT
def lit_batch_1_values():
	return lit_batch_values(lit_dat[0])

def lit_batch_2_values():
	return lit_batch_values(lit_dat[1])

def lit_batch_3_values():
	return lit_batch_values(lit_dat[2])

def lit_batch_4_values():
	return lit_batch_values(lit_dat[3])

def lit_batch_5_values():
	return lit_batch_values(lit_dat[4])


# Format required SPHD entries___________________________________________________________________________
sphd_dat = sphd_fu(training_data)

# Daily change for SPHD batches 1 to 5
def sphd_batch_values(sphd_dat):
	sphd_open_stop = pd.DataFrame(sphd_dat)  # Define the value we are subtracting from
	sphd_open_start = pd.DataFrame(sphd_dat).shift(periods=1)  # Define the value we are subtracting
	sphd_stop = sphd_open_stop.to_numpy()  # Convert to array
	sphd_start = sphd_open_start.to_numpy()  # Convert to array
	sphd_start[np.isnan(sphd_start)] = np.mean(sphd_start[np.logical_not(np.isnan(sphd_start))])  # Remove NaN values
	sphd_change = sphd_stop - sphd_start  # Calculate difference
	sphd_change = np.transpose(sphd_change)  # Transpose so we calculate the per day change magnitude
	sphd_change_mag = np.linalg.norm(sphd_change, axis=0)  # Calculate the magnitude
	sphd_values = sphd_change_mag * sphd_change  # Calculate the data we will work with
	return sphd_values

# Retrieving formatted data for SPHD
def sphd_batch_1_values():
	return sphd_batch_values(sphd_dat[0])

def sphd_batch_2_values():
	return sphd_batch_values(sphd_dat[1])

def sphd_batch_3_values():
	return sphd_batch_values(sphd_dat[2])

def sphd_batch_4_values():
	return sphd_batch_values(sphd_dat[3])

def sphd_batch_5_values():
	return sphd_batch_values(sphd_dat[4])


# Format required ISCF entries___________________________________________________________________________
iscf_dat = iscf_fu(training_data)

# Daily change for ISCF batches 1 to 5
def iscf_batch_values(iscf_dat):
	iscf_open_stop = pd.DataFrame(iscf_dat)  # Define the value we are subtracting from
	iscf_open_start = pd.DataFrame(iscf_dat).shift(periods=1)  # Define the value we are subtracting
	iscf_stop = iscf_open_stop.to_numpy()  # Convert to array
	iscf_start = iscf_open_start.to_numpy()  # Convert to array
	iscf_start[np.isnan(iscf_start)] = np.mean(iscf_start[np.logical_not(np.isnan(iscf_start))])  # Remove NaN values
	iscf_change = iscf_stop - iscf_start  # Calculate difference
	iscf_change = np.transpose(iscf_change)  # Transpose so we calculate the per day change magnitude
	iscf_change_mag = np.linalg.norm(iscf_change, axis=0)  # Calculate the magnitude
	iscf_values = iscf_change_mag * iscf_change  # Calculate the data we will work with
	return iscf_values

# Retrieving formatted data for ISCF
def iscf_batch_1_values():
	return iscf_batch_values(iscf_dat[0])

def iscf_batch_2_values():
	return iscf_batch_values(iscf_dat[1])

def iscf_batch_3_values():
	return iscf_batch_values(iscf_dat[2])

def iscf_batch_4_values():
	return iscf_batch_values(iscf_dat[3])

def iscf_batch_5_values():
	return iscf_batch_values(iscf_dat[4])


# Format required HSCZ entries___________________________________________________________________________
hscz_dat = hscz_fu(training_data)

# Daily change for HSCZ batches 1 to 5
def hscz_batch_values(hscz_dat):
	hscz_open_stop = pd.DataFrame(hscz_dat)  # Define the value we are subtracting from
	hscz_open_start = pd.DataFrame(hscz_dat).shift(periods=1)  # Define the value we are subtracting
	hscz_stop = hscz_open_stop.to_numpy()  # Convert to array
	hscz_start = hscz_open_start.to_numpy()  # Convert to array
	hscz_start[np.isnan(hscz_start)] = np.mean(hscz_start[np.logical_not(np.isnan(hscz_start))])  # Remove NaN values
	hscz_change = hscz_stop - hscz_start  # Calculate difference
	hscz_change = np.transpose(hscz_change)  # Transpose so we calculate the per day change magnitude
	hscz_change_mag = np.linalg.norm(hscz_change, axis=0)  # Calculate the magnitude
	hscz_values = hscz_change_mag * hscz_change  # Calculate the data we will work with
	return hscz_values

# Retrieving formatted data for HSCZ
def hscz_batch_1_values():
	return hscz_batch_values(hscz_dat[0])

def hscz_batch_2_values():
	return hscz_batch_values(hscz_dat[1])

def hscz_batch_3_values():
	return hscz_batch_values(hscz_dat[2])

def hscz_batch_4_values():
	return hscz_batch_values(hscz_dat[3])

def hscz_batch_5_values():
	return hscz_batch_values(hscz_dat[4])


# Format required HDEF entries___________________________________________________________________________
hdef_dat = hdef_fu(training_data)

# Daily change for HDEF batches 1 to 5
def hdef_batch_values(hdef_dat):
	hdef_open_stop = pd.DataFrame(hdef_dat)  # Define the value we are subtracting from
	hdef_open_start = pd.DataFrame(hdef_dat).shift(periods=1)  # Define the value we are subtracting
	hdef_stop = hdef_open_stop.to_numpy()  # Convert to array
	hdef_start = hdef_open_start.to_numpy()  # Convert to array
	hdef_start[np.isnan(hdef_start)] = np.mean(hdef_start[np.logical_not(np.isnan(hdef_start))])  # Remove NaN values
	hdef_change = hdef_stop - hdef_start  # Calculate difference
	hdef_change = np.transpose(hdef_change)  # Transpose so we calculate the per day change magnitude
	hdef_change_mag = np.linalg.norm(hdef_change, axis=0)  # Calculate the magnitude
	hdef_values = hdef_change_mag * hdef_change  # Calculate the data we will work with
	return hdef_values

# Retrieving formatted data for HDEF
def hdef_batch_1_values():
	return hdef_batch_values(hdef_dat[0])

def hdef_batch_2_values():
	return hdef_batch_values(hdef_dat[1])

def hdef_batch_3_values():
	return hdef_batch_values(hdef_dat[2])

def hdef_batch_4_values():
	return hdef_batch_values(hdef_dat[3])

def hdef_batch_5_values():
	return hdef_batch_values(hdef_dat[4])


# Format required NOBL entries___________________________________________________________________________
pcy_dat = pcy_fu(training_data)

# Daily change for PCY batches 1 to 5
def pcy_batch_values(pcy_dat):
	pcy_open_stop = pd.DataFrame(pcy_dat)  # Define the value we are subtracting from
	pcy_open_start = pd.DataFrame(pcy_dat).shift(periods=1)  # Define the value we are subtracting
	pcy_stop = pcy_open_stop.to_numpy()  # Convert to array
	pcy_start = pcy_open_start.to_numpy()  # Convert to array
	pcy_start[np.isnan(pcy_start)] = np.mean(pcy_start[np.logical_not(np.isnan(pcy_start))])  # Remove NaN values
	pcy_change = pcy_stop - pcy_start  # Calculate difference
	pcy_change = np.transpose(pcy_change)  # Transpose so we calculate the per day change magnitude
	pcy_change_mag = np.linalg.norm(pcy_change, axis=0)  # Calculate the magnitude
	pcy_values = pcy_change_mag * pcy_change  # Calculate the data we will work with
	return pcy_values

# Retrieving formatted data for PCY
def pcy_batch_1_values():
	return pcy_batch_values(pcy_dat[0])

def pcy_batch_2_values():
	return pcy_batch_values(pcy_dat[1])

def pcy_batch_3_values():
	return pcy_batch_values(pcy_dat[2])

def pcy_batch_4_values():
	return pcy_batch_values(pcy_dat[3])

def pcy_batch_5_values():
	return pcy_batch_values(pcy_dat[4])


# Format required BNDX entries___________________________________________________________________________
bndx_dat = bndx_fu(training_data)

# Daily change for BNDX batches 1 to 5
def bndx_batch_values(bndx_dat):
	bndx_open_stop = pd.DataFrame(bndx_dat)  # Define the value we are subtracting from
	bndx_open_start = pd.DataFrame(bndx_dat).shift(periods=1)  # Define the value we are subtracting
	bndx_stop = bndx_open_stop.to_numpy()  # Convert to array
	bndx_start = bndx_open_start.to_numpy()  # Convert to array
	bndx_start[np.isnan(bndx_start)] = np.mean(bndx_start[np.logical_not(np.isnan(bndx_start))])  # Remove NaN values
	bndx_change = bndx_stop - bndx_start  # Calculate difference
	bndx_change = np.transpose(bndx_change)  # Transpose so we calculate the per day change magnitude
	bndx_change_mag = np.linalg.norm(bndx_change, axis=0)  # Calculate the magnitude
	bndx_values = bndx_change_mag * bndx_change  # Calculate the data we will work with
	return bndx_values

# Retrieving formatted data for BNDX
def bndx_batch_1_values():
	return bndx_batch_values(bndx_dat[0])

def bndx_batch_2_values():
	return bndx_batch_values(bndx_dat[1])

def bndx_batch_3_values():
	return bndx_batch_values(bndx_dat[2])

def bndx_batch_4_values():
	return bndx_batch_values(bndx_dat[3])

def bndx_batch_5_values():
	return bndx_batch_values(bndx_dat[4])


# Format required SMX entries___________________________________________________________________________
smx_dat = smx_fu(training_data)

# Daily change for SMX batches 1 to 5
def smx_batch_values(smx_dat):
	smx_open_stop = pd.DataFrame(smx_dat)  # Define the value we are subtracting from
	smx_open_start = pd.DataFrame(smx_dat).shift(periods=1)  # Define the value we are subtracting
	smx_stop = smx_open_stop.to_numpy()  # Convert to array
	smx_start = smx_open_start.to_numpy()  # Convert to array
	smx_start[np.isnan(smx_start)] = np.mean(smx_start[np.logical_not(np.isnan(smx_start))])  # Remove NaN values
	smx_change = smx_stop - smx_start  # Calculate difference
	smx_change = np.transpose(smx_change)  # Transpose so we calculate the per day change magnitude
	smx_change_mag = np.linalg.norm(smx_change, axis=0)  # Calculate the magnitude
	smx_values = smx_change_mag * smx_change  # Calculate the data we will work with
	return smx_values

# Retrieving formatted data for SMX
def smx_batch_1_values():
	return smx_batch_values(smx_dat[0])

def smx_batch_2_values():
	return smx_batch_values(smx_dat[1])

def smx_batch_3_values():
	return smx_batch_values(smx_dat[2])

def smx_batch_4_values():
	return smx_batch_values(smx_dat[3])

def smx_batch_5_values():
	return smx_batch_values(smx_dat[4])


# Format required NOBL entries___________________________________________________________________________
hefa_dat = hefa_fu(training_data)

# Daily change for HEFA batches 1 to 5
def hefa_batch_values(hefa_dat):
	hefa_open_stop = pd.DataFrame(hefa_dat)  # Define the value we are subtracting from
	hefa_open_start = pd.DataFrame(hefa_dat).shift(periods=1)  # Define the value we are subtracting
	hefa_stop = hefa_open_stop.to_numpy()  # Convert to array
	hefa_start = hefa_open_start.to_numpy()  # Convert to array
	hefa_start[np.isnan(hefa_start)] = np.mean(hefa_start[np.logical_not(np.isnan(hefa_start))])  # Remove NaN values
	hefa_change = hefa_stop - hefa_start  # Calculate difference
	hefa_change = np.transpose(hefa_change)  # Transpose so we calculate the per day change magnitude
	hefa_change_mag = np.linalg.norm(hefa_change, axis=0)  # Calculate the magnitude
	hefa_values = hefa_change_mag * hefa_change  # Calculate the data we will work with
	return hefa_values

# Retrieving formatted data for HEFA
def hefa_batch_1_values():
	return hefa_batch_values(hefa_dat[0])

def hefa_batch_2_values():
	return hefa_batch_values(hefa_dat[1])

def hefa_batch_3_values():
	return hefa_batch_values(hefa_dat[2])

def hefa_batch_4_values():
	return hefa_batch_values(hefa_dat[3])

def hefa_batch_5_values():
	return hefa_batch_values(hefa_dat[4])


# Format required NOBL entries___________________________________________________________________________
iyk_dat = iyk_fu(training_data)

# Daily change for IYK batches 1 to 5
def iyk_batch_values(iyk_dat):
	iyk_open_stop = pd.DataFrame(iyk_dat)  # Define the value we are subtracting from
	iyk_open_start = pd.DataFrame(iyk_dat).shift(periods=1)  # Define the value we are subtracting
	iyk_stop = iyk_open_stop.to_numpy()  # Convert to array
	iyk_start = iyk_open_start.to_numpy()  # Convert to array
	iyk_start[np.isnan(iyk_start)] = np.mean(iyk_start[np.logical_not(np.isnan(iyk_start))])  # Remove NaN values
	iyk_change = iyk_stop - iyk_start  # Calculate difference
	iyk_change = np.transpose(iyk_change)  # Transpose so we calculate the per day change magnitude
	iyk_change_mag = np.linalg.norm(iyk_change, axis=0)  # Calculate the magnitude
	iyk_values = iyk_change_mag * iyk_change  # Calculate the data we will work with
	return iyk_values

# Retrieving formatted data for IYK
def iyk_batch_1_values():
	return iyk_batch_values(iyk_dat[0])

def iyk_batch_2_values():
	return iyk_batch_values(iyk_dat[1])

def iyk_batch_3_values():
	return iyk_batch_values(iyk_dat[2])

def iyk_batch_4_values():
	return iyk_batch_values(iyk_dat[3])

def iyk_batch_5_values():
	return iyk_batch_values(iyk_dat[4])


# Format required NOBL entries___________________________________________________________________________
usoi_dat = usoi_fu(training_data)

# Daily change for USOI batches 1 to 5
def usoi_batch_values(usoi_dat):
	usoi_open_stop = pd.DataFrame(usoi_dat)  # Define the value we are subtracting from
	usoi_open_start = pd.DataFrame(usoi_dat).shift(periods=1)  # Define the value we are subtracting
	usoi_stop = usoi_open_stop.to_numpy()  # Convert to array
	usoi_start = usoi_open_start.to_numpy()  # Convert to array
	usoi_start[np.isnan(usoi_start)] = np.mean(usoi_start[np.logical_not(np.isnan(usoi_start))])  # Remove NaN values
	usoi_change = usoi_stop - usoi_start  # Calculate difference
	usoi_change = np.transpose(usoi_change)  # Transpose so we calculate the per day change magnitude
	usoi_change_mag = np.linalg.norm(usoi_change, axis=0)  # Calculate the magnitude
	usoi_values = usoi_change_mag * usoi_change  # Calculate the data we will work with
	return usoi_values

# Retrieving formatted data for USOI
def usoi_batch_1_values():
	return usoi_batch_values(usoi_dat[0])

def usoi_batch_2_values():
	return usoi_batch_values(usoi_dat[1])

def usoi_batch_3_values():
	return usoi_batch_values(usoi_dat[2])

def usoi_batch_4_values():
	return usoi_batch_values(usoi_dat[3])

def usoi_batch_5_values():
	return usoi_batch_values(usoi_dat[4])


# Format required NOBL entries___________________________________________________________________________
xlf_dat = xlf_fu(training_data)

# Daily change for XLF batches 1 to 5
def xlf_batch_values(xlf_dat):
	xlf_open_stop = pd.DataFrame(xlf_dat)  # Define the value we are subtracting from
	xlf_open_start = pd.DataFrame(xlf_dat).shift(periods=1)  # Define the value we are subtracting
	xlf_stop = xlf_open_stop.to_numpy()  # Convert to array
	xlf_start = xlf_open_start.to_numpy()  # Convert to array
	xlf_start[np.isnan(xlf_start)] = np.mean(xlf_start[np.logical_not(np.isnan(xlf_start))])  # Remove NaN values
	xlf_change = xlf_stop - xlf_start  # Calculate difference
	xlf_change = np.transpose(xlf_change)  # Transpose so we calculate the per day change magnitude
	xlf_change_mag = np.linalg.norm(xlf_change, axis=0)  # Calculate the magnitude
	xlf_values = xlf_change_mag * xlf_change  # Calculate the data we will work with
	return xlf_values

# Retrieving formatted data for XLF
def xlf_batch_1_values():
	return xlf_batch_values(xlf_dat[0])

def xlf_batch_2_values():
	return xlf_batch_values(xlf_dat[1])

def xlf_batch_3_values():
	return xlf_batch_values(xlf_dat[2])

def xlf_batch_4_values():
	return xlf_batch_values(xlf_dat[3])

def xlf_batch_5_values():
	return xlf_batch_values(xlf_dat[4])


# Format required NOBL entries___________________________________________________________________________
xly_dat = xly_fu(training_data)

# Daily change for XLY batches 1 to 5
def xly_batch_values(xly_dat):
	xly_open_stop = pd.DataFrame(xly_dat)  # Define the value we are subtracting from
	xly_open_start = pd.DataFrame(xly_dat).shift(periods=1)  # Define the value we are subtracting
	xly_stop = xly_open_stop.to_numpy()  # Convert to array
	xly_start = xly_open_start.to_numpy()  # Convert to array
	xly_start[np.isnan(xly_start)] = np.mean(xly_start[np.logical_not(np.isnan(xly_start))])  # Remove NaN values
	xly_change = xly_stop - xly_start  # Calculate difference
	xly_change = np.transpose(xly_change)  # Transpose so we calculate the per day change magnitude
	xly_change_mag = np.linalg.norm(xly_change, axis=0)  # Calculate the magnitude
	xly_values = xly_change_mag * xly_change  # Calculate the data we will work with
	return xly_values

# Retrieving formatted data for XLY
def xly_batch_1_values():
	return xly_batch_values(xly_dat[0])

def xly_batch_2_values():
	return xly_batch_values(xly_dat[1])

def xly_batch_3_values():
	return xly_batch_values(xly_dat[2])

def xly_batch_4_values():
	return xly_batch_values(xly_dat[3])

def xly_batch_5_values():
	return xly_batch_values(xly_dat[4])


# Format required NOBL entries___________________________________________________________________________
xlv_dat = xlv_fu(training_data)

# Daily change for XLV batches 1 to 5
def xlv_batch_values(xlv_dat):
	xlv_open_stop = pd.DataFrame(xlv_dat)  # Define the value we are subtracting from
	xlv_open_start = pd.DataFrame(xlv_dat).shift(periods=1)  # Define the value we are subtracting
	xlv_stop = xlv_open_stop.to_numpy()  # Convert to array
	xlv_start = xlv_open_start.to_numpy()  # Convert to array
	xlv_start[np.isnan(xlv_start)] = np.mean(xlv_start[np.logical_not(np.isnan(xlv_start))])  # Remove NaN values
	xlv_change = xlv_stop - xlv_start  # Calculate difference
	xlv_change = np.transpose(xlv_change)  # Transpose so we calculate the per day change magnitude
	xlv_change_mag = np.linalg.norm(xlv_change, axis=0)  # Calculate the magnitude
	xlv_values = xlv_change_mag * xlv_change  # Calculate the data we will work with
	return xlv_values

# Retrieving formatted data for XLV
def xlv_batch_1_values():
	return xlv_batch_values(xlv_dat[0])

def xlv_batch_2_values():
	return xlv_batch_values(xlv_dat[1])

def xlv_batch_3_values():
	return xlv_batch_values(xlv_dat[2])

def xlv_batch_4_values():
	return xlv_batch_values(xlv_dat[3])

def xlv_batch_5_values():
	return xlv_batch_values(xlv_dat[4])


# Format required NOBL entries___________________________________________________________________________
eem_dat = eem_fu(training_data)

# Daily change for EEM batches 1 to 5
def eem_batch_values(eem_dat):
	eem_open_stop = pd.DataFrame(eem_dat)  # Define the value we are subtracting from
	eem_open_start = pd.DataFrame(eem_dat).shift(periods=1)  # Define the value we are subtracting
	eem_stop = eem_open_stop.to_numpy()  # Convert to array
	eem_start = eem_open_start.to_numpy()  # Convert to array
	eem_start[np.isnan(eem_start)] = np.mean(eem_start[np.logical_not(np.isnan(eem_start))])  # Remove NaN values
	eem_change = eem_stop - eem_start  # Calculate difference
	eem_change = np.transpose(eem_change)  # Transpose so we calculate the per day change magnitude
	eem_change_mag = np.linalg.norm(eem_change, axis=0)  # Calculate the magnitude
	eem_values = eem_change_mag * eem_change  # Calculate the data we will work with
	return eem_values

# Retrieving formatted data for EEM
def eem_batch_1_values():
	return eem_batch_values(eem_dat[0])

def eem_batch_2_values():
	return eem_batch_values(eem_dat[1])

def eem_batch_3_values():
	return eem_batch_values(eem_dat[2])

def eem_batch_4_values():
	return eem_batch_values(eem_dat[3])

def eem_batch_5_values():
	return eem_batch_values(eem_dat[4])


# Format required NOBL entries___________________________________________________________________________
veu_dat = veu_fu(training_data)

# Daily change for VEU batches 1 to 5
def veu_batch_values(veu_dat):
	veu_open_stop = pd.DataFrame(veu_dat)  # Define the value we are subtracting from
	veu_open_start = pd.DataFrame(veu_dat).shift(periods=1)  # Define the value we are subtracting
	veu_stop = veu_open_stop.to_numpy()  # Convert to array
	veu_start = veu_open_start.to_numpy()  # Convert to array
	veu_start[np.isnan(veu_start)] = np.mean(veu_start[np.logical_not(np.isnan(veu_start))])  # Remove NaN values
	veu_change = veu_stop - veu_start  # Calculate difference
	veu_change = np.transpose(veu_change)  # Transpose so we calculate the per day change magnitude
	veu_change_mag = np.linalg.norm(veu_change, axis=0)  # Calculate the magnitude
	veu_values = veu_change_mag * veu_change  # Calculate the data we will work with
	return veu_values

# Retrieving formatted data for VEU
def veu_batch_1_values():
	return veu_batch_values(veu_dat[0])

def veu_batch_2_values():
	return veu_batch_values(veu_dat[1])

def veu_batch_3_values():
	return veu_batch_values(veu_dat[2])

def veu_batch_4_values():
	return veu_batch_values(veu_dat[3])

def veu_batch_5_values():
	return veu_batch_values(veu_dat[4])


# Format required NOBL entries___________________________________________________________________________
vfh_dat = vfh_fu(training_data)

# Daily change for VFH batches 1 to 5
def vfh_batch_values(vfh_dat):
	vfh_open_stop = pd.DataFrame(vfh_dat)  # Define the value we are subtracting from
	vfh_open_start = pd.DataFrame(vfh_dat).shift(periods=1)  # Define the value we are subtracting
	vfh_stop = vfh_open_stop.to_numpy()  # Convert to array
	vfh_start = vfh_open_start.to_numpy()  # Convert to array
	vfh_start[np.isnan(vfh_start)] = np.mean(vfh_start[np.logical_not(np.isnan(vfh_start))])  # Remove NaN values
	vfh_change = vfh_stop - vfh_start  # Calculate difference
	vfh_change = np.transpose(vfh_change)  # Transpose so we calculate the per day change magnitude
	vfh_change_mag = np.linalg.norm(vfh_change, axis=0)  # Calculate the magnitude
	vfh_values = vfh_change_mag * vfh_change  # Calculate the data we will work with
	return vfh_values

# Retrieving formatted data for VFH
def vfh_batch_1_values():
	return vfh_batch_values(vfh_dat[0])

def vfh_batch_2_values():
	return vfh_batch_values(vfh_dat[1])

def vfh_batch_3_values():
	return vfh_batch_values(vfh_dat[2])

def vfh_batch_4_values():
	return vfh_batch_values(vfh_dat[3])

def vfh_batch_5_values():
	return vfh_batch_values(vfh_dat[4])


# Format required NOBL entries___________________________________________________________________________
kre_dat = kre_fu(training_data)

# Daily change for KRE batches 1 to 5
def kre_batch_values(kre_dat):
	kre_open_stop = pd.DataFrame(kre_dat)  # Define the value we are subtracting from
	kre_open_start = pd.DataFrame(kre_dat).shift(periods=1)  # Define the value we are subtracting
	kre_stop = kre_open_stop.to_numpy()  # Convert to array
	kre_start = kre_open_start.to_numpy()  # Convert to array
	kre_start[np.isnan(kre_start)] = np.mean(kre_start[np.logical_not(np.isnan(kre_start))])  # Remove NaN values
	kre_change = kre_stop - kre_start  # Calculate difference
	kre_change = np.transpose(kre_change)  # Transpose so we calculate the per day change magnitude
	kre_change_mag = np.linalg.norm(kre_change, axis=0)  # Calculate the magnitude
	kre_values = kre_change_mag * kre_change  # Calculate the data we will work with
	return kre_values

# Retrieving formatted data for KRE
def kre_batch_1_values():
	return kre_batch_values(kre_dat[0])

def kre_batch_2_values():
	return kre_batch_values(kre_dat[1])

def kre_batch_3_values():
	return kre_batch_values(kre_dat[2])

def kre_batch_4_values():
	return kre_batch_values(kre_dat[3])

def kre_batch_5_values():
	return kre_batch_values(kre_dat[4])


# Format required NOBL entries___________________________________________________________________________
iyf_dat = iyf_fu(training_data)

# Daily change for IYF batches 1 to 5
def iyf_batch_values(iyf_dat):
	iyf_open_stop = pd.DataFrame(iyf_dat)  # Define the value we are subtracting from
	iyf_open_start = pd.DataFrame(iyf_dat).shift(periods=1)  # Define the value we are subtracting
	iyf_stop = iyf_open_stop.to_numpy()  # Convert to array
	iyf_start = iyf_open_start.to_numpy()  # Convert to array
	iyf_start[np.isnan(iyf_start)] = np.mean(iyf_start[np.logical_not(np.isnan(iyf_start))])  # Remove NaN values
	iyf_change = iyf_stop - iyf_start  # Calculate difference
	iyf_change = np.transpose(iyf_change)  # Transpose so we calculate the per day change magnitude
	iyf_change_mag = np.linalg.norm(iyf_change, axis=0)  # Calculate the magnitude
	iyf_values = iyf_change_mag * iyf_change  # Calculate the data we will work with
	return iyf_values

# Retrieving formatted data for IYF
def iyf_batch_1_values():
	return iyf_batch_values(iyf_dat[0])

def iyf_batch_2_values():
	return iyf_batch_values(iyf_dat[1])

def iyf_batch_3_values():
	return iyf_batch_values(iyf_dat[2])

def iyf_batch_4_values():
	return iyf_batch_values(iyf_dat[3])

def iyf_batch_5_values():
	return iyf_batch_values(iyf_dat[4])


# Format required NOBL entries___________________________________________________________________________
fncl_dat = fncl_fu(training_data)

# Daily change for FNCL batches 1 to 5
def fncl_batch_values(fncl_dat):
	fncl_open_stop = pd.DataFrame(fncl_dat)  # Define the value we are subtracting from
	fncl_open_start = pd.DataFrame(fncl_dat).shift(periods=1)  # Define the value we are subtracting
	fncl_stop = fncl_open_stop.to_numpy()  # Convert to array
	fncl_start = fncl_open_start.to_numpy()  # Convert to array
	fncl_start[np.isnan(fncl_start)] = np.mean(fncl_start[np.logical_not(np.isnan(fncl_start))])  # Remove NaN values
	fncl_change = fncl_stop - fncl_start  # Calculate difference
	fncl_change = np.transpose(fncl_change)  # Transpose so we calculate the per day change magnitude
	fncl_change_mag = np.linalg.norm(fncl_change, axis=0)  # Calculate the magnitude
	fncl_values = fncl_change_mag * fncl_change  # Calculate the data we will work with
	return fncl_values

# Retrieving formatted data for FNCL
def fncl_batch_1_values():
	return fncl_batch_values(fncl_dat[0])

def fncl_batch_2_values():
	return fncl_batch_values(fncl_dat[1])

def fncl_batch_3_values():
	return fncl_batch_values(fncl_dat[2])

def fncl_batch_4_values():
	return fncl_batch_values(fncl_dat[3])

def fncl_batch_5_values():
	return fncl_batch_values(fncl_dat[4])


# Format required NOBL entries___________________________________________________________________________
qqq_dat = qqq_fu(training_data)

# Daily change for QQQ batches 1 to 5
def qqq_batch_values(qqq_dat):
	qqq_open_stop = pd.DataFrame(qqq_dat)  # Define the value we are subtracting from
	qqq_open_start = pd.DataFrame(qqq_dat).shift(periods=1)  # Define the value we are subtracting
	qqq_stop = qqq_open_stop.to_numpy()  # Convert to array
	qqq_start = qqq_open_start.to_numpy()  # Convert to array
	qqq_start[np.isnan(qqq_start)] = np.mean(qqq_start[np.logical_not(np.isnan(qqq_start))])  # Remove NaN values
	qqq_change = qqq_stop - qqq_start  # Calculate difference
	qqq_change = np.transpose(qqq_change)  # Transpose so we calculate the per day change magnitude
	qqq_change_mag = np.linalg.norm(qqq_change, axis=0)  # Calculate the magnitude
	qqq_values = qqq_change_mag * qqq_change  # Calculate the data we will work with
	return qqq_values

# Retrieving formatted data for QQQ
def qqq_batch_1_values():
	return qqq_batch_values(qqq_dat[0])

def qqq_batch_2_values():
	return qqq_batch_values(qqq_dat[1])

def qqq_batch_3_values():
	return qqq_batch_values(qqq_dat[2])

def qqq_batch_4_values():
	return qqq_batch_values(qqq_dat[3])

def qqq_batch_5_values():
	return qqq_batch_values(qqq_dat[4])


# Format required NOBL entries___________________________________________________________________________
spy_dat = spy_fu(training_data)

# Daily change for SPY batches 1 to 5
def spy_batch_values(spy_dat):
	spy_open_stop = pd.DataFrame(spy_dat)  # Define the value we are subtracting from
	spy_open_start = pd.DataFrame(spy_dat).shift(periods=1)  # Define the value we are subtracting
	spy_stop = spy_open_stop.to_numpy()  # Convert to array
	spy_start = spy_open_start.to_numpy()  # Convert to array
	spy_start[np.isnan(spy_start)] = np.mean(spy_start[np.logical_not(np.isnan(spy_start))])  # Remove NaN values
	spy_change = spy_stop - spy_start  # Calculate difference
	spy_change = np.transpose(spy_change)  # Transpose so we calculate the per day change magnitude
	spy_change_mag = np.linalg.norm(spy_change, axis=0)  # Calculate the magnitude
	spy_values = spy_change_mag * spy_change  # Calculate the data we will work with
	return spy_values

# Retrieving formatted data for SPY
def spy_batch_1_values():
	return spy_batch_values(spy_dat[0])

def spy_batch_2_values():
	return spy_batch_values(spy_dat[1])

def spy_batch_3_values():
	return spy_batch_values(spy_dat[2])

def spy_batch_4_values():
	return spy_batch_values(spy_dat[3])

def spy_batch_5_values():
	return spy_batch_values(spy_dat[4])


# Format required NOBL entries___________________________________________________________________________
vti_dat = vti_fu(training_data)

# Daily change for VTI batches 1 to 5
def vti_batch_values(vti_dat):
	vti_open_stop = pd.DataFrame(vti_dat)  # Define the value we are subtracting from
	vti_open_start = pd.DataFrame(vti_dat).shift(periods=1)  # Define the value we are subtracting
	vti_stop = vti_open_stop.to_numpy()  # Convert to array
	vti_start = vti_open_start.to_numpy()  # Convert to array
	vti_start[np.isnan(vti_start)] = np.mean(vti_start[np.logical_not(np.isnan(vti_start))])  # Remove NaN values
	vti_change = vti_stop - vti_start  # Calculate difference
	vti_change = np.transpose(vti_change)  # Transpose so we calculate the per day change magnitude
	vti_change_mag = np.linalg.norm(vti_change, axis=0)  # Calculate the magnitude
	vti_values = vti_change_mag * vti_change  # Calculate the data we will work with
	return vti_values

# Retrieving formatted data for VTI
def vti_batch_1_values():
	return vti_batch_values(vti_dat[0])

def vti_batch_2_values():
	return vti_batch_values(vti_dat[1])

def vti_batch_3_values():
	return vti_batch_values(vti_dat[2])

def vti_batch_4_values():
	return vti_batch_values(vti_dat[3])

def vti_batch_5_values():
	return vti_batch_values(vti_dat[4])


# Format required NOBL entries___________________________________________________________________________
itot_dat = itot_fu(training_data)

# Daily change for ITOT batches 1 to 5
def itot_batch_values(itot_dat):
	itot_open_stop = pd.DataFrame(itot_dat)  # Define the value we are subtracting from
	itot_open_start = pd.DataFrame(itot_dat).shift(periods=1)  # Define the value we are subtracting
	itot_stop = itot_open_stop.to_numpy()  # Convert to array
	itot_start = itot_open_start.to_numpy()  # Convert to array
	itot_start[np.isnan(itot_start)] = np.mean(itot_start[np.logical_not(np.isnan(itot_start))])  # Remove NaN values
	itot_change = itot_stop - itot_start  # Calculate difference
	itot_change = np.transpose(itot_change)  # Transpose so we calculate the per day change magnitude
	itot_change_mag = np.linalg.norm(itot_change, axis=0)  # Calculate the magnitude
	itot_values = itot_change_mag * itot_change  # Calculate the data we will work with
	return itot_values

# Retrieving formatted data for ITOT
def itot_batch_1_values():
	return itot_batch_values(itot_dat[0])

def itot_batch_2_values():
	return itot_batch_values(itot_dat[1])

def itot_batch_3_values():
	return itot_batch_values(itot_dat[2])

def itot_batch_4_values():
	return itot_batch_values(itot_dat[3])

def itot_batch_5_values():
	return itot_batch_values(itot_dat[4])


# Format required NOBL entries___________________________________________________________________________
xlk_dat = xlk_fu(training_data)

# Daily change for XLK batches 1 to 5
def xlk_batch_values(xlk_dat):
	xlk_open_stop = pd.DataFrame(xlk_dat)  # Define the value we are subtracting from
	xlk_open_start = pd.DataFrame(xlk_dat).shift(periods=1)  # Define the value we are subtracting
	xlk_stop = xlk_open_stop.to_numpy()  # Convert to array
	xlk_start = xlk_open_start.to_numpy()  # Convert to array
	xlk_start[np.isnan(xlk_start)] = np.mean(xlk_start[np.logical_not(np.isnan(xlk_start))])  # Remove NaN values
	xlk_change = xlk_stop - xlk_start  # Calculate difference
	xlk_change = np.transpose(xlk_change)  # Transpose so we calculate the per day change magnitude
	xlk_change_mag = np.linalg.norm(xlk_change, axis=0)  # Calculate the magnitude
	xlk_values = xlk_change_mag * xlk_change  # Calculate the data we will work with
	return xlk_values

# Retrieving formatted data for XLK
def xlk_batch_1_values():
	return xlk_batch_values(xlk_dat[0])

def xlk_batch_2_values():
	return xlk_batch_values(xlk_dat[1])

def xlk_batch_3_values():
	return xlk_batch_values(xlk_dat[2])

def xlk_batch_4_values():
	return xlk_batch_values(xlk_dat[3])

def xlk_batch_5_values():
	return xlk_batch_values(xlk_dat[4])

