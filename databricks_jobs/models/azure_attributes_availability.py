from enum import Enum


class AzureAttributesAvailability(str, Enum):
    SPOT_AZURE = "SPOT_AZURE"
    ON_DEMAND_AZURE = "ON_DEMAND_AZURE"
    SPOT_WITH_FALLBACK_AZURE = "SPOT_WITH_FALLBACK_AZURE"

    def __str__(self) -> str:
        return str(self.value)
