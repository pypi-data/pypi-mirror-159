from mavtel_client.client.base import MAVTelClientBase
from mavtel_client.client.mixins.metrics_mixin import MetricsMixin
from mavtel_client.client.mixins.services_mixin import ServicesMixin


class MAVTelClient(MAVTelClientBase, MetricsMixin, ServicesMixin):
    pass
