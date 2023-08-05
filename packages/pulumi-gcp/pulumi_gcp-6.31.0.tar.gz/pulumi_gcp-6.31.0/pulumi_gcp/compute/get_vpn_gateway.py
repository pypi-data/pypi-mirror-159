# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = [
    'GetVPNGatewayResult',
    'AwaitableGetVPNGatewayResult',
    'get_vpn_gateway',
    'get_vpn_gateway_output',
]

@pulumi.output_type
class GetVPNGatewayResult:
    """
    A collection of values returned by getVPNGateway.
    """
    def __init__(__self__, description=None, id=None, name=None, network=None, project=None, region=None, self_link=None):
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if network and not isinstance(network, str):
            raise TypeError("Expected argument 'network' to be a str")
        pulumi.set(__self__, "network", network)
        if project and not isinstance(project, str):
            raise TypeError("Expected argument 'project' to be a str")
        pulumi.set(__self__, "project", project)
        if region and not isinstance(region, str):
            raise TypeError("Expected argument 'region' to be a str")
        pulumi.set(__self__, "region", region)
        if self_link and not isinstance(self_link, str):
            raise TypeError("Expected argument 'self_link' to be a str")
        pulumi.set(__self__, "self_link", self_link)

    @property
    @pulumi.getter
    def description(self) -> str:
        """
        Description of this VPN gateway.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> str:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def network(self) -> str:
        """
        The network of this VPN gateway.
        """
        return pulumi.get(self, "network")

    @property
    @pulumi.getter
    def project(self) -> str:
        return pulumi.get(self, "project")

    @property
    @pulumi.getter
    def region(self) -> str:
        """
        Region of this VPN gateway.
        """
        return pulumi.get(self, "region")

    @property
    @pulumi.getter(name="selfLink")
    def self_link(self) -> str:
        """
        The URI of the resource.
        """
        return pulumi.get(self, "self_link")


class AwaitableGetVPNGatewayResult(GetVPNGatewayResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetVPNGatewayResult(
            description=self.description,
            id=self.id,
            name=self.name,
            network=self.network,
            project=self.project,
            region=self.region,
            self_link=self.self_link)


def get_vpn_gateway(name: Optional[str] = None,
                    project: Optional[str] = None,
                    region: Optional[str] = None,
                    opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetVPNGatewayResult:
    """
    Get a VPN gateway within GCE from its name.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_gcp as gcp

    my_vpn_gateway = gcp.compute.get_vpn_gateway(name="vpn-gateway-us-east1")
    ```


    :param str name: The name of the VPN gateway.
    :param str project: The project in which the resource belongs. If it
           is not provided, the provider project is used.
    :param str region: The region in which the resource belongs. If it
           is not provided, the project region is used.
    """
    __args__ = dict()
    __args__['name'] = name
    __args__['project'] = project
    __args__['region'] = region
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('gcp:compute/getVPNGateway:getVPNGateway', __args__, opts=opts, typ=GetVPNGatewayResult).value

    return AwaitableGetVPNGatewayResult(
        description=__ret__.description,
        id=__ret__.id,
        name=__ret__.name,
        network=__ret__.network,
        project=__ret__.project,
        region=__ret__.region,
        self_link=__ret__.self_link)


@_utilities.lift_output_func(get_vpn_gateway)
def get_vpn_gateway_output(name: Optional[pulumi.Input[str]] = None,
                           project: Optional[pulumi.Input[Optional[str]]] = None,
                           region: Optional[pulumi.Input[Optional[str]]] = None,
                           opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetVPNGatewayResult]:
    """
    Get a VPN gateway within GCE from its name.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_gcp as gcp

    my_vpn_gateway = gcp.compute.get_vpn_gateway(name="vpn-gateway-us-east1")
    ```


    :param str name: The name of the VPN gateway.
    :param str project: The project in which the resource belongs. If it
           is not provided, the provider project is used.
    :param str region: The region in which the resource belongs. If it
           is not provided, the project region is used.
    """
    ...
