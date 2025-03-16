
from typing import List

class Device(List[int]):
    def __init__(self, channels: int):
        super.__init__([0 for _ in range(channels)])

