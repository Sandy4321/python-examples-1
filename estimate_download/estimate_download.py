def convert_unit_to_kB(data, unit):
    if unit == 'TB':
        return data * (2 ** 40 * 8) / (2 ** 10 * 8)
    elif unit == 'GB':
        return data * (2 ** 30 * 8) / (2 ** 10 * 8)
    elif unit == 'MB':
        return data * (2 ** 20 * 8) / (2 ** 10 * 8)
    elif unit == 'kB':
        return data
    
    if unit == 'Tb':
        return data * 2 ** 40 / 2 ** 10 / 8
    elif unit == 'Gb':
        return data * 2 ** 30 / 2 ** 10 / 8
    elif unit == 'Mb':
        return data * 2 ** 20 / 2 ** 10 / 8
    elif unit == 'kb':
        return data / 8.0

def convert_seconds(seconds):
    if seconds > 0:
        hours = int((seconds - seconds % 3600) / 3600)
        secleft = seconds - (hours * 3600)
        minutes = int((secleft - secleft % 60) / 60)
        seconds = (seconds % 3600) % 60
        h_label = 'hour' if hours == 1 else 'hours'
        m_label = 'minute' if minutes == 1 else 'minutes'
        s_label = 'second' if seconds == 1 else 'seconds'
        out = "%d %s, %d %s, %s %s" % (hours, h_label, minutes, m_label, seconds, s_label)
        return out

def download_time(size, size_unit, band, band_unit):
    band = convert_unit_to_kB(band, band_unit)
    size = convert_unit_to_kB(size, size_unit)
        
    #print size, ' / ', band, ' = ', float(size) / band, 's'
    return convert_seconds(float(size) / band)

print download_time(1024,'kB', 1, 'MB')
#>>> 0 hours, 0 minutes, 1 second

print download_time(1024,'kB', 1, 'Mb')
#>>> 0 hours, 0 minutes, 8 seconds  # 8.0 seconds is also acceptable

print download_time(13,'GB', 5.6, 'MB')
#>>> 0 hours, 39 minutes, 37.1428571429 seconds

print download_time(13,'GB', 5.6, 'Mb')
#>>> 5 hours, 16 minutes, 57.1428571429 seconds

print download_time(10,'MB', 2, 'kB')
#>>> 1 hour, 25 minutes, 20 seconds  # 20.0 seconds is also acceptable

print download_time(10,'MB', 2, 'kb')
#>>> 11 hours, 22 minutes, 40 seconds  # 40.0 seconds is also acceptable
