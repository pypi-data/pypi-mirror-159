import cProfile
import pstats
import io

from pstats import SortKey


def profiler(function):
    """_summary_

    Args:
        function (_type_): _description_
    """
    def inner(*args, **kwargs):
        profile = cProfile.Profile()
        profile.enable()
        result = function(*args, **kwargs)
        profile.disable()
        stream = io.StringIO()
        sort_by = SortKey.CUMULATIVE
        stats = pstats.Stats(profile, stream=stream).sort_stats(sort_by)
        stats.print_stats()
        print(stream.getvalue())
        return result
    
    return inner


def timer(function):
    """_summary_
        TODO: finish implementation
    Args:
        function (_type_): _description_
    """
    pass