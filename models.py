from dataclasses import dataclass
from enum import Enum


class SuspensionStatus(Enum):
    NONE = "none"
    SUSPENDED = "suspended"
    POSSIBLY_SUSPENDED = "possibly_suspended"


@dataclass
class ParsedMedication:
    raw_text: str
    medication_name: str
    dose: str | None = None
    posology_code: str | None = None
    quantity_per_dose: str | None = None
    frequency: str | None = None
    timing: str | None = None
    condition: str | None = None
    extra_info: str | None = None
    brand_in_parens: str | None = None
    is_tarv: bool = False
    suspension: SuspensionStatus = SuspensionStatus.NONE
    suspension_reason: str | None = None
