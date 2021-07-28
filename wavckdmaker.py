from os import makedirs, listdir, remove, rmdir
from os.path import basename
from subprocess import Popen
makedirs('output/temp')
for audio in listdir("input/"):
	audioname = f'{basename(audio)}.wav'
	Popen(['ffmpeg'
		   '-i',
		   f'input/{audio}',
		   '-f',
		   'wav',
		   '-bitexact',
		   '-acodec',
		   'pcm_s16le',
		   '-ar',
		   '48000',
		   '-ac',
		   '2',
		   f'output/temp/{audioname}'])
	with open(f'output/temp/{audioname}','rb') as f:
		f.seek(71)
		data = f.read()
		rakiheader = b'\x52\x41\x4B\x49\x0A\x00\x00\x00\x57\x69\x6E\x20\x70\x63\x6D\x20\x48\x00\x00\x00\x48\x00\x00\x00\x02\x00\x00\x00\x03\x00\x00\x00\x66\x6D\x74\x20\x38\x00\x00\x00\x10\x00\x00\x00\x64\x61\x74\x61\x48\x00\x00\x00\x74\xAE\x14\x02\x01\x00\x02\x00\x80\xBB\x00\x00\x00\xEE\x02\x00\x04\x00\x10'
	wavckd = open(f'output/{audioname}.ckd', 'wb')
	wavckd.write(rakiheader + data)
	wavckd.close()
	
	remove(f'output/temp/{audioname}')
rmdir('output/temp')