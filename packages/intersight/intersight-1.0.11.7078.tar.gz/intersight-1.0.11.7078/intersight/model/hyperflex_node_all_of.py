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
    from intersight.model.asset_cluster_member_relationship import AssetClusterMemberRelationship
    from intersight.model.compute_physical_relationship import ComputePhysicalRelationship
    from intersight.model.hyperflex_cluster_relationship import HyperflexClusterRelationship
    from intersight.model.hyperflex_drive_relationship import HyperflexDriveRelationship
    from intersight.model.hyperflex_hx_network_address_dt import HyperflexHxNetworkAddressDt
    from intersight.model.hyperflex_hx_uu_id_dt import HyperflexHxUuIdDt
    globals()['AssetClusterMemberRelationship'] = AssetClusterMemberRelationship
    globals()['ComputePhysicalRelationship'] = ComputePhysicalRelationship
    globals()['HyperflexClusterRelationship'] = HyperflexClusterRelationship
    globals()['HyperflexDriveRelationship'] = HyperflexDriveRelationship
    globals()['HyperflexHxNetworkAddressDt'] = HyperflexHxNetworkAddressDt
    globals()['HyperflexHxUuIdDt'] = HyperflexHxUuIdDt


class HyperflexNodeAllOf(ModelNormal):
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
            'HYPERFLEX.NODE': "hyperflex.Node",
        },
        ('object_type',): {
            'HYPERFLEX.NODE': "hyperflex.Node",
        },
        ('node_maintenance_mode',): {
            'UNKNOWN': "Unknown",
            'INMAINTENANCEMODE': "InMaintenanceMode",
            'NOTINMAINTENANCEMODE': "NotInMaintenanceMode",
        },
        ('node_status',): {
            'UNKNOWN': "Unknown",
            'INVALID': "Invalid",
            'READY': "Ready",
            'UNPUBLISHED': "Unpublished",
            'DELETED': "Deleted",
            'BLOCKED': "Blocked",
            'BLACKLISTED': "Blacklisted",
            'ALLOWED': "Allowed",
            'WHITELISTED': "Whitelisted",
            'INMAINTENANCE': "InMaintenance",
            'ONLINE': "Online",
            'OFFLINE': "Offline",
        },
        ('role',): {
            'UNKNOWN': "UNKNOWN",
            'STORAGE': "STORAGE",
            'COMPUTE': "COMPUTE",
        },
        ('status',): {
            'UNKNOWN': "UNKNOWN",
            'ONLINE': "ONLINE",
            'OFFLINE': "OFFLINE",
            'INMAINTENANCE': "INMAINTENANCE",
            'DEGRADED': "DEGRADED",
        },
    }

    validations = {
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
            'build_number': (str,),  # noqa: E501
            'display_version': (str,),  # noqa: E501
            'empty_slots_list': ([str], none_type,),  # noqa: E501
            'host_name': (str,),  # noqa: E501
            'hxdp_data_ip': (HyperflexHxNetworkAddressDt,),  # noqa: E501
            'hxdp_mmgt_ip': (HyperflexHxNetworkAddressDt,),  # noqa: E501
            'hypervisor': (str,),  # noqa: E501
            'hypervisor_data_ip': (HyperflexHxNetworkAddressDt,),  # noqa: E501
            'identity': (HyperflexHxUuIdDt,),  # noqa: E501
            'ip': (HyperflexHxNetworkAddressDt,),  # noqa: E501
            'lockdown': (bool,),  # noqa: E501
            'model_number': (str,),  # noqa: E501
            'node_maintenance_mode': (str,),  # noqa: E501
            'node_status': (str,),  # noqa: E501
            'node_uuid': (str,),  # noqa: E501
            'role': (str,),  # noqa: E501
            'serial_number': (str,),  # noqa: E501
            'status': (str,),  # noqa: E501
            'version': (str,),  # noqa: E501
            'cluster': (HyperflexClusterRelationship,),  # noqa: E501
            'cluster_member': (AssetClusterMemberRelationship,),  # noqa: E501
            'drives': ([HyperflexDriveRelationship], none_type,),  # noqa: E501
            'physical_server': (ComputePhysicalRelationship,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'class_id': 'ClassId',  # noqa: E501
        'object_type': 'ObjectType',  # noqa: E501
        'build_number': 'BuildNumber',  # noqa: E501
        'display_version': 'DisplayVersion',  # noqa: E501
        'empty_slots_list': 'EmptySlotsList',  # noqa: E501
        'host_name': 'HostName',  # noqa: E501
        'hxdp_data_ip': 'HxdpDataIp',  # noqa: E501
        'hxdp_mmgt_ip': 'HxdpMmgtIp',  # noqa: E501
        'hypervisor': 'Hypervisor',  # noqa: E501
        'hypervisor_data_ip': 'HypervisorDataIp',  # noqa: E501
        'identity': 'Identity',  # noqa: E501
        'ip': 'Ip',  # noqa: E501
        'lockdown': 'Lockdown',  # noqa: E501
        'model_number': 'ModelNumber',  # noqa: E501
        'node_maintenance_mode': 'NodeMaintenanceMode',  # noqa: E501
        'node_status': 'NodeStatus',  # noqa: E501
        'node_uuid': 'NodeUuid',  # noqa: E501
        'role': 'Role',  # noqa: E501
        'serial_number': 'SerialNumber',  # noqa: E501
        'status': 'Status',  # noqa: E501
        'version': 'Version',  # noqa: E501
        'cluster': 'Cluster',  # noqa: E501
        'cluster_member': 'ClusterMember',  # noqa: E501
        'drives': 'Drives',  # noqa: E501
        'physical_server': 'PhysicalServer',  # noqa: E501
    }

    read_only_vars = {
        'build_number',  # noqa: E501
        'display_version',  # noqa: E501
        'host_name',  # noqa: E501
        'hypervisor',  # noqa: E501
        'lockdown',  # noqa: E501
        'model_number',  # noqa: E501
        'node_maintenance_mode',  # noqa: E501
        'node_status',  # noqa: E501
        'node_uuid',  # noqa: E501
        'role',  # noqa: E501
        'serial_number',  # noqa: E501
        'status',  # noqa: E501
        'version',  # noqa: E501
        'drives',  # noqa: E501
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):  # noqa: E501
        """HyperflexNodeAllOf - a model defined in OpenAPI

        Args:

        Keyword Args:
            class_id (str): The fully-qualified name of the instantiated, concrete type. This property is used as a discriminator to identify the type of the payload when marshaling and unmarshaling data.. defaults to "hyperflex.Node", must be one of ["hyperflex.Node", ]  # noqa: E501
            object_type (str): The fully-qualified name of the instantiated, concrete type. The value should be the same as the 'ClassId' property.. defaults to "hyperflex.Node", must be one of ["hyperflex.Node", ]  # noqa: E501
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
            build_number (str): The build number of the hypervisor running on the host.. [optional]  # noqa: E501
            display_version (str): The user-friendly string representation of the hypervisor version of the host.. [optional]  # noqa: E501
            empty_slots_list ([str], none_type): [optional]  # noqa: E501
            host_name (str): The hostname configured for the hypervisor running on the host.. [optional]  # noqa: E501
            hxdp_data_ip (HyperflexHxNetworkAddressDt): [optional]  # noqa: E501
            hxdp_mmgt_ip (HyperflexHxNetworkAddressDt): [optional]  # noqa: E501
            hypervisor (str): The type of hypervisor running on the host.. [optional]  # noqa: E501
            hypervisor_data_ip (HyperflexHxNetworkAddressDt): [optional]  # noqa: E501
            identity (HyperflexHxUuIdDt): [optional]  # noqa: E501
            ip (HyperflexHxNetworkAddressDt): [optional]  # noqa: E501
            lockdown (bool): The admin state of lockdown mode on the host. If 'true', lockdown mode is enabled.. [optional]  # noqa: E501
            model_number (str): The model of the host server.. [optional]  # noqa: E501
            node_maintenance_mode (str): The status of maintenance mode on the HyperFlex node. * `Unknown` - The maintenance mode status could not be determined. * `InMaintenanceMode` - The node has maintenance mode enabled. The node has been temporarily been relinquished from the cluster to allow for maintenance operations. * `NotInMaintenanceMode` - The node does not have maintenance mode enabled.. [optional] if omitted the server will use the default value of "Unknown"  # noqa: E501
            node_status (str): The operational status of the HyperFlex node. * `Unknown` - The default operational status of a HyperFlex node. * `Invalid` - The status of the node cannot be determined by the storage platform. * `Ready` - The platform node has been acknowledged by the cluster. * `Unpublished` - The node is not yet added to the storage cluster. * `Deleted` - The node has been removed from the cluster. * `Blocked` - The node is blocked from being added to the cluster. * `Blacklisted` - The deprecated value for 'Blocked'. It is included to maintain backwards compatibility with clusters running a HyperFlex Data Platform version older than 5.0(1a). * `Allowed` - The node is allowd to be added to the cluster. * `Whitelisted` - The deprecated value for 'Allowed'. It is included to maintain backwards compatibility with clusters running a HyperFlex Data Platform version older than 5.0(1a). * `InMaintenance` - The node is in maintenance mode. It has been temporarily relinquished from the cluster to allow for maintenance operations such as software upgrades. * `Online` - The node is participating in the storage cluster and is available for storage operations. * `Offline` - The node is part of the storage cluster, but is not available for storage operations.. [optional] if omitted the server will use the default value of "Unknown"  # noqa: E501
            node_uuid (str): The unique identifier of the HyperFlex node.. [optional]  # noqa: E501
            role (str): The role of the host in the HyperFlex cluster. Specifies whether this host is used for compute or for both compute and storage. * `UNKNOWN` - The role of the HyperFlex cluster node is not known. * `STORAGE` - The HyperFlex cluster node provides both storage and compute resources for the cluster. * `COMPUTE` - The HyperFlex cluster node provides compute resources for the cluster.. [optional] if omitted the server will use the default value of "UNKNOWN"  # noqa: E501
            serial_number (str): The serial of the host server.. [optional]  # noqa: E501
            status (str): The status of the host. Indicates whether the hypervisor is online. * `UNKNOWN` - The host status cannot be determined. * `ONLINE` - The host is online and operational. * `OFFLINE` - The host is offline and is currently not participating in the HyperFlex cluster. * `INMAINTENANCE` - The host is not participating in the HyperFlex cluster because of a maintenance operation, such as firmware or data platform upgrade. * `DEGRADED` - The host is degraded and may not be performing in its full operational capacity.. [optional] if omitted the server will use the default value of "UNKNOWN"  # noqa: E501
            version (str): The version of the hypervisor running on the host.. [optional]  # noqa: E501
            cluster (HyperflexClusterRelationship): [optional]  # noqa: E501
            cluster_member (AssetClusterMemberRelationship): [optional]  # noqa: E501
            drives ([HyperflexDriveRelationship], none_type): An array of relationships to hyperflexDrive resources.. [optional]  # noqa: E501
            physical_server (ComputePhysicalRelationship): [optional]  # noqa: E501
        """

        class_id = kwargs.get('class_id', "hyperflex.Node")
        object_type = kwargs.get('object_type', "hyperflex.Node")
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
        """HyperflexNodeAllOf - a model defined in OpenAPI

        Args:

        Keyword Args:
            class_id (str): The fully-qualified name of the instantiated, concrete type. This property is used as a discriminator to identify the type of the payload when marshaling and unmarshaling data.. defaults to "hyperflex.Node", must be one of ["hyperflex.Node", ]  # noqa: E501
            object_type (str): The fully-qualified name of the instantiated, concrete type. The value should be the same as the 'ClassId' property.. defaults to "hyperflex.Node", must be one of ["hyperflex.Node", ]  # noqa: E501
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
            build_number (str): The build number of the hypervisor running on the host.. [optional]  # noqa: E501
            display_version (str): The user-friendly string representation of the hypervisor version of the host.. [optional]  # noqa: E501
            empty_slots_list ([str], none_type): [optional]  # noqa: E501
            host_name (str): The hostname configured for the hypervisor running on the host.. [optional]  # noqa: E501
            hxdp_data_ip (HyperflexHxNetworkAddressDt): [optional]  # noqa: E501
            hxdp_mmgt_ip (HyperflexHxNetworkAddressDt): [optional]  # noqa: E501
            hypervisor (str): The type of hypervisor running on the host.. [optional]  # noqa: E501
            hypervisor_data_ip (HyperflexHxNetworkAddressDt): [optional]  # noqa: E501
            identity (HyperflexHxUuIdDt): [optional]  # noqa: E501
            ip (HyperflexHxNetworkAddressDt): [optional]  # noqa: E501
            lockdown (bool): The admin state of lockdown mode on the host. If 'true', lockdown mode is enabled.. [optional]  # noqa: E501
            model_number (str): The model of the host server.. [optional]  # noqa: E501
            node_maintenance_mode (str): The status of maintenance mode on the HyperFlex node. * `Unknown` - The maintenance mode status could not be determined. * `InMaintenanceMode` - The node has maintenance mode enabled. The node has been temporarily been relinquished from the cluster to allow for maintenance operations. * `NotInMaintenanceMode` - The node does not have maintenance mode enabled.. [optional] if omitted the server will use the default value of "Unknown"  # noqa: E501
            node_status (str): The operational status of the HyperFlex node. * `Unknown` - The default operational status of a HyperFlex node. * `Invalid` - The status of the node cannot be determined by the storage platform. * `Ready` - The platform node has been acknowledged by the cluster. * `Unpublished` - The node is not yet added to the storage cluster. * `Deleted` - The node has been removed from the cluster. * `Blocked` - The node is blocked from being added to the cluster. * `Blacklisted` - The deprecated value for 'Blocked'. It is included to maintain backwards compatibility with clusters running a HyperFlex Data Platform version older than 5.0(1a). * `Allowed` - The node is allowd to be added to the cluster. * `Whitelisted` - The deprecated value for 'Allowed'. It is included to maintain backwards compatibility with clusters running a HyperFlex Data Platform version older than 5.0(1a). * `InMaintenance` - The node is in maintenance mode. It has been temporarily relinquished from the cluster to allow for maintenance operations such as software upgrades. * `Online` - The node is participating in the storage cluster and is available for storage operations. * `Offline` - The node is part of the storage cluster, but is not available for storage operations.. [optional] if omitted the server will use the default value of "Unknown"  # noqa: E501
            node_uuid (str): The unique identifier of the HyperFlex node.. [optional]  # noqa: E501
            role (str): The role of the host in the HyperFlex cluster. Specifies whether this host is used for compute or for both compute and storage. * `UNKNOWN` - The role of the HyperFlex cluster node is not known. * `STORAGE` - The HyperFlex cluster node provides both storage and compute resources for the cluster. * `COMPUTE` - The HyperFlex cluster node provides compute resources for the cluster.. [optional] if omitted the server will use the default value of "UNKNOWN"  # noqa: E501
            serial_number (str): The serial of the host server.. [optional]  # noqa: E501
            status (str): The status of the host. Indicates whether the hypervisor is online. * `UNKNOWN` - The host status cannot be determined. * `ONLINE` - The host is online and operational. * `OFFLINE` - The host is offline and is currently not participating in the HyperFlex cluster. * `INMAINTENANCE` - The host is not participating in the HyperFlex cluster because of a maintenance operation, such as firmware or data platform upgrade. * `DEGRADED` - The host is degraded and may not be performing in its full operational capacity.. [optional] if omitted the server will use the default value of "UNKNOWN"  # noqa: E501
            version (str): The version of the hypervisor running on the host.. [optional]  # noqa: E501
            cluster (HyperflexClusterRelationship): [optional]  # noqa: E501
            cluster_member (AssetClusterMemberRelationship): [optional]  # noqa: E501
            drives ([HyperflexDriveRelationship], none_type): An array of relationships to hyperflexDrive resources.. [optional]  # noqa: E501
            physical_server (ComputePhysicalRelationship): [optional]  # noqa: E501
        """

        class_id = kwargs.get('class_id', "hyperflex.Node")
        object_type = kwargs.get('object_type', "hyperflex.Node")
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
