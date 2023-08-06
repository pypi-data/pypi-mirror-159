import string, random, hashlib
import os, logging
import time, datetime
from typing import Any, Dict, List

def get_random_string(l=10):
    letters = string.digits + string.ascii_letters
    return ''.join(random.choice(letters) for i in range(l))

class Logger:
    def __init__(self, log_fn='/tmp/log/log.log', timezone=8):
        def _timezone_converter(sec, what):
            localtime = datetime.datetime.utcnow() + datetime.timedelta(hours=timezone)
            return localtime.timetuple()
        logging.Formatter.converter = _timezone_converter
        log_dir = os.path.dirname(log_fn)
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)
        logging.basicConfig(
            level = logging.INFO,
            format = '%(asctime)s - %(levelname)s - [%(filename)s:%(lineno)d] - %(message)s'
        )
        self.logger = logging.getLogger(__name__)
        handler = logging.FileHandler(log_fn)
        console = logging.StreamHandler()
        handler.setLevel(logging.INFO)
        console.setLevel(logging.ERROR)
        formatter = logging.Formatter('%(asctime)s -  %(levelname)s - [%(filename)s:%(lineno)d] - %(message)s')
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)
        self.logger.addHandler(console)
        self.labels = 'none'
        self.info = self.logger.info
        self.warn = self.logger.warn
        self.error = self.logger.error

    def start_timer(self):
        self.curr = time.time()

    def get_runtime(self, format='s', log_metrics=False, labels=None):
        curr = time.time()
        t = (curr-self.curr)
        if labels is None:
            labels = self.labels
        if format=='s':
            pass
        elif format=='m':
            t = t/60
        elif format=='h':
            t = t/3600
        else:
            raise ValueError('wrong value for parameter "format"!')
        if log_metrics:
            self.info(f'runtime: {t}, labels: {labels}')
        return t

    def set_process_value(self, value, total=None, labels=None):
        if total is None:
            total = 100
        if labels is None:
            labels = self.labels
        self.info(f'the task is completed {value/total} percent, labels: {labels}')

    def set_labels(self, labels=None, file_name=None):
        if labels is None:
            labels = '/'.join(file_name.split('/')[-2:])
            labels = '.'.join(labels.split('.')[:-1])
            labels += f'-{get_random_string(5)}'
            labels = f'task%{labels}|'
        self.labels = labels

def get_md5(txt):
    md5hash = hashlib.md5(str(txt).encode('utf-8'))
    return md5hash.hexdigest()

class RoutineStep:
    def __init__(self, func, verify_func=None, name=None) -> None:
        self.name = name
        self.func = func
        self.verify_func = verify_func
        self.init_kwds = {}
        self.error_process = None

    def __call__(self,**kwds: Any) -> Dict:
        return self.func(**kwds)

    def set_error_process(self, func=None)->Dict:
        self.error_process=func

    def set_init(self, init_kwds):
        self.init_kwds = init_kwds

    def verify(self, **kwds: Any) -> bool:
        self.init_kwds.update(kwds)
        if self.verify_func is None:
            return True
        else:
            result = self.verify_func(**kwds)
            assert isinstance(result, bool), 'Result of verify function should be a bool type'
            return result

class Routine:
    def __init__(self, name, steps:List[RoutineStep]=[], verbose=False, logger=None) -> None:
        self.name = name
        self.steps = steps
        self.verbose = verbose
        self.logger = logger
        self.init_kwds = {}
        self.error_process = None

    def set_init(self, init_kwds):
        self.init_kwds = init_kwds
    
    def add(self, step):
        self.steps.append(step)
    
    def set_steps(self, steps):
        self.steps = steps

    def set_error_process(self, func=None):
        self.error_process = func

    def __call__(self, verbose=None) -> Any:
        verbose = verbose or self.verbose
        kwds = self.init_kwds
        if verbose:
            self.logger.info(f'start routine {self.name}')
        for i,step in enumerate(self.steps):
            name = step.name or i
            if verbose and self.logger:
                self.logger.info(f'start step {name}')
                start_time = time.time()
            kwds = step(**kwds)
            if verbose and self.logger:
                use_time = time.time()-start_time
                self.logger.info(f'step {name} is completed in {use_time} seconds')
                self.logger.info(f'result for step {name}: {kwds}')
            succeed = step.verify(**kwds)
            if not succeed:
                self.logger.error(f'Fail to run step {name} in routine {self.name}')
                if step.error_process is not None:
                    step.error_process(**kwds)
                if self.error_process is not None:
                    self.error_process(**kwds)
                return False
        return kwds['result']