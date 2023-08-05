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
    from intersight.model.storage_base_capacity import StorageBaseCapacity
    globals()['StorageBaseCapacity'] = StorageBaseCapacity


class StorageBaseArrayDiskAllOf(ModelNormal):
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
            'HITACHIDISK': "storage.HitachiDisk",
            'NETAPPBASEDISK': "storage.NetAppBaseDisk",
            'PUREDISK': "storage.PureDisk",
        },
        ('object_type',): {
            'HITACHIDISK': "storage.HitachiDisk",
            'NETAPPBASEDISK': "storage.NetAppBaseDisk",
            'PUREDISK': "storage.PureDisk",
        },
        ('protocol',): {
            'UNKNOWN': "Unknown",
            'SAS': "SAS",
            'NVME': "NVMe",
            'SATA': "SATA",
        },
        ('status',): {
            'UNKNOWN': "Unknown",
            'OK': "Ok",
            'DEGRADED': "Degraded",
            'CRITICAL': "Critical",
            'OFFLINE': "Offline",
            'IDENTIFYING': "Identifying",
            'NOTAVAILABLE': "NotAvailable",
            'UPDATING': "Updating",
            'UNRECOGNIZED': "Unrecognized",
        },
        ('type',): {
            'UNKNOWN': "Unknown",
            'SSD': "SSD",
            'HDD': "HDD",
            'NVRAM': "NVRAM",
            'SATA': "SATA",
            'BSAS': "BSAS",
            'FC': "FC",
            'FSAS': "FSAS",
            'LUN': "LUN",
            'MSATA': "MSATA",
            'SAS': "SAS",
            'VMDISK': "VMDISK",
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
            'name': (str,),  # noqa: E501
            'part_number': (str,),  # noqa: E501
            'protocol': (str,),  # noqa: E501
            'speed': (int,),  # noqa: E501
            'status': (str,),  # noqa: E501
            'storage_utilization': (StorageBaseCapacity,),  # noqa: E501
            'type': (str,),  # noqa: E501
            'version': (str,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'class_id': 'ClassId',  # noqa: E501
        'object_type': 'ObjectType',  # noqa: E501
        'name': 'Name',  # noqa: E501
        'part_number': 'PartNumber',  # noqa: E501
        'protocol': 'Protocol',  # noqa: E501
        'speed': 'Speed',  # noqa: E501
        'status': 'Status',  # noqa: E501
        'storage_utilization': 'StorageUtilization',  # noqa: E501
        'type': 'Type',  # noqa: E501
        'version': 'Version',  # noqa: E501
    }

    read_only_vars = {
        'name',  # noqa: E501
        'part_number',  # noqa: E501
        'protocol',  # noqa: E501
        'speed',  # noqa: E501
        'status',  # noqa: E501
        'type',  # noqa: E501
        'version',  # noqa: E501
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, class_id, object_type, *args, **kwargs):  # noqa: E501
        """StorageBaseArrayDiskAllOf - a model defined in OpenAPI

        Args:
            class_id (str): The fully-qualified name of the instantiated, concrete type. This property is used as a discriminator to identify the type of the payload when marshaling and unmarshaling data. The enum values provides the list of concrete types that can be instantiated from this abstract type.
            object_type (str): The fully-qualified name of the instantiated, concrete type. The value should be the same as the 'ClassId' property. The enum values provides the list of concrete types that can be instantiated from this abstract type.

        Keyword Args:
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
            name (str): Disk name available in storage array.. [optional]  # noqa: E501
            part_number (str): Storage disk part number.. [optional]  # noqa: E501
            protocol (str): Storage protocol used in disk for communication. Possible values are SAS, SATA and NVMe. * `Unknown` - Disk protocol is unknown. * `SAS` - Serial Attached SCSI protocol (SAS) used in disk. * `NVMe` - Non-volatile memory express (NVMe) protocol used in disk. * `SATA` - Serial Advanced Technology Attachment (SATA) used in disk.. [optional] if omitted the server will use the default value of "Unknown"  # noqa: E501
            speed (int): Disk speed for read or write operation measured in rpm.. [optional]  # noqa: E501
            status (str): Storage disk health status. * `Unknown` - Component status is not available. * `Ok` - Component is healthy and no issues found. * `Degraded` - Functioning, but not at full capability due to a non-fatal failure. * `Critical` - Not functioning or requiring immediate attention. * `Offline` - Component is installed, but powered off. * `Identifying` - Component is in initialization process. * `NotAvailable` - Component is not installed or not available. * `Updating` - Software update is in progress. * `Unrecognized` - Component is not recognized. It may be because the component is not installed properly or it is not supported.. [optional] if omitted the server will use the default value of "Unknown"  # noqa: E501
            storage_utilization (StorageBaseCapacity): [optional]  # noqa: E501
            type (str): Storage disk type - it can be SSD, HDD, NVRAM. * `Unknown` - Default unknown disk type. * `SSD` - Storage disk with Solid state disk. * `HDD` - Storage disk with Hard disk drive. * `NVRAM` - Storage disk with Non-volatile random-access memory type. * `SATA` - Disk drive implementation with Serial Advanced Technology Attachment (SATA). * `BSAS` - Bridged SAS-SATA disks with added hardware to enable them to be plugged into a SAS-connected storage shelf. * `FC` - Storage disk with Fiber Channel. * `FSAS` - Near Line SAS. NL-SAS drives are enterprise SATA drives with a SAS interface, head, media, androtational speed of traditional enterprise-class SATA drives with the fully capable SAS interfacetypical for classic SAS drives. * `LUN` - Logical Unit Number refers to a logical disk. * `MSATA` - SATA disk in multi-disk carrier storage shelf. * `SAS` - Storage disk with serial attached SCSI. * `VMDISK` - Virtual machine Data Disk.. [optional] if omitted the server will use the default value of "Unknown"  # noqa: E501
            version (str): Storage disk version number.. [optional]  # noqa: E501
        """

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
    def __init__(self, class_id, object_type, *args, **kwargs):  # noqa: E501
        """StorageBaseArrayDiskAllOf - a model defined in OpenAPI

        Args:
            class_id (str): The fully-qualified name of the instantiated, concrete type. This property is used as a discriminator to identify the type of the payload when marshaling and unmarshaling data. The enum values provides the list of concrete types that can be instantiated from this abstract type.
            object_type (str): The fully-qualified name of the instantiated, concrete type. The value should be the same as the 'ClassId' property. The enum values provides the list of concrete types that can be instantiated from this abstract type.

        Keyword Args:
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
            name (str): Disk name available in storage array.. [optional]  # noqa: E501
            part_number (str): Storage disk part number.. [optional]  # noqa: E501
            protocol (str): Storage protocol used in disk for communication. Possible values are SAS, SATA and NVMe. * `Unknown` - Disk protocol is unknown. * `SAS` - Serial Attached SCSI protocol (SAS) used in disk. * `NVMe` - Non-volatile memory express (NVMe) protocol used in disk. * `SATA` - Serial Advanced Technology Attachment (SATA) used in disk.. [optional] if omitted the server will use the default value of "Unknown"  # noqa: E501
            speed (int): Disk speed for read or write operation measured in rpm.. [optional]  # noqa: E501
            status (str): Storage disk health status. * `Unknown` - Component status is not available. * `Ok` - Component is healthy and no issues found. * `Degraded` - Functioning, but not at full capability due to a non-fatal failure. * `Critical` - Not functioning or requiring immediate attention. * `Offline` - Component is installed, but powered off. * `Identifying` - Component is in initialization process. * `NotAvailable` - Component is not installed or not available. * `Updating` - Software update is in progress. * `Unrecognized` - Component is not recognized. It may be because the component is not installed properly or it is not supported.. [optional] if omitted the server will use the default value of "Unknown"  # noqa: E501
            storage_utilization (StorageBaseCapacity): [optional]  # noqa: E501
            type (str): Storage disk type - it can be SSD, HDD, NVRAM. * `Unknown` - Default unknown disk type. * `SSD` - Storage disk with Solid state disk. * `HDD` - Storage disk with Hard disk drive. * `NVRAM` - Storage disk with Non-volatile random-access memory type. * `SATA` - Disk drive implementation with Serial Advanced Technology Attachment (SATA). * `BSAS` - Bridged SAS-SATA disks with added hardware to enable them to be plugged into a SAS-connected storage shelf. * `FC` - Storage disk with Fiber Channel. * `FSAS` - Near Line SAS. NL-SAS drives are enterprise SATA drives with a SAS interface, head, media, androtational speed of traditional enterprise-class SATA drives with the fully capable SAS interfacetypical for classic SAS drives. * `LUN` - Logical Unit Number refers to a logical disk. * `MSATA` - SATA disk in multi-disk carrier storage shelf. * `SAS` - Storage disk with serial attached SCSI. * `VMDISK` - Virtual machine Data Disk.. [optional] if omitted the server will use the default value of "Unknown"  # noqa: E501
            version (str): Storage disk version number.. [optional]  # noqa: E501
        """

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
