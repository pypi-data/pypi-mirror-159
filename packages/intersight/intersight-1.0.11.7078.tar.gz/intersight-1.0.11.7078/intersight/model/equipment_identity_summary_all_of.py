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
    from intersight.model.equipment_io_card_identity import EquipmentIoCardIdentity
    globals()['AssetDeviceRegistrationRelationship'] = AssetDeviceRegistrationRelationship
    globals()['EquipmentIoCardIdentity'] = EquipmentIoCardIdentity


class EquipmentIdentitySummaryAllOf(ModelNormal):
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
            'EQUIPMENT.IDENTITYSUMMARY': "equipment.IdentitySummary",
        },
        ('object_type',): {
            'EQUIPMENT.IDENTITYSUMMARY': "equipment.IdentitySummary",
        },
        ('admin_action',): {
            'NONE': "None",
            'DECOMMISSION': "Decommission",
            'RECOMMISSION': "Recommission",
            'REACK': "Reack",
            'REMOVE': "Remove",
            'REPLACE': "Replace",
        },
        ('admin_action_state',): {
            'NONE': "None",
            'APPLIED': "Applied",
            'APPLYING': "Applying",
            'FAILED': "Failed",
        },
        ('firmware_supportability',): {
            'UNKNOWN': "Unknown",
            'SUPPORTED': "Supported",
            'NOTSUPPORTED': "NotSupported",
        },
        ('last_discovery_triggered',): {
            'UNKNOWN': "Unknown",
            'DEEP': "Deep",
            'SHALLOW': "Shallow",
        },
        ('lifecycle',): {
            'NONE': "None",
            'ACTIVE': "Active",
            'DECOMMISSIONED': "Decommissioned",
            'DECOMMISSIONINPROGRESS': "DecommissionInProgress",
            'RECOMMISSIONINPROGRESS': "RecommissionInProgress",
            'OPERATIONFAILED': "OperationFailed",
            'REACKINPROGRESS': "ReackInProgress",
            'REMOVEINPROGRESS': "RemoveInProgress",
            'DISCOVERED': "Discovered",
            'DISCOVERYINPROGRESS': "DiscoveryInProgress",
            'DISCOVERYFAILED': "DiscoveryFailed",
            'FIRMWAREUPGRADEINPROGRESS': "FirmwareUpgradeInProgress",
            'BLADEMIGRATIONINPROGRESS': "BladeMigrationInProgress",
            'INACTIVE': "Inactive",
            'REPLACEINPROGRESS': "ReplaceInProgress",
            'SLOTMISMATCH': "SlotMismatch",
        },
        ('presence',): {
            'UNKNOWN': "Unknown",
            'EQUIPPED': "Equipped",
            'EQUIPPEDMISMATCH': "EquippedMismatch",
            'MISSING': "Missing",
        },
    }

    validations = {
        ('identifier',): {
            'inclusive_minimum': 1,
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
            'adapter_serial': (str,),  # noqa: E501
            'admin_action': (str,),  # noqa: E501
            'admin_action_state': (str,),  # noqa: E501
            'chassis_id': (int,),  # noqa: E501
            'current_chassis_id': (int,),  # noqa: E501
            'current_slot_id': (int,),  # noqa: E501
            'firmware_supportability': (str,),  # noqa: E501
            'identifier': (int,),  # noqa: E501
            'io_card_identity_list': ([EquipmentIoCardIdentity], none_type,),  # noqa: E501
            'last_discovery_triggered': (str,),  # noqa: E501
            'lifecycle': (str,),  # noqa: E501
            'model': (str,),  # noqa: E501
            'presence': (str,),  # noqa: E501
            'serial': (str,),  # noqa: E501
            'slot_id': (int,),  # noqa: E501
            'source_object_type': (str,),  # noqa: E501
            'switch_id': (int,),  # noqa: E501
            'vendor': (str,),  # noqa: E501
            'registered_device': (AssetDeviceRegistrationRelationship,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'class_id': 'ClassId',  # noqa: E501
        'object_type': 'ObjectType',  # noqa: E501
        'adapter_serial': 'AdapterSerial',  # noqa: E501
        'admin_action': 'AdminAction',  # noqa: E501
        'admin_action_state': 'AdminActionState',  # noqa: E501
        'chassis_id': 'ChassisId',  # noqa: E501
        'current_chassis_id': 'CurrentChassisId',  # noqa: E501
        'current_slot_id': 'CurrentSlotId',  # noqa: E501
        'firmware_supportability': 'FirmwareSupportability',  # noqa: E501
        'identifier': 'Identifier',  # noqa: E501
        'io_card_identity_list': 'IoCardIdentityList',  # noqa: E501
        'last_discovery_triggered': 'LastDiscoveryTriggered',  # noqa: E501
        'lifecycle': 'Lifecycle',  # noqa: E501
        'model': 'Model',  # noqa: E501
        'presence': 'Presence',  # noqa: E501
        'serial': 'Serial',  # noqa: E501
        'slot_id': 'SlotId',  # noqa: E501
        'source_object_type': 'SourceObjectType',  # noqa: E501
        'switch_id': 'SwitchId',  # noqa: E501
        'vendor': 'Vendor',  # noqa: E501
        'registered_device': 'RegisteredDevice',  # noqa: E501
    }

    read_only_vars = {
        'adapter_serial',  # noqa: E501
        'admin_action',  # noqa: E501
        'admin_action_state',  # noqa: E501
        'chassis_id',  # noqa: E501
        'current_chassis_id',  # noqa: E501
        'current_slot_id',  # noqa: E501
        'firmware_supportability',  # noqa: E501
        'identifier',  # noqa: E501
        'last_discovery_triggered',  # noqa: E501
        'lifecycle',  # noqa: E501
        'model',  # noqa: E501
        'presence',  # noqa: E501
        'serial',  # noqa: E501
        'slot_id',  # noqa: E501
        'source_object_type',  # noqa: E501
        'switch_id',  # noqa: E501
        'vendor',  # noqa: E501
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):  # noqa: E501
        """EquipmentIdentitySummaryAllOf - a model defined in OpenAPI

        Args:

        Keyword Args:
            class_id (str): The fully-qualified name of the instantiated, concrete type. This property is used as a discriminator to identify the type of the payload when marshaling and unmarshaling data.. defaults to "equipment.IdentitySummary", must be one of ["equipment.IdentitySummary", ]  # noqa: E501
            object_type (str): The fully-qualified name of the instantiated, concrete type. The value should be the same as the 'ClassId' property.. defaults to "equipment.IdentitySummary", must be one of ["equipment.IdentitySummary", ]  # noqa: E501
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
            adapter_serial (str): Serial Identifier of an adapter participating in SWM.. [optional]  # noqa: E501
            admin_action (str): Updated by UI/API to trigger specific action type. * `None` - No operation value for maintenance actions on an equipment. * `Decommission` - Decommission the equipment and temporarily remove it from being managed by Intersight. * `Recommission` - Recommission the equipment. * `Reack` - Reacknowledge the equipment and discover it again. * `Remove` - Remove the equipment permanently from Intersight management. * `Replace` - Replace the equipment with the other one.. [optional] if omitted the server will use the default value of "None"  # noqa: E501
            admin_action_state (str): The state of Maintenance Action performed. This will have three states. Applying - Action is in progress. Applied - Action is completed and applied. Failed - Action has failed. * `None` - Nil value when no action has been triggered by the user. * `Applied` - User configured settings are in applied state. * `Applying` - User settings are being applied on the target server. * `Failed` - User configured settings could not be applied.. [optional] if omitted the server will use the default value of "None"  # noqa: E501
            chassis_id (int): Chassis Identifier of a blade server.. [optional]  # noqa: E501
            current_chassis_id (int): The id of the chassis that the blade is currently located in.. [optional]  # noqa: E501
            current_slot_id (int): The slot number in the chassis that the blade is currently located in.. [optional]  # noqa: E501
            firmware_supportability (str): Describes whether the running CIMC version supports Intersight managed mode. * `Unknown` - The running firmware version is unknown. * `Supported` - The running firmware version is known and supports IMM mode. * `NotSupported` - The running firmware version is known and does not support IMM mode.. [optional] if omitted the server will use the default value of "Unknown"  # noqa: E501
            identifier (int): Numeric Identifier assigned by the management system to the equipment. Identifier can only be changed if it has been PATCHED with the AdminAction property set to 'Recommission'.. [optional]  # noqa: E501
            io_card_identity_list ([EquipmentIoCardIdentity], none_type): [optional]  # noqa: E501
            last_discovery_triggered (str): Denotes the type of discovery that was most recently triggered on this server. * `Unknown` - The last discovery type is unknown. * `Deep` - The last discovery triggered is deep. * `Shallow` - The last discovery triggered is shallow.. [optional] if omitted the server will use the default value of "Unknown"  # noqa: E501
            lifecycle (str): The equipment's lifecycle status. * `None` - Default state of an equipment. This should be an initial state when no state is defined for an equipment. * `Active` - Default Lifecycle State for a physical entity. * `Decommissioned` - Decommission Lifecycle state. * `DecommissionInProgress` - Decommission Inprogress Lifecycle state. * `RecommissionInProgress` - Recommission Inprogress Lifecycle state. * `OperationFailed` - Failed Operation Lifecycle state. * `ReackInProgress` - ReackInProgress Lifecycle state. * `RemoveInProgress` - RemoveInProgress Lifecycle state. * `Discovered` - Discovered Lifecycle state. * `DiscoveryInProgress` - DiscoveryInProgress Lifecycle state. * `DiscoveryFailed` - DiscoveryFailed Lifecycle state. * `FirmwareUpgradeInProgress` - Firmware upgrade is in progress on given physical entity. * `BladeMigrationInProgress` - Server slot migration is in progress on given physical entity. * `Inactive` - Inactive Lifecycle state. * `ReplaceInProgress` - ReplaceInProgress Lifecycle state. * `SlotMismatch` - The blade server is detected in a different chassis/slot than it was previously.. [optional] if omitted the server will use the default value of "None"  # noqa: E501
            model (str): The vendor provided model name for the equipment.. [optional]  # noqa: E501
            presence (str): The presence state of the blade server. * `Unknown` - The default presence state. * `Equipped` - The server is equipped in the slot. * `EquippedMismatch` - The slot is equipped, but there is another server currently inventoried in the slot. * `Missing` - The server is not present in the given slot.. [optional] if omitted the server will use the default value of "Unknown"  # noqa: E501
            serial (str): The serial number of the equipment.. [optional]  # noqa: E501
            slot_id (int): Chassis slot number of a blade server.. [optional]  # noqa: E501
            source_object_type (str): The source object type of this view MO.. [optional]  # noqa: E501
            switch_id (int): Switch ID to which Fabric Extender is connected, ID can be either 1 or 2, equalent to A or B.. [optional]  # noqa: E501
            vendor (str): The manufacturer of the equipment.. [optional]  # noqa: E501
            registered_device (AssetDeviceRegistrationRelationship): [optional]  # noqa: E501
        """

        class_id = kwargs.get('class_id', "equipment.IdentitySummary")
        object_type = kwargs.get('object_type', "equipment.IdentitySummary")
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
        """EquipmentIdentitySummaryAllOf - a model defined in OpenAPI

        Args:

        Keyword Args:
            class_id (str): The fully-qualified name of the instantiated, concrete type. This property is used as a discriminator to identify the type of the payload when marshaling and unmarshaling data.. defaults to "equipment.IdentitySummary", must be one of ["equipment.IdentitySummary", ]  # noqa: E501
            object_type (str): The fully-qualified name of the instantiated, concrete type. The value should be the same as the 'ClassId' property.. defaults to "equipment.IdentitySummary", must be one of ["equipment.IdentitySummary", ]  # noqa: E501
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
            adapter_serial (str): Serial Identifier of an adapter participating in SWM.. [optional]  # noqa: E501
            admin_action (str): Updated by UI/API to trigger specific action type. * `None` - No operation value for maintenance actions on an equipment. * `Decommission` - Decommission the equipment and temporarily remove it from being managed by Intersight. * `Recommission` - Recommission the equipment. * `Reack` - Reacknowledge the equipment and discover it again. * `Remove` - Remove the equipment permanently from Intersight management. * `Replace` - Replace the equipment with the other one.. [optional] if omitted the server will use the default value of "None"  # noqa: E501
            admin_action_state (str): The state of Maintenance Action performed. This will have three states. Applying - Action is in progress. Applied - Action is completed and applied. Failed - Action has failed. * `None` - Nil value when no action has been triggered by the user. * `Applied` - User configured settings are in applied state. * `Applying` - User settings are being applied on the target server. * `Failed` - User configured settings could not be applied.. [optional] if omitted the server will use the default value of "None"  # noqa: E501
            chassis_id (int): Chassis Identifier of a blade server.. [optional]  # noqa: E501
            current_chassis_id (int): The id of the chassis that the blade is currently located in.. [optional]  # noqa: E501
            current_slot_id (int): The slot number in the chassis that the blade is currently located in.. [optional]  # noqa: E501
            firmware_supportability (str): Describes whether the running CIMC version supports Intersight managed mode. * `Unknown` - The running firmware version is unknown. * `Supported` - The running firmware version is known and supports IMM mode. * `NotSupported` - The running firmware version is known and does not support IMM mode.. [optional] if omitted the server will use the default value of "Unknown"  # noqa: E501
            identifier (int): Numeric Identifier assigned by the management system to the equipment. Identifier can only be changed if it has been PATCHED with the AdminAction property set to 'Recommission'.. [optional]  # noqa: E501
            io_card_identity_list ([EquipmentIoCardIdentity], none_type): [optional]  # noqa: E501
            last_discovery_triggered (str): Denotes the type of discovery that was most recently triggered on this server. * `Unknown` - The last discovery type is unknown. * `Deep` - The last discovery triggered is deep. * `Shallow` - The last discovery triggered is shallow.. [optional] if omitted the server will use the default value of "Unknown"  # noqa: E501
            lifecycle (str): The equipment's lifecycle status. * `None` - Default state of an equipment. This should be an initial state when no state is defined for an equipment. * `Active` - Default Lifecycle State for a physical entity. * `Decommissioned` - Decommission Lifecycle state. * `DecommissionInProgress` - Decommission Inprogress Lifecycle state. * `RecommissionInProgress` - Recommission Inprogress Lifecycle state. * `OperationFailed` - Failed Operation Lifecycle state. * `ReackInProgress` - ReackInProgress Lifecycle state. * `RemoveInProgress` - RemoveInProgress Lifecycle state. * `Discovered` - Discovered Lifecycle state. * `DiscoveryInProgress` - DiscoveryInProgress Lifecycle state. * `DiscoveryFailed` - DiscoveryFailed Lifecycle state. * `FirmwareUpgradeInProgress` - Firmware upgrade is in progress on given physical entity. * `BladeMigrationInProgress` - Server slot migration is in progress on given physical entity. * `Inactive` - Inactive Lifecycle state. * `ReplaceInProgress` - ReplaceInProgress Lifecycle state. * `SlotMismatch` - The blade server is detected in a different chassis/slot than it was previously.. [optional] if omitted the server will use the default value of "None"  # noqa: E501
            model (str): The vendor provided model name for the equipment.. [optional]  # noqa: E501
            presence (str): The presence state of the blade server. * `Unknown` - The default presence state. * `Equipped` - The server is equipped in the slot. * `EquippedMismatch` - The slot is equipped, but there is another server currently inventoried in the slot. * `Missing` - The server is not present in the given slot.. [optional] if omitted the server will use the default value of "Unknown"  # noqa: E501
            serial (str): The serial number of the equipment.. [optional]  # noqa: E501
            slot_id (int): Chassis slot number of a blade server.. [optional]  # noqa: E501
            source_object_type (str): The source object type of this view MO.. [optional]  # noqa: E501
            switch_id (int): Switch ID to which Fabric Extender is connected, ID can be either 1 or 2, equalent to A or B.. [optional]  # noqa: E501
            vendor (str): The manufacturer of the equipment.. [optional]  # noqa: E501
            registered_device (AssetDeviceRegistrationRelationship): [optional]  # noqa: E501
        """

        class_id = kwargs.get('class_id', "equipment.IdentitySummary")
        object_type = kwargs.get('object_type', "equipment.IdentitySummary")
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
