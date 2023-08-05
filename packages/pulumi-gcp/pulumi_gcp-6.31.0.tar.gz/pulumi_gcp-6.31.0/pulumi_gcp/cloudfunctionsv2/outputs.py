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
    'FunctionBuildConfig',
    'FunctionBuildConfigSource',
    'FunctionBuildConfigSourceRepoSource',
    'FunctionBuildConfigSourceStorageSource',
    'FunctionEventTrigger',
    'FunctionIamBindingCondition',
    'FunctionIamMemberCondition',
    'FunctionServiceConfig',
]

@pulumi.output_type
class FunctionBuildConfig(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "dockerRepository":
            suggest = "docker_repository"
        elif key == "entryPoint":
            suggest = "entry_point"
        elif key == "environmentVariables":
            suggest = "environment_variables"
        elif key == "workerPool":
            suggest = "worker_pool"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in FunctionBuildConfig. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        FunctionBuildConfig.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        FunctionBuildConfig.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 build: Optional[str] = None,
                 docker_repository: Optional[str] = None,
                 entry_point: Optional[str] = None,
                 environment_variables: Optional[Mapping[str, str]] = None,
                 runtime: Optional[str] = None,
                 source: Optional['outputs.FunctionBuildConfigSource'] = None,
                 worker_pool: Optional[str] = None):
        """
        :param str build: -
               The Cloud Build name of the latest successful
               deployment of the function.
        :param str docker_repository: User managed repository created in Artifact Registry optionally with a customer managed encryption key.
        :param str entry_point: The name of the function (as defined in source code) that will be executed.
               Defaults to the resource name suffix, if not specified. For backward
               compatibility, if function with given name is not found, then the system
               will try to use function named "function". For Node.js this is name of a
               function exported by the module specified in source_location.
        :param Mapping[str, str] environment_variables: Environment variables that shall be available during function execution.
        :param str runtime: The runtime in which to run the function. Required when deploying a new
               function, optional when updating an existing function.
        :param 'FunctionBuildConfigSourceArgs' source: The location of the function source code.
               Structure is documented below.
        :param str worker_pool: Name of the Cloud Build Custom Worker Pool that should be used to build the function.
        """
        if build is not None:
            pulumi.set(__self__, "build", build)
        if docker_repository is not None:
            pulumi.set(__self__, "docker_repository", docker_repository)
        if entry_point is not None:
            pulumi.set(__self__, "entry_point", entry_point)
        if environment_variables is not None:
            pulumi.set(__self__, "environment_variables", environment_variables)
        if runtime is not None:
            pulumi.set(__self__, "runtime", runtime)
        if source is not None:
            pulumi.set(__self__, "source", source)
        if worker_pool is not None:
            pulumi.set(__self__, "worker_pool", worker_pool)

    @property
    @pulumi.getter
    def build(self) -> Optional[str]:
        """
        -
        The Cloud Build name of the latest successful
        deployment of the function.
        """
        return pulumi.get(self, "build")

    @property
    @pulumi.getter(name="dockerRepository")
    def docker_repository(self) -> Optional[str]:
        """
        User managed repository created in Artifact Registry optionally with a customer managed encryption key.
        """
        return pulumi.get(self, "docker_repository")

    @property
    @pulumi.getter(name="entryPoint")
    def entry_point(self) -> Optional[str]:
        """
        The name of the function (as defined in source code) that will be executed.
        Defaults to the resource name suffix, if not specified. For backward
        compatibility, if function with given name is not found, then the system
        will try to use function named "function". For Node.js this is name of a
        function exported by the module specified in source_location.
        """
        return pulumi.get(self, "entry_point")

    @property
    @pulumi.getter(name="environmentVariables")
    def environment_variables(self) -> Optional[Mapping[str, str]]:
        """
        Environment variables that shall be available during function execution.
        """
        return pulumi.get(self, "environment_variables")

    @property
    @pulumi.getter
    def runtime(self) -> Optional[str]:
        """
        The runtime in which to run the function. Required when deploying a new
        function, optional when updating an existing function.
        """
        return pulumi.get(self, "runtime")

    @property
    @pulumi.getter
    def source(self) -> Optional['outputs.FunctionBuildConfigSource']:
        """
        The location of the function source code.
        Structure is documented below.
        """
        return pulumi.get(self, "source")

    @property
    @pulumi.getter(name="workerPool")
    def worker_pool(self) -> Optional[str]:
        """
        Name of the Cloud Build Custom Worker Pool that should be used to build the function.
        """
        return pulumi.get(self, "worker_pool")


@pulumi.output_type
class FunctionBuildConfigSource(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "repoSource":
            suggest = "repo_source"
        elif key == "storageSource":
            suggest = "storage_source"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in FunctionBuildConfigSource. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        FunctionBuildConfigSource.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        FunctionBuildConfigSource.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 repo_source: Optional['outputs.FunctionBuildConfigSourceRepoSource'] = None,
                 storage_source: Optional['outputs.FunctionBuildConfigSourceStorageSource'] = None):
        """
        :param 'FunctionBuildConfigSourceRepoSourceArgs' repo_source: If provided, get the source from this location in a Cloud Source Repository.
               Structure is documented below.
        :param 'FunctionBuildConfigSourceStorageSourceArgs' storage_source: If provided, get the source from this location in Google Cloud Storage.
               Structure is documented below.
        """
        if repo_source is not None:
            pulumi.set(__self__, "repo_source", repo_source)
        if storage_source is not None:
            pulumi.set(__self__, "storage_source", storage_source)

    @property
    @pulumi.getter(name="repoSource")
    def repo_source(self) -> Optional['outputs.FunctionBuildConfigSourceRepoSource']:
        """
        If provided, get the source from this location in a Cloud Source Repository.
        Structure is documented below.
        """
        return pulumi.get(self, "repo_source")

    @property
    @pulumi.getter(name="storageSource")
    def storage_source(self) -> Optional['outputs.FunctionBuildConfigSourceStorageSource']:
        """
        If provided, get the source from this location in Google Cloud Storage.
        Structure is documented below.
        """
        return pulumi.get(self, "storage_source")


@pulumi.output_type
class FunctionBuildConfigSourceRepoSource(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "branchName":
            suggest = "branch_name"
        elif key == "commitSha":
            suggest = "commit_sha"
        elif key == "invertRegex":
            suggest = "invert_regex"
        elif key == "projectId":
            suggest = "project_id"
        elif key == "repoName":
            suggest = "repo_name"
        elif key == "tagName":
            suggest = "tag_name"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in FunctionBuildConfigSourceRepoSource. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        FunctionBuildConfigSourceRepoSource.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        FunctionBuildConfigSourceRepoSource.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 branch_name: Optional[str] = None,
                 commit_sha: Optional[str] = None,
                 dir: Optional[str] = None,
                 invert_regex: Optional[bool] = None,
                 project_id: Optional[str] = None,
                 repo_name: Optional[str] = None,
                 tag_name: Optional[str] = None):
        """
        :param str branch_name: Regex matching branches to build.
        :param str commit_sha: Regex matching tags to build.
        :param str dir: Directory, relative to the source root, in which to run the build.
        :param bool invert_regex: Only trigger a build if the revision regex does
               NOT match the revision regex.
        :param str project_id: ID of the project that owns the Cloud Source Repository. If omitted, the
               project ID requesting the build is assumed.
        :param str repo_name: Name of the Cloud Source Repository.
        :param str tag_name: Regex matching tags to build.
        """
        if branch_name is not None:
            pulumi.set(__self__, "branch_name", branch_name)
        if commit_sha is not None:
            pulumi.set(__self__, "commit_sha", commit_sha)
        if dir is not None:
            pulumi.set(__self__, "dir", dir)
        if invert_regex is not None:
            pulumi.set(__self__, "invert_regex", invert_regex)
        if project_id is not None:
            pulumi.set(__self__, "project_id", project_id)
        if repo_name is not None:
            pulumi.set(__self__, "repo_name", repo_name)
        if tag_name is not None:
            pulumi.set(__self__, "tag_name", tag_name)

    @property
    @pulumi.getter(name="branchName")
    def branch_name(self) -> Optional[str]:
        """
        Regex matching branches to build.
        """
        return pulumi.get(self, "branch_name")

    @property
    @pulumi.getter(name="commitSha")
    def commit_sha(self) -> Optional[str]:
        """
        Regex matching tags to build.
        """
        return pulumi.get(self, "commit_sha")

    @property
    @pulumi.getter
    def dir(self) -> Optional[str]:
        """
        Directory, relative to the source root, in which to run the build.
        """
        return pulumi.get(self, "dir")

    @property
    @pulumi.getter(name="invertRegex")
    def invert_regex(self) -> Optional[bool]:
        """
        Only trigger a build if the revision regex does
        NOT match the revision regex.
        """
        return pulumi.get(self, "invert_regex")

    @property
    @pulumi.getter(name="projectId")
    def project_id(self) -> Optional[str]:
        """
        ID of the project that owns the Cloud Source Repository. If omitted, the
        project ID requesting the build is assumed.
        """
        return pulumi.get(self, "project_id")

    @property
    @pulumi.getter(name="repoName")
    def repo_name(self) -> Optional[str]:
        """
        Name of the Cloud Source Repository.
        """
        return pulumi.get(self, "repo_name")

    @property
    @pulumi.getter(name="tagName")
    def tag_name(self) -> Optional[str]:
        """
        Regex matching tags to build.
        """
        return pulumi.get(self, "tag_name")


@pulumi.output_type
class FunctionBuildConfigSourceStorageSource(dict):
    def __init__(__self__, *,
                 bucket: Optional[str] = None,
                 generation: Optional[int] = None,
                 object: Optional[str] = None):
        """
        :param str bucket: Google Cloud Storage bucket containing the source
        :param int generation: Google Cloud Storage generation for the object. If the generation
               is omitted, the latest generation will be used.
        :param str object: Google Cloud Storage object containing the source.
        """
        if bucket is not None:
            pulumi.set(__self__, "bucket", bucket)
        if generation is not None:
            pulumi.set(__self__, "generation", generation)
        if object is not None:
            pulumi.set(__self__, "object", object)

    @property
    @pulumi.getter
    def bucket(self) -> Optional[str]:
        """
        Google Cloud Storage bucket containing the source
        """
        return pulumi.get(self, "bucket")

    @property
    @pulumi.getter
    def generation(self) -> Optional[int]:
        """
        Google Cloud Storage generation for the object. If the generation
        is omitted, the latest generation will be used.
        """
        return pulumi.get(self, "generation")

    @property
    @pulumi.getter
    def object(self) -> Optional[str]:
        """
        Google Cloud Storage object containing the source.
        """
        return pulumi.get(self, "object")


@pulumi.output_type
class FunctionEventTrigger(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "eventType":
            suggest = "event_type"
        elif key == "pubsubTopic":
            suggest = "pubsub_topic"
        elif key == "retryPolicy":
            suggest = "retry_policy"
        elif key == "serviceAccountEmail":
            suggest = "service_account_email"
        elif key == "triggerRegion":
            suggest = "trigger_region"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in FunctionEventTrigger. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        FunctionEventTrigger.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        FunctionEventTrigger.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 event_type: Optional[str] = None,
                 pubsub_topic: Optional[str] = None,
                 retry_policy: Optional[str] = None,
                 service_account_email: Optional[str] = None,
                 trigger: Optional[str] = None,
                 trigger_region: Optional[str] = None):
        """
        :param str event_type: Required. The type of event to observe.
        :param str pubsub_topic: The name of a Pub/Sub topic in the same project that will be used
               as the transport topic for the event delivery.
        :param str retry_policy: Describes the retry policy in case of function's execution failure.
               Retried execution is charged as any other execution.
               Possible values are `RETRY_POLICY_UNSPECIFIED`, `RETRY_POLICY_DO_NOT_RETRY`, and `RETRY_POLICY_RETRY`.
        :param str service_account_email: The email of the service account for this function.
        :param str trigger: -
               The resource name of the Eventarc trigger.
        :param str trigger_region: The region that the trigger will be in. The trigger will only receive
               events originating in this region. It can be the same
               region as the function, a different region or multi-region, or the global
               region. If not provided, defaults to the same region as the function.
        """
        if event_type is not None:
            pulumi.set(__self__, "event_type", event_type)
        if pubsub_topic is not None:
            pulumi.set(__self__, "pubsub_topic", pubsub_topic)
        if retry_policy is not None:
            pulumi.set(__self__, "retry_policy", retry_policy)
        if service_account_email is not None:
            pulumi.set(__self__, "service_account_email", service_account_email)
        if trigger is not None:
            pulumi.set(__self__, "trigger", trigger)
        if trigger_region is not None:
            pulumi.set(__self__, "trigger_region", trigger_region)

    @property
    @pulumi.getter(name="eventType")
    def event_type(self) -> Optional[str]:
        """
        Required. The type of event to observe.
        """
        return pulumi.get(self, "event_type")

    @property
    @pulumi.getter(name="pubsubTopic")
    def pubsub_topic(self) -> Optional[str]:
        """
        The name of a Pub/Sub topic in the same project that will be used
        as the transport topic for the event delivery.
        """
        return pulumi.get(self, "pubsub_topic")

    @property
    @pulumi.getter(name="retryPolicy")
    def retry_policy(self) -> Optional[str]:
        """
        Describes the retry policy in case of function's execution failure.
        Retried execution is charged as any other execution.
        Possible values are `RETRY_POLICY_UNSPECIFIED`, `RETRY_POLICY_DO_NOT_RETRY`, and `RETRY_POLICY_RETRY`.
        """
        return pulumi.get(self, "retry_policy")

    @property
    @pulumi.getter(name="serviceAccountEmail")
    def service_account_email(self) -> Optional[str]:
        """
        The email of the service account for this function.
        """
        return pulumi.get(self, "service_account_email")

    @property
    @pulumi.getter
    def trigger(self) -> Optional[str]:
        """
        -
        The resource name of the Eventarc trigger.
        """
        return pulumi.get(self, "trigger")

    @property
    @pulumi.getter(name="triggerRegion")
    def trigger_region(self) -> Optional[str]:
        """
        The region that the trigger will be in. The trigger will only receive
        events originating in this region. It can be the same
        region as the function, a different region or multi-region, or the global
        region. If not provided, defaults to the same region as the function.
        """
        return pulumi.get(self, "trigger_region")


@pulumi.output_type
class FunctionIamBindingCondition(dict):
    def __init__(__self__, *,
                 expression: str,
                 title: str,
                 description: Optional[str] = None):
        pulumi.set(__self__, "expression", expression)
        pulumi.set(__self__, "title", title)
        if description is not None:
            pulumi.set(__self__, "description", description)

    @property
    @pulumi.getter
    def expression(self) -> str:
        return pulumi.get(self, "expression")

    @property
    @pulumi.getter
    def title(self) -> str:
        return pulumi.get(self, "title")

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        return pulumi.get(self, "description")


@pulumi.output_type
class FunctionIamMemberCondition(dict):
    def __init__(__self__, *,
                 expression: str,
                 title: str,
                 description: Optional[str] = None):
        pulumi.set(__self__, "expression", expression)
        pulumi.set(__self__, "title", title)
        if description is not None:
            pulumi.set(__self__, "description", description)

    @property
    @pulumi.getter
    def expression(self) -> str:
        return pulumi.get(self, "expression")

    @property
    @pulumi.getter
    def title(self) -> str:
        return pulumi.get(self, "title")

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        return pulumi.get(self, "description")


@pulumi.output_type
class FunctionServiceConfig(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "allTrafficOnLatestRevision":
            suggest = "all_traffic_on_latest_revision"
        elif key == "availableMemory":
            suggest = "available_memory"
        elif key == "environmentVariables":
            suggest = "environment_variables"
        elif key == "gcfUri":
            suggest = "gcf_uri"
        elif key == "ingressSettings":
            suggest = "ingress_settings"
        elif key == "maxInstanceCount":
            suggest = "max_instance_count"
        elif key == "minInstanceCount":
            suggest = "min_instance_count"
        elif key == "serviceAccountEmail":
            suggest = "service_account_email"
        elif key == "timeoutSeconds":
            suggest = "timeout_seconds"
        elif key == "vpcConnector":
            suggest = "vpc_connector"
        elif key == "vpcConnectorEgressSettings":
            suggest = "vpc_connector_egress_settings"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in FunctionServiceConfig. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        FunctionServiceConfig.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        FunctionServiceConfig.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 all_traffic_on_latest_revision: Optional[bool] = None,
                 available_memory: Optional[str] = None,
                 environment_variables: Optional[Mapping[str, str]] = None,
                 gcf_uri: Optional[str] = None,
                 ingress_settings: Optional[str] = None,
                 max_instance_count: Optional[int] = None,
                 min_instance_count: Optional[int] = None,
                 service: Optional[str] = None,
                 service_account_email: Optional[str] = None,
                 timeout_seconds: Optional[int] = None,
                 uri: Optional[str] = None,
                 vpc_connector: Optional[str] = None,
                 vpc_connector_egress_settings: Optional[str] = None):
        """
        :param bool all_traffic_on_latest_revision: Whether 100% of traffic is routed to the latest revision. Defaults to true.
        :param str available_memory: The amount of memory available for a function.
               Defaults to 256M. Supported units are k, M, G, Mi, Gi. If no unit is
               supplied the value is interpreted as bytes.
        :param Mapping[str, str] environment_variables: Environment variables that shall be available during function execution.
        :param str gcf_uri: -
               URIs of the Service deployed
        :param str ingress_settings: Available ingress settings. Defaults to "ALLOW_ALL" if unspecified.
               Default value is `ALLOW_ALL`.
               Possible values are `ALLOW_ALL`, `ALLOW_INTERNAL_ONLY`, and `ALLOW_INTERNAL_AND_GCLB`.
        :param int max_instance_count: The limit on the maximum number of function instances that may coexist at a
               given time.
        :param int min_instance_count: The limit on the minimum number of function instances that may coexist at a
               given time.
        :param str service: Name of the service associated with a Function.
        :param str service_account_email: The email of the service account for this function.
        :param int timeout_seconds: The function execution timeout. Execution is considered failed and
               can be terminated if the function is not completed at the end of the
               timeout period. Defaults to 60 seconds.
        :param str uri: -
               URI of the Service deployed.
        :param str vpc_connector: The Serverless VPC Access connector that this cloud function can connect to.
        :param str vpc_connector_egress_settings: Available egress settings.
               Possible values are `VPC_CONNECTOR_EGRESS_SETTINGS_UNSPECIFIED`, `PRIVATE_RANGES_ONLY`, and `ALL_TRAFFIC`.
        """
        if all_traffic_on_latest_revision is not None:
            pulumi.set(__self__, "all_traffic_on_latest_revision", all_traffic_on_latest_revision)
        if available_memory is not None:
            pulumi.set(__self__, "available_memory", available_memory)
        if environment_variables is not None:
            pulumi.set(__self__, "environment_variables", environment_variables)
        if gcf_uri is not None:
            pulumi.set(__self__, "gcf_uri", gcf_uri)
        if ingress_settings is not None:
            pulumi.set(__self__, "ingress_settings", ingress_settings)
        if max_instance_count is not None:
            pulumi.set(__self__, "max_instance_count", max_instance_count)
        if min_instance_count is not None:
            pulumi.set(__self__, "min_instance_count", min_instance_count)
        if service is not None:
            pulumi.set(__self__, "service", service)
        if service_account_email is not None:
            pulumi.set(__self__, "service_account_email", service_account_email)
        if timeout_seconds is not None:
            pulumi.set(__self__, "timeout_seconds", timeout_seconds)
        if uri is not None:
            pulumi.set(__self__, "uri", uri)
        if vpc_connector is not None:
            pulumi.set(__self__, "vpc_connector", vpc_connector)
        if vpc_connector_egress_settings is not None:
            pulumi.set(__self__, "vpc_connector_egress_settings", vpc_connector_egress_settings)

    @property
    @pulumi.getter(name="allTrafficOnLatestRevision")
    def all_traffic_on_latest_revision(self) -> Optional[bool]:
        """
        Whether 100% of traffic is routed to the latest revision. Defaults to true.
        """
        return pulumi.get(self, "all_traffic_on_latest_revision")

    @property
    @pulumi.getter(name="availableMemory")
    def available_memory(self) -> Optional[str]:
        """
        The amount of memory available for a function.
        Defaults to 256M. Supported units are k, M, G, Mi, Gi. If no unit is
        supplied the value is interpreted as bytes.
        """
        return pulumi.get(self, "available_memory")

    @property
    @pulumi.getter(name="environmentVariables")
    def environment_variables(self) -> Optional[Mapping[str, str]]:
        """
        Environment variables that shall be available during function execution.
        """
        return pulumi.get(self, "environment_variables")

    @property
    @pulumi.getter(name="gcfUri")
    def gcf_uri(self) -> Optional[str]:
        """
        -
        URIs of the Service deployed
        """
        return pulumi.get(self, "gcf_uri")

    @property
    @pulumi.getter(name="ingressSettings")
    def ingress_settings(self) -> Optional[str]:
        """
        Available ingress settings. Defaults to "ALLOW_ALL" if unspecified.
        Default value is `ALLOW_ALL`.
        Possible values are `ALLOW_ALL`, `ALLOW_INTERNAL_ONLY`, and `ALLOW_INTERNAL_AND_GCLB`.
        """
        return pulumi.get(self, "ingress_settings")

    @property
    @pulumi.getter(name="maxInstanceCount")
    def max_instance_count(self) -> Optional[int]:
        """
        The limit on the maximum number of function instances that may coexist at a
        given time.
        """
        return pulumi.get(self, "max_instance_count")

    @property
    @pulumi.getter(name="minInstanceCount")
    def min_instance_count(self) -> Optional[int]:
        """
        The limit on the minimum number of function instances that may coexist at a
        given time.
        """
        return pulumi.get(self, "min_instance_count")

    @property
    @pulumi.getter
    def service(self) -> Optional[str]:
        """
        Name of the service associated with a Function.
        """
        return pulumi.get(self, "service")

    @property
    @pulumi.getter(name="serviceAccountEmail")
    def service_account_email(self) -> Optional[str]:
        """
        The email of the service account for this function.
        """
        return pulumi.get(self, "service_account_email")

    @property
    @pulumi.getter(name="timeoutSeconds")
    def timeout_seconds(self) -> Optional[int]:
        """
        The function execution timeout. Execution is considered failed and
        can be terminated if the function is not completed at the end of the
        timeout period. Defaults to 60 seconds.
        """
        return pulumi.get(self, "timeout_seconds")

    @property
    @pulumi.getter
    def uri(self) -> Optional[str]:
        """
        -
        URI of the Service deployed.
        """
        return pulumi.get(self, "uri")

    @property
    @pulumi.getter(name="vpcConnector")
    def vpc_connector(self) -> Optional[str]:
        """
        The Serverless VPC Access connector that this cloud function can connect to.
        """
        return pulumi.get(self, "vpc_connector")

    @property
    @pulumi.getter(name="vpcConnectorEgressSettings")
    def vpc_connector_egress_settings(self) -> Optional[str]:
        """
        Available egress settings.
        Possible values are `VPC_CONNECTOR_EGRESS_SETTINGS_UNSPECIFIED`, `PRIVATE_RANGES_ONLY`, and `ALL_TRAFFIC`.
        """
        return pulumi.get(self, "vpc_connector_egress_settings")


