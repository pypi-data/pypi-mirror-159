# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['SecretVersionArgs', 'SecretVersion']

@pulumi.input_type
class SecretVersionArgs:
    def __init__(__self__, *,
                 secret: pulumi.Input[str],
                 secret_data: pulumi.Input[str],
                 enabled: Optional[pulumi.Input[bool]] = None):
        """
        The set of arguments for constructing a SecretVersion resource.
        :param pulumi.Input[str] secret: Secret Manager secret resource
        :param pulumi.Input[str] secret_data: The secret data. Must be no larger than 64KiB.
               **Note**: This property is sensitive and will not be displayed in the plan.
        :param pulumi.Input[bool] enabled: The current state of the SecretVersion.
        """
        pulumi.set(__self__, "secret", secret)
        pulumi.set(__self__, "secret_data", secret_data)
        if enabled is not None:
            pulumi.set(__self__, "enabled", enabled)

    @property
    @pulumi.getter
    def secret(self) -> pulumi.Input[str]:
        """
        Secret Manager secret resource
        """
        return pulumi.get(self, "secret")

    @secret.setter
    def secret(self, value: pulumi.Input[str]):
        pulumi.set(self, "secret", value)

    @property
    @pulumi.getter(name="secretData")
    def secret_data(self) -> pulumi.Input[str]:
        """
        The secret data. Must be no larger than 64KiB.
        **Note**: This property is sensitive and will not be displayed in the plan.
        """
        return pulumi.get(self, "secret_data")

    @secret_data.setter
    def secret_data(self, value: pulumi.Input[str]):
        pulumi.set(self, "secret_data", value)

    @property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        The current state of the SecretVersion.
        """
        return pulumi.get(self, "enabled")

    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "enabled", value)


@pulumi.input_type
class _SecretVersionState:
    def __init__(__self__, *,
                 create_time: Optional[pulumi.Input[str]] = None,
                 destroy_time: Optional[pulumi.Input[str]] = None,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 secret: Optional[pulumi.Input[str]] = None,
                 secret_data: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering SecretVersion resources.
        :param pulumi.Input[str] create_time: The time at which the Secret was created.
        :param pulumi.Input[str] destroy_time: The time at which the Secret was destroyed. Only present if state is DESTROYED.
        :param pulumi.Input[bool] enabled: The current state of the SecretVersion.
        :param pulumi.Input[str] name: The resource name of the SecretVersion. Format: 'projects/{{project}}/secrets/{{secret_id}}/versions/{{version}}'
        :param pulumi.Input[str] secret: Secret Manager secret resource
        :param pulumi.Input[str] secret_data: The secret data. Must be no larger than 64KiB.
               **Note**: This property is sensitive and will not be displayed in the plan.
        """
        if create_time is not None:
            pulumi.set(__self__, "create_time", create_time)
        if destroy_time is not None:
            pulumi.set(__self__, "destroy_time", destroy_time)
        if enabled is not None:
            pulumi.set(__self__, "enabled", enabled)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if secret is not None:
            pulumi.set(__self__, "secret", secret)
        if secret_data is not None:
            pulumi.set(__self__, "secret_data", secret_data)

    @property
    @pulumi.getter(name="createTime")
    def create_time(self) -> Optional[pulumi.Input[str]]:
        """
        The time at which the Secret was created.
        """
        return pulumi.get(self, "create_time")

    @create_time.setter
    def create_time(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "create_time", value)

    @property
    @pulumi.getter(name="destroyTime")
    def destroy_time(self) -> Optional[pulumi.Input[str]]:
        """
        The time at which the Secret was destroyed. Only present if state is DESTROYED.
        """
        return pulumi.get(self, "destroy_time")

    @destroy_time.setter
    def destroy_time(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "destroy_time", value)

    @property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        The current state of the SecretVersion.
        """
        return pulumi.get(self, "enabled")

    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "enabled", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The resource name of the SecretVersion. Format: 'projects/{{project}}/secrets/{{secret_id}}/versions/{{version}}'
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def secret(self) -> Optional[pulumi.Input[str]]:
        """
        Secret Manager secret resource
        """
        return pulumi.get(self, "secret")

    @secret.setter
    def secret(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "secret", value)

    @property
    @pulumi.getter(name="secretData")
    def secret_data(self) -> Optional[pulumi.Input[str]]:
        """
        The secret data. Must be no larger than 64KiB.
        **Note**: This property is sensitive and will not be displayed in the plan.
        """
        return pulumi.get(self, "secret_data")

    @secret_data.setter
    def secret_data(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "secret_data", value)


class SecretVersion(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 secret: Optional[pulumi.Input[str]] = None,
                 secret_data: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        A secret version resource.

        > **Warning:** All arguments including `payload.secret_data` will be stored in the raw
        state as plain-text.

        ## Example Usage
        ### Secret Version Basic

        ```python
        import pulumi
        import pulumi_gcp as gcp

        secret_basic = gcp.secretmanager.Secret("secret-basic",
            secret_id="secret-version",
            labels={
                "label": "my-label",
            },
            replication=gcp.secretmanager.SecretReplicationArgs(
                automatic=True,
            ))
        secret_version_basic = gcp.secretmanager.SecretVersion("secret-version-basic",
            secret=secret_basic.id,
            secret_data="secret-data")
        ```

        ## Import

        SecretVersion can be imported using any of these accepted formats

        ```sh
         $ pulumi import gcp:secretmanager/secretVersion:SecretVersion default {{name}}/{{name}}
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] enabled: The current state of the SecretVersion.
        :param pulumi.Input[str] secret: Secret Manager secret resource
        :param pulumi.Input[str] secret_data: The secret data. Must be no larger than 64KiB.
               **Note**: This property is sensitive and will not be displayed in the plan.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: SecretVersionArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        A secret version resource.

        > **Warning:** All arguments including `payload.secret_data` will be stored in the raw
        state as plain-text.

        ## Example Usage
        ### Secret Version Basic

        ```python
        import pulumi
        import pulumi_gcp as gcp

        secret_basic = gcp.secretmanager.Secret("secret-basic",
            secret_id="secret-version",
            labels={
                "label": "my-label",
            },
            replication=gcp.secretmanager.SecretReplicationArgs(
                automatic=True,
            ))
        secret_version_basic = gcp.secretmanager.SecretVersion("secret-version-basic",
            secret=secret_basic.id,
            secret_data="secret-data")
        ```

        ## Import

        SecretVersion can be imported using any of these accepted formats

        ```sh
         $ pulumi import gcp:secretmanager/secretVersion:SecretVersion default {{name}}/{{name}}
        ```

        :param str resource_name: The name of the resource.
        :param SecretVersionArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(SecretVersionArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 secret: Optional[pulumi.Input[str]] = None,
                 secret_data: Optional[pulumi.Input[str]] = None,
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
            __props__ = SecretVersionArgs.__new__(SecretVersionArgs)

            __props__.__dict__["enabled"] = enabled
            if secret is None and not opts.urn:
                raise TypeError("Missing required property 'secret'")
            __props__.__dict__["secret"] = secret
            if secret_data is None and not opts.urn:
                raise TypeError("Missing required property 'secret_data'")
            __props__.__dict__["secret_data"] = secret_data
            __props__.__dict__["create_time"] = None
            __props__.__dict__["destroy_time"] = None
            __props__.__dict__["name"] = None
        super(SecretVersion, __self__).__init__(
            'gcp:secretmanager/secretVersion:SecretVersion',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            create_time: Optional[pulumi.Input[str]] = None,
            destroy_time: Optional[pulumi.Input[str]] = None,
            enabled: Optional[pulumi.Input[bool]] = None,
            name: Optional[pulumi.Input[str]] = None,
            secret: Optional[pulumi.Input[str]] = None,
            secret_data: Optional[pulumi.Input[str]] = None) -> 'SecretVersion':
        """
        Get an existing SecretVersion resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] create_time: The time at which the Secret was created.
        :param pulumi.Input[str] destroy_time: The time at which the Secret was destroyed. Only present if state is DESTROYED.
        :param pulumi.Input[bool] enabled: The current state of the SecretVersion.
        :param pulumi.Input[str] name: The resource name of the SecretVersion. Format: 'projects/{{project}}/secrets/{{secret_id}}/versions/{{version}}'
        :param pulumi.Input[str] secret: Secret Manager secret resource
        :param pulumi.Input[str] secret_data: The secret data. Must be no larger than 64KiB.
               **Note**: This property is sensitive and will not be displayed in the plan.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _SecretVersionState.__new__(_SecretVersionState)

        __props__.__dict__["create_time"] = create_time
        __props__.__dict__["destroy_time"] = destroy_time
        __props__.__dict__["enabled"] = enabled
        __props__.__dict__["name"] = name
        __props__.__dict__["secret"] = secret
        __props__.__dict__["secret_data"] = secret_data
        return SecretVersion(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="createTime")
    def create_time(self) -> pulumi.Output[str]:
        """
        The time at which the Secret was created.
        """
        return pulumi.get(self, "create_time")

    @property
    @pulumi.getter(name="destroyTime")
    def destroy_time(self) -> pulumi.Output[str]:
        """
        The time at which the Secret was destroyed. Only present if state is DESTROYED.
        """
        return pulumi.get(self, "destroy_time")

    @property
    @pulumi.getter
    def enabled(self) -> pulumi.Output[Optional[bool]]:
        """
        The current state of the SecretVersion.
        """
        return pulumi.get(self, "enabled")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The resource name of the SecretVersion. Format: 'projects/{{project}}/secrets/{{secret_id}}/versions/{{version}}'
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def secret(self) -> pulumi.Output[str]:
        """
        Secret Manager secret resource
        """
        return pulumi.get(self, "secret")

    @property
    @pulumi.getter(name="secretData")
    def secret_data(self) -> pulumi.Output[str]:
        """
        The secret data. Must be no larger than 64KiB.
        **Note**: This property is sensitive and will not be displayed in the plan.
        """
        return pulumi.get(self, "secret_data")

