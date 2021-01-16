from typing import Any, Dict


class Loader:
    def load(self, input_: Any) -> Dict[str, Any]: ...

    def can_read(self, input_: Any) -> bool: ...