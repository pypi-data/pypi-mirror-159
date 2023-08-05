"""
    Cisco Intersight

    Cisco Intersight is a management platform delivered as a service with embedded analytics for your Cisco and 3rd party IT infrastructure. This platform offers an intelligent level of management that enables IT organizations to analyze, simplify, and automate their environments in more advanced ways than the prior generations of tools. Cisco Intersight provides an integrated and intuitive management experience for resources in the traditional data center as well as at the edge. With flexible deployment options to address complex security needs, getting started with Intersight is quick and easy. Cisco Intersight has deep integration with Cisco UCS and HyperFlex systems allowing for remote deployment, configuration, and ongoing maintenance. The model-based deployment works for a single system in a remote location or hundreds of systems in a data center and enables rapid, standardized configuration and deployment. It also streamlines maintaining those systems whether you are working with small or very large configurations. The Intersight OpenAPI document defines the complete set of properties that are returned in the HTTP response. From that perspective, a client can expect that no additional properties are returned, unless these properties are explicitly defined in the OpenAPI document. However, when a client uses an older version of the Intersight OpenAPI document, the server may send additional properties because the software is more recent than the client. In that case, the client may receive properties that it does not know about. Some generated SDKs perform a strict validation of the HTTP response body against the OpenAPI document.  # noqa: E501

    The version of the OpenAPI document: 1.0.11-7078
    Contact: intersight@cisco.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from intersight.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    change_keys_js_to_python,
    convert_js_args_to_python_args,
    date,
    datetime,
    file_type,
    none_type,
    validate_get_composed_info,
    OpenApiModel
)
from intersight.exceptions import ApiAttributeError


def lazy_import():
    from intersight.model.comm_http_proxy_policy_relationship import CommHttpProxyPolicyRelationship
    from intersight.model.comm_ip_v4_interface import CommIpV4Interface
    from intersight.model.hyperflex_auto_support_policy_relationship import HyperflexAutoSupportPolicyRelationship
    from intersight.model.hyperflex_cluster_network_policy_relationship import HyperflexClusterNetworkPolicyRelationship
    from intersight.model.hyperflex_cluster_relationship import HyperflexClusterRelationship
    from intersight.model.hyperflex_cluster_storage_policy_relationship import HyperflexClusterStoragePolicyRelationship
    from intersight.model.hyperflex_config_result_relationship import HyperflexConfigResultRelationship
    from intersight.model.hyperflex_ext_fc_storage_policy_relationship import HyperflexExtFcStoragePolicyRelationship
    from intersight.model.hyperflex_ext_iscsi_storage_policy_relationship import HyperflexExtIscsiStoragePolicyRelationship
    from intersight.model.hyperflex_local_credential_policy_relationship import HyperflexLocalCredentialPolicyRelationship
    from intersight.model.hyperflex_named_vlan import HyperflexNamedVlan
    from intersight.model.hyperflex_node_config_policy_relationship import HyperflexNodeConfigPolicyRelationship
    from intersight.model.hyperflex_node_profile_relationship import HyperflexNodeProfileRelationship
    from intersight.model.hyperflex_proxy_setting_policy_relationship import HyperflexProxySettingPolicyRelationship
    from intersight.model.hyperflex_software_version_policy_relationship import HyperflexSoftwareVersionPolicyRelationship
    from intersight.model.hyperflex_sys_config_policy_relationship import HyperflexSysConfigPolicyRelationship
    from intersight.model.hyperflex_ucsm_config_policy_relationship import HyperflexUcsmConfigPolicyRelationship
    from intersight.model.hyperflex_vcenter_config_policy_relationship import HyperflexVcenterConfigPolicyRelationship
    from intersight.model.organization_organization_relationship import OrganizationOrganizationRelationship
    from intersight.model.virtualization_iwe_cluster_relationship import VirtualizationIweClusterRelationship
    from intersight.model.workflow_workflow_info_relationship import WorkflowWorkflowInfoRelationship
    globals()['CommHttpProxyPolicyRelationship'] = CommHttpProxyPolicyRelationship
    globals()['CommIpV4Interface'] = CommIpV4Interface
    globals()['HyperflexAutoSupportPolicyRelationship'] = HyperflexAutoSupportPolicyRelationship
    globals()['HyperflexClusterNetworkPolicyRelationship'] = HyperflexClusterNetworkPolicyRelationship
    globals()['HyperflexClusterRelationship'] = HyperflexClusterRelationship
    globals()['HyperflexClusterStoragePolicyRelationship'] = HyperflexClusterStoragePolicyRelationship
    globals()['HyperflexConfigResultRelationship'] = HyperflexConfigResultRelationship
    globals()['HyperflexExtFcStoragePolicyRelationship'] = HyperflexExtFcStoragePolicyRelationship
    globals()['HyperflexExtIscsiStoragePolicyRelationship'] = HyperflexExtIscsiStoragePolicyRelationship
    globals()['HyperflexLocalCredentialPolicyRelationship'] = HyperflexLocalCredentialPolicyRelationship
    globals()['HyperflexNamedVlan'] = HyperflexNamedVlan
    globals()['HyperflexNodeConfigPolicyRelationship'] = HyperflexNodeConfigPolicyRelationship
    globals()['HyperflexNodeProfileRelationship'] = HyperflexNodeProfileRelationship
    globals()['HyperflexProxySettingPolicyRelationship'] = HyperflexProxySettingPolicyRelationship
    globals()['HyperflexSoftwareVersionPolicyRelationship'] = HyperflexSoftwareVersionPolicyRelationship
    globals()['HyperflexSysConfigPolicyRelationship'] = HyperflexSysConfigPolicyRelationship
    globals()['HyperflexUcsmConfigPolicyRelationship'] = HyperflexUcsmConfigPolicyRelationship
    globals()['HyperflexVcenterConfigPolicyRelationship'] = HyperflexVcenterConfigPolicyRelationship
    globals()['OrganizationOrganizationRelationship'] = OrganizationOrganizationRelationship
    globals()['VirtualizationIweClusterRelationship'] = VirtualizationIweClusterRelationship
    globals()['WorkflowWorkflowInfoRelationship'] = WorkflowWorkflowInfoRelationship


class HyperflexClusterProfileAllOf(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {
        ('class_id',): {
            'HYPERFLEX.CLUSTERPROFILE': "hyperflex.ClusterProfile",
        },
        ('object_type',): {
            'HYPERFLEX.CLUSTERPROFILE': "hyperflex.ClusterProfile",
        },
        ('hypervisor_type',): {
            'ESXI': "ESXi",
            'HYPERFLEXAP': "HyperFlexAp",
            'IWE': "IWE",
            'HYPER-V': "Hyper-V",
            'UNKNOWN': "Unknown",
        },
        ('mgmt_platform',): {
            'FI': "FI",
            'EDGE': "EDGE",
        },
        ('storage_type',): {
            'HYPERFLEXDP': "HyperFlexDp",
            'THIRDPARTY': "ThirdParty",
        },
    }

    validations = {
        ('data_ip_address',): {
            'regex': {
                'pattern': r'^$|^([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])$',  # noqa: E501
            },
        },
        ('host_name_prefix',): {
            'regex': {
                'pattern': r'^$|^[a-zA-Z0-9][a-zA-Z0-9-]{1,59}$',  # noqa: E501
            },
        },
        ('hypervisor_control_ip_address',): {
            'regex': {
                'pattern': r'^$|^([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])$',  # noqa: E501
            },
        },
        ('mac_address_prefix',): {
            'regex': {
                'pattern': r'^$|^00:25:B5:[0-9a-fA-F]{2}$',  # noqa: E501
            },
        },
        ('mgmt_ip_address',): {
            'regex': {
                'pattern': r'^$|^([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])$',  # noqa: E501
            },
        },
        ('storage_client_ip_address',): {
            'regex': {
                'pattern': r'^$|^([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])$',  # noqa: E501
            },
        },
        ('storage_cluster_auxiliary_ip',): {
            'regex': {
                'pattern': r'^$|^([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])$',  # noqa: E501
            },
        },
        ('wwxn_prefix',): {
            'regex': {
                'pattern': r'^$|^20:00:00:25:B5:[0-9a-fA-F]{2}$',  # noqa: E501
            },
        },
    }

    @cached_property
    def additional_properties_type():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded
        """
        lazy_import()
        return (bool, date, datetime, dict, float, int, list, str, none_type,)  # noqa: E501

    _nullable = False

    @cached_property
    def openapi_types():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        lazy_import()
        return {
            'class_id': (str,),  # noqa: E501
            'object_type': (str,),  # noqa: E501
            'cluster_internal_subnet': (CommIpV4Interface,),  # noqa: E501
            'data_ip_address': (str,),  # noqa: E501
            'host_name_prefix': (str,),  # noqa: E501
            'hypervisor_control_ip_address': (str,),  # noqa: E501
            'hypervisor_type': (str,),  # noqa: E501
            'mac_address_prefix': (str,),  # noqa: E501
            'mgmt_ip_address': (str,),  # noqa: E501
            'mgmt_platform': (str,),  # noqa: E501
            'replication': (int,),  # noqa: E501
            'storage_client_ip_address': (str,),  # noqa: E501
            'storage_client_netmask': (str,),  # noqa: E501
            'storage_client_vlan': (HyperflexNamedVlan,),  # noqa: E501
            'storage_cluster_auxiliary_ip': (str,),  # noqa: E501
            'storage_data_vlan': (HyperflexNamedVlan,),  # noqa: E501
            'storage_type': (str,),  # noqa: E501
            'wwxn_prefix': (str,),  # noqa: E501
            'associated_cluster': (HyperflexClusterRelationship,),  # noqa: E501
            'associated_compute_cluster': (VirtualizationIweClusterRelationship,),  # noqa: E501
            'auto_support': (HyperflexAutoSupportPolicyRelationship,),  # noqa: E501
            'cluster_network': (HyperflexClusterNetworkPolicyRelationship,),  # noqa: E501
            'cluster_storage': (HyperflexClusterStoragePolicyRelationship,),  # noqa: E501
            'config_result': (HyperflexConfigResultRelationship,),  # noqa: E501
            'ext_fc_storage': (HyperflexExtFcStoragePolicyRelationship,),  # noqa: E501
            'ext_iscsi_storage': (HyperflexExtIscsiStoragePolicyRelationship,),  # noqa: E501
            'httpproxypolicy': (CommHttpProxyPolicyRelationship,),  # noqa: E501
            'local_credential': (HyperflexLocalCredentialPolicyRelationship,),  # noqa: E501
            'node_config': (HyperflexNodeConfigPolicyRelationship,),  # noqa: E501
            'node_profile_config': ([HyperflexNodeProfileRelationship], none_type,),  # noqa: E501
            'organization': (OrganizationOrganizationRelationship,),  # noqa: E501
            'proxy_setting': (HyperflexProxySettingPolicyRelationship,),  # noqa: E501
            'running_workflows': ([WorkflowWorkflowInfoRelationship], none_type,),  # noqa: E501
            'software_version': (HyperflexSoftwareVersionPolicyRelationship,),  # noqa: E501
            'sys_config': (HyperflexSysConfigPolicyRelationship,),  # noqa: E501
            'ucsm_config': (HyperflexUcsmConfigPolicyRelationship,),  # noqa: E501
            'vcenter_config': (HyperflexVcenterConfigPolicyRelationship,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'class_id': 'ClassId',  # noqa: E501
        'object_type': 'ObjectType',  # noqa: E501
        'cluster_internal_subnet': 'ClusterInternalSubnet',  # noqa: E501
        'data_ip_address': 'DataIpAddress',  # noqa: E501
        'host_name_prefix': 'HostNamePrefix',  # noqa: E501
        'hypervisor_control_ip_address': 'HypervisorControlIpAddress',  # noqa: E501
        'hypervisor_type': 'HypervisorType',  # noqa: E501
        'mac_address_prefix': 'MacAddressPrefix',  # noqa: E501
        'mgmt_ip_address': 'MgmtIpAddress',  # noqa: E501
        'mgmt_platform': 'MgmtPlatform',  # noqa: E501
        'replication': 'Replication',  # noqa: E501
        'storage_client_ip_address': 'StorageClientIpAddress',  # noqa: E501
        'storage_client_netmask': 'StorageClientNetmask',  # noqa: E501
        'storage_client_vlan': 'StorageClientVlan',  # noqa: E501
        'storage_cluster_auxiliary_ip': 'StorageClusterAuxiliaryIp',  # noqa: E501
        'storage_data_vlan': 'StorageDataVlan',  # noqa: E501
        'storage_type': 'StorageType',  # noqa: E501
        'wwxn_prefix': 'WwxnPrefix',  # noqa: E501
        'associated_cluster': 'AssociatedCluster',  # noqa: E501
        'associated_compute_cluster': 'AssociatedComputeCluster',  # noqa: E501
        'auto_support': 'AutoSupport',  # noqa: E501
        'cluster_network': 'ClusterNetwork',  # noqa: E501
        'cluster_storage': 'ClusterStorage',  # noqa: E501
        'config_result': 'ConfigResult',  # noqa: E501
        'ext_fc_storage': 'ExtFcStorage',  # noqa: E501
        'ext_iscsi_storage': 'ExtIscsiStorage',  # noqa: E501
        'httpproxypolicy': 'Httpproxypolicy',  # noqa: E501
        'local_credential': 'LocalCredential',  # noqa: E501
        'node_config': 'NodeConfig',  # noqa: E501
        'node_profile_config': 'NodeProfileConfig',  # noqa: E501
        'organization': 'Organization',  # noqa: E501
        'proxy_setting': 'ProxySetting',  # noqa: E501
        'running_workflows': 'RunningWorkflows',  # noqa: E501
        'software_version': 'SoftwareVersion',  # noqa: E501
        'sys_config': 'SysConfig',  # noqa: E501
        'ucsm_config': 'UcsmConfig',  # noqa: E501
        'vcenter_config': 'VcenterConfig',  # noqa: E501
    }

    read_only_vars = {
        'running_workflows',  # noqa: E501
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):  # noqa: E501
        """HyperflexClusterProfileAllOf - a model defined in OpenAPI

        Args:

        Keyword Args:
            class_id (str): The fully-qualified name of the instantiated, concrete type. This property is used as a discriminator to identify the type of the payload when marshaling and unmarshaling data.. defaults to "hyperflex.ClusterProfile", must be one of ["hyperflex.ClusterProfile", ]  # noqa: E501
            object_type (str): The fully-qualified name of the instantiated, concrete type. The value should be the same as the 'ClassId' property.. defaults to "hyperflex.ClusterProfile", must be one of ["hyperflex.ClusterProfile", ]  # noqa: E501
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            cluster_internal_subnet (CommIpV4Interface): [optional]  # noqa: E501
            data_ip_address (str): The storage data IP address for the HyperFlex cluster.. [optional]  # noqa: E501
            host_name_prefix (str): The node name prefix that is used to automatically generate the default hostname for each server. A dash (-) will be appended to the prefix followed by the node number to form a hostname. This default naming scheme can be manually overridden in the node configuration. The maximum length of a prefix is 60, must only contain alphanumeric characters or dash (-), and must start with an alphanumeric character.. [optional]  # noqa: E501
            hypervisor_control_ip_address (str): The hypervisor control virtual IP address for the HyperFlex compute cluster that is used for node/pod management.. [optional]  # noqa: E501
            hypervisor_type (str): The hypervisor type for the HyperFlex cluster. * `ESXi` - The hypervisor running on the HyperFlex cluster is a Vmware ESXi hypervisor of any version. * `HyperFlexAp` - The hypervisor of the virtualization platform is Cisco HyperFlex Application Platform. * `IWE` - The hypervisor of the virtualization platform is Cisco Intersight Workload Engine. * `Hyper-V` - The hypervisor running on the HyperFlex cluster is Microsoft Hyper-V. * `Unknown` - The hypervisor running on the HyperFlex cluster is not known.. [optional] if omitted the server will use the default value of "ESXi"  # noqa: E501
            mac_address_prefix (str): The MAC address prefix in the form of 00:25:B5:XX.. [optional]  # noqa: E501
            mgmt_ip_address (str): The management IP address for the HyperFlex cluster.. [optional]  # noqa: E501
            mgmt_platform (str): The management platform for the HyperFlex cluster. * `FI` - The host servers used in the cluster deployment are managed by a UCS Fabric Interconnect. * `EDGE` - The host servers used in the cluster deployment are standalone severs.. [optional] if omitted the server will use the default value of "FI"  # noqa: E501
            replication (int): The number of copies of each data block written.. [optional]  # noqa: E501
            storage_client_ip_address (str): The storage data IP address for the HyperFlex cluster.. [optional]  # noqa: E501
            storage_client_netmask (str): The netmask for the Storage client network IP address.. [optional]  # noqa: E501
            storage_client_vlan (HyperflexNamedVlan): [optional]  # noqa: E501
            storage_cluster_auxiliary_ip (str): The auxiliary storage IP address for the HyperFlex cluster. For two node clusters, this is the IP address of the auxiliary ZK controller.. [optional]  # noqa: E501
            storage_data_vlan (HyperflexNamedVlan): [optional]  # noqa: E501
            storage_type (str): The storage type used for the HyperFlex cluster (HyperFlex Storage or 3rd party). * `HyperFlexDp` - The type of storage is HyperFlex Data Platform. * `ThirdParty` - The type of storage is 3rd Party Storage (PureStorage, etc..).. [optional] if omitted the server will use the default value of "HyperFlexDp"  # noqa: E501
            wwxn_prefix (str): The WWxN prefix in the form of 20:00:00:25:B5:XX.. [optional]  # noqa: E501
            associated_cluster (HyperflexClusterRelationship): [optional]  # noqa: E501
            associated_compute_cluster (VirtualizationIweClusterRelationship): [optional]  # noqa: E501
            auto_support (HyperflexAutoSupportPolicyRelationship): [optional]  # noqa: E501
            cluster_network (HyperflexClusterNetworkPolicyRelationship): [optional]  # noqa: E501
            cluster_storage (HyperflexClusterStoragePolicyRelationship): [optional]  # noqa: E501
            config_result (HyperflexConfigResultRelationship): [optional]  # noqa: E501
            ext_fc_storage (HyperflexExtFcStoragePolicyRelationship): [optional]  # noqa: E501
            ext_iscsi_storage (HyperflexExtIscsiStoragePolicyRelationship): [optional]  # noqa: E501
            httpproxypolicy (CommHttpProxyPolicyRelationship): [optional]  # noqa: E501
            local_credential (HyperflexLocalCredentialPolicyRelationship): [optional]  # noqa: E501
            node_config (HyperflexNodeConfigPolicyRelationship): [optional]  # noqa: E501
            node_profile_config ([HyperflexNodeProfileRelationship], none_type): An array of relationships to hyperflexNodeProfile resources.. [optional]  # noqa: E501
            organization (OrganizationOrganizationRelationship): [optional]  # noqa: E501
            proxy_setting (HyperflexProxySettingPolicyRelationship): [optional]  # noqa: E501
            running_workflows ([WorkflowWorkflowInfoRelationship], none_type): An array of relationships to workflowWorkflowInfo resources.. [optional]  # noqa: E501
            software_version (HyperflexSoftwareVersionPolicyRelationship): [optional]  # noqa: E501
            sys_config (HyperflexSysConfigPolicyRelationship): [optional]  # noqa: E501
            ucsm_config (HyperflexUcsmConfigPolicyRelationship): [optional]  # noqa: E501
            vcenter_config (HyperflexVcenterConfigPolicyRelationship): [optional]  # noqa: E501
        """

        class_id = kwargs.get('class_id', "hyperflex.ClusterProfile")
        object_type = kwargs.get('object_type', "hyperflex.ClusterProfile")
        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', True)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        self = super(OpenApiModel, cls).__new__(cls)

        if args:
            for arg in args:
                if isinstance(arg, dict):
                    kwargs.update(arg)
                else:
                    raise ApiTypeError(
                        "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                            args,
                            self.__class__.__name__,
                        ),
                        path_to_item=_path_to_item,
                        valid_classes=(self.__class__,),
                    )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        self.class_id = class_id
        self.object_type = object_type
        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
        return self

    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
    ])

    @convert_js_args_to_python_args
    def __init__(self, *args, **kwargs):  # noqa: E501
        """HyperflexClusterProfileAllOf - a model defined in OpenAPI

        Args:

        Keyword Args:
            class_id (str): The fully-qualified name of the instantiated, concrete type. This property is used as a discriminator to identify the type of the payload when marshaling and unmarshaling data.. defaults to "hyperflex.ClusterProfile", must be one of ["hyperflex.ClusterProfile", ]  # noqa: E501
            object_type (str): The fully-qualified name of the instantiated, concrete type. The value should be the same as the 'ClassId' property.. defaults to "hyperflex.ClusterProfile", must be one of ["hyperflex.ClusterProfile", ]  # noqa: E501
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            cluster_internal_subnet (CommIpV4Interface): [optional]  # noqa: E501
            data_ip_address (str): The storage data IP address for the HyperFlex cluster.. [optional]  # noqa: E501
            host_name_prefix (str): The node name prefix that is used to automatically generate the default hostname for each server. A dash (-) will be appended to the prefix followed by the node number to form a hostname. This default naming scheme can be manually overridden in the node configuration. The maximum length of a prefix is 60, must only contain alphanumeric characters or dash (-), and must start with an alphanumeric character.. [optional]  # noqa: E501
            hypervisor_control_ip_address (str): The hypervisor control virtual IP address for the HyperFlex compute cluster that is used for node/pod management.. [optional]  # noqa: E501
            hypervisor_type (str): The hypervisor type for the HyperFlex cluster. * `ESXi` - The hypervisor running on the HyperFlex cluster is a Vmware ESXi hypervisor of any version. * `HyperFlexAp` - The hypervisor of the virtualization platform is Cisco HyperFlex Application Platform. * `IWE` - The hypervisor of the virtualization platform is Cisco Intersight Workload Engine. * `Hyper-V` - The hypervisor running on the HyperFlex cluster is Microsoft Hyper-V. * `Unknown` - The hypervisor running on the HyperFlex cluster is not known.. [optional] if omitted the server will use the default value of "ESXi"  # noqa: E501
            mac_address_prefix (str): The MAC address prefix in the form of 00:25:B5:XX.. [optional]  # noqa: E501
            mgmt_ip_address (str): The management IP address for the HyperFlex cluster.. [optional]  # noqa: E501
            mgmt_platform (str): The management platform for the HyperFlex cluster. * `FI` - The host servers used in the cluster deployment are managed by a UCS Fabric Interconnect. * `EDGE` - The host servers used in the cluster deployment are standalone severs.. [optional] if omitted the server will use the default value of "FI"  # noqa: E501
            replication (int): The number of copies of each data block written.. [optional]  # noqa: E501
            storage_client_ip_address (str): The storage data IP address for the HyperFlex cluster.. [optional]  # noqa: E501
            storage_client_netmask (str): The netmask for the Storage client network IP address.. [optional]  # noqa: E501
            storage_client_vlan (HyperflexNamedVlan): [optional]  # noqa: E501
            storage_cluster_auxiliary_ip (str): The auxiliary storage IP address for the HyperFlex cluster. For two node clusters, this is the IP address of the auxiliary ZK controller.. [optional]  # noqa: E501
            storage_data_vlan (HyperflexNamedVlan): [optional]  # noqa: E501
            storage_type (str): The storage type used for the HyperFlex cluster (HyperFlex Storage or 3rd party). * `HyperFlexDp` - The type of storage is HyperFlex Data Platform. * `ThirdParty` - The type of storage is 3rd Party Storage (PureStorage, etc..).. [optional] if omitted the server will use the default value of "HyperFlexDp"  # noqa: E501
            wwxn_prefix (str): The WWxN prefix in the form of 20:00:00:25:B5:XX.. [optional]  # noqa: E501
            associated_cluster (HyperflexClusterRelationship): [optional]  # noqa: E501
            associated_compute_cluster (VirtualizationIweClusterRelationship): [optional]  # noqa: E501
            auto_support (HyperflexAutoSupportPolicyRelationship): [optional]  # noqa: E501
            cluster_network (HyperflexClusterNetworkPolicyRelationship): [optional]  # noqa: E501
            cluster_storage (HyperflexClusterStoragePolicyRelationship): [optional]  # noqa: E501
            config_result (HyperflexConfigResultRelationship): [optional]  # noqa: E501
            ext_fc_storage (HyperflexExtFcStoragePolicyRelationship): [optional]  # noqa: E501
            ext_iscsi_storage (HyperflexExtIscsiStoragePolicyRelationship): [optional]  # noqa: E501
            httpproxypolicy (CommHttpProxyPolicyRelationship): [optional]  # noqa: E501
            local_credential (HyperflexLocalCredentialPolicyRelationship): [optional]  # noqa: E501
            node_config (HyperflexNodeConfigPolicyRelationship): [optional]  # noqa: E501
            node_profile_config ([HyperflexNodeProfileRelationship], none_type): An array of relationships to hyperflexNodeProfile resources.. [optional]  # noqa: E501
            organization (OrganizationOrganizationRelationship): [optional]  # noqa: E501
            proxy_setting (HyperflexProxySettingPolicyRelationship): [optional]  # noqa: E501
            running_workflows ([WorkflowWorkflowInfoRelationship], none_type): An array of relationships to workflowWorkflowInfo resources.. [optional]  # noqa: E501
            software_version (HyperflexSoftwareVersionPolicyRelationship): [optional]  # noqa: E501
            sys_config (HyperflexSysConfigPolicyRelationship): [optional]  # noqa: E501
            ucsm_config (HyperflexUcsmConfigPolicyRelationship): [optional]  # noqa: E501
            vcenter_config (HyperflexVcenterConfigPolicyRelationship): [optional]  # noqa: E501
        """

        class_id = kwargs.get('class_id', "hyperflex.ClusterProfile")
        object_type = kwargs.get('object_type', "hyperflex.ClusterProfile")
        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
            for arg in args:
                if isinstance(arg, dict):
                    kwargs.update(arg)
                else:
                    raise ApiTypeError(
                        "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                            args,
                            self.__class__.__name__,
                        ),
                        path_to_item=_path_to_item,
                        valid_classes=(self.__class__,),
                    )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        self.class_id = class_id
        self.object_type = object_type
        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
            if var_name in self.read_only_vars:
                raise ApiAttributeError(f"`{var_name}` is a read-only attribute. Use `from_openapi_data` to instantiate "
                                     f"class with read only attributes.")
