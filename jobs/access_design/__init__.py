"""Initial data required for controllers."""
from nautobot.apps.jobs import register_jobs, ObjectVar, IntegerVar

from nautobot.dcim.models import Location

from nautobot_design_builder.design_job import DesignJob

from .context import AccessNetworkDesignContext


class NewAccessSwitch(DesignJob):
    """Add new access switch to the Site."""
    site = ObjectVar(
        label="Site",
        description="Site for the new access switch to be deployed in",
        model=Location,
    )
    data_vlan_id = IntegerVar(
        label="Data Vlan ID",
        description="(optional) Data Vlan ID - use this value instead of auto-generated",
        required=False,
        min_value=1,
        max_value=4094,
    )

    voice_vlan_id = IntegerVar(
        label="Voice Vlan ID",
        description="(optional) Voice Vlan ID - use this value instead of auto-generated",
        required=False,
        min_value=1,
        max_value=4094,
    )

    class Meta:
        """Add new access switch to the Site."""

        name = "New Access Switch test"
        commit_default = False
        design_file = "designs/0001_design.yaml.j2"
        context_class = AccessNetworkDesignContext
        has_sensitive_variables = False

name = "Test Designs"
register_jobs(NewAccessSwitch)
