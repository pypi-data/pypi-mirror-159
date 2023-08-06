from pyasic.miners import BaseMiner


class S19a(BaseMiner):
    def __init__(self, ip: str):
        super().__init__()
        self.ip = ip
        self.model = "S19a"
        self.nominal_chips = 72
        self.fan_count = 4
