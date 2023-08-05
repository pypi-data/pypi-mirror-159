# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs
from ._inputs import *

__all__ = ['RegionPerInstanceConfigArgs', 'RegionPerInstanceConfig']

@pulumi.input_type
class RegionPerInstanceConfigArgs:
    def __init__(__self__, *,
                 region_instance_group_manager: pulumi.Input[str],
                 minimal_action: Optional[pulumi.Input[str]] = None,
                 most_disruptive_allowed_action: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 preserved_state: Optional[pulumi.Input['RegionPerInstanceConfigPreservedStateArgs']] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 remove_instance_state_on_destroy: Optional[pulumi.Input[bool]] = None):
        """
        The set of arguments for constructing a RegionPerInstanceConfig resource.
        :param pulumi.Input[str] region_instance_group_manager: The region instance group manager this instance config is part of.
        :param pulumi.Input[str] minimal_action: The minimal action to perform on the instance during an update.
               Default is `NONE`. Possible values are:
               * REPLACE
               * RESTART
               * REFRESH
               * NONE
        :param pulumi.Input[str] most_disruptive_allowed_action: The most disruptive action to perform on the instance during an update.
               Default is `REPLACE`. Possible values are:
               * REPLACE
               * RESTART
               * REFRESH
               * NONE
        :param pulumi.Input[str] name: The name for this per-instance config and its corresponding instance.
        :param pulumi.Input['RegionPerInstanceConfigPreservedStateArgs'] preserved_state: The preserved state for this instance.
               Structure is documented below.
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the provider project is used.
        :param pulumi.Input[str] region: Region where the containing instance group manager is located
        :param pulumi.Input[bool] remove_instance_state_on_destroy: When true, deleting this config will immediately remove any specified state from the underlying instance.
               When false, deleting this config will *not* immediately remove any state from the underlying instance.
               State will be removed on the next instance recreation or update.
        """
        pulumi.set(__self__, "region_instance_group_manager", region_instance_group_manager)
        if minimal_action is not None:
            pulumi.set(__self__, "minimal_action", minimal_action)
        if most_disruptive_allowed_action is not None:
            pulumi.set(__self__, "most_disruptive_allowed_action", most_disruptive_allowed_action)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if preserved_state is not None:
            pulumi.set(__self__, "preserved_state", preserved_state)
        if project is not None:
            pulumi.set(__self__, "project", project)
        if region is not None:
            pulumi.set(__self__, "region", region)
        if remove_instance_state_on_destroy is not None:
            pulumi.set(__self__, "remove_instance_state_on_destroy", remove_instance_state_on_destroy)

    @property
    @pulumi.getter(name="regionInstanceGroupManager")
    def region_instance_group_manager(self) -> pulumi.Input[str]:
        """
        The region instance group manager this instance config is part of.
        """
        return pulumi.get(self, "region_instance_group_manager")

    @region_instance_group_manager.setter
    def region_instance_group_manager(self, value: pulumi.Input[str]):
        pulumi.set(self, "region_instance_group_manager", value)

    @property
    @pulumi.getter(name="minimalAction")
    def minimal_action(self) -> Optional[pulumi.Input[str]]:
        """
        The minimal action to perform on the instance during an update.
        Default is `NONE`. Possible values are:
        * REPLACE
        * RESTART
        * REFRESH
        * NONE
        """
        return pulumi.get(self, "minimal_action")

    @minimal_action.setter
    def minimal_action(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "minimal_action", value)

    @property
    @pulumi.getter(name="mostDisruptiveAllowedAction")
    def most_disruptive_allowed_action(self) -> Optional[pulumi.Input[str]]:
        """
        The most disruptive action to perform on the instance during an update.
        Default is `REPLACE`. Possible values are:
        * REPLACE
        * RESTART
        * REFRESH
        * NONE
        """
        return pulumi.get(self, "most_disruptive_allowed_action")

    @most_disruptive_allowed_action.setter
    def most_disruptive_allowed_action(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "most_disruptive_allowed_action", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name for this per-instance config and its corresponding instance.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="preservedState")
    def preserved_state(self) -> Optional[pulumi.Input['RegionPerInstanceConfigPreservedStateArgs']]:
        """
        The preserved state for this instance.
        Structure is documented below.
        """
        return pulumi.get(self, "preserved_state")

    @preserved_state.setter
    def preserved_state(self, value: Optional[pulumi.Input['RegionPerInstanceConfigPreservedStateArgs']]):
        pulumi.set(self, "preserved_state", value)

    @property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the project in which the resource belongs.
        If it is not provided, the provider project is used.
        """
        return pulumi.get(self, "project")

    @project.setter
    def project(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "project", value)

    @property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[str]]:
        """
        Region where the containing instance group manager is located
        """
        return pulumi.get(self, "region")

    @region.setter
    def region(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "region", value)

    @property
    @pulumi.getter(name="removeInstanceStateOnDestroy")
    def remove_instance_state_on_destroy(self) -> Optional[pulumi.Input[bool]]:
        """
        When true, deleting this config will immediately remove any specified state from the underlying instance.
        When false, deleting this config will *not* immediately remove any state from the underlying instance.
        State will be removed on the next instance recreation or update.
        """
        return pulumi.get(self, "remove_instance_state_on_destroy")

    @remove_instance_state_on_destroy.setter
    def remove_instance_state_on_destroy(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "remove_instance_state_on_destroy", value)


@pulumi.input_type
class _RegionPerInstanceConfigState:
    def __init__(__self__, *,
                 minimal_action: Optional[pulumi.Input[str]] = None,
                 most_disruptive_allowed_action: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 preserved_state: Optional[pulumi.Input['RegionPerInstanceConfigPreservedStateArgs']] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 region_instance_group_manager: Optional[pulumi.Input[str]] = None,
                 remove_instance_state_on_destroy: Optional[pulumi.Input[bool]] = None):
        """
        Input properties used for looking up and filtering RegionPerInstanceConfig resources.
        :param pulumi.Input[str] minimal_action: The minimal action to perform on the instance during an update.
               Default is `NONE`. Possible values are:
               * REPLACE
               * RESTART
               * REFRESH
               * NONE
        :param pulumi.Input[str] most_disruptive_allowed_action: The most disruptive action to perform on the instance during an update.
               Default is `REPLACE`. Possible values are:
               * REPLACE
               * RESTART
               * REFRESH
               * NONE
        :param pulumi.Input[str] name: The name for this per-instance config and its corresponding instance.
        :param pulumi.Input['RegionPerInstanceConfigPreservedStateArgs'] preserved_state: The preserved state for this instance.
               Structure is documented below.
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the provider project is used.
        :param pulumi.Input[str] region: Region where the containing instance group manager is located
        :param pulumi.Input[str] region_instance_group_manager: The region instance group manager this instance config is part of.
        :param pulumi.Input[bool] remove_instance_state_on_destroy: When true, deleting this config will immediately remove any specified state from the underlying instance.
               When false, deleting this config will *not* immediately remove any state from the underlying instance.
               State will be removed on the next instance recreation or update.
        """
        if minimal_action is not None:
            pulumi.set(__self__, "minimal_action", minimal_action)
        if most_disruptive_allowed_action is not None:
            pulumi.set(__self__, "most_disruptive_allowed_action", most_disruptive_allowed_action)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if preserved_state is not None:
            pulumi.set(__self__, "preserved_state", preserved_state)
        if project is not None:
            pulumi.set(__self__, "project", project)
        if region is not None:
            pulumi.set(__self__, "region", region)
        if region_instance_group_manager is not None:
            pulumi.set(__self__, "region_instance_group_manager", region_instance_group_manager)
        if remove_instance_state_on_destroy is not None:
            pulumi.set(__self__, "remove_instance_state_on_destroy", remove_instance_state_on_destroy)

    @property
    @pulumi.getter(name="minimalAction")
    def minimal_action(self) -> Optional[pulumi.Input[str]]:
        """
        The minimal action to perform on the instance during an update.
        Default is `NONE`. Possible values are:
        * REPLACE
        * RESTART
        * REFRESH
        * NONE
        """
        return pulumi.get(self, "minimal_action")

    @minimal_action.setter
    def minimal_action(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "minimal_action", value)

    @property
    @pulumi.getter(name="mostDisruptiveAllowedAction")
    def most_disruptive_allowed_action(self) -> Optional[pulumi.Input[str]]:
        """
        The most disruptive action to perform on the instance during an update.
        Default is `REPLACE`. Possible values are:
        * REPLACE
        * RESTART
        * REFRESH
        * NONE
        """
        return pulumi.get(self, "most_disruptive_allowed_action")

    @most_disruptive_allowed_action.setter
    def most_disruptive_allowed_action(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "most_disruptive_allowed_action", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name for this per-instance config and its corresponding instance.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="preservedState")
    def preserved_state(self) -> Optional[pulumi.Input['RegionPerInstanceConfigPreservedStateArgs']]:
        """
        The preserved state for this instance.
        Structure is documented below.
        """
        return pulumi.get(self, "preserved_state")

    @preserved_state.setter
    def preserved_state(self, value: Optional[pulumi.Input['RegionPerInstanceConfigPreservedStateArgs']]):
        pulumi.set(self, "preserved_state", value)

    @property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the project in which the resource belongs.
        If it is not provided, the provider project is used.
        """
        return pulumi.get(self, "project")

    @project.setter
    def project(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "project", value)

    @property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[str]]:
        """
        Region where the containing instance group manager is located
        """
        return pulumi.get(self, "region")

    @region.setter
    def region(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "region", value)

    @property
    @pulumi.getter(name="regionInstanceGroupManager")
    def region_instance_group_manager(self) -> Optional[pulumi.Input[str]]:
        """
        The region instance group manager this instance config is part of.
        """
        return pulumi.get(self, "region_instance_group_manager")

    @region_instance_group_manager.setter
    def region_instance_group_manager(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "region_instance_group_manager", value)

    @property
    @pulumi.getter(name="removeInstanceStateOnDestroy")
    def remove_instance_state_on_destroy(self) -> Optional[pulumi.Input[bool]]:
        """
        When true, deleting this config will immediately remove any specified state from the underlying instance.
        When false, deleting this config will *not* immediately remove any state from the underlying instance.
        State will be removed on the next instance recreation or update.
        """
        return pulumi.get(self, "remove_instance_state_on_destroy")

    @remove_instance_state_on_destroy.setter
    def remove_instance_state_on_destroy(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "remove_instance_state_on_destroy", value)


class RegionPerInstanceConfig(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 minimal_action: Optional[pulumi.Input[str]] = None,
                 most_disruptive_allowed_action: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 preserved_state: Optional[pulumi.Input[pulumi.InputType['RegionPerInstanceConfigPreservedStateArgs']]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 region_instance_group_manager: Optional[pulumi.Input[str]] = None,
                 remove_instance_state_on_destroy: Optional[pulumi.Input[bool]] = None,
                 __props__=None):
        """
        A config defined for a single managed instance that belongs to an instance group manager. It preserves the instance name
        across instance group manager operations and can define stateful disks or metadata that are unique to the instance.
        This resource works with regional instance group managers.

        To get more information about RegionPerInstanceConfig, see:

        * [API documentation](https://cloud.google.com/compute/docs/reference/rest/v1/instanceGroupManagers)
        * How-to Guides
            * [Official Documentation](https://cloud.google.com/compute/docs/instance-groups/stateful-migs#per-instance_configs)

        ## Example Usage
        ### Stateful Rigm

        ```python
        import pulumi
        import pulumi_gcp as gcp

        my_image = gcp.compute.get_image(family="debian-9",
            project="debian-cloud")
        igm_basic = gcp.compute.InstanceTemplate("igm-basic",
            machine_type="e2-medium",
            can_ip_forward=False,
            tags=[
                "foo",
                "bar",
            ],
            disks=[gcp.compute.InstanceTemplateDiskArgs(
                source_image=my_image.self_link,
                auto_delete=True,
                boot=True,
            )],
            network_interfaces=[gcp.compute.InstanceTemplateNetworkInterfaceArgs(
                network="default",
            )],
            service_account=gcp.compute.InstanceTemplateServiceAccountArgs(
                scopes=[
                    "userinfo-email",
                    "compute-ro",
                    "storage-ro",
                ],
            ))
        rigm = gcp.compute.RegionInstanceGroupManager("rigm",
            description="Demo test instance group manager",
            versions=[gcp.compute.RegionInstanceGroupManagerVersionArgs(
                name="prod",
                instance_template=igm_basic.self_link,
            )],
            update_policy=gcp.compute.RegionInstanceGroupManagerUpdatePolicyArgs(
                type="OPPORTUNISTIC",
                instance_redistribution_type="NONE",
                minimal_action="RESTART",
            ),
            base_instance_name="rigm",
            region="us-central1",
            target_size=2)
        default = gcp.compute.Disk("default",
            type="pd-ssd",
            zone="us-central1-a",
            image="debian-8-jessie-v20170523",
            physical_block_size_bytes=4096)
        with_disk = gcp.compute.RegionPerInstanceConfig("withDisk",
            region=google_compute_region_instance_group_manager["igm"]["region"],
            region_instance_group_manager=rigm.name,
            preserved_state=gcp.compute.RegionPerInstanceConfigPreservedStateArgs(
                metadata={
                    "foo": "bar",
                    "instance_template": igm_basic.self_link,
                },
                disks=[gcp.compute.RegionPerInstanceConfigPreservedStateDiskArgs(
                    device_name="my-stateful-disk",
                    source=default.id,
                    mode="READ_ONLY",
                )],
            ))
        ```

        ## Import

        RegionPerInstanceConfig can be imported using any of these accepted formats

        ```sh
         $ pulumi import gcp:compute/regionPerInstanceConfig:RegionPerInstanceConfig default projects/{{project}}/regions/{{region}}/instanceGroupManagers/{{region_instance_group_manager}}/{{name}}
        ```

        ```sh
         $ pulumi import gcp:compute/regionPerInstanceConfig:RegionPerInstanceConfig default {{project}}/{{region}}/{{region_instance_group_manager}}/{{name}}
        ```

        ```sh
         $ pulumi import gcp:compute/regionPerInstanceConfig:RegionPerInstanceConfig default {{region}}/{{region_instance_group_manager}}/{{name}}
        ```

        ```sh
         $ pulumi import gcp:compute/regionPerInstanceConfig:RegionPerInstanceConfig default {{region_instance_group_manager}}/{{name}}
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] minimal_action: The minimal action to perform on the instance during an update.
               Default is `NONE`. Possible values are:
               * REPLACE
               * RESTART
               * REFRESH
               * NONE
        :param pulumi.Input[str] most_disruptive_allowed_action: The most disruptive action to perform on the instance during an update.
               Default is `REPLACE`. Possible values are:
               * REPLACE
               * RESTART
               * REFRESH
               * NONE
        :param pulumi.Input[str] name: The name for this per-instance config and its corresponding instance.
        :param pulumi.Input[pulumi.InputType['RegionPerInstanceConfigPreservedStateArgs']] preserved_state: The preserved state for this instance.
               Structure is documented below.
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the provider project is used.
        :param pulumi.Input[str] region: Region where the containing instance group manager is located
        :param pulumi.Input[str] region_instance_group_manager: The region instance group manager this instance config is part of.
        :param pulumi.Input[bool] remove_instance_state_on_destroy: When true, deleting this config will immediately remove any specified state from the underlying instance.
               When false, deleting this config will *not* immediately remove any state from the underlying instance.
               State will be removed on the next instance recreation or update.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: RegionPerInstanceConfigArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        A config defined for a single managed instance that belongs to an instance group manager. It preserves the instance name
        across instance group manager operations and can define stateful disks or metadata that are unique to the instance.
        This resource works with regional instance group managers.

        To get more information about RegionPerInstanceConfig, see:

        * [API documentation](https://cloud.google.com/compute/docs/reference/rest/v1/instanceGroupManagers)
        * How-to Guides
            * [Official Documentation](https://cloud.google.com/compute/docs/instance-groups/stateful-migs#per-instance_configs)

        ## Example Usage
        ### Stateful Rigm

        ```python
        import pulumi
        import pulumi_gcp as gcp

        my_image = gcp.compute.get_image(family="debian-9",
            project="debian-cloud")
        igm_basic = gcp.compute.InstanceTemplate("igm-basic",
            machine_type="e2-medium",
            can_ip_forward=False,
            tags=[
                "foo",
                "bar",
            ],
            disks=[gcp.compute.InstanceTemplateDiskArgs(
                source_image=my_image.self_link,
                auto_delete=True,
                boot=True,
            )],
            network_interfaces=[gcp.compute.InstanceTemplateNetworkInterfaceArgs(
                network="default",
            )],
            service_account=gcp.compute.InstanceTemplateServiceAccountArgs(
                scopes=[
                    "userinfo-email",
                    "compute-ro",
                    "storage-ro",
                ],
            ))
        rigm = gcp.compute.RegionInstanceGroupManager("rigm",
            description="Demo test instance group manager",
            versions=[gcp.compute.RegionInstanceGroupManagerVersionArgs(
                name="prod",
                instance_template=igm_basic.self_link,
            )],
            update_policy=gcp.compute.RegionInstanceGroupManagerUpdatePolicyArgs(
                type="OPPORTUNISTIC",
                instance_redistribution_type="NONE",
                minimal_action="RESTART",
            ),
            base_instance_name="rigm",
            region="us-central1",
            target_size=2)
        default = gcp.compute.Disk("default",
            type="pd-ssd",
            zone="us-central1-a",
            image="debian-8-jessie-v20170523",
            physical_block_size_bytes=4096)
        with_disk = gcp.compute.RegionPerInstanceConfig("withDisk",
            region=google_compute_region_instance_group_manager["igm"]["region"],
            region_instance_group_manager=rigm.name,
            preserved_state=gcp.compute.RegionPerInstanceConfigPreservedStateArgs(
                metadata={
                    "foo": "bar",
                    "instance_template": igm_basic.self_link,
                },
                disks=[gcp.compute.RegionPerInstanceConfigPreservedStateDiskArgs(
                    device_name="my-stateful-disk",
                    source=default.id,
                    mode="READ_ONLY",
                )],
            ))
        ```

        ## Import

        RegionPerInstanceConfig can be imported using any of these accepted formats

        ```sh
         $ pulumi import gcp:compute/regionPerInstanceConfig:RegionPerInstanceConfig default projects/{{project}}/regions/{{region}}/instanceGroupManagers/{{region_instance_group_manager}}/{{name}}
        ```

        ```sh
         $ pulumi import gcp:compute/regionPerInstanceConfig:RegionPerInstanceConfig default {{project}}/{{region}}/{{region_instance_group_manager}}/{{name}}
        ```

        ```sh
         $ pulumi import gcp:compute/regionPerInstanceConfig:RegionPerInstanceConfig default {{region}}/{{region_instance_group_manager}}/{{name}}
        ```

        ```sh
         $ pulumi import gcp:compute/regionPerInstanceConfig:RegionPerInstanceConfig default {{region_instance_group_manager}}/{{name}}
        ```

        :param str resource_name: The name of the resource.
        :param RegionPerInstanceConfigArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(RegionPerInstanceConfigArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 minimal_action: Optional[pulumi.Input[str]] = None,
                 most_disruptive_allowed_action: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 preserved_state: Optional[pulumi.Input[pulumi.InputType['RegionPerInstanceConfigPreservedStateArgs']]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 region_instance_group_manager: Optional[pulumi.Input[str]] = None,
                 remove_instance_state_on_destroy: Optional[pulumi.Input[bool]] = None,
                 __props__=None):
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = _utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = RegionPerInstanceConfigArgs.__new__(RegionPerInstanceConfigArgs)

            __props__.__dict__["minimal_action"] = minimal_action
            __props__.__dict__["most_disruptive_allowed_action"] = most_disruptive_allowed_action
            __props__.__dict__["name"] = name
            __props__.__dict__["preserved_state"] = preserved_state
            __props__.__dict__["project"] = project
            __props__.__dict__["region"] = region
            if region_instance_group_manager is None and not opts.urn:
                raise TypeError("Missing required property 'region_instance_group_manager'")
            __props__.__dict__["region_instance_group_manager"] = region_instance_group_manager
            __props__.__dict__["remove_instance_state_on_destroy"] = remove_instance_state_on_destroy
        super(RegionPerInstanceConfig, __self__).__init__(
            'gcp:compute/regionPerInstanceConfig:RegionPerInstanceConfig',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            minimal_action: Optional[pulumi.Input[str]] = None,
            most_disruptive_allowed_action: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            preserved_state: Optional[pulumi.Input[pulumi.InputType['RegionPerInstanceConfigPreservedStateArgs']]] = None,
            project: Optional[pulumi.Input[str]] = None,
            region: Optional[pulumi.Input[str]] = None,
            region_instance_group_manager: Optional[pulumi.Input[str]] = None,
            remove_instance_state_on_destroy: Optional[pulumi.Input[bool]] = None) -> 'RegionPerInstanceConfig':
        """
        Get an existing RegionPerInstanceConfig resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] minimal_action: The minimal action to perform on the instance during an update.
               Default is `NONE`. Possible values are:
               * REPLACE
               * RESTART
               * REFRESH
               * NONE
        :param pulumi.Input[str] most_disruptive_allowed_action: The most disruptive action to perform on the instance during an update.
               Default is `REPLACE`. Possible values are:
               * REPLACE
               * RESTART
               * REFRESH
               * NONE
        :param pulumi.Input[str] name: The name for this per-instance config and its corresponding instance.
        :param pulumi.Input[pulumi.InputType['RegionPerInstanceConfigPreservedStateArgs']] preserved_state: The preserved state for this instance.
               Structure is documented below.
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the provider project is used.
        :param pulumi.Input[str] region: Region where the containing instance group manager is located
        :param pulumi.Input[str] region_instance_group_manager: The region instance group manager this instance config is part of.
        :param pulumi.Input[bool] remove_instance_state_on_destroy: When true, deleting this config will immediately remove any specified state from the underlying instance.
               When false, deleting this config will *not* immediately remove any state from the underlying instance.
               State will be removed on the next instance recreation or update.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _RegionPerInstanceConfigState.__new__(_RegionPerInstanceConfigState)

        __props__.__dict__["minimal_action"] = minimal_action
        __props__.__dict__["most_disruptive_allowed_action"] = most_disruptive_allowed_action
        __props__.__dict__["name"] = name
        __props__.__dict__["preserved_state"] = preserved_state
        __props__.__dict__["project"] = project
        __props__.__dict__["region"] = region
        __props__.__dict__["region_instance_group_manager"] = region_instance_group_manager
        __props__.__dict__["remove_instance_state_on_destroy"] = remove_instance_state_on_destroy
        return RegionPerInstanceConfig(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="minimalAction")
    def minimal_action(self) -> pulumi.Output[Optional[str]]:
        """
        The minimal action to perform on the instance during an update.
        Default is `NONE`. Possible values are:
        * REPLACE
        * RESTART
        * REFRESH
        * NONE
        """
        return pulumi.get(self, "minimal_action")

    @property
    @pulumi.getter(name="mostDisruptiveAllowedAction")
    def most_disruptive_allowed_action(self) -> pulumi.Output[Optional[str]]:
        """
        The most disruptive action to perform on the instance during an update.
        Default is `REPLACE`. Possible values are:
        * REPLACE
        * RESTART
        * REFRESH
        * NONE
        """
        return pulumi.get(self, "most_disruptive_allowed_action")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name for this per-instance config and its corresponding instance.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="preservedState")
    def preserved_state(self) -> pulumi.Output[Optional['outputs.RegionPerInstanceConfigPreservedState']]:
        """
        The preserved state for this instance.
        Structure is documented below.
        """
        return pulumi.get(self, "preserved_state")

    @property
    @pulumi.getter
    def project(self) -> pulumi.Output[str]:
        """
        The ID of the project in which the resource belongs.
        If it is not provided, the provider project is used.
        """
        return pulumi.get(self, "project")

    @property
    @pulumi.getter
    def region(self) -> pulumi.Output[str]:
        """
        Region where the containing instance group manager is located
        """
        return pulumi.get(self, "region")

    @property
    @pulumi.getter(name="regionInstanceGroupManager")
    def region_instance_group_manager(self) -> pulumi.Output[str]:
        """
        The region instance group manager this instance config is part of.
        """
        return pulumi.get(self, "region_instance_group_manager")

    @property
    @pulumi.getter(name="removeInstanceStateOnDestroy")
    def remove_instance_state_on_destroy(self) -> pulumi.Output[Optional[bool]]:
        """
        When true, deleting this config will immediately remove any specified state from the underlying instance.
        When false, deleting this config will *not* immediately remove any state from the underlying instance.
        State will be removed on the next instance recreation or update.
        """
        return pulumi.get(self, "remove_instance_state_on_destroy")

