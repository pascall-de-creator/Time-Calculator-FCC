def add_time(start, duration, day = None):
    day_map = {"Saturday": 0, "Sunday": 1, "Monday": 2, "Tuesday": 3, "Wednesday": 4, "Thursday": 5, "Friday": 6}
    # Getting Hour and mins from start string
    timely, midday = start.split()
    hour, minutes = timely.split(':')
    hour = int(hour)
    minutes = int(minutes)

    # Making it 24 hour format
    if midday == "PM":
        hour += 12

    # Getting Hour and mins from duration string
    duration_hour, duration_minutes = duration.split(':')
    duration_hour = int(duration_hour)
    duration_minutes = int(duration_minutes)

    # Calculating
    total_minutes = minutes + duration_minutes
    result_minutes = total_minutes % 60
    extra_hours = total_minutes // 60
    total_hour = hour + duration_hour + extra_hours

    # final hours as per 12 Hour clock
    result_hour = (total_hour % 24) % 12

    # Edge case
    if result_hour == 0:
        result_hour = 12
    result_hour = str(result_hour)

    # total days 24 hr 1 day
    total_day = (total_hour // 24)

    # determine (AM/PM)
    result_midday = ""
    if (total_hour % 24) <= 11:
        result_midday = "AM"
    else:
        result_midday = "PM"

    # Handling single digit minutes case
    if result_minutes <= 9:
        result_minutes = '0' + str(result_minutes)
    else:
        result_minutes = str(result_minutes)

    # returning
    time_stamp = result_hour + ":" + result_minutes + ' ' + result_midday
    if day == None:
        if total_day == 0:
            return time_stamp

        if total_day == 1:
            return time_stamp + ' (next day)'
        return time_stamp + ' (' + str(total_day) + ' days later)'
    else:
        result_day = (day_map[day.lower().capitalize()] + total_day) % 7
        for i, j in day_map.items():
            if j == result_day:
                result_day = i
                break

        if total_day == 0:
            return time_stamp + ', ' + result_day

        if total_day == 1:
            return time_stamp + ', ' + result_day + ' (next day)'

        return time_stamp + ', ' + result_day + ' (' + str(total_day) + ' days later)'