# Wrapper for JSDoc
import sys
import platform
from subprocess import call

def invokeJSDoc(File):
	cmd = ['jsdoc', File, '-d', 'doc']
	if platform.system() == 'Windows': cmd[0] = 'jsdoc.cmd'
	print('JSDoc ~ Documenting JavaScript file: {0}'.format(File))
	call(cmd)

invokeJSDoc(sys.argv[1])
