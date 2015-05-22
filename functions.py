from time import *
import pandas as pd
import urllib2
import os
import glob
def download(index, area):
    url = "http://www.star.nesdis.noaa.gov/smcd/emb/vci/gvix/G04/ts_L1/ByProvince/Mean/L1_Mean_UKR.R%s.txt" % index
    vhi_url = urllib2.urlopen(url)
    time = strftime("%Y-%m-%d.%H-%M-%S", gmtime())
    out = open('Downloads/%s.csv' % (index + ' ' + area + ' ' + time), 'wb')
    out.write(vhi_url.read())
    out.close()
    return time

def read_in_frame(file_name):
    df = pd.read_csv("Downloads/%s" % file_name, index_col=False, header=1)
    return df

def output(df):
    print list(df.columns.values)

def sort(area):
    area.sort()

def max_value(file_name, year):
    df = read_in_frame(file_name)
    yr = df[df['year'] == year]
    print "A max value VHI in this region was in: %s" % year
    maximum = max(yr.VHI)
    return maximum

def min_value(file_name, year):
    df = read_in_frame(file_name)
    yr = df[df['year'] == year]
    print "A min value VHI in this region was in: %s" % year
    minimum = min(yr.VHI)
    return minimum

def drought(file_name, percent1, percent2):
    df = read_in_frame(file_name)
    interval = df[(df['VHI'] > percent1) & (df['VHI'] < percent2)]
    return interval

def extreme_drought(file_name):
    extr_drought = drought(file_name, 0, 15)
    print "Extreme drought was in:"
    return extr_drought

def tepid_drought(file_name):
    tep_drought = drought(file_name, 15, 35)
    print "Tepid drought was in:"
    return tep_drought
	
def years_drought_more_than_third_year(file_name, Regname):      #addition
    df = read_in_frame(file_name)
    print("Lugans'k:")
    print ("Years when there was a tepid drought more than third of the year (15% < VHI < 35%) "
           "in this region was in:" + os.linesep)
    year = 1982
    while year < 2016:
        yr = df[df['year'] == year]
        test = yr[(yr['VHI'] > 15) & (yr['VHI'] < 35)]
        check = len(test.index)
        if check > 17:   #17
            print (year)
            print(os.linesep)
        year += 1

def delete():
    for files in glob.glob('Downloads/*.csv'):
        os.remove(files)

