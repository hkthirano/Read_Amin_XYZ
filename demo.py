from Read_XYZ.main import Read_xyz as r_xyz

config = ['A', 'NA', 'NA']
# config = ['A', '10', '100']

demo = r_xyz('./Data/1A6N.pdb', config)
# demo = r_xyz('./Data/1A6N.pdb', config)

demo.matching_lines()

demo.save_matching_lines('./demo_line.txt')

demo.extract_xyz()

demo.save_extract_xyz('./demo_xyz.txt')
