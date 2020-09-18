second = int(input("Number of a second: "))

second_minute = 60
second_hour = 3600
second_day = 86400

minute = second/second_minute
second = second%second_minute

hour = second/second_hour
second = second%second_hour

day = second/second_day
second = second%second_day

print("The equivalent amount of time: ","%d:%02d:%02d:%02d."%(minute,hour,day,second))