
import logging
from typing import Any

from pytorch_lightning.__about__ import *  # noqa: F401, F403

from pytorch_lightning import _DETAIL  # noqa: F401
from pytorch_lightning import _detail  # noqa: F401
logging.addLevelName(_DETAIL, "DETAIL")
from pytorch_lightning import logging  # noqa: F401
from pytorch_lightning import _root_logger  # noqa: F401
from pytorch_lightning import _logger  # noqa: F401
_logger.setLevel(logging.INFO)

if not _root_logger.hasHandlers():
    _logger.addHandler(logging.StreamHandler())
    from pytorch_lightning import _logger  # noqa: F401
from pytorch_lightning.callbacks import Callback  # noqa: E402
from pytorch_lightning.core import LightningDataModule, LightningModule  # noqa: E402
from pytorch_lightning.trainer import Trainer  # noqa: E402
from pytorch_lightning.utilities.seed import seed_everything  # noqa: E402

from pytorch_lightning import __all__  # noqa: F401
__import__("pkg_resources").declare_namespace(__name__)
