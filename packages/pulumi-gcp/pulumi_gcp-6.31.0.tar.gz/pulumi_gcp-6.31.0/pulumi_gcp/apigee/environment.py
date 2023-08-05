# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['EnvironmentArgs', 'Environment']

@pulumi.input_type
class EnvironmentArgs:
    def __init__(__self__, *,
                 org_id: pulumi.Input[str],
                 api_proxy_type: Optional[pulumi.Input[str]] = None,
                 deployment_type: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Environment resource.
        :param pulumi.Input[str] org_id: The Apigee Organization associated with the Apigee environment,
               in the format `organizations/{{org_name}}`.
        :param pulumi.Input[str] api_proxy_type: Optional. API Proxy type supported by the environment. The type can be set when creating
               the Environment and cannot be changed.
               Possible values are `API_PROXY_TYPE_UNSPECIFIED`, `PROGRAMMABLE`, and `CONFIGURABLE`.
        :param pulumi.Input[str] deployment_type: Optional. Deployment type supported by the environment. The deployment type can be
               set when creating the environment and cannot be changed. When you enable archive
               deployment, you will be prevented from performing a subset of actions within the
               environment, including:
               Managing the deployment of API proxy or shared flow revisions;
               Creating, updating, or deleting resource files;
               Creating, updating, or deleting target servers.
               Possible values are `DEPLOYMENT_TYPE_UNSPECIFIED`, `PROXY`, and `ARCHIVE`.
        :param pulumi.Input[str] description: Description of the environment.
        :param pulumi.Input[str] display_name: Display name of the environment.
        :param pulumi.Input[str] name: The resource ID of the environment.
        """
        pulumi.set(__self__, "org_id", org_id)
        if api_proxy_type is not None:
            pulumi.set(__self__, "api_proxy_type", api_proxy_type)
        if deployment_type is not None:
            pulumi.set(__self__, "deployment_type", deployment_type)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if display_name is not None:
            pulumi.set(__self__, "display_name", display_name)
        if name is not None:
            pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter(name="orgId")
    def org_id(self) -> pulumi.Input[str]:
        """
        The Apigee Organization associated with the Apigee environment,
        in the format `organizations/{{org_name}}`.
        """
        return pulumi.get(self, "org_id")

    @org_id.setter
    def org_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "org_id", value)

    @property
    @pulumi.getter(name="apiProxyType")
    def api_proxy_type(self) -> Optional[pulumi.Input[str]]:
        """
        Optional. API Proxy type supported by the environment. The type can be set when creating
        the Environment and cannot be changed.
        Possible values are `API_PROXY_TYPE_UNSPECIFIED`, `PROGRAMMABLE`, and `CONFIGURABLE`.
        """
        return pulumi.get(self, "api_proxy_type")

    @api_proxy_type.setter
    def api_proxy_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "api_proxy_type", value)

    @property
    @pulumi.getter(name="deploymentType")
    def deployment_type(self) -> Optional[pulumi.Input[str]]:
        """
        Optional. Deployment type supported by the environment. The deployment type can be
        set when creating the environment and cannot be changed. When you enable archive
        deployment, you will be prevented from performing a subset of actions within the
        environment, including:
        Managing the deployment of API proxy or shared flow revisions;
        Creating, updating, or deleting resource files;
        Creating, updating, or deleting target servers.
        Possible values are `DEPLOYMENT_TYPE_UNSPECIFIED`, `PROXY`, and `ARCHIVE`.
        """
        return pulumi.get(self, "deployment_type")

    @deployment_type.setter
    def deployment_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "deployment_type", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        Description of the environment.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[str]]:
        """
        Display name of the environment.
        """
        return pulumi.get(self, "display_name")

    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "display_name", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The resource ID of the environment.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)


@pulumi.input_type
class _EnvironmentState:
    def __init__(__self__, *,
                 api_proxy_type: Optional[pulumi.Input[str]] = None,
                 deployment_type: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 org_id: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering Environment resources.
        :param pulumi.Input[str] api_proxy_type: Optional. API Proxy type supported by the environment. The type can be set when creating
               the Environment and cannot be changed.
               Possible values are `API_PROXY_TYPE_UNSPECIFIED`, `PROGRAMMABLE`, and `CONFIGURABLE`.
        :param pulumi.Input[str] deployment_type: Optional. Deployment type supported by the environment. The deployment type can be
               set when creating the environment and cannot be changed. When you enable archive
               deployment, you will be prevented from performing a subset of actions within the
               environment, including:
               Managing the deployment of API proxy or shared flow revisions;
               Creating, updating, or deleting resource files;
               Creating, updating, or deleting target servers.
               Possible values are `DEPLOYMENT_TYPE_UNSPECIFIED`, `PROXY`, and `ARCHIVE`.
        :param pulumi.Input[str] description: Description of the environment.
        :param pulumi.Input[str] display_name: Display name of the environment.
        :param pulumi.Input[str] name: The resource ID of the environment.
        :param pulumi.Input[str] org_id: The Apigee Organization associated with the Apigee environment,
               in the format `organizations/{{org_name}}`.
        """
        if api_proxy_type is not None:
            pulumi.set(__self__, "api_proxy_type", api_proxy_type)
        if deployment_type is not None:
            pulumi.set(__self__, "deployment_type", deployment_type)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if display_name is not None:
            pulumi.set(__self__, "display_name", display_name)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if org_id is not None:
            pulumi.set(__self__, "org_id", org_id)

    @property
    @pulumi.getter(name="apiProxyType")
    def api_proxy_type(self) -> Optional[pulumi.Input[str]]:
        """
        Optional. API Proxy type supported by the environment. The type can be set when creating
        the Environment and cannot be changed.
        Possible values are `API_PROXY_TYPE_UNSPECIFIED`, `PROGRAMMABLE`, and `CONFIGURABLE`.
        """
        return pulumi.get(self, "api_proxy_type")

    @api_proxy_type.setter
    def api_proxy_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "api_proxy_type", value)

    @property
    @pulumi.getter(name="deploymentType")
    def deployment_type(self) -> Optional[pulumi.Input[str]]:
        """
        Optional. Deployment type supported by the environment. The deployment type can be
        set when creating the environment and cannot be changed. When you enable archive
        deployment, you will be prevented from performing a subset of actions within the
        environment, including:
        Managing the deployment of API proxy or shared flow revisions;
        Creating, updating, or deleting resource files;
        Creating, updating, or deleting target servers.
        Possible values are `DEPLOYMENT_TYPE_UNSPECIFIED`, `PROXY`, and `ARCHIVE`.
        """
        return pulumi.get(self, "deployment_type")

    @deployment_type.setter
    def deployment_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "deployment_type", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        Description of the environment.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[str]]:
        """
        Display name of the environment.
        """
        return pulumi.get(self, "display_name")

    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "display_name", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The resource ID of the environment.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="orgId")
    def org_id(self) -> Optional[pulumi.Input[str]]:
        """
        The Apigee Organization associated with the Apigee environment,
        in the format `organizations/{{org_name}}`.
        """
        return pulumi.get(self, "org_id")

    @org_id.setter
    def org_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "org_id", value)


class Environment(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 api_proxy_type: Optional[pulumi.Input[str]] = None,
                 deployment_type: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 org_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        An `Environment` in Apigee.

        To get more information about Environment, see:

        * [API documentation](https://cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments/create)
        * How-to Guides
            * [Creating an environment](https://cloud.google.com/apigee/docs/api-platform/get-started/create-environment)

        ## Example Usage
        ### Apigee Environment Basic

        ```python
        import pulumi
        import pulumi_gcp as gcp

        current = gcp.organizations.get_client_config()
        apigee_network = gcp.compute.Network("apigeeNetwork")
        apigee_range = gcp.compute.GlobalAddress("apigeeRange",
            purpose="VPC_PEERING",
            address_type="INTERNAL",
            prefix_length=16,
            network=apigee_network.id)
        apigee_vpc_connection = gcp.servicenetworking.Connection("apigeeVpcConnection",
            network=apigee_network.id,
            service="servicenetworking.googleapis.com",
            reserved_peering_ranges=[apigee_range.name])
        apigee_org = gcp.apigee.Organization("apigeeOrg",
            analytics_region="us-central1",
            project_id=current.project,
            authorized_network=apigee_network.id,
            opts=pulumi.ResourceOptions(depends_on=[apigee_vpc_connection]))
        env = gcp.apigee.Environment("env",
            description="Apigee Environment",
            display_name="environment-1",
            org_id=apigee_org.id)
        ```

        ## Import

        Environment can be imported using any of these accepted formats

        ```sh
         $ pulumi import gcp:apigee/environment:Environment default {{org_id}}/environments/{{name}}
        ```

        ```sh
         $ pulumi import gcp:apigee/environment:Environment default {{org_id}}/{{name}}
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] api_proxy_type: Optional. API Proxy type supported by the environment. The type can be set when creating
               the Environment and cannot be changed.
               Possible values are `API_PROXY_TYPE_UNSPECIFIED`, `PROGRAMMABLE`, and `CONFIGURABLE`.
        :param pulumi.Input[str] deployment_type: Optional. Deployment type supported by the environment. The deployment type can be
               set when creating the environment and cannot be changed. When you enable archive
               deployment, you will be prevented from performing a subset of actions within the
               environment, including:
               Managing the deployment of API proxy or shared flow revisions;
               Creating, updating, or deleting resource files;
               Creating, updating, or deleting target servers.
               Possible values are `DEPLOYMENT_TYPE_UNSPECIFIED`, `PROXY`, and `ARCHIVE`.
        :param pulumi.Input[str] description: Description of the environment.
        :param pulumi.Input[str] display_name: Display name of the environment.
        :param pulumi.Input[str] name: The resource ID of the environment.
        :param pulumi.Input[str] org_id: The Apigee Organization associated with the Apigee environment,
               in the format `organizations/{{org_name}}`.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: EnvironmentArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        An `Environment` in Apigee.

        To get more information about Environment, see:

        * [API documentation](https://cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments/create)
        * How-to Guides
            * [Creating an environment](https://cloud.google.com/apigee/docs/api-platform/get-started/create-environment)

        ## Example Usage
        ### Apigee Environment Basic

        ```python
        import pulumi
        import pulumi_gcp as gcp

        current = gcp.organizations.get_client_config()
        apigee_network = gcp.compute.Network("apigeeNetwork")
        apigee_range = gcp.compute.GlobalAddress("apigeeRange",
            purpose="VPC_PEERING",
            address_type="INTERNAL",
            prefix_length=16,
            network=apigee_network.id)
        apigee_vpc_connection = gcp.servicenetworking.Connection("apigeeVpcConnection",
            network=apigee_network.id,
            service="servicenetworking.googleapis.com",
            reserved_peering_ranges=[apigee_range.name])
        apigee_org = gcp.apigee.Organization("apigeeOrg",
            analytics_region="us-central1",
            project_id=current.project,
            authorized_network=apigee_network.id,
            opts=pulumi.ResourceOptions(depends_on=[apigee_vpc_connection]))
        env = gcp.apigee.Environment("env",
            description="Apigee Environment",
            display_name="environment-1",
            org_id=apigee_org.id)
        ```

        ## Import

        Environment can be imported using any of these accepted formats

        ```sh
         $ pulumi import gcp:apigee/environment:Environment default {{org_id}}/environments/{{name}}
        ```

        ```sh
         $ pulumi import gcp:apigee/environment:Environment default {{org_id}}/{{name}}
        ```

        :param str resource_name: The name of the resource.
        :param EnvironmentArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(EnvironmentArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 api_proxy_type: Optional[pulumi.Input[str]] = None,
                 deployment_type: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 org_id: Optional[pulumi.Input[str]] = None,
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
            __props__ = EnvironmentArgs.__new__(EnvironmentArgs)

            __props__.__dict__["api_proxy_type"] = api_proxy_type
            __props__.__dict__["deployment_type"] = deployment_type
            __props__.__dict__["description"] = description
            __props__.__dict__["display_name"] = display_name
            __props__.__dict__["name"] = name
            if org_id is None and not opts.urn:
                raise TypeError("Missing required property 'org_id'")
            __props__.__dict__["org_id"] = org_id
        super(Environment, __self__).__init__(
            'gcp:apigee/environment:Environment',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            api_proxy_type: Optional[pulumi.Input[str]] = None,
            deployment_type: Optional[pulumi.Input[str]] = None,
            description: Optional[pulumi.Input[str]] = None,
            display_name: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            org_id: Optional[pulumi.Input[str]] = None) -> 'Environment':
        """
        Get an existing Environment resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] api_proxy_type: Optional. API Proxy type supported by the environment. The type can be set when creating
               the Environment and cannot be changed.
               Possible values are `API_PROXY_TYPE_UNSPECIFIED`, `PROGRAMMABLE`, and `CONFIGURABLE`.
        :param pulumi.Input[str] deployment_type: Optional. Deployment type supported by the environment. The deployment type can be
               set when creating the environment and cannot be changed. When you enable archive
               deployment, you will be prevented from performing a subset of actions within the
               environment, including:
               Managing the deployment of API proxy or shared flow revisions;
               Creating, updating, or deleting resource files;
               Creating, updating, or deleting target servers.
               Possible values are `DEPLOYMENT_TYPE_UNSPECIFIED`, `PROXY`, and `ARCHIVE`.
        :param pulumi.Input[str] description: Description of the environment.
        :param pulumi.Input[str] display_name: Display name of the environment.
        :param pulumi.Input[str] name: The resource ID of the environment.
        :param pulumi.Input[str] org_id: The Apigee Organization associated with the Apigee environment,
               in the format `organizations/{{org_name}}`.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _EnvironmentState.__new__(_EnvironmentState)

        __props__.__dict__["api_proxy_type"] = api_proxy_type
        __props__.__dict__["deployment_type"] = deployment_type
        __props__.__dict__["description"] = description
        __props__.__dict__["display_name"] = display_name
        __props__.__dict__["name"] = name
        __props__.__dict__["org_id"] = org_id
        return Environment(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="apiProxyType")
    def api_proxy_type(self) -> pulumi.Output[str]:
        """
        Optional. API Proxy type supported by the environment. The type can be set when creating
        the Environment and cannot be changed.
        Possible values are `API_PROXY_TYPE_UNSPECIFIED`, `PROGRAMMABLE`, and `CONFIGURABLE`.
        """
        return pulumi.get(self, "api_proxy_type")

    @property
    @pulumi.getter(name="deploymentType")
    def deployment_type(self) -> pulumi.Output[str]:
        """
        Optional. Deployment type supported by the environment. The deployment type can be
        set when creating the environment and cannot be changed. When you enable archive
        deployment, you will be prevented from performing a subset of actions within the
        environment, including:
        Managing the deployment of API proxy or shared flow revisions;
        Creating, updating, or deleting resource files;
        Creating, updating, or deleting target servers.
        Possible values are `DEPLOYMENT_TYPE_UNSPECIFIED`, `PROXY`, and `ARCHIVE`.
        """
        return pulumi.get(self, "deployment_type")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        Description of the environment.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[Optional[str]]:
        """
        Display name of the environment.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The resource ID of the environment.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="orgId")
    def org_id(self) -> pulumi.Output[str]:
        """
        The Apigee Organization associated with the Apigee environment,
        in the format `organizations/{{org_name}}`.
        """
        return pulumi.get(self, "org_id")

