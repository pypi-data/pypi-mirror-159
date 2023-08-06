from timeit import default_timer
from datetime import timedelta

class TicTecToc:
    MSG = '[TTT:{}] Elapsed time is'
    Temp_MSG = '[TTT:{}] Temp Elapsed time is'
    _timestamps: dict = None

    def __init__(self):
        self._timestamps = dict()

    def tic(self, name: str = 'default'):
        '''Start.'''
        if name not in self._timestamps:
            self._timestamps[name] = {
                'start': default_timer(),
                'elapsed': 0.
            }
        else: 
            self._timestamps[name]['start'] = default_timer()

    def tec(self, name: str = 'default', msg: str = None, tmp_msg: str = None, verbose: int = 0):
        '''End temp.'''
        if name not in self._timestamps:
            return None
        if self._timestamps[name] is None:
            return None
        if self._timestamps[name]['start'] is None:
            return None
        if msg is None:
            msg = TicTecToc.MSG
        if tmp_msg is None:
            tmp_msg = TicTecToc.Temp_MSG
            
        start = self._timestamps[name]['start']
        elapsed = self._timestamps[name]['elapsed']
        end = default_timer()
        temp_elapsed = end - start
        elapsed += temp_elapsed
        self._timestamps[name]['start'] = None
        self._timestamps[name]['elapsed'] = elapsed

        if verbose == 1: 
            print(msg.format(name), timedelta(seconds=elapsed), tmp_msg.format(name), timedelta(seconds=temp_elapsed))

        if verbose == 2: 
            print(msg.format+ timedelta(seconds=elapsed))

        if verbose == 3: 
            print(tmp_msg.format(name), timedelta(seconds=temp_elapsed))

        return temp_elapsed, elapsed

    def toc(self, name: str = "default", msg: str = None, verbose: int = 1):
        '''End.'''
        if name not in self._timestamps:
            return None
        if self._timestamps[name]['start'] is not None:
            self.tec(name)
        if msg is None:
            msg = TicTecToc.MSG

        elapsed = self._timestamps[name]['elapsed']
        if verbose == 1:
            print(msg.format(name), timedelta(seconds=elapsed))

        del self._timestamps[name]

        return elapsed

    def __enter__(self):
        self.start = default_timer()
    
    def __exit__(self, *args):
        msg = TicTecToc.MSG.replace(':{}','')
        self.end = default_timer()
        self.elapsed = self.end - self.start
        print(msg, timedelta(seconds=self.elapsed))