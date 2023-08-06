
from pytorch_lightning.accelerators.accelerator import Accelerator  # noqa: F401
from pytorch_lightning.accelerators.cpu import CPUAccelerator  # noqa: F401
from pytorch_lightning.accelerators.gpu import GPUAccelerator  # noqa: F401
from pytorch_lightning.accelerators.hpu import HPUAccelerator  # noqa: F401
from pytorch_lightning.accelerators.ipu import IPUAccelerator  # noqa: F401
from pytorch_lightning.accelerators.registry import AcceleratorRegistry, call_register_accelerators  # noqa: F401
from pytorch_lightning.accelerators.tpu import TPUAccelerator  # noqa: F401

from pytorch_lightning.accelerators import ACCELERATORS_BASE_MODULE  # noqa: F401
call_register_accelerators(ACCELERATORS_BASE_MODULE)
