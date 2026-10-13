def convertSeconds(total_seconds: int) -> str:
    hour = total_seconds//3600
    minute = (total_seconds % 3600)//60
    second = total_seconds % 60
    return "{:02d}:{:02d}:{:02d}".format(hour,minute,second)