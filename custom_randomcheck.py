import random
from datadog_checks.base import AgentCheck

# content of the special variable __version__ will be shown in the Agent status page
__version__ = "1.0.0"

class CustomRandomCheck(AgentCheck):
    def check(self, instance):
        self.gauge("my_metric", random.randint(1, 1001), tags=["check:random"])
