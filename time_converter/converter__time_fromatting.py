from datetime import datetime


def time_converter(time_in: str):
    """
    This function takes time string in 12-hours format and converts it to 24-hours\n
    Example: "12:30 p.m." -> "12:30"; "9:15 p.m." -> "21:15"
    :param time_in: time string in 12-hours format
    :return: time str in 24-hours format
    """
    time_in = time_in.replace('.', '').upper()      # %p takes only AM / PM, so we convert a.m./p.m. to it
    time = datetime.strptime(time_in, '%I:%M %p')       # here time is parsed, using %I, because it is a 12-hour directive
    result = str(time.strftime('%H:%M'))        # same as above, but %I is %H now - 24-hours directive
    return result
