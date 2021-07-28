import os

os.makedirs('output/temp')

for audio in os.listdir("input/"):
	audioname=audio.replace(".webm","").replace(".mpeg","").replace(".flv","").replace(".mp4","").replace(".avi","").replace(".wmv","").replace(".aac","").replace(".m4a","").replace(".wma","").replace(".ogg","").replace(".mp3","").replace(".wav","")+'.wav'
	
	os.system('ffmpeg -i input/'+audio+' -f wav -bitexact -acodec pcm_s16le -ar 48000 -ac 2 output/temp/'+audioname)
	
	with open('output/temp/'+audioname,'rb') as f:
		header=str(f.read(71))
	
		data=f.read()
		
		rakiheader=b'\x52\x41\x4B\x49\x0A\x00\x00\x00\x57\x69\x6E\x20\x70\x63\x6D\x20\x48\x00\x00\x00\x48\x00\x00\x00\x02\x00\x00\x00\x03\x00\x00\x00\x66\x6D\x74\x20\x38\x00\x00\x00\x10\x00\x00\x00\x64\x61\x74\x61\x48\x00\x00\x00\x74\xAE\x14\x02\x01\x00\x02\x00\x80\xBB\x00\x00\x00\xEE\x02\x00\x04\x00\x10'
	
	wavckd=open('output/'+audioname+'.ckd','wb')
	
	wavckd.write(rakiheader+data)
	wavckd.close()
	
	os.remove('output/temp/'+audioname)
os.rmdir('output/temp')