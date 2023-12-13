def time_converter(time: str):
    """
    This function takes time string in 12-hours format and converts it to 24-hours\n
    Example: "12:30 p.m." -> "12:30"; "9:15 p.m." -> "21:15"
    :param time: time string in 12-hours format
    :return: time str in 24-hours format
    """
    # split time into the time itself and its part of the 24-hrs (AM / PM)
    time, indicator = time.split()
    hours, minutes = map(int, time.split(':'))

    # if it is PM - just add 12 to hrs. Exception - when it is 12(midday) already
    if indicator == 'p.m.':
        if hours == 12:
            result_time = "%.2d:%.2d" % (hours, minutes)
        else:
            result_time = "%.2d:%.2d" % (hours + 12, minutes)
    # just format the hours if it is AM
    else:
        result_time = "%.2d:%.2d" % (hours, minutes)

    return result_time
