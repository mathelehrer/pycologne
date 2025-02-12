import profile
import time
@profile
def f():
    time.sleep(0.1)
    (g(1),g(2))
    g(3)

@profile
def g(n):
    if n==0:
        return
    time.sleep(0.1)
    g(n-1)

f()


# pipenv run python -m line_profiler  ./line_profile |less
# pipenv run kernprof -o ./line_profile -l -p ./e1.py --prof-imports ./e1.py
# github.com/pyutils/line_profiler