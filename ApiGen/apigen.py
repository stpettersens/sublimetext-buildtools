# Wrapper for ApiGen (PHP)
import sys
import platform
from subprocess import call

def invokeApiGen(File):
	cmd = ['apigen', '--quiet', '--source', File, '--destination', 'doc']
	if platform.system() == 'Windows': cmd[0] = 'apigen.cmd'
	print('ApiGen ~ Documenting PHP file: {0}'.format(File))
	call(cmd)

invokeApiGen(sys.argv[1])
