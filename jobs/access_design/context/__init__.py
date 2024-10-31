from nautobot_design_builder.context import Context

from nautobot.dcim.models import Location

from nautobot.apps.jobs import IntegerVar


class AccessNetworkDesignContext(Context):
    """Render context for Access switch network design"""
    site: Location
    data_vlan_id = IntegerVar
    voice_vlan_id = IntegerVar

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if not self.data_vlan_id or not self.voice_vlan_id:
            self.data_vlan_id, self.voice_vlan_id = 100, 101
