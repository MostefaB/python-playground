# 981. Time Based Key-Value Store
import collections
from datetime import datetime


class TimeMap:

    """
    Initializes the object of the data structure
    """
    def __init__(self):
        self.ds = collections.defaultdict(list)

    """
    Stores the key key with the value value at the given time timestamp.
    """
    def set(self, key: str, value: str, timestamp: int) -> None:
        # print(f" -- Received: set(key = {key},value = {value}, timestamp = {timestamp}) -- ")
        self.ds[key].append([value, timestamp])

    """
    Returns a value such that set was called previously, with timestamp_prev <= timestamp. 
    If there are multiple such values, it returns the value associated with the largest timestamp_prev. 
    If there are no values, it returns "".
    """
    def get(self, key: str, timestamp: int) -> str:
        ret = self.ds.get(key,[])
        # print(f" -- Received: get({key},{timestamp}) | Potential answers: {ret} -- ")
        candidate_vals = list()
        current_max = 0
        get_v = ""

        # Linear search
        # for r in ret: 
        #     if r[1] == timestamp:
        #         return r[0]
        #     elif r[1] < timestamp:
        #         if r[1] >= current_max:
        #             get_v = r[0]
        #             current_max = r[1]
        # Binary search - timestamps are strictly increasing
        l, r = 0, len(ret)-1

        while l <= r:
            m = (l + r) // 2
            # print(f"l:{l}, r:{r}, m:{m}")
            if timestamp > ret[m][1]:
                # Store this one in case there is no value associated with timestamp
                get_v = ret[m][0]
                # Search right
                l = m + 1
            elif timestamp < ret[m][1]:
                # Search left
                r = m - 1
            elif timestamp == ret[m][1]:
                return ret[m][0]

        return get_v

# Your TimeMap object will be instantiated and called as such:
obj = TimeMap()
obj.set("foo","bar",2)
obj.set("foo","bar2",3)
obj.set("foo","bar3",4)
obj.set("foo2","bar4",2)
obj.set("foo","bar5",5)
obj.set("foo3","bar6",2)
param_2 = obj.get("foo",6)