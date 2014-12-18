# Wrapper for ApiGen All (PHP)
import sys
import platform
import os
import glob
from subprocess import call

def invokeApiGen(dir, out_dir):
	cmd = ['apigen', '--quiet', '--source', dir]
	if platform.system() == 'Windows': cmd[0] = 'apigen.cmd'
	os.chdir(dir)
	for php in glob.glob('*.php'):
		print('ApiGen ~ Documenting PHP file: {0}'.format(php))
	cmd.append('--destination')
	cmd.append(out_dir)
	call(cmd)

invokeApiGen(sys.argv[1], sys.argv[2])
