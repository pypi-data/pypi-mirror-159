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
    from intersight.model.equipment_switch_card_relationship import EquipmentSwitchCardRelationship
    from intersight.model.inventory_device_info_relationship import InventoryDeviceInfoRelationship
    from intersight.model.network_supervisor_card_relationship import NetworkSupervisorCardRelationship
    from intersight.model.port_group_relationship import PortGroupRelationship
    from intersight.model.port_sub_group_relationship import PortSubGroupRelationship
    globals()['AssetDeviceRegistrationRelationship'] = AssetDeviceRegistrationRelationship
    globals()['EquipmentSwitchCardRelationship'] = EquipmentSwitchCardRelationship
    globals()['InventoryDeviceInfoRelationship'] = InventoryDeviceInfoRelationship
    globals()['NetworkSupervisorCardRelationship'] = NetworkSupervisorCardRelationship
    globals()['PortGroupRelationship'] = PortGroupRelationship
    globals()['PortSubGroupRelationship'] = PortSubGroupRelationship


class FcPhysicalPortAllOf(ModelNormal):
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
            'FC.PHYSICALPORT': "fc.PhysicalPort",
        },
        ('object_type',): {
            'FC.PHYSICALPORT': "fc.PhysicalPort",
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
            'admin_speed': (str,),  # noqa: E501
            'admin_state': (str,),  # noqa: E501
            'aggregate_port_id': (int,),  # noqa: E501
            'b2b_credit': (int,),  # noqa: E501
            'max_speed': (str,),  # noqa: E501
            'mode': (str,),  # noqa: E501
            'name': (str,),  # noqa: E501
            'oper_speed': (str,),  # noqa: E501
            'peer_dn': (str,),  # noqa: E501
            'port_channel_id': (int,),  # noqa: E501
            'transceiver_type': (str,),  # noqa: E501
            'vsan': (int,),  # noqa: E501
            'wwn': (str,),  # noqa: E501
            'equipment_switch_card': (EquipmentSwitchCardRelationship,),  # noqa: E501
            'inventory_device_info': (InventoryDeviceInfoRelationship,),  # noqa: E501
            'network_supervisor_card': (NetworkSupervisorCardRelationship,),  # noqa: E501
            'port_group': (PortGroupRelationship,),  # noqa: E501
            'port_sub_group': (PortSubGroupRelationship,),  # noqa: E501
            'registered_device': (AssetDeviceRegistrationRelationship,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'class_id': 'ClassId',  # noqa: E501
        'object_type': 'ObjectType',  # noqa: E501
        'admin_speed': 'AdminSpeed',  # noqa: E501
        'admin_state': 'AdminState',  # noqa: E501
        'aggregate_port_id': 'AggregatePortId',  # noqa: E501
        'b2b_credit': 'B2bCredit',  # noqa: E501
        'max_speed': 'MaxSpeed',  # noqa: E501
        'mode': 'Mode',  # noqa: E501
        'name': 'Name',  # noqa: E501
        'oper_speed': 'OperSpeed',  # noqa: E501
        'peer_dn': 'PeerDn',  # noqa: E501
        'port_channel_id': 'PortChannelId',  # noqa: E501
        'transceiver_type': 'TransceiverType',  # noqa: E501
        'vsan': 'Vsan',  # noqa: E501
        'wwn': 'Wwn',  # noqa: E501
        'equipment_switch_card': 'EquipmentSwitchCard',  # noqa: E501
        'inventory_device_info': 'InventoryDeviceInfo',  # noqa: E501
        'network_supervisor_card': 'NetworkSupervisorCard',  # noqa: E501
        'port_group': 'PortGroup',  # noqa: E501
        'port_sub_group': 'PortSubGroup',  # noqa: E501
        'registered_device': 'RegisteredDevice',  # noqa: E501
    }

    read_only_vars = {
        'admin_speed',  # noqa: E501
        'admin_state',  # noqa: E501
        'aggregate_port_id',  # noqa: E501
        'b2b_credit',  # noqa: E501
        'max_speed',  # noqa: E501
        'mode',  # noqa: E501
        'name',  # noqa: E501
        'oper_speed',  # noqa: E501
        'peer_dn',  # noqa: E501
        'port_channel_id',  # noqa: E501
        'transceiver_type',  # noqa: E501
        'vsan',  # noqa: E501
        'wwn',  # noqa: E501
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):  # noqa: E501
        """FcPhysicalPortAllOf - a model defined in OpenAPI

        Args:

        Keyword Args:
            class_id (str): The fully-qualified name of the instantiated, concrete type. This property is used as a discriminator to identify the type of the payload when marshaling and unmarshaling data.. defaults to "fc.PhysicalPort", must be one of ["fc.PhysicalPort", ]  # noqa: E501
            object_type (str): The fully-qualified name of the instantiated, concrete type. The value should be the same as the 'ClassId' property.. defaults to "fc.PhysicalPort", must be one of ["fc.PhysicalPort", ]  # noqa: E501
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
            admin_speed (str): Administrator configured Speed applied on the port.. [optional]  # noqa: E501
            admin_state (str): Administratively configured state (enabled/disabled) for this port.. [optional]  # noqa: E501
            aggregate_port_id (int): Breakout port member in the Fabric Interconnect.. [optional] if omitted the server will use the default value of 0  # noqa: E501
            b2b_credit (int): Buffer to Buffer credits of FC port.. [optional]  # noqa: E501
            max_speed (str): Maximum Speed with which the port operates.. [optional]  # noqa: E501
            mode (str): Mode information N_proxy, F or E associated to the Fibre Channel port.. [optional]  # noqa: E501
            name (str): Name of the physical port of FC.. [optional]  # noqa: E501
            oper_speed (str): Operational Speed with which the port operates.. [optional]  # noqa: E501
            peer_dn (str): PeerDn for fibre channel physical port.. [optional]  # noqa: E501
            port_channel_id (int): Port channel id of FC port channel created on FI switch.. [optional]  # noqa: E501
            transceiver_type (str): Transceiver type of a Fibre Channel port.. [optional]  # noqa: E501
            vsan (int): Virtual San that is associated to the port.. [optional]  # noqa: E501
            wwn (str): World Wide Name of a Fibre Channel port.. [optional]  # noqa: E501
            equipment_switch_card (EquipmentSwitchCardRelationship): [optional]  # noqa: E501
            inventory_device_info (InventoryDeviceInfoRelationship): [optional]  # noqa: E501
            network_supervisor_card (NetworkSupervisorCardRelationship): [optional]  # noqa: E501
            port_group (PortGroupRelationship): [optional]  # noqa: E501
            port_sub_group (PortSubGroupRelationship): [optional]  # noqa: E501
            registered_device (AssetDeviceRegistrationRelationship): [optional]  # noqa: E501
        """

        class_id = kwargs.get('class_id', "fc.PhysicalPort")
        object_type = kwargs.get('object_type', "fc.PhysicalPort")
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
        """FcPhysicalPortAllOf - a model defined in OpenAPI

        Args:

        Keyword Args:
            class_id (str): The fully-qualified name of the instantiated, concrete type. This property is used as a discriminator to identify the type of the payload when marshaling and unmarshaling data.. defaults to "fc.PhysicalPort", must be one of ["fc.PhysicalPort", ]  # noqa: E501
            object_type (str): The fully-qualified name of the instantiated, concrete type. The value should be the same as the 'ClassId' property.. defaults to "fc.PhysicalPort", must be one of ["fc.PhysicalPort", ]  # noqa: E501
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
            admin_speed (str): Administrator configured Speed applied on the port.. [optional]  # noqa: E501
            admin_state (str): Administratively configured state (enabled/disabled) for this port.. [optional]  # noqa: E501
            aggregate_port_id (int): Breakout port member in the Fabric Interconnect.. [optional] if omitted the server will use the default value of 0  # noqa: E501
            b2b_credit (int): Buffer to Buffer credits of FC port.. [optional]  # noqa: E501
            max_speed (str): Maximum Speed with which the port operates.. [optional]  # noqa: E501
            mode (str): Mode information N_proxy, F or E associated to the Fibre Channel port.. [optional]  # noqa: E501
            name (str): Name of the physical port of FC.. [optional]  # noqa: E501
            oper_speed (str): Operational Speed with which the port operates.. [optional]  # noqa: E501
            peer_dn (str): PeerDn for fibre channel physical port.. [optional]  # noqa: E501
            port_channel_id (int): Port channel id of FC port channel created on FI switch.. [optional]  # noqa: E501
            transceiver_type (str): Transceiver type of a Fibre Channel port.. [optional]  # noqa: E501
            vsan (int): Virtual San that is associated to the port.. [optional]  # noqa: E501
            wwn (str): World Wide Name of a Fibre Channel port.. [optional]  # noqa: E501
            equipment_switch_card (EquipmentSwitchCardRelationship): [optional]  # noqa: E501
            inventory_device_info (InventoryDeviceInfoRelationship): [optional]  # noqa: E501
            network_supervisor_card (NetworkSupervisorCardRelationship): [optional]  # noqa: E501
            port_group (PortGroupRelationship): [optional]  # noqa: E501
            port_sub_group (PortSubGroupRelationship): [optional]  # noqa: E501
            registered_device (AssetDeviceRegistrationRelationship): [optional]  # noqa: E501
        """

        class_id = kwargs.get('class_id', "fc.PhysicalPort")
        object_type = kwargs.get('object_type', "fc.PhysicalPort")
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
