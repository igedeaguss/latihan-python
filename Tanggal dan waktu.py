import datetime
from time import strftime
#menampilkan tanggal dan waktu
#dengan format tanggal-bulan-tahun jam:menit:detik
print(strftime("%d-%m-%Y %H:%M:%S"))
#dengan format tanggal/bulan/tahun jam:menit:detik
print(strftime("%d/%m/%Y %H:%M:%S"))
#dengan format tahun-bulan-tanggal jam:menit:detik
print(datetime.datetime.now().replace(microsecond=0).isoformat(" "))
