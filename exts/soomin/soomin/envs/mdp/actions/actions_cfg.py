# type: ignore

from dataclasses import MISSING

from omni.isaac.lab.managers.action_manager import ActionTerm, ActionTermCfg
from omni.isaac.lab.utils import configclass

from . import holonomic_actions
from soomin.envs.mdp.controllers.holonomic import HolnomicControllerCfg

@configclass
class HolonomicActionCfg(ActionTermCfg):
    """Configuration for the holonomic action term with 4 mecanum wheel joints in the base.

    See :class:`HolonomicAction` for more details.
    """

    class_type: type[ActionTerm] = holonomic_actions.HolonomicAction

    fl_joint_name: str = MISSING
    """The front left wheel joint name."""
    fr_joint_name: str = MISSING
    """The front right wheel joint name."""
    rl_joint_name: str = MISSING
    """The rear left wheel joint name."""
    rr_joint_name: str = MISSING
    """The rear right wheel joint name."""
    scale: tuple[float, float, float] = (1.0, 1.0, 1.0)
    """Scale factor for the base action. Defaults to (1.0, 1.0, 1.0)."""
    offset: tuple[float, float, float] = (0.0, 0.0, 0.0)
    """Offset factor for the base action. Defaults to (0.0, 0.0, 0.0)."""
    controller: HolnomicControllerCfg = MISSING
    """The configuration for the holonomic drive controller."""