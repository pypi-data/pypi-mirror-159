import pytz
import datetime as dt

def msconverttz(ms, tz):
    """Pass a millisecond utc timestamp (ms) and a timezone information (tz) to return datetime.
        :param ms: Unix UTC timestamp in milliseconds
        :param tz: timezone info
        :return: timezone aware datetime
    """

    utc_datetime = dt.datetime.utcfromtimestamp(ms / 1000.)
    dt_final = utc_datetime.replace(tzinfo=pytz.timezone('UTC')).astimezone(tz)

    return dt_final