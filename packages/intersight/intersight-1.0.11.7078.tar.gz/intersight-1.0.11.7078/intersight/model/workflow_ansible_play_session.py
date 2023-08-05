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
    from intersight.model.workflow_ansible_play_session_all_of import WorkflowAnsiblePlaySessionAllOf
    from intersight.model.workflow_api import WorkflowApi
    globals()['WorkflowAnsiblePlaySessionAllOf'] = WorkflowAnsiblePlaySessionAllOf
    globals()['WorkflowApi'] = WorkflowApi


class WorkflowAnsiblePlaySession(ModelComposed):
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
            'WORKFLOW.ANSIBLEPLAYSESSION': "workflow.AnsiblePlaySession",
        },
        ('object_type',): {
            'WORKFLOW.ANSIBLEPLAYSESSION': "workflow.AnsiblePlaySession",
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
            'command_line_arguments': (str,),  # noqa: E501
            'host_inventory': (str,),  # noqa: E501
            'playbook_path': (str,),  # noqa: E501
            'ssh_op_timeout': (str,),  # noqa: E501
            'asset_target_moid': (str,),  # noqa: E501
            'body': (str,),  # noqa: E501
            'content_type': (str,),  # noqa: E501
            'description': (str,),  # noqa: E501
            'error_content_type': (str,),  # noqa: E501
            'label': (str,),  # noqa: E501
            'name': (str,),  # noqa: E501
            'outcomes': (bool, date, datetime, dict, float, int, list, str, none_type,),  # noqa: E501
            'response_spec': (bool, date, datetime, dict, float, int, list, str, none_type,),  # noqa: E501
            'skip_on_condition': (str,),  # noqa: E501
            'start_delay': (int,),  # noqa: E501
            'timeout': (int,),  # noqa: E501
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
        'command_line_arguments': 'CommandLineArguments',  # noqa: E501
        'host_inventory': 'HostInventory',  # noqa: E501
        'playbook_path': 'PlaybookPath',  # noqa: E501
        'ssh_op_timeout': 'SshOpTimeout',  # noqa: E501
        'asset_target_moid': 'AssetTargetMoid',  # noqa: E501
        'body': 'Body',  # noqa: E501
        'content_type': 'ContentType',  # noqa: E501
        'description': 'Description',  # noqa: E501
        'error_content_type': 'ErrorContentType',  # noqa: E501
        'label': 'Label',  # noqa: E501
        'name': 'Name',  # noqa: E501
        'outcomes': 'Outcomes',  # noqa: E501
        'response_spec': 'ResponseSpec',  # noqa: E501
        'skip_on_condition': 'SkipOnCondition',  # noqa: E501
        'start_delay': 'StartDelay',  # noqa: E501
        'timeout': 'Timeout',  # noqa: E501
    }

    read_only_vars = {
        'asset_target_moid',  # noqa: E501
    }

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):  # noqa: E501
        """WorkflowAnsiblePlaySession - a model defined in OpenAPI

        Keyword Args:
            class_id (str): The fully-qualified name of the instantiated, concrete type. This property is used as a discriminator to identify the type of the payload when marshaling and unmarshaling data.. defaults to "workflow.AnsiblePlaySession", must be one of ["workflow.AnsiblePlaySession", ]  # noqa: E501
            object_type (str): The fully-qualified name of the instantiated, concrete type. The value should be the same as the 'ClassId' property.. defaults to "workflow.AnsiblePlaySession", must be one of ["workflow.AnsiblePlaySession", ]  # noqa: E501
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
            command_line_arguments (str): The command line arguments for running the Ansible playbook against the given endpoint. Escape character backslash needs to be used when the command line arguments contain double quotes in them.. [optional]  # noqa: E501
            host_inventory (str): The path of the host inventory file that resides on the Ansible Endpoint target or the comma separated list of hosts on which the Ansible playbook is to be run. Make sure to suffix a comma when the list of hosts is provided as input, even if the list has only one value.. [optional]  # noqa: E501
            playbook_path (str): The path of the Ansible playbook that resides on the Ansible Endpoint target.. [optional]  # noqa: E501
            ssh_op_timeout (str): SSH operation timeout value in seconds. Value provided should be string representation of an interger.. [optional]  # noqa: E501
            asset_target_moid (str): Asset target defines the remote target endpoints which are either managed by Intersight or their service APIs are invoked from Intersight. Generic API executor service Jasmine can invoke these remote APIs via its executors. Asset targets can be accessed directly for cloud targets or via an associated Intersight Assist. Prerequisite to use asset targets is to persist the target details. Asset target MoRef can be given as task input of type TargetDataType. Fusion determines and populates the target context with the Assist if associated with. It is set internally at the API level. In case of an associated assist, it is used by Assist to fetch the target details and form the API request to send to endpoints. In case of cloud asset targets, Jasmine fetched the target details from DB, forms the API request and sends it to the target.. [optional]  # noqa: E501
            body (str): The optional request body that is sent as part of this API request. The request body can contain a golang template that can be populated with task input parameters and previous API output parameters.. [optional]  # noqa: E501
            content_type (str): Intersight Orchestrator, with the support of response parser specification, can extract the values from API responses and map them to task output parameters. The value extraction is supported for response content types XML, JSON and Text. The type of the content that gets passed as payload and response in this API. The supported values are json, xml, text.. [optional]  # noqa: E501
            description (str): A description that task designer can add to individual API requests that explain  what the API call is about.. [optional]  # noqa: E501
            error_content_type (str): Intersight Orchestrator, with the support of response parser specification, can extract the values from API responses and map them to task output parameters. The value extraction is supported for response content types XML, JSON and Text. Optional input to specify the content type in case of error API response. This should be used if the content type of error response is different from that of the success response. If not specified, contentType input value is used to parse the error response.. [optional]  # noqa: E501
            label (str): A user friendly label that task designers have given to the batch API request.. [optional]  # noqa: E501
            name (str): A reference name for this API request within the batch API request. This name shall be used to map the API output parameters to subsequent API input parameters within a batch API task.. [optional]  # noqa: E501
            outcomes (bool, date, datetime, dict, float, int, list, str, none_type): All the possible outcomes of this API are captured here. Outcomes property is a collection property of type workflow.Outcome objects. The outcomes can be mapped to the message to be shown. The outcomes are evaluated in the order they are given. At the end of the outcomes list, an catchall success/fail outcome can be added with condition as 'true'. This is an optional property and if not specified the task will be marked as success.. [optional]  # noqa: E501
            response_spec (bool, date, datetime, dict, float, int, list, str, none_type): The optional grammar specification for parsing the response to extract the required values. The specification should have extraction specification specified for all the API output parameters.. [optional]  # noqa: E501
            skip_on_condition (str): The skip expression, if provided, allows the batch API executor to skip the api execution when the given expression evaluates to true. The expression is given as such a golang template that has to be evaluated to a final content true/false. The expression is an optional and in case not provided, the API will always be executed.. [optional]  # noqa: E501
            start_delay (int): The delay in seconds after which the API needs to be executed. By default, the given API is executed immediately. Specifying a start delay adds to the delay to execution. Start Delay is not supported for the first API in the Batch and cumulative delay of all the APIs in the Batch should not exceed the task time out.. [optional]  # noqa: E501
            timeout (int): The duration in seconds by which the API response is expected from the API target. If the end point does not respond for the API request within this timeout duration, the task will be marked as failed.. [optional]  # noqa: E501
        """

        class_id = kwargs.get('class_id', "workflow.AnsiblePlaySession")
        object_type = kwargs.get('object_type', "workflow.AnsiblePlaySession")
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
        """WorkflowAnsiblePlaySession - a model defined in OpenAPI

        Keyword Args:
            class_id (str): The fully-qualified name of the instantiated, concrete type. This property is used as a discriminator to identify the type of the payload when marshaling and unmarshaling data.. defaults to "workflow.AnsiblePlaySession", must be one of ["workflow.AnsiblePlaySession", ]  # noqa: E501
            object_type (str): The fully-qualified name of the instantiated, concrete type. The value should be the same as the 'ClassId' property.. defaults to "workflow.AnsiblePlaySession", must be one of ["workflow.AnsiblePlaySession", ]  # noqa: E501
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
            command_line_arguments (str): The command line arguments for running the Ansible playbook against the given endpoint. Escape character backslash needs to be used when the command line arguments contain double quotes in them.. [optional]  # noqa: E501
            host_inventory (str): The path of the host inventory file that resides on the Ansible Endpoint target or the comma separated list of hosts on which the Ansible playbook is to be run. Make sure to suffix a comma when the list of hosts is provided as input, even if the list has only one value.. [optional]  # noqa: E501
            playbook_path (str): The path of the Ansible playbook that resides on the Ansible Endpoint target.. [optional]  # noqa: E501
            ssh_op_timeout (str): SSH operation timeout value in seconds. Value provided should be string representation of an interger.. [optional]  # noqa: E501
            asset_target_moid (str): Asset target defines the remote target endpoints which are either managed by Intersight or their service APIs are invoked from Intersight. Generic API executor service Jasmine can invoke these remote APIs via its executors. Asset targets can be accessed directly for cloud targets or via an associated Intersight Assist. Prerequisite to use asset targets is to persist the target details. Asset target MoRef can be given as task input of type TargetDataType. Fusion determines and populates the target context with the Assist if associated with. It is set internally at the API level. In case of an associated assist, it is used by Assist to fetch the target details and form the API request to send to endpoints. In case of cloud asset targets, Jasmine fetched the target details from DB, forms the API request and sends it to the target.. [optional]  # noqa: E501
            body (str): The optional request body that is sent as part of this API request. The request body can contain a golang template that can be populated with task input parameters and previous API output parameters.. [optional]  # noqa: E501
            content_type (str): Intersight Orchestrator, with the support of response parser specification, can extract the values from API responses and map them to task output parameters. The value extraction is supported for response content types XML, JSON and Text. The type of the content that gets passed as payload and response in this API. The supported values are json, xml, text.. [optional]  # noqa: E501
            description (str): A description that task designer can add to individual API requests that explain  what the API call is about.. [optional]  # noqa: E501
            error_content_type (str): Intersight Orchestrator, with the support of response parser specification, can extract the values from API responses and map them to task output parameters. The value extraction is supported for response content types XML, JSON and Text. Optional input to specify the content type in case of error API response. This should be used if the content type of error response is different from that of the success response. If not specified, contentType input value is used to parse the error response.. [optional]  # noqa: E501
            label (str): A user friendly label that task designers have given to the batch API request.. [optional]  # noqa: E501
            name (str): A reference name for this API request within the batch API request. This name shall be used to map the API output parameters to subsequent API input parameters within a batch API task.. [optional]  # noqa: E501
            outcomes (bool, date, datetime, dict, float, int, list, str, none_type): All the possible outcomes of this API are captured here. Outcomes property is a collection property of type workflow.Outcome objects. The outcomes can be mapped to the message to be shown. The outcomes are evaluated in the order they are given. At the end of the outcomes list, an catchall success/fail outcome can be added with condition as 'true'. This is an optional property and if not specified the task will be marked as success.. [optional]  # noqa: E501
            response_spec (bool, date, datetime, dict, float, int, list, str, none_type): The optional grammar specification for parsing the response to extract the required values. The specification should have extraction specification specified for all the API output parameters.. [optional]  # noqa: E501
            skip_on_condition (str): The skip expression, if provided, allows the batch API executor to skip the api execution when the given expression evaluates to true. The expression is given as such a golang template that has to be evaluated to a final content true/false. The expression is an optional and in case not provided, the API will always be executed.. [optional]  # noqa: E501
            start_delay (int): The delay in seconds after which the API needs to be executed. By default, the given API is executed immediately. Specifying a start delay adds to the delay to execution. Start Delay is not supported for the first API in the Batch and cumulative delay of all the APIs in the Batch should not exceed the task time out.. [optional]  # noqa: E501
            timeout (int): The duration in seconds by which the API response is expected from the API target. If the end point does not respond for the API request within this timeout duration, the task will be marked as failed.. [optional]  # noqa: E501
        """

        class_id = kwargs.get('class_id', "workflow.AnsiblePlaySession")
        object_type = kwargs.get('object_type', "workflow.AnsiblePlaySession")
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
              WorkflowAnsiblePlaySessionAllOf,
              WorkflowApi,
          ],
          'oneOf': [
          ],
        }
