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
    from intersight.model.display_names import DisplayNames
    from intersight.model.mo_base_mo import MoBaseMo
    from intersight.model.mo_base_mo_relationship import MoBaseMoRelationship
    from intersight.model.mo_tag import MoTag
    from intersight.model.mo_version_context import MoVersionContext
    from intersight.model.niaapi_apic_hweol import NiaapiApicHweol
    from intersight.model.niaapi_dcnm_hweol import NiaapiDcnmHweol
    from intersight.model.niaapi_hardware_eol_all_of import NiaapiHardwareEolAllOf
    globals()['DisplayNames'] = DisplayNames
    globals()['MoBaseMo'] = MoBaseMo
    globals()['MoBaseMoRelationship'] = MoBaseMoRelationship
    globals()['MoTag'] = MoTag
    globals()['MoVersionContext'] = MoVersionContext
    globals()['NiaapiApicHweol'] = NiaapiApicHweol
    globals()['NiaapiDcnmHweol'] = NiaapiDcnmHweol
    globals()['NiaapiHardwareEolAllOf'] = NiaapiHardwareEolAllOf


class NiaapiHardwareEol(ModelComposed):
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
            'APICHWEOL': "niaapi.ApicHweol",
            'DCNMHWEOL': "niaapi.DcnmHweol",
        },
        ('object_type',): {
            'APICHWEOL': "niaapi.ApicHweol",
            'DCNMHWEOL': "niaapi.DcnmHweol",
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
            'affected_pids': (str,),  # noqa: E501
            'announcement_date': (datetime,),  # noqa: E501
            'announcement_date_epoch': (int,),  # noqa: E501
            'bulletin_no': (str,),  # noqa: E501
            'description': (str,),  # noqa: E501
            'endof_new_service_attachment_date': (datetime,),  # noqa: E501
            'endof_new_service_attachment_date_epoch': (int,),  # noqa: E501
            'endof_routine_failure_analysis_date': (datetime,),  # noqa: E501
            'endof_routine_failure_analysis_date_epoch': (int,),  # noqa: E501
            'endof_sale_date': (datetime,),  # noqa: E501
            'endof_sale_date_epoch': (int,),  # noqa: E501
            'endof_security_support': (datetime,),  # noqa: E501
            'endof_security_support_epoch': (int,),  # noqa: E501
            'endof_service_contract_renewal_date': (datetime,),  # noqa: E501
            'endof_service_contract_renewal_date_epoch': (int,),  # noqa: E501
            'endof_sw_maintenance_date': (datetime,),  # noqa: E501
            'endof_sw_maintenance_date_epoch': (int,),  # noqa: E501
            'hardware_eol_url': (str,),  # noqa: E501
            'headline': (str,),  # noqa: E501
            'last_dateof_support': (datetime,),  # noqa: E501
            'last_dateof_support_epoch': (int,),  # noqa: E501
            'last_ship_date': (datetime,),  # noqa: E501
            'last_ship_date_epoch': (int,),  # noqa: E501
            'migration_url': (str,),  # noqa: E501
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
        }

    @cached_property
    def discriminator():
        lazy_import()
        val = {
            'niaapi.ApicHweol': NiaapiApicHweol,
            'niaapi.DcnmHweol': NiaapiDcnmHweol,
        }
        if not val:
            return None
        return {'class_id': val}

    attribute_map = {
        'class_id': 'ClassId',  # noqa: E501
        'object_type': 'ObjectType',  # noqa: E501
        'affected_pids': 'AffectedPids',  # noqa: E501
        'announcement_date': 'AnnouncementDate',  # noqa: E501
        'announcement_date_epoch': 'AnnouncementDateEpoch',  # noqa: E501
        'bulletin_no': 'BulletinNo',  # noqa: E501
        'description': 'Description',  # noqa: E501
        'endof_new_service_attachment_date': 'EndofNewServiceAttachmentDate',  # noqa: E501
        'endof_new_service_attachment_date_epoch': 'EndofNewServiceAttachmentDateEpoch',  # noqa: E501
        'endof_routine_failure_analysis_date': 'EndofRoutineFailureAnalysisDate',  # noqa: E501
        'endof_routine_failure_analysis_date_epoch': 'EndofRoutineFailureAnalysisDateEpoch',  # noqa: E501
        'endof_sale_date': 'EndofSaleDate',  # noqa: E501
        'endof_sale_date_epoch': 'EndofSaleDateEpoch',  # noqa: E501
        'endof_security_support': 'EndofSecuritySupport',  # noqa: E501
        'endof_security_support_epoch': 'EndofSecuritySupportEpoch',  # noqa: E501
        'endof_service_contract_renewal_date': 'EndofServiceContractRenewalDate',  # noqa: E501
        'endof_service_contract_renewal_date_epoch': 'EndofServiceContractRenewalDateEpoch',  # noqa: E501
        'endof_sw_maintenance_date': 'EndofSwMaintenanceDate',  # noqa: E501
        'endof_sw_maintenance_date_epoch': 'EndofSwMaintenanceDateEpoch',  # noqa: E501
        'hardware_eol_url': 'HardwareEolUrl',  # noqa: E501
        'headline': 'Headline',  # noqa: E501
        'last_dateof_support': 'LastDateofSupport',  # noqa: E501
        'last_dateof_support_epoch': 'LastDateofSupportEpoch',  # noqa: E501
        'last_ship_date': 'LastShipDate',  # noqa: E501
        'last_ship_date_epoch': 'LastShipDateEpoch',  # noqa: E501
        'migration_url': 'MigrationUrl',  # noqa: E501
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
    }

    read_only_vars = {
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
    def _from_openapi_data(cls, class_id, object_type, *args, **kwargs):  # noqa: E501
        """NiaapiHardwareEol - a model defined in OpenAPI

        Keyword Args:
            class_id (str): The fully-qualified name of the instantiated, concrete type. This property is used as a discriminator to identify the type of the payload when marshaling and unmarshaling data. The enum values provides the list of concrete types that can be instantiated from this abstract type.
            object_type (str): The fully-qualified name of the instantiated, concrete type. The value should be the same as the 'ClassId' property. The enum values provides the list of concrete types that can be instantiated from this abstract type.
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
            affected_pids (str): String contains the PID of hardwares affected by this notice, seperated by comma.. [optional]  # noqa: E501
            announcement_date (datetime): When this notice is announced.. [optional]  # noqa: E501
            announcement_date_epoch (int): Epoch time of Announcement Date.. [optional]  # noqa: E501
            bulletin_no (str): The bulletinno of this hardware end of life notice.. [optional]  # noqa: E501
            description (str): The description of this hardware end of life notice.. [optional]  # noqa: E501
            endof_new_service_attachment_date (datetime): Date time of end of new services attachment  .. [optional]  # noqa: E501
            endof_new_service_attachment_date_epoch (int): Epoch time of New service attachment Date .. [optional]  # noqa: E501
            endof_routine_failure_analysis_date (datetime): Date time of end of routinefailure analysis.. [optional]  # noqa: E501
            endof_routine_failure_analysis_date_epoch (int): Epoch time of End of Routine Failure Analysis Date.. [optional]  # noqa: E501
            endof_sale_date (datetime): When this hardware will end sale.. [optional]  # noqa: E501
            endof_sale_date_epoch (int): Epoch time of End of Sale Date.. [optional]  # noqa: E501
            endof_security_support (datetime): Date time of end of security support .. [optional]  # noqa: E501
            endof_security_support_epoch (int): Epoch time of End of Security Support Date .. [optional]  # noqa: E501
            endof_service_contract_renewal_date (datetime): Date time of end of service contract renew .. [optional]  # noqa: E501
            endof_service_contract_renewal_date_epoch (int): Epoch time of End of Renewal service contract.. [optional]  # noqa: E501
            endof_sw_maintenance_date (datetime): The date of end of maintainance.. [optional]  # noqa: E501
            endof_sw_maintenance_date_epoch (int): Epoch time of End of maintenance Date.. [optional]  # noqa: E501
            hardware_eol_url (str): Hardware end of sale URL link to the notice webpage.. [optional]  # noqa: E501
            headline (str): The title of this hardware end of life notice.. [optional]  # noqa: E501
            last_dateof_support (datetime): Date time of end of support .. [optional]  # noqa: E501
            last_dateof_support_epoch (int): Epoch time of last date of support .. [optional]  # noqa: E501
            last_ship_date (datetime): Date time of Lastship Date.. [optional]  # noqa: E501
            last_ship_date_epoch (int): Epoch time of last ship Date.. [optional]  # noqa: E501
            migration_url (str): The URL of this migration notice.. [optional]  # noqa: E501
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
        """

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
    def __init__(self, class_id, object_type, *args, **kwargs):  # noqa: E501
        """NiaapiHardwareEol - a model defined in OpenAPI

        Keyword Args:
            class_id (str): The fully-qualified name of the instantiated, concrete type. This property is used as a discriminator to identify the type of the payload when marshaling and unmarshaling data. The enum values provides the list of concrete types that can be instantiated from this abstract type.
            object_type (str): The fully-qualified name of the instantiated, concrete type. The value should be the same as the 'ClassId' property. The enum values provides the list of concrete types that can be instantiated from this abstract type.
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
            affected_pids (str): String contains the PID of hardwares affected by this notice, seperated by comma.. [optional]  # noqa: E501
            announcement_date (datetime): When this notice is announced.. [optional]  # noqa: E501
            announcement_date_epoch (int): Epoch time of Announcement Date.. [optional]  # noqa: E501
            bulletin_no (str): The bulletinno of this hardware end of life notice.. [optional]  # noqa: E501
            description (str): The description of this hardware end of life notice.. [optional]  # noqa: E501
            endof_new_service_attachment_date (datetime): Date time of end of new services attachment  .. [optional]  # noqa: E501
            endof_new_service_attachment_date_epoch (int): Epoch time of New service attachment Date .. [optional]  # noqa: E501
            endof_routine_failure_analysis_date (datetime): Date time of end of routinefailure analysis.. [optional]  # noqa: E501
            endof_routine_failure_analysis_date_epoch (int): Epoch time of End of Routine Failure Analysis Date.. [optional]  # noqa: E501
            endof_sale_date (datetime): When this hardware will end sale.. [optional]  # noqa: E501
            endof_sale_date_epoch (int): Epoch time of End of Sale Date.. [optional]  # noqa: E501
            endof_security_support (datetime): Date time of end of security support .. [optional]  # noqa: E501
            endof_security_support_epoch (int): Epoch time of End of Security Support Date .. [optional]  # noqa: E501
            endof_service_contract_renewal_date (datetime): Date time of end of service contract renew .. [optional]  # noqa: E501
            endof_service_contract_renewal_date_epoch (int): Epoch time of End of Renewal service contract.. [optional]  # noqa: E501
            endof_sw_maintenance_date (datetime): The date of end of maintainance.. [optional]  # noqa: E501
            endof_sw_maintenance_date_epoch (int): Epoch time of End of maintenance Date.. [optional]  # noqa: E501
            hardware_eol_url (str): Hardware end of sale URL link to the notice webpage.. [optional]  # noqa: E501
            headline (str): The title of this hardware end of life notice.. [optional]  # noqa: E501
            last_dateof_support (datetime): Date time of end of support .. [optional]  # noqa: E501
            last_dateof_support_epoch (int): Epoch time of last date of support .. [optional]  # noqa: E501
            last_ship_date (datetime): Date time of Lastship Date.. [optional]  # noqa: E501
            last_ship_date_epoch (int): Epoch time of last ship Date.. [optional]  # noqa: E501
            migration_url (str): The URL of this migration notice.. [optional]  # noqa: E501
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
              MoBaseMo,
              NiaapiHardwareEolAllOf,
          ],
          'oneOf': [
          ],
        }
