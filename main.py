from functions import *

index = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10',
         '11', '12', '13', '14', '15', "16", '17', '18', '19', '20',
         '21', '22', '23', '24', '25', '26', '27']

area = ["Cherkasy", "Chernihiv", "Chernivci", "Crimea", "Dnipropetrovs'k", "Donets'k", "Ivano-Frankivs'k", "Kharkiv",
          "Kherson", "Khmel'nyts'kyy", "Kiev", "Kiev City", "Kirovohrad", "Luhans'k", "L'viv", "Mykolayiv", "Odessa",
          "Poltava", "Rivne", "Sevastopol'", "Sumy", "Ternopil'", "Transcarpathia", "Vinnytsya", "Volyn",
          "Zaporizhzhya", "Zhytomyr"]

download_index = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10',
                  '11', '12', '13', '14', '15', '16', '17', '18', '19', '20',
                  '21', '22', '23', '24', '25', '26', '27']

area.sort()
delete()
print area

i = 0
while i < len(index):
    download_index[i] = download(index[i], area[i])
    i += 1

i = 0
while i < len(index):
    print(area[i] + ":" + os.linesep + str(max_value("%s.csv" % (index[i] + " " + area[i] + " " + download_index[i]), 2007)) + os.linesep)
    i += 1

i = 0
while i < len(index):
    print(area[i] + ":" + os.linesep + str(min_value("%s.csv" % (index[i] + " " + area[i] + " " + download_index[i]), 2007)) + os.linesep)
    i += 1

i = 0
while i < len(index):
    print(area[i] + ":" + os.linesep
          + str(extreme_drought("%s.csv" % (index[i] + " " + area[i] + " " + download_index[i]))) + os.linesep)
    i += 1

i = 0
while i < len(index):
    print(area[i] + ":" + os.linesep
          + str(tepid_drought("%s.csv" % (index[i] + " " + area[i] + " " + download_index[i]))) + os.linesep)
    i += 1

#addition
print("--------------------------------")
print(str(years_drought_more_than_third_year("%s.csv" % (index[15] + " " + area[15] + " " + download_index[15]), "Lugansk")) + os.linesep)
