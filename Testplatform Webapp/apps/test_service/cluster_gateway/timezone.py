from datetime import datetime



event_time = '2021-12-06 08:26:13+01:00'
year = '2021/12/06'
#event_time = '2021-12-06 08:26:13'

date_time_str = '18-09-2019 01:55:19'

#date_time_obj = datetime.strptime(date_time_str, '%d-%m-%y %H:%M:%S')

date_time_object = datetime.strptime(event_time, '%Y-%m-%d %H:%M:%S%z') 
#date_time_event = datetime.strptime(event_time, '%y-%m-%d %H:%M:%S')

print(date_time_object.strftime('%m/%d/%Y - %z'))