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
    from intersight.model.asset_device_registration_relationship import AssetDeviceRegistrationRelationship
    from intersight.model.compute_physical_relationship import ComputePhysicalRelationship
    from intersight.model.display_names import DisplayNames
    from intersight.model.equipment_chassis_relationship import EquipmentChassisRelationship
    from intersight.model.firmware_base_impact import FirmwareBaseImpact
    from intersight.model.firmware_distributable_relationship import FirmwareDistributableRelationship
    from intersight.model.firmware_upgrade_impact_all_of import FirmwareUpgradeImpactAllOf
    from intersight.model.firmware_upgrade_impact_base import FirmwareUpgradeImpactBase
    from intersight.model.mo_base_mo_relationship import MoBaseMoRelationship
    from intersight.model.mo_tag import MoTag
    from intersight.model.mo_version_context import MoVersionContext
    from intersight.model.network_element_relationship import NetworkElementRelationship
    from intersight.model.softwarerepository_release_relationship import SoftwarerepositoryReleaseRelationship
    globals()['AssetDeviceRegistrationRelationship'] = AssetDeviceRegistrationRelationship
    globals()['ComputePhysicalRelationship'] = ComputePhysicalRelationship
    globals()['DisplayNames'] = DisplayNames
    globals()['EquipmentChassisRelationship'] = EquipmentChassisRelationship
    globals()['FirmwareBaseImpact'] = FirmwareBaseImpact
    globals()['FirmwareDistributableRelationship'] = FirmwareDistributableRelationship
    globals()['FirmwareUpgradeImpactAllOf'] = FirmwareUpgradeImpactAllOf
    globals()['FirmwareUpgradeImpactBase'] = FirmwareUpgradeImpactBase
    globals()['MoBaseMoRelationship'] = MoBaseMoRelationship
    globals()['MoTag'] = MoTag
    globals()['MoVersionContext'] = MoVersionContext
    globals()['NetworkElementRelationship'] = NetworkElementRelationship
    globals()['SoftwarerepositoryReleaseRelationship'] = SoftwarerepositoryReleaseRelationship


class FirmwareUpgradeImpact(ModelComposed):
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
            'FIRMWARE.UPGRADEIMPACT': "firmware.UpgradeImpact",
        },
        ('object_type',): {
            'FIRMWARE.UPGRADEIMPACT': "firmware.UpgradeImpact",
        },
        ('components',): {
            'None': None,
            'ALL': "ALL",
            'ALL,HDD': "ALL,HDD",
            'DRIVE-U.2': "Drive-U.2",
            'STORAGE': "Storage",
            'NONE': "None",
            'NXOS': "NXOS",
            'IOM': "IOM",
            'PSU': "PSU",
            'CIMC': "CIMC",
            'BIOS': "BIOS",
            'PCIE': "PCIE",
            'DRIVE': "Drive",
            'DIMM': "DIMM",
            'BOARDCONTROLLER': "BoardController",
            'STORAGECONTROLLER': "StorageController",
            'STORAGE-SASEXPANDER': "Storage-Sasexpander",
            'STORAGE-U.2': "Storage-U.2",
            'HBA': "HBA",
            'GPU': "GPU",
            'SASEXPANDER': "SasExpander",
            'MSWITCH': "MSwitch",
            'CMC': "CMC",
        },
        ('computation_state',): {
            'INPROGRESS': "Inprogress",
            'COMPLETED': "Completed",
            'UNAVAILABLE': "Unavailable",
        },
        ('exclude_components',): {
            'None': None,
            'ALL': "ALL",
            'ALL,HDD': "ALL,HDD",
            'DRIVE-U.2': "Drive-U.2",
            'STORAGE': "Storage",
            'NONE': "None",
            'NXOS': "NXOS",
            'IOM': "IOM",
            'PSU': "PSU",
            'CIMC': "CIMC",
            'BIOS': "BIOS",
            'PCIE': "PCIE",
            'DRIVE': "Drive",
            'DIMM': "DIMM",
            'BOARDCONTROLLER': "BoardController",
            'STORAGECONTROLLER': "StorageController",
            'STORAGE-SASEXPANDER': "Storage-Sasexpander",
            'STORAGE-U.2': "Storage-U.2",
            'HBA': "HBA",
            'GPU': "GPU",
            'SASEXPANDER': "SasExpander",
            'MSWITCH': "MSwitch",
            'CMC': "CMC",
        },
        ('summary',): {
            'BASIC': "Basic",
            'DETAIL': "Detail",
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
            'chassis': ([EquipmentChassisRelationship], none_type,),  # noqa: E501
            'device': ([AssetDeviceRegistrationRelationship], none_type,),  # noqa: E501
            'distributable': (FirmwareDistributableRelationship,),  # noqa: E501
            'network_elements': ([NetworkElementRelationship], none_type,),  # noqa: E501
            'release': (SoftwarerepositoryReleaseRelationship,),  # noqa: E501
            'server': ([ComputePhysicalRelationship], none_type,),  # noqa: E501
            'account_moid': (str,),  # noqa: E501
            'create_time': (datetime,),  # noqa: E501
            'domain_group_moid': (str,),  # noqa: E501
            'mod_time': (datetime,),  # noqa: E501
            'moid': (str,),  # noqa: E501
            'owners': ([str], none_type,),  # noqa: E501
            'shared_scope': (str,),  # noqa: E501
            'tags': ([MoTag], none_type,),  # noqa: E501
            'version_context': (MoVersionContext,),  # noqa: E501
            'ancestors': ([MoBaseMoRelationship], none_type,),  # noqa: E501
            'parent': (MoBaseMoRelationship,),  # noqa: E501
            'permission_resources': ([MoBaseMoRelationship], none_type,),  # noqa: E501
            'display_names': (DisplayNames,),  # noqa: E501
            'components': ([str], none_type,),  # noqa: E501
            'computation_state': (str,),  # noqa: E501
            'exclude_components': ([str], none_type,),  # noqa: E501
            'impacts': ([FirmwareBaseImpact], none_type,),  # noqa: E501
            'summary': (str,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        val = {
        }
        if not val:
            return None
        return {'class_id': val}

    attribute_map = {
        'class_id': 'ClassId',  # noqa: E501
        'object_type': 'ObjectType',  # noqa: E501
        'chassis': 'Chassis',  # noqa: E501
        'device': 'Device',  # noqa: E501
        'distributable': 'Distributable',  # noqa: E501
        'network_elements': 'NetworkElements',  # noqa: E501
        'release': 'Release',  # noqa: E501
        'server': 'Server',  # noqa: E501
        'account_moid': 'AccountMoid',  # noqa: E501
        'create_time': 'CreateTime',  # noqa: E501
        'domain_group_moid': 'DomainGroupMoid',  # noqa: E501
        'mod_time': 'ModTime',  # noqa: E501
        'moid': 'Moid',  # noqa: E501
        'owners': 'Owners',  # noqa: E501
        'shared_scope': 'SharedScope',  # noqa: E501
        'tags': 'Tags',  # noqa: E501
        'version_context': 'VersionContext',  # noqa: E501
        'ancestors': 'Ancestors',  # noqa: E501
        'parent': 'Parent',  # noqa: E501
        'permission_resources': 'PermissionResources',  # noqa: E501
        'display_names': 'DisplayNames',  # noqa: E501
        'components': 'Components',  # noqa: E501
        'computation_state': 'ComputationState',  # noqa: E501
        'exclude_components': 'ExcludeComponents',  # noqa: E501
        'impacts': 'Impacts',  # noqa: E501
        'summary': 'Summary',  # noqa: E501
    }

    read_only_vars = {
        'device',  # noqa: E501
        'account_moid',  # noqa: E501
        'create_time',  # noqa: E501
        'domain_group_moid',  # noqa: E501
        'mod_time',  # noqa: E501
        'shared_scope',  # noqa: E501
        'ancestors',  # noqa: E501
        'permission_resources',  # noqa: E501
    }

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):  # noqa: E501
        """FirmwareUpgradeImpact - a model defined in OpenAPI

        Keyword Args:
            class_id (str): The fully-qualified name of the instantiated, concrete type. This property is used as a discriminator to identify the type of the payload when marshaling and unmarshaling data.. defaults to "firmware.UpgradeImpact", must be one of ["firmware.UpgradeImpact", ]  # noqa: E501
            object_type (str): The fully-qualified name of the instantiated, concrete type. The value should be the same as the 'ClassId' property.. defaults to "firmware.UpgradeImpact", must be one of ["firmware.UpgradeImpact", ]  # noqa: E501
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
            chassis ([EquipmentChassisRelationship], none_type): An array of relationships to equipmentChassis resources.. [optional]  # noqa: E501
            device ([AssetDeviceRegistrationRelationship], none_type): An array of relationships to assetDeviceRegistration resources.. [optional]  # noqa: E501
            distributable (FirmwareDistributableRelationship): [optional]  # noqa: E501
            network_elements ([NetworkElementRelationship], none_type): An array of relationships to networkElement resources.. [optional]  # noqa: E501
            release (SoftwarerepositoryReleaseRelationship): [optional]  # noqa: E501
            server ([ComputePhysicalRelationship], none_type): An array of relationships to computePhysical resources.. [optional]  # noqa: E501
            account_moid (str): The Account ID for this managed object.. [optional]  # noqa: E501
            create_time (datetime): The time when this managed object was created.. [optional]  # noqa: E501
            domain_group_moid (str): The DomainGroup ID for this managed object.. [optional]  # noqa: E501
            mod_time (datetime): The time when this managed object was last modified.. [optional]  # noqa: E501
            moid (str): The unique identifier of this Managed Object instance.. [optional]  # noqa: E501
            owners ([str], none_type): [optional]  # noqa: E501
            shared_scope (str): Intersight provides pre-built workflows, tasks and policies to end users through global catalogs. Objects that are made available through global catalogs are said to have a 'shared' ownership. Shared objects are either made globally available to all end users or restricted to end users based on their license entitlement. Users can use this property to differentiate the scope (global or a specific license tier) to which a shared MO belongs.. [optional]  # noqa: E501
            tags ([MoTag], none_type): [optional]  # noqa: E501
            version_context (MoVersionContext): [optional]  # noqa: E501
            ancestors ([MoBaseMoRelationship], none_type): An array of relationships to moBaseMo resources.. [optional]  # noqa: E501
            parent (MoBaseMoRelationship): [optional]  # noqa: E501
            permission_resources ([MoBaseMoRelationship], none_type): An array of relationships to moBaseMo resources.. [optional]  # noqa: E501
            display_names (DisplayNames): [optional]  # noqa: E501
            components ([str], none_type): [optional]  # noqa: E501
            computation_state (str): Captures the status of an upgrade impact calculation. Indicates whether the calculation is complete, in progress or the calculation is impossible due to the absence of the target image on the endpoint. * `Inprogress` - Upgrade impact calculation is in progress. * `Completed` - Upgrade impact calculation is completed. * `Unavailable` - Upgrade impact is not available since image is not present in FI.. [optional] if omitted the server will use the default value of "Inprogress"  # noqa: E501
            exclude_components ([str], none_type): [optional]  # noqa: E501
            impacts ([FirmwareBaseImpact], none_type): [optional]  # noqa: E501
            summary (str): The summary on the component or components getting impacted by the upgrade. * `Basic` - Summary of a single instance involved in the upgrade operation. * `Detail` - Summary of the collection of single instances for a complex component involved in the upgrade operation. For example, in case of a server upgrade, a detailed summary indicates impact of all the single instances which are part of the server, such as storage controller, drives, and BIOS.. [optional] if omitted the server will use the default value of "Basic"  # noqa: E501
        """

        class_id = kwargs.get('class_id', "firmware.UpgradeImpact")
        object_type = kwargs.get('object_type', "firmware.UpgradeImpact")
        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
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

        constant_args = {
            '_check_type': _check_type,
            '_path_to_item': _path_to_item,
            '_spec_property_naming': _spec_property_naming,
            '_configuration': _configuration,
            '_visited_composed_classes': self._visited_composed_classes,
        }
        required_args = {
            'class_id': class_id,
            'object_type': object_type,
        }
        kwargs.update(required_args)
        composed_info = validate_get_composed_info(
            constant_args, kwargs, self)
        self._composed_instances = composed_info[0]
        self._var_name_to_model_instances = composed_info[1]
        self._additional_properties_model_instances = composed_info[2]
        discarded_args = composed_info[3]

        for var_name, var_value in kwargs.items():
            if var_name in discarded_args and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self._additional_properties_model_instances:
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
        '_composed_instances',
        '_var_name_to_model_instances',
        '_additional_properties_model_instances',
    ])

    @convert_js_args_to_python_args
    def __init__(self, *args, **kwargs):  # noqa: E501
        """FirmwareUpgradeImpact - a model defined in OpenAPI

        Keyword Args:
            class_id (str): The fully-qualified name of the instantiated, concrete type. This property is used as a discriminator to identify the type of the payload when marshaling and unmarshaling data.. defaults to "firmware.UpgradeImpact", must be one of ["firmware.UpgradeImpact", ]  # noqa: E501
            object_type (str): The fully-qualified name of the instantiated, concrete type. The value should be the same as the 'ClassId' property.. defaults to "firmware.UpgradeImpact", must be one of ["firmware.UpgradeImpact", ]  # noqa: E501
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
            chassis ([EquipmentChassisRelationship], none_type): An array of relationships to equipmentChassis resources.. [optional]  # noqa: E501
            device ([AssetDeviceRegistrationRelationship], none_type): An array of relationships to assetDeviceRegistration resources.. [optional]  # noqa: E501
            distributable (FirmwareDistributableRelationship): [optional]  # noqa: E501
            network_elements ([NetworkElementRelationship], none_type): An array of relationships to networkElement resources.. [optional]  # noqa: E501
            release (SoftwarerepositoryReleaseRelationship): [optional]  # noqa: E501
            server ([ComputePhysicalRelationship], none_type): An array of relationships to computePhysical resources.. [optional]  # noqa: E501
            account_moid (str): The Account ID for this managed object.. [optional]  # noqa: E501
            create_time (datetime): The time when this managed object was created.. [optional]  # noqa: E501
            domain_group_moid (str): The DomainGroup ID for this managed object.. [optional]  # noqa: E501
            mod_time (datetime): The time when this managed object was last modified.. [optional]  # noqa: E501
            moid (str): The unique identifier of this Managed Object instance.. [optional]  # noqa: E501
            owners ([str], none_type): [optional]  # noqa: E501
            shared_scope (str): Intersight provides pre-built workflows, tasks and policies to end users through global catalogs. Objects that are made available through global catalogs are said to have a 'shared' ownership. Shared objects are either made globally available to all end users or restricted to end users based on their license entitlement. Users can use this property to differentiate the scope (global or a specific license tier) to which a shared MO belongs.. [optional]  # noqa: E501
            tags ([MoTag], none_type): [optional]  # noqa: E501
            version_context (MoVersionContext): [optional]  # noqa: E501
            ancestors ([MoBaseMoRelationship], none_type): An array of relationships to moBaseMo resources.. [optional]  # noqa: E501
            parent (MoBaseMoRelationship): [optional]  # noqa: E501
            permission_resources ([MoBaseMoRelationship], none_type): An array of relationships to moBaseMo resources.. [optional]  # noqa: E501
            display_names (DisplayNames): [optional]  # noqa: E501
            components ([str], none_type): [optional]  # noqa: E501
            computation_state (str): Captures the status of an upgrade impact calculation. Indicates whether the calculation is complete, in progress or the calculation is impossible due to the absence of the target image on the endpoint. * `Inprogress` - Upgrade impact calculation is in progress. * `Completed` - Upgrade impact calculation is completed. * `Unavailable` - Upgrade impact is not available since image is not present in FI.. [optional] if omitted the server will use the default value of "Inprogress"  # noqa: E501
            exclude_components ([str], none_type): [optional]  # noqa: E501
            impacts ([FirmwareBaseImpact], none_type): [optional]  # noqa: E501
            summary (str): The summary on the component or components getting impacted by the upgrade. * `Basic` - Summary of a single instance involved in the upgrade operation. * `Detail` - Summary of the collection of single instances for a complex component involved in the upgrade operation. For example, in case of a server upgrade, a detailed summary indicates impact of all the single instances which are part of the server, such as storage controller, drives, and BIOS.. [optional] if omitted the server will use the default value of "Basic"  # noqa: E501
        """

        class_id = kwargs.get('class_id', "firmware.UpgradeImpact")
        object_type = kwargs.get('object_type', "firmware.UpgradeImpact")
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

        constant_args = {
            '_check_type': _check_type,
            '_path_to_item': _path_to_item,
            '_spec_property_naming': _spec_property_naming,
            '_configuration': _configuration,
            '_visited_composed_classes': self._visited_composed_classes,
        }
        required_args = {
            'class_id': class_id,
            'object_type': object_type,
        }
        kwargs.update(required_args)
        composed_info = validate_get_composed_info(
            constant_args, kwargs, self)
        self._composed_instances = composed_info[0]
        self._var_name_to_model_instances = composed_info[1]
        self._additional_properties_model_instances = composed_info[2]
        discarded_args = composed_info[3]

        for var_name, var_value in kwargs.items():
            if var_name in discarded_args and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self._additional_properties_model_instances:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
            if var_name in self.read_only_vars:
                raise ApiAttributeError(f"`{var_name}` is a read-only attribute. Use `from_openapi_data` to instantiate "
                                     f"class with read only attributes.")

    @cached_property
    def _composed_schemas():
        # we need this here to make our import statements work
        # we must store _composed_schemas in here so the code is only run
        # when we invoke this method. If we kept this at the class
        # level we would get an error because the class level
        # code would be run when this module is imported, and these composed
        # classes don't exist yet because their module has not finished
        # loading
        lazy_import()
        return {
          'anyOf': [
          ],
          'allOf': [
              FirmwareUpgradeImpactAllOf,
              FirmwareUpgradeImpactBase,
          ],
          'oneOf': [
          ],
        }
