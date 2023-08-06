from pyasic.miners import BaseMiner


class M20S(BaseMiner):
    def __init__(self, ip: str):
        super().__init__()
        self.ip = ip
        self.model = "M20S"
        self.nominal_chips = 66
        self.fan_count = 2


class M20SV10(BaseMiner):
    def __init__(self, ip: str):
        super().__init__()
        self.ip = ip
        self.model = "M20S"
        self.nominal_chips = 105
        self.fan_count = 2


class M20SV20(BaseMiner):
    def __init__(self, ip: str):
        super().__init__()
        self.ip = ip
        self.model = "M20S"
        self.nominal_chips = 111
        self.fan_count = 2
