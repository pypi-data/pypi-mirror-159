from enum import Enum


class PluginStatusState(str, Enum):
    NOTRUNNING = "NotRunning"
    STARTING = "Starting"
    RUNNING = "Running"
    FAILEDTOSTART = "FailedToStart"
    FAILEDTOSTAYRUNNING = "FailedToStayRunning"
    STOPPING = "Stopping"

    def __str__(self) -> str:
        return str(self.value)
