
from pytorch_lightning.overrides.fairscale import _FAIRSCALE_AVAILABLE  # noqa: F401
from pytorch_lightning.overrides.fairscale import _FAIRSCALE_OSS_FP16_BROADCAST_AVAILABLE  # noqa: F401
from pytorch_lightning.overrides.fairscale import _FAIRSCALE_FULLY_SHARDED_AVAILABLE  # noqa: F401
if _FAIRSCALE_AVAILABLE:
    from pytorch_lightning.overrides.fairscale import LightningShardedDataParallel  # noqa: F401
    from pytorch_lightning.overrides.fairscale import unwrap_lightning_module_sharded  # noqa: F401
