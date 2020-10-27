import re
mc_file = open('mc115L.iv', 'r')
mc_mesh = mc_file.readlines()
mc_mesh = mc_mesh.split(',')
for n in mc_file.read():
     if n.startswith('point'):
        print('point')
#mc_mesh = re.sub(r'(?m)^\*.*\n?', '', mc_mesh)
#tokens = re(input,'(.*)point\s+\[([^\]]*)\](.*)coordIndex\s+\[([\d\s\,\n\r\.-]*)\](.*)','tokens')
#mc_mesh = re.sub('{', '', mc_mesh)
#mc_mesh = mc_mesh.split(',')
print(mc_mesh[0])

#mc_coord_file = open('SCS_mc1.dat', 'r')
#mc_coord = mc_coord_file.read().splitlines()

#lines = csv.reader(open(filename, newline=''), delimiter=',', quotechar='|')