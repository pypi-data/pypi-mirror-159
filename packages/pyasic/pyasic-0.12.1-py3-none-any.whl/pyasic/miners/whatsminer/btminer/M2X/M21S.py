from pyasic.miners._backends import BTMiner  # noqa - Ignore access to _module
from pyasic.miners._types import M21S, M21SV20, M21SV60  # noqa - Ignore access to _module


class BTMinerM21S(BTMiner, M21S):
    def __init__(self, ip: str) -> None:
        super().__init__(ip)
        self.ip = ip


class BTMinerM21SV20(BTMiner, M21SV20):
    def __init__(self, ip: str) -> None:
        super().__init__(ip)
        self.ip = ip


class BTMinerM21SV60(BTMiner, M21SV60):
    def __init__(self, ip: str) -> None:
        super().__init__(ip)
        self.ip = ip
