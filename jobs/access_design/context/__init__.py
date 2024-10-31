from nautobot_design_builder.context import Context, context_file
from nautobot.dcim.models import Location


@context_file("context.yaml")
class AccessNetworkDesignContext(Context):
    """Render context for Access switch network design"""

    # site: Location
