import multiprocessing
from multiprocessing import Pool
from multiprocessing import Manager
import time
import numpy as np
from tqdm import tqdm
from ..utils import vvd_round

from concurrent.futures import ThreadPoolExecutor


def single_process(main_fun, paras, share_list, share_lock, total_size, start_time, catch_exception):

    if catch_exception:
        try:
            res = main_fun(paras)
        except Exception as e:
            print(e)
            return
    else:
        res = main_fun(paras)
    if res is not None:
        share_lock.acquire()
        share_list.append(res)
        share_lock.release()
    else:
        print("None res got, and it won't appear in the share_list. ")

    print(f"{len(share_list)} / {total_size}")
    
    min_time = (time.time() - start_time) / max(1, len(share_list)) * (total_size - max(1, len(share_list))) / 60
    print(f"time passed: {(time.time() - start_time)/ 60} min      time left: {min_time} min")




def multi_process(main_fun, para_fun, total_size, max_pool_num=8, catch_exception=True, method=None):
    """_summary_

    Args:
        main_fun (func): main function
        para_fun (func): fun(id) is the input data
        total_size (int): total number of inputs
        max_pool_num (int, optional): worker number. Defaults to 8.
        catch_exception (bool, optional): if True, a try-except will be applied. Defaults to True.
        method (str, optional): method to setup multiprocessing, could be one of ['spawn', 'fork', 'forkserver']. Defaults to None.

    Returns:
        _type_: _description_
    """
    if method is not None:
        multiprocessing.set_start_method(method)
        # multiprocessing.set_start_method('spawn')
    start_time = time.time()
    if max_pool_num > 0:
        mp_manager = Manager()
        share_list = mp_manager.list()
        share_lock = mp_manager.Lock()
        pool = Pool(max_pool_num)
        for index in range(total_size):
            paras = para_fun(index)
            pool.apply_async(func=single_process, args=(main_fun, paras, share_list, share_lock, total_size, start_time, catch_exception))
        pool.close()
        pool.join()
        result_list = list(share_list)
    else:
        result_list = list()
        for index in tqdm(range(total_size)):
            res = main_fun(para_fun(index))
            result_list.append(res)
    print(f"total time: {(time.time() - start_time) / 60} min     mean time {(time.time() - start_time) / max(1, len(result_list))} s")
    return result_list


class MultiProcessManager:
    TaskModeList = ['multiprocessing', 'multithreading', 'sequence']

    def __init__(self, core_function, running_mode='sequence', max_worker_num=None):
        self.core_function = core_function
        assert running_mode in type(self).TaskModeList, f"running_mode {running_mode} must in {type(self).TaskModeList}."
        self.running_mode = running_mode
        if max_worker_num is None:
            self.max_worker_num = 16
        else:
            self.max_worker_num = max(1, vvd_round(max_worker_num))

        if self.running_mode == 'multiprocessing':
            self.process_pool = Pool(self.max_worker_num)
        elif self.running_mode == 'multithreading':
            self.thread_pool = ThreadPoolExecutor(max_workers=self.max_worker_num)

    def get_processed_func(self, core_function, pbar):
        def thread_func(data):
            pbar.update(1)
            res = None
            try:
                res = core_function(data)
            except Exception as e:
                print(e, data)
            return res
        return thread_func

    def infer(self, input_list):
        """
            "Pool.map results are ordered. If you need order, great; if you don't,
            Pool.imap_unordered may be a useful optimization. Note that while the
            order in which you receive the results from Pool.map is fixed, the
            order in which they are computed is arbitrary."
        -- https://stackoverflow.com/questions/41273960/python-3-does-pool-keep-the-original-order-of-data-passed-to-map
        """

        num_tasks = len(input_list)

        if None: pass
        elif self.running_mode == 'multiprocessing':
            # * multiprocessing
            pool = self.process_pool
            result_list = pool.map(self.core_function, input_list)
            pool.close()
            pool.join()

        elif self.running_mode == 'multithreading':
            pbar = tqdm(total = num_tasks)
            core_func = self.get_processed_func(self.core_function, pbar)
            # * multi threading
            result_list = list(self.thread_pool.map(core_func, input_list))

        elif self.running_mode == 'sequence':
            # * sequence
            result_list = list(map(self.core_function, input_list))
        else:
            raise TypeError

        assert isinstance(result_list, list), f"result_list {result_list} must be a list"

        # check the output order
        if len(result_list) != num_tasks:
            raise RuntimeError(f"Error: Something fatal happened during inference!!!!\
                len(result_list) {len(result_list)} != len(result_list) {len(result_list)}")

        return result_list



if __name__ == '__main__':
    def para_gen(index):
        para_1 = np.random.randint(0, 200)
        para_2 = np.random.randint(0, 200)
        return {'para_1':para_1, 'para_2':para_2}

    def main_fun_v(para_dict):
        para_1 = para_dict['para_1']
        para_2 = para_dict['para_2']
        return para_1 + para_2

    res_list = multi_process(main_fun_v, para_gen, 200, 0)
    pass