# Wrapper for YUI Compressor
import sys
import re
import platform
from subprocess import call

def invokeYUICompressor(File):
	pattern = re.compile('services|app')
	out = re.sub('.js', '.min.js', File)
	out = re.sub('.css', '.min.css', File)
	cmd = ['yuicompressor']
	if platform.system() == 'Windows': cmd[0] = 'yuicompressor.cmd'
	cmd.append(File)

	if pattern.match(File):
		cmd.append('--nomunge')
		cmd.append('--preserve-semi')

	cmd.append('-o')
	cmd.append(out)
	print('YUI Compressor ~ Generating {0} -> {1}'.format(File, out));
	call(cmd)

invokeYUICompressor(sys.argv[1])
