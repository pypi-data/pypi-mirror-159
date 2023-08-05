# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = [
    'GetRecordSetResult',
    'AwaitableGetRecordSetResult',
    'get_record_set',
    'get_record_set_output',
]

@pulumi.output_type
class GetRecordSetResult:
    """
    A collection of values returned by getRecordSet.
    """
    def __init__(__self__, id=None, managed_zone=None, name=None, project=None, rrdatas=None, ttl=None, type=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if managed_zone and not isinstance(managed_zone, str):
            raise TypeError("Expected argument 'managed_zone' to be a str")
        pulumi.set(__self__, "managed_zone", managed_zone)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if project and not isinstance(project, str):
            raise TypeError("Expected argument 'project' to be a str")
        pulumi.set(__self__, "project", project)
        if rrdatas and not isinstance(rrdatas, list):
            raise TypeError("Expected argument 'rrdatas' to be a list")
        pulumi.set(__self__, "rrdatas", rrdatas)
        if ttl and not isinstance(ttl, int):
            raise TypeError("Expected argument 'ttl' to be a int")
        pulumi.set(__self__, "ttl", ttl)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="managedZone")
    def managed_zone(self) -> str:
        return pulumi.get(self, "managed_zone")

    @property
    @pulumi.getter
    def name(self) -> str:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def project(self) -> Optional[str]:
        return pulumi.get(self, "project")

    @property
    @pulumi.getter
    def rrdatas(self) -> Sequence[str]:
        """
        The string data for the records in this record set.
        """
        return pulumi.get(self, "rrdatas")

    @property
    @pulumi.getter
    def ttl(self) -> int:
        """
        The time-to-live of this record set (seconds).
        """
        return pulumi.get(self, "ttl")

    @property
    @pulumi.getter
    def type(self) -> str:
        return pulumi.get(self, "type")


class AwaitableGetRecordSetResult(GetRecordSetResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetRecordSetResult(
            id=self.id,
            managed_zone=self.managed_zone,
            name=self.name,
            project=self.project,
            rrdatas=self.rrdatas,
            ttl=self.ttl,
            type=self.type)


def get_record_set(managed_zone: Optional[str] = None,
                   name: Optional[str] = None,
                   project: Optional[str] = None,
                   type: Optional[str] = None,
                   opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetRecordSetResult:
    """
    Get a DNS record set within Google Cloud DNS
    For more information see
    [the official documentation](https://cloud.google.com/dns/docs/records)
    and
    [API](https://cloud.google.com/dns/docs/reference/v1/resourceRecordSets)

    ## Example Usage

    ```python
    import pulumi
    import pulumi_gcp as gcp

    sample = gcp.dns.get_managed_zone(name="sample-zone")
    rs = gcp.dns.get_record_set(managed_zone=sample.name,
        name=f"my-record.{sample.dns_name}",
        type="A")
    ```


    :param str managed_zone: The Name of the zone.
    :param str name: The DNS name for the resource.
    :param str project: The ID of the project for the Google Cloud.
    """
    __args__ = dict()
    __args__['managedZone'] = managed_zone
    __args__['name'] = name
    __args__['project'] = project
    __args__['type'] = type
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('gcp:dns/getRecordSet:getRecordSet', __args__, opts=opts, typ=GetRecordSetResult).value

    return AwaitableGetRecordSetResult(
        id=__ret__.id,
        managed_zone=__ret__.managed_zone,
        name=__ret__.name,
        project=__ret__.project,
        rrdatas=__ret__.rrdatas,
        ttl=__ret__.ttl,
        type=__ret__.type)


@_utilities.lift_output_func(get_record_set)
def get_record_set_output(managed_zone: Optional[pulumi.Input[str]] = None,
                          name: Optional[pulumi.Input[str]] = None,
                          project: Optional[pulumi.Input[Optional[str]]] = None,
                          type: Optional[pulumi.Input[str]] = None,
                          opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetRecordSetResult]:
    """
    Get a DNS record set within Google Cloud DNS
    For more information see
    [the official documentation](https://cloud.google.com/dns/docs/records)
    and
    [API](https://cloud.google.com/dns/docs/reference/v1/resourceRecordSets)

    ## Example Usage

    ```python
    import pulumi
    import pulumi_gcp as gcp

    sample = gcp.dns.get_managed_zone(name="sample-zone")
    rs = gcp.dns.get_record_set(managed_zone=sample.name,
        name=f"my-record.{sample.dns_name}",
        type="A")
    ```


    :param str managed_zone: The Name of the zone.
    :param str name: The DNS name for the resource.
    :param str project: The ID of the project for the Google Cloud.
    """
    ...
