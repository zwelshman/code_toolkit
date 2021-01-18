import fingertips_py as ftp 

phof = ftp.get_profile_by_name('public health outcomes framework') 
phof_meta = ftp.get_metadata_for_profile_as_dataframe(phof['Id']) 
indicator_meta = phof_meta[phof_meta['Indicator'].str.contains('Healthy')] 
print(phof_meta)