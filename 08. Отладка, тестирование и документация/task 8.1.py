import cProfile
import pstats
from functions_to_profile import load_files, read_database, get_id, get_user_data, generate_words


TASK_FUNCTIONS = ['load_files', 'read_database', 'get_id', 'get_user_data', 'generate_words']

def profile_functions():
    profiler = cProfile.Profile()
    profiler.enable()

    load_files()
    read_database()
    get_id()
    get_user_data()
    generate_words()

    profiler.disable()

    stats = pstats.Stats(profiler)
    total_time = stats.total_tt

    for func_name in TASK_FUNCTIONS:
        cumtime = next(v[3] for k, v in stats.stats.items() if func_name in k)
        time = round(cumtime, 4)
        percent = round((cumtime / total_time) * 100)
        print(f"{time}: {percent}%")


profile_functions()