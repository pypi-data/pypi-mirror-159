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
    from intersight.model.organization_organization_relationship import OrganizationOrganizationRelationship
    from intersight.model.tam_action import TamAction
    from intersight.model.tam_api_data_source import TamApiDataSource
    globals()['OrganizationOrganizationRelationship'] = OrganizationOrganizationRelationship
    globals()['TamAction'] = TamAction
    globals()['TamApiDataSource'] = TamApiDataSource


class TamSecurityAdvisoryAllOf(ModelNormal):
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
            'TAM.SECURITYADVISORY': "tam.SecurityAdvisory",
        },
        ('object_type',): {
            'TAM.SECURITYADVISORY': "tam.SecurityAdvisory",
        },
        ('status',): {
            'INTERIM': "interim",
            'FINAL': "final",
        },
    }

    validations = {
        ('base_score',): {
            'inclusive_maximum': 10.0,
            'inclusive_minimum': 0.0,
        },
        ('environmental_score',): {
            'inclusive_maximum': 10.0,
            'inclusive_minimum': 0.0,
        },
        ('external_url',): {
            'regex': {
                'pattern': r'^$|^(?:http(s)?:\/\/)?[\w.-]+(?:\.[\w\.-]+)+[\w\-\._~:\/?#[\]@!\$&\'\(\)\*\+,;=.]+$',  # noqa: E501
            },
        },
        ('temporal_score',): {
            'inclusive_maximum': 10.0,
            'inclusive_minimum': 0.0,
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
            'actions': ([TamAction], none_type,),  # noqa: E501
            'advisory_id': (str,),  # noqa: E501
            'api_data_sources': ([TamApiDataSource], none_type,),  # noqa: E501
            'base_score': (float,),  # noqa: E501
            'cve_ids': ([str], none_type,),  # noqa: E501
            'date_published': (datetime,),  # noqa: E501
            'date_updated': (datetime,),  # noqa: E501
            'environmental_score': (float,),  # noqa: E501
            'external_url': (str,),  # noqa: E501
            'recommendation': (str,),  # noqa: E501
            'status': (str,),  # noqa: E501
            'temporal_score': (float,),  # noqa: E501
            'version': (str,),  # noqa: E501
            'workaround': (str,),  # noqa: E501
            'organization': (OrganizationOrganizationRelationship,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'class_id': 'ClassId',  # noqa: E501
        'object_type': 'ObjectType',  # noqa: E501
        'actions': 'Actions',  # noqa: E501
        'advisory_id': 'AdvisoryId',  # noqa: E501
        'api_data_sources': 'ApiDataSources',  # noqa: E501
        'base_score': 'BaseScore',  # noqa: E501
        'cve_ids': 'CveIds',  # noqa: E501
        'date_published': 'DatePublished',  # noqa: E501
        'date_updated': 'DateUpdated',  # noqa: E501
        'environmental_score': 'EnvironmentalScore',  # noqa: E501
        'external_url': 'ExternalUrl',  # noqa: E501
        'recommendation': 'Recommendation',  # noqa: E501
        'status': 'Status',  # noqa: E501
        'temporal_score': 'TemporalScore',  # noqa: E501
        'version': 'Version',  # noqa: E501
        'workaround': 'Workaround',  # noqa: E501
        'organization': 'Organization',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):  # noqa: E501
        """TamSecurityAdvisoryAllOf - a model defined in OpenAPI

        Args:

        Keyword Args:
            class_id (str): The fully-qualified name of the instantiated, concrete type. This property is used as a discriminator to identify the type of the payload when marshaling and unmarshaling data.. defaults to "tam.SecurityAdvisory", must be one of ["tam.SecurityAdvisory", ]  # noqa: E501
            object_type (str): The fully-qualified name of the instantiated, concrete type. The value should be the same as the 'ClassId' property.. defaults to "tam.SecurityAdvisory", must be one of ["tam.SecurityAdvisory", ]  # noqa: E501
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
            actions ([TamAction], none_type): [optional]  # noqa: E501
            advisory_id (str): Cisco generated identifier for the published security advisory.. [optional]  # noqa: E501
            api_data_sources ([TamApiDataSource], none_type): [optional]  # noqa: E501
            base_score (float): CVSS version 3 base score for the security Advisory.. [optional]  # noqa: E501
            cve_ids ([str], none_type): [optional]  # noqa: E501
            date_published (datetime): Date when the security advisory was first published by Cisco.. [optional]  # noqa: E501
            date_updated (datetime): Date when the security advisory was last updated by Cisco.. [optional]  # noqa: E501
            environmental_score (float): CVSS version 3 environmental score for the security Advisory.. [optional]  # noqa: E501
            external_url (str): A link to an external URL describing security Advisory in more details.. [optional]  # noqa: E501
            recommendation (str): Recommended action to resolve the security advisory.. [optional]  # noqa: E501
            status (str): Cisco assigned status of the published advisory based on whether the investigation is complete or on-going. * `interim` - The Cisco investigation for the advisory is ongoing. Cisco will issue revisions to the advisory when additional information, including fixed software release data, becomes available. * `final` - Cisco has completed its evaluation of the vulnerability described in the advisory. There will be no further updates unless there is a material change in the nature of the vulnerability.. [optional] if omitted the server will use the default value of "interim"  # noqa: E501
            temporal_score (float): CVSS version 3 temporal score for the security Advisory.. [optional]  # noqa: E501
            version (str): Cisco assigned advisory version after latest revision.. [optional]  # noqa: E501
            workaround (str): Workarounds available for the advisory.. [optional]  # noqa: E501
            organization (OrganizationOrganizationRelationship): [optional]  # noqa: E501
        """

        class_id = kwargs.get('class_id', "tam.SecurityAdvisory")
        object_type = kwargs.get('object_type', "tam.SecurityAdvisory")
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
        """TamSecurityAdvisoryAllOf - a model defined in OpenAPI

        Args:

        Keyword Args:
            class_id (str): The fully-qualified name of the instantiated, concrete type. This property is used as a discriminator to identify the type of the payload when marshaling and unmarshaling data.. defaults to "tam.SecurityAdvisory", must be one of ["tam.SecurityAdvisory", ]  # noqa: E501
            object_type (str): The fully-qualified name of the instantiated, concrete type. The value should be the same as the 'ClassId' property.. defaults to "tam.SecurityAdvisory", must be one of ["tam.SecurityAdvisory", ]  # noqa: E501
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
            actions ([TamAction], none_type): [optional]  # noqa: E501
            advisory_id (str): Cisco generated identifier for the published security advisory.. [optional]  # noqa: E501
            api_data_sources ([TamApiDataSource], none_type): [optional]  # noqa: E501
            base_score (float): CVSS version 3 base score for the security Advisory.. [optional]  # noqa: E501
            cve_ids ([str], none_type): [optional]  # noqa: E501
            date_published (datetime): Date when the security advisory was first published by Cisco.. [optional]  # noqa: E501
            date_updated (datetime): Date when the security advisory was last updated by Cisco.. [optional]  # noqa: E501
            environmental_score (float): CVSS version 3 environmental score for the security Advisory.. [optional]  # noqa: E501
            external_url (str): A link to an external URL describing security Advisory in more details.. [optional]  # noqa: E501
            recommendation (str): Recommended action to resolve the security advisory.. [optional]  # noqa: E501
            status (str): Cisco assigned status of the published advisory based on whether the investigation is complete or on-going. * `interim` - The Cisco investigation for the advisory is ongoing. Cisco will issue revisions to the advisory when additional information, including fixed software release data, becomes available. * `final` - Cisco has completed its evaluation of the vulnerability described in the advisory. There will be no further updates unless there is a material change in the nature of the vulnerability.. [optional] if omitted the server will use the default value of "interim"  # noqa: E501
            temporal_score (float): CVSS version 3 temporal score for the security Advisory.. [optional]  # noqa: E501
            version (str): Cisco assigned advisory version after latest revision.. [optional]  # noqa: E501
            workaround (str): Workarounds available for the advisory.. [optional]  # noqa: E501
            organization (OrganizationOrganizationRelationship): [optional]  # noqa: E501
        """

        class_id = kwargs.get('class_id', "tam.SecurityAdvisory")
        object_type = kwargs.get('object_type', "tam.SecurityAdvisory")
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
