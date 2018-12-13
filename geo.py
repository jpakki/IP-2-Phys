import pygeoip
import argparse

gi = pygeoip.GeoIP('./opt/GeoIP/Geo.dat')

def printRecord(tgt):
    rec = gi.record_by_name(tgt)
    if(rec == None):
        print('[*] Target: ' + tgt + ' Unable to Geo-locate.')
        return
    city = rec['city']
    region = rec['region_code']
    country = rec['country_name']
    longitude = rec['longitude']
    latitude = rec['latitude']
    time_zone = rec['time_zone']
    print('[*] Target: ' + tgt + ' Geo-located.')
    print('[+] ' + str(city) + ', ' + str(country))
    print('[+] Time Zone: ' + str(time_zone))
    print('[+] ' + 'Latitude ' + str(latitude) + ', Longitude: ' + str(longitude))

def main():
    parser = argparse.ArgumentParser(usage='-ip <IP Addresses>')
    parser.add_argument('-ip', dest='targetIP', type=str, help='specify target IP address(es) separated by comma')
    args = parser.parse_args()

    targetIP = str(args.targetIP).split(',')
    for ip in targetIP:
        printRecord(ip)
        print('\n')
if __name__ == '__main__':
    main()
