from pytube import YouTube


link = input('Masukkan Link Url Youtube : ')
YouTube(link)

#Cek Link 
print(f''' Terdownload
Title          :  {YouTube(link).title} 
Lama Video     : {round(YouTube(link).length / 60, 2)} Menit
Channel        : {YouTube(link).author}
Lokasi Di ==>
{YouTube(link).streams.get_highest_resolution().download()}''')