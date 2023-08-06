
from os import environ

from pytorch_lightning.loggers.base import LightningLoggerBase, LoggerCollection
from pytorch_lightning.loggers.csv_logs import CSVLogger
from pytorch_lightning.loggers.tensorboard import TensorBoardLogger

from pytorch_lightning.loggers import __all__  # noqa: F401
from pytorch_lightning.loggers.comet import _COMET_AVAILABLE, CometLogger  # noqa: F401
from pytorch_lightning.loggers.mlflow import _MLFLOW_AVAILABLE, MLFlowLogger  # noqa: F401
from pytorch_lightning.loggers.neptune import _NEPTUNE_AVAILABLE, NeptuneLogger  # noqa: F401
from pytorch_lightning.loggers.test_tube import _TESTTUBE_AVAILABLE, TestTubeLogger  # noqa: F401
from pytorch_lightning.loggers.wandb import WandbLogger  # noqa: F401
from pytorch_lightning.utilities.imports import _WANDB_AVAILABLE

if _COMET_AVAILABLE:
    __all__.append("CometLogger")

    environ["COMET_DISABLE_AUTO_LOGGING"] = "1"

if _MLFLOW_AVAILABLE:
    __all__.append("MLFlowLogger")

if _NEPTUNE_AVAILABLE:
    __all__.append("NeptuneLogger")

if _TESTTUBE_AVAILABLE:
    __all__.append("TestTubeLogger")

if _WANDB_AVAILABLE:
    __all__.append("WandbLogger")
