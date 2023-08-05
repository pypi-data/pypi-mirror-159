from typing import Optional, List, Union, Dict, Any, Tuple

import numpy as np

from moving_targets.learners import Learner
from moving_targets.util.errors import MissingDependencyError
from moving_targets.util.scalers import Scaler


class TorchLearner(Learner):
    """Wrapper for a custom Torch model."""

    class _Dataset:
        """Inner utility class to deal with torch expected input."""

        def __init__(self, x, y):
            import torch
            assert len(x) == len(y), f"Data should have the same length, but len(x) = {len(x)} and len(y) = {len(y)} "
            self.x = torch.tensor(x, dtype=torch.float32)
            self.y = torch.tensor(np.expand_dims(y, axis=-1), dtype=torch.float32)

        def __len__(self):
            return len(self.y)

        def __getitem__(self, idx):
            return self.x[idx], self.y[idx]

    def __init__(self,
                 model,
                 loss,
                 optimizer='Adam',
                 epochs: int = 1,
                 shuffle: bool = True,
                 validation_split: float = 0.,
                 batch_size: Optional[int] = 128,
                 num_workers: int = 0,
                 verbose: bool = True,
                 mask: Optional[float] = None,
                 x_scaler: Union[None, Scaler, str] = None,
                 y_scaler: Union[None, Scaler, str] = None,
                 stats: Union[bool, List[str]] = False,
                 **fit_kwargs):
        """
        :param model:
            The torch model which should have been already compiled.

        :param loss:
            Either the neural network loss function or its name to retrieve it from `torch.nn`.

        :param optimizer:
            Either the neural network optimizer or its name to retrieve it from `torch.optim`.

        :param epochs:
            The number of training epochs.

        :param shuffle:
            Whether or not to shuffle the dataset when training.

        :param validation_split:
            The validation split for neural network training.

        :param batch_size:
            The batch size for neural network training.

        :param num_workers:
            Defines how many subprocesses to use for data loading ('0' to load data in the main process).

        :param verbose:
            Whether or not to print information during the neural network training.

        :param mask:
            The (optional) masking value used to mask the original targets.

        :param x_scaler:
            The (optional) scaler for the input data, or a string representing the default scaling method.

        :param y_scaler:
            The (optional) scaler for the output data, or a string representing the default scaling method.

        :param stats:
            Either a boolean value indicating whether or not to log statistics, or a list of parameters whose
            statistics must be logged.

        :param fit_kwargs:
            Custom arguments to be passed to the model '.fit()' method.
        """
        try:
            from torch import nn, optim
        except ModuleNotFoundError:
            raise MissingDependencyError(package='torch')

        super(TorchLearner, self).__init__(mask=mask, x_scaler=x_scaler, y_scaler=y_scaler, stats=stats)

        # handle loss
        if isinstance(loss, str):
            loss = getattr(nn, loss)
            loss = loss()

        # handle optimizer
        if isinstance(optimizer, str):
            optimizer = getattr(optim, optimizer)
            optimizer = optimizer(model.parameters())

        self.model: nn.Module = model
        """The torch model."""

        self.loss: nn.Module = loss
        """The neural network loss function."""

        self.optimizer: optim.Optimizer = optimizer
        """The neural network optimizer."""

        self.epochs: int = epochs
        """The number of training epochs."""

        self.shuffle: bool = shuffle
        """Whether or not to shuffle the dataset when training."""

        self.validation_split: float = validation_split
        """The validation split for neural network training."""

        self.batch_size: int = batch_size
        """The batch size for neural network training."""

        self.num_workers: int = num_workers
        """The number of subprocesses to use for data loading."""

        self.verbose: bool = verbose
        """Whether or not to print information during the neural network training."""

        self.fit_kwargs: Dict[str, Any] = fit_kwargs
        """Custom arguments to be passed to the model '.fit()' method."""

    def _print(self, epoch: int, loss: float, batch: Optional[Tuple[int, int]] = None):
        if not self.verbose:
            return

        # carriage return to write in the same line
        print(f'\r', end='')
        # print the epoch number with trailing spaces on the left to match the maximum epoch
        print(f'Epoch {epoch:{len(str(self.epochs))}}', end=' ')
        # print the loss value (either loss for this single batch or for the whole epoch)
        print(f'- loss = {loss:.4f}', end='')
        # check whether this is the information of a single batch or of the whole epoch and for the latter case (batch
        # is None) print a new line, while for the former (batch is a tuple) print the batch number and no new line
        if batch is None:
            print()
        else:
            batch, batches = batch
            print(f' (batch {batch:{len(str(batches))}} of {batches})', end='')

    # noinspection PyTypeChecker
    def _fit(self, x, y: np.ndarray, sample_weight: Optional[np.ndarray] = None):
        from torch.utils.data import DataLoader

        if sample_weight is not None:
            self.logger.warning("TorchLearner does not support sample weights, please pass 'sample_weight'=None")

        ds = TorchLearner._Dataset(x=x, y=y)
        loader = DataLoader(dataset=ds, batch_size=self.batch_size, shuffle=self.shuffle, num_workers=self.num_workers)
        batches = np.ceil(len(ds) / self.batch_size).astype(int)
        self.model.train()
        for epoch in np.arange(self.epochs) + 1:
            epoch_loss = 0.0
            for batch, (inp, out) in enumerate(loader):
                self.optimizer.zero_grad()
                pred = self.model(inp)
                loss = self.loss(pred, out)
                loss.backward()
                self.optimizer.step()
                epoch_loss += loss.item() * inp.size(0)
                self._print(epoch=epoch, loss=loss.item(), batch=(batch + 1, batches))
            self._print(epoch=epoch, loss=epoch_loss / len(ds))
        self.model.eval()

    def _predict(self, x) -> np.ndarray:
        import torch
        return self.model(torch.tensor(x, dtype=torch.float32)).detach().numpy().squeeze()


class TorchMLP(TorchLearner):
    """Torch Dense Neural Network Wrapper"""

    def __init__(self,
                 loss,
                 input_units: int,
                 output_units: int = 1,
                 output_activation: Optional = None,
                 hidden_units: List[int] = (128,),
                 hidden_activation: Optional = 'ReLU',
                 optimizer: str = 'Adam',
                 epochs: int = 1,
                 shuffle: bool = True,
                 batch_size: Optional[int] = 128,
                 num_workers: int = 0,
                 verbose: bool = True,
                 mask: Optional[float] = None,
                 x_scaler: Union[None, Scaler, str] = None,
                 y_scaler: Union[None, Scaler, str] = None,
                 stats: Union[bool, List[str]] = False):
        """
        :param loss:
            Either the neural network loss function or its name to retrieve it from `torch.nn`.

        :param input_units:
            The neural network number of input units.

        :param output_units:
            The neural network number of output units.

        :param output_activation:
            Either the neural network output activation module or its name to retrieve it from `torch.nn`.

        :param hidden_units:
            The tuple of neural network hidden units.

        :param hidden_activation:
            Either the neural network hidden activation module or its name to retrieve it from `torch.nn`.

        :param optimizer:
            The name of the neural network optimizer to retrieve it from `torch.optim`.

        :param epochs:
            The number of training epochs.

        :param shuffle:
            Whether or not to shuffle the dataset when training.

        :param batch_size:
            The batch size for neural network training.

        :param num_workers:
            Defines how many subprocesses to use for data loading ('0' to load data in the main process).

        :param verbose:
            Whether or not to print information during the neural network training.

        :param mask:
            The (optional) masking value used to mask the original targets.

        :param x_scaler:
            The (optional) scaler for the input data, or a string representing the default scaling method.

        :param y_scaler:
            The (optional) scaler for the output data, or a string representing the default scaling method.

        :param stats:
            Either a boolean value indicating whether or not to log statistics, or a list of parameters whose
            statistics must be logged.
        """
        try:
            from torch import nn
        except ModuleNotFoundError:
            raise MissingDependencyError(package='torch')

        # handle hidden activation
        if isinstance(hidden_activation, str):
            hidden_activation = getattr(nn, hidden_activation)
            hidden_activation = hidden_activation()

        # handle output activation
        if isinstance(output_activation, str):
            output_activation = getattr(nn, output_activation)
            output_activation = output_activation()

        # build the hidden linear layers and optionally append an activation layer if passed
        layers = []
        hidden_units = [input_units] + list(hidden_units)
        for i, h in enumerate(hidden_units[:-1]):
            layers += [nn.Linear(in_features=hidden_units[i], out_features=hidden_units[i + 1])]
            layers += [] if hidden_activation is None else [hidden_activation]
        # build the output layer and optionally append an output activation layer if passed
        layers += [nn.Linear(in_features=hidden_units[-1], out_features=output_units)]
        layers += [] if output_activation is None else [output_activation]
        # eventually build the network
        network = nn.Sequential(*layers)

        super(TorchMLP, self).__init__(model=network,
                                       loss=loss,
                                       optimizer=optimizer,
                                       epochs=epochs,
                                       shuffle=shuffle,
                                       batch_size=batch_size,
                                       num_workers=num_workers,
                                       verbose=verbose,
                                       mask=mask,
                                       x_scaler=x_scaler,
                                       y_scaler=y_scaler,
                                       stats=stats)
