# Wrapper for JSDoc All
import sys
import platform
import os
import glob
from subprocess import call

def invokeJSDoc(dir, out_dir):
	cmd = ['jsdoc']
	if platform.system() == 'Windows': cmd[0] = 'jsdoc.cmd'
	os.chdir(dir)
	for js in glob.glob('*.js'):
		print('JSDoc ~ Documenting JavaScript file: {0}'.format(js))
		cmd.append(js)
	cmd.append('-d')
	cmd.append(out_dir + '/doc')
	call(cmd)

invokeJSDoc(sys.argv[1], sys.argv[2])
