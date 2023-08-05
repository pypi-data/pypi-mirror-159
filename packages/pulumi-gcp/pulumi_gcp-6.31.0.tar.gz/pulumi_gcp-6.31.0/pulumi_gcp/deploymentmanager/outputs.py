# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs

__all__ = [
    'DeploymentLabel',
    'DeploymentTarget',
    'DeploymentTargetConfig',
    'DeploymentTargetImport',
]

@pulumi.output_type
class DeploymentLabel(dict):
    def __init__(__self__, *,
                 key: Optional[str] = None,
                 value: Optional[str] = None):
        """
        :param str key: Key for label.
        :param str value: Value of label.
        """
        if key is not None:
            pulumi.set(__self__, "key", key)
        if value is not None:
            pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def key(self) -> Optional[str]:
        """
        Key for label.
        """
        return pulumi.get(self, "key")

    @property
    @pulumi.getter
    def value(self) -> Optional[str]:
        """
        Value of label.
        """
        return pulumi.get(self, "value")


@pulumi.output_type
class DeploymentTarget(dict):
    def __init__(__self__, *,
                 config: 'outputs.DeploymentTargetConfig',
                 imports: Optional[Sequence['outputs.DeploymentTargetImport']] = None):
        """
        :param 'DeploymentTargetConfigArgs' config: The root configuration file to use for this deployment.
               Structure is documented below.
        :param Sequence['DeploymentTargetImportArgs'] imports: Specifies import files for this configuration. This can be
               used to import templates or other files. For example, you might
               import a text file in order to use the file in a template.
               Structure is documented below.
        """
        pulumi.set(__self__, "config", config)
        if imports is not None:
            pulumi.set(__self__, "imports", imports)

    @property
    @pulumi.getter
    def config(self) -> 'outputs.DeploymentTargetConfig':
        """
        The root configuration file to use for this deployment.
        Structure is documented below.
        """
        return pulumi.get(self, "config")

    @property
    @pulumi.getter
    def imports(self) -> Optional[Sequence['outputs.DeploymentTargetImport']]:
        """
        Specifies import files for this configuration. This can be
        used to import templates or other files. For example, you might
        import a text file in order to use the file in a template.
        Structure is documented below.
        """
        return pulumi.get(self, "imports")


@pulumi.output_type
class DeploymentTargetConfig(dict):
    def __init__(__self__, *,
                 content: str):
        """
        :param str content: The full contents of the template that you want to import.
        """
        pulumi.set(__self__, "content", content)

    @property
    @pulumi.getter
    def content(self) -> str:
        """
        The full contents of the template that you want to import.
        """
        return pulumi.get(self, "content")


@pulumi.output_type
class DeploymentTargetImport(dict):
    def __init__(__self__, *,
                 content: Optional[str] = None,
                 name: Optional[str] = None):
        """
        :param str content: The full contents of the template that you want to import.
        :param str name: The name of the template to import, as declared in the YAML
               configuration.
        """
        if content is not None:
            pulumi.set(__self__, "content", content)
        if name is not None:
            pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter
    def content(self) -> Optional[str]:
        """
        The full contents of the template that you want to import.
        """
        return pulumi.get(self, "content")

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        """
        The name of the template to import, as declared in the YAML
        configuration.
        """
        return pulumi.get(self, "name")


