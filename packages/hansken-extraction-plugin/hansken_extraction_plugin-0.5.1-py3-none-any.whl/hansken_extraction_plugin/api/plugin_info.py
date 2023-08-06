"""This module contains all definitions to describe meta data of a plugin, a.k.a. PluginInfo."""
from dataclasses import dataclass
from enum import Enum
from typing import Any, Optional


@dataclass(frozen=True)
class Author:
    """
    The author of an Extraction Plugin.

    This information can be retrieved by an end-user from Hansken.
    """

    name: str
    email: str
    organisation: str


class MaturityLevel(Enum):
    """This class represents the maturity level of an extraction plugin."""

    PROOF_OF_CONCEPT = 0
    READY_FOR_TEST = 1
    PRODUCTION_READY = 2


@dataclass(frozen=True)
class PluginId:
    """Identifier of a plugin, consisting of domain, category and name. Needs to be unique among all tools/plugins."""

    domain: str
    category: str
    name: str


class PluginResources:
    """
    PluginResources contains information about how many resources will be used for a plugin.

    The most common resources to specify are CPU and memory (RAM).

    CPU resources are measured in cpu units. One cpu is equivalent to 1 vCPU/Core for cloud providers and 1 hyperthread
    on bare-metal Intel processors. Also, fractional requests are allowed. A plugin that asks 0.5 CPU uses half as
    much CPU as one that asks for 1 CPU.

    Memory resources are measured in Megabytes.

    Here is an example to set resources for a plugin:

    .. code-block:: python

        PluginResources.builder()
            .maximum_cpu(0.5)
            .maximum_memory(1000)
            .build()

    In this example the plugin has a limit of 0.5 cpu and 1G of memory.
    """

    def __init__(self, max_cpu: float, max_memory: int) -> None:
        """
        Initialize PluginResources (don't use this, use .PluginResources.Builder instead).

        :param maxima: map of resource type and maximum quantities
        """
        self._max_cpu = max_cpu
        self._max_memory = max_memory

    def maximum_cpu(self) -> Optional[float]:
        """
        Return the maximum cpu.

        :return: Maximum cpu
        """
        return self._max_cpu

    def maximum_memory(self) -> Optional[int]:
        """
        Return the maximum memory.

        :return: Maximum memory
        """
        return self._max_memory

    @staticmethod
    def builder():
        """:return a Builder."""
        return PluginResources.Builder()

    class Builder:
        """Helper class that implements a resources builder."""

        def __init__(self) -> None:
            """Initialize a Builder."""
            self._max_cpu: float
            self._max_memory: int

        def maximum_cpu(self, quantity: float):
            """
            Set maximum cpu usage to plugin resources.

            :param quantity the cpu resource quantity
            :return: this `.PluginResources.Builder`
            """
            self._max_cpu = quantity
            return self

        def maximum_memory(self, quantity: int):
            """
            Set maximum memory usage to plugin resources.

            :param quantity the memory resource quantity
            :return: this `.PluginResources.Builder`
            """
            self._max_memory = quantity
            return self

        def build(self) -> 'PluginResources':
            """
            Return PluginResources.

            :return: PluginResources
            """
            return PluginResources(self._max_cpu, self._max_memory)


@dataclass
class PluginInfo:
    """This information is used by Hansken to identify and run the plugin."""

    plugin: Any  #: the plugin that returns this plugin info, pass self
    version: str  #: version of the plugin
    description: str  #: short description of the functionality of the plugin
    author: Author  #: the plugin's author, see Author
    maturity: MaturityLevel  #: maturity level, see MaturityLevel
    matcher: str  #: this matcher selects the traces offered to the plugin
    webpage_url: str  #: plugin url
    id: PluginId  #: a plugin's unique identifier, see PluginId
    license: Optional[str] = None  #: license of this plugin
    deferred_iterations: int = 1  #: number of deferred iterations (1 to 20), nly for deferred plugins (optional)
    resources: Optional[PluginResources] = None  #: resources to be reserved for a plugin (optional)

    def __post_init__(self):
        if not 1 <= self.deferred_iterations <= 20:
            raise ValueError(f'Invalid value for deferred_iterations: {self.deferred_iterations}. '
                             f'Valid values are 1 =< 20.')
