from Read_XYZ.main import Read_xyz as r_xyz

config = ['A', 'NA', 'NA']
# config = ['A', '10', '100']

demo = r_xyz('./Data/1A6N.pdb', config)
# demo = r_xyz('./Data/1APS.pdb', config)

demo.matching_lines()
demo.save_matching_lines('./1A6N_line.txt')

demo.extract_xyz()
demo.save_extract_xyz('./1A6N_xyz.txt')

# VDWr:Van der Waals radius or IEP:Isoelectric point
demo.extract_xyz_with_weight('VDWr')
demo.save_extract_xyz('./1A6N_xyz_VDWr.txt')
