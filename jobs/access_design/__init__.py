"""Initial data required for controllers."""
from nautobot.apps.jobs import register_jobs, ObjectVar, StringVar, IPNetworkVar

from nautobot.dcim.models import Location

from nautobot_design_builder.design_job import DesignJob


from .context import AccessNetworkDesignContext


class NewAccessSwitch(DesignJob):
    """Add new access switch to the Site."""
    has_sensitive_variables = False
    site = ObjectVar(
        label="Site",
        description="Site for the new access switch to be deployed in",
        model=Location,
    )

    container_prefix = IPNetworkVar(min_prefix_length=16, max_prefix_length=22)
    loopback_prefix = IPNetworkVar(min_prefix_length=16, max_prefix_length=22)

    class Meta:
        """Add new access switch to the Site."""

        name = "New Access Switch"
        commit_default = False
        design_file = "designs/0001_design.yaml.j2"
        context_class = AccessNetworkDesignContext
        has_sensitive_variables = False

name = "BaxConfig Designs"
register_jobs(NewAccessSwitch)
