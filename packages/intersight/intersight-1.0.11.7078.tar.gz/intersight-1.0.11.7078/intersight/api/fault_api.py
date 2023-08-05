"""
    Cisco Intersight

    Cisco Intersight is a management platform delivered as a service with embedded analytics for your Cisco and 3rd party IT infrastructure. This platform offers an intelligent level of management that enables IT organizations to analyze, simplify, and automate their environments in more advanced ways than the prior generations of tools. Cisco Intersight provides an integrated and intuitive management experience for resources in the traditional data center as well as at the edge. With flexible deployment options to address complex security needs, getting started with Intersight is quick and easy. Cisco Intersight has deep integration with Cisco UCS and HyperFlex systems allowing for remote deployment, configuration, and ongoing maintenance. The model-based deployment works for a single system in a remote location or hundreds of systems in a data center and enables rapid, standardized configuration and deployment. It also streamlines maintaining those systems whether you are working with small or very large configurations. The Intersight OpenAPI document defines the complete set of properties that are returned in the HTTP response. From that perspective, a client can expect that no additional properties are returned, unless these properties are explicitly defined in the OpenAPI document. However, when a client uses an older version of the Intersight OpenAPI document, the server may send additional properties because the software is more recent than the client. In that case, the client may receive properties that it does not know about. Some generated SDKs perform a strict validation of the HTTP response body against the OpenAPI document.  # noqa: E501

    The version of the OpenAPI document: 1.0.11-7078
    Contact: intersight@cisco.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from intersight.api_client import ApiClient, Endpoint as _Endpoint
from intersight.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from intersight.model.error import Error
from intersight.model.fault_instance import FaultInstance
from intersight.model.fault_instance_response import FaultInstanceResponse
from intersight.model.patch_document import PatchDocument


class FaultApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.get_fault_instance_by_moid_endpoint = _Endpoint(
            settings={
                'response_type': (FaultInstance,),
                'auth': [
                    'cookieAuth',
                    'http_signature',
                    'oAuth2',
                    'oAuth2'
                ],
                'endpoint_path': '/api/v1/fault/Instances/{Moid}',
                'operation_id': 'get_fault_instance_by_moid',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'moid',
                ],
                'required': [
                    'moid',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'moid':
                        (str,),
                },
                'attribute_map': {
                    'moid': 'Moid',
                },
                'location_map': {
                    'moid': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json',
                    'text/csv',
                    'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.get_fault_instance_list_endpoint = _Endpoint(
            settings={
                'response_type': (FaultInstanceResponse,),
                'auth': [
                    'cookieAuth',
                    'http_signature',
                    'oAuth2',
                    'oAuth2'
                ],
                'endpoint_path': '/api/v1/fault/Instances',
                'operation_id': 'get_fault_instance_list',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'filter',
                    'orderby',
                    'top',
                    'skip',
                    'select',
                    'expand',
                    'apply',
                    'count',
                    'inlinecount',
                    'at',
                    'tags',
                ],
                'required': [],
                'nullable': [
                ],
                'enum': [
                    'inlinecount',
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                    ('inlinecount',): {

                        "ALLPAGES": "allpages",
                        "NONE": "none"
                    },
                },
                'openapi_types': {
                    'filter':
                        (str,),
                    'orderby':
                        (str,),
                    'top':
                        (int,),
                    'skip':
                        (int,),
                    'select':
                        (str,),
                    'expand':
                        (str,),
                    'apply':
                        (str,),
                    'count':
                        (bool,),
                    'inlinecount':
                        (str,),
                    'at':
                        (str,),
                    'tags':
                        (str,),
                },
                'attribute_map': {
                    'filter': '$filter',
                    'orderby': '$orderby',
                    'top': '$top',
                    'skip': '$skip',
                    'select': '$select',
                    'expand': '$expand',
                    'apply': '$apply',
                    'count': '$count',
                    'inlinecount': '$inlinecount',
                    'at': 'at',
                    'tags': 'tags',
                },
                'location_map': {
                    'filter': 'query',
                    'orderby': 'query',
                    'top': 'query',
                    'skip': 'query',
                    'select': 'query',
                    'expand': 'query',
                    'apply': 'query',
                    'count': 'query',
                    'inlinecount': 'query',
                    'at': 'query',
                    'tags': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json',
                    'text/csv',
                    'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.patch_fault_instance_endpoint = _Endpoint(
            settings={
                'response_type': (FaultInstance,),
                'auth': [
                    'cookieAuth',
                    'http_signature',
                    'oAuth2',
                    'oAuth2'
                ],
                'endpoint_path': '/api/v1/fault/Instances/{Moid}',
                'operation_id': 'patch_fault_instance',
                'http_method': 'PATCH',
                'servers': None,
            },
            params_map={
                'all': [
                    'moid',
                    'fault_instance',
                    'if_match',
                ],
                'required': [
                    'moid',
                    'fault_instance',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'moid':
                        (str,),
                    'fault_instance':
                        (FaultInstance,),
                    'if_match':
                        (str,),
                },
                'attribute_map': {
                    'moid': 'Moid',
                    'if_match': 'If-Match',
                },
                'location_map': {
                    'moid': 'path',
                    'fault_instance': 'body',
                    'if_match': 'header',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json',
                    'application/json-patch+json'
                ]
            },
            api_client=api_client
        )
        self.update_fault_instance_endpoint = _Endpoint(
            settings={
                'response_type': (FaultInstance,),
                'auth': [
                    'cookieAuth',
                    'http_signature',
                    'oAuth2',
                    'oAuth2'
                ],
                'endpoint_path': '/api/v1/fault/Instances/{Moid}',
                'operation_id': 'update_fault_instance',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'moid',
                    'fault_instance',
                    'if_match',
                ],
                'required': [
                    'moid',
                    'fault_instance',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'moid':
                        (str,),
                    'fault_instance':
                        (FaultInstance,),
                    'if_match':
                        (str,),
                },
                'attribute_map': {
                    'moid': 'Moid',
                    'if_match': 'If-Match',
                },
                'location_map': {
                    'moid': 'path',
                    'fault_instance': 'body',
                    'if_match': 'header',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json',
                    'application/json-patch+json'
                ]
            },
            api_client=api_client
        )

    def get_fault_instance_by_moid(
        self,
        moid,
        **kwargs
    ):
        """Read a 'fault.Instance' resource.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_fault_instance_by_moid(moid, async_req=True)
        >>> result = thread.get()

        Args:
            moid (str): The unique Moid identifier of a resource instance.

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            FaultInstance
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['moid'] = \
            moid
        return self.get_fault_instance_by_moid_endpoint.call_with_http_info(**kwargs)

    def get_fault_instance_list(
        self,
        **kwargs
    ):
        """Read a 'fault.Instance' resource.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_fault_instance_list(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            filter (str): Filter criteria for the resources to return. A URI with a $filter query option identifies a subset of the entries from the Collection of Entries. The subset is determined by selecting only the Entries that satisfy the predicate expression specified by the $filter option. The expression language that is used in $filter queries supports references to properties and literals. The literal values can be strings enclosed in single quotes, numbers and boolean values (true or false).. [optional] if omitted the server will use the default value of ""
            orderby (str): Determines what properties are used to sort the collection of resources.. [optional]
            top (int): Specifies the maximum number of resources to return in the response.. [optional] if omitted the server will use the default value of 100
            skip (int): Specifies the number of resources to skip in the response.. [optional] if omitted the server will use the default value of 0
            select (str): Specifies a subset of properties to return.. [optional] if omitted the server will use the default value of ""
            expand (str): Specify additional attributes or related resources to return in addition to the primary resources.. [optional]
            apply (str): Specify one or more transformation operations to perform aggregation on the resources. The transformations are processed in order with the output from a transformation being used as input for the subsequent transformation. The \"$apply\" query takes a sequence of set transformations, separated by forward slashes to express that they are consecutively applied, i.e. the result of each transformation is the input to the next transformation. Supported aggregation methods are \"aggregate\" and \"groupby\". The **aggregate** transformation takes a comma-separated list of one or more aggregate expressions as parameters and returns a result set with a single instance, representing the aggregated value for all instances in the input set. The **groupby** transformation takes one or two parameters and 1. Splits the initial set into subsets where all instances in a subset have the same values for the grouping properties specified in the first parameter, 2. Applies set transformations to each subset according to the second parameter, resulting in a new set of potentially different structure and cardinality, 3. Ensures that the instances in the result set contain all grouping properties with the correct values for the group, 4. Concatenates the intermediate result sets into one result set. A groupby transformation affects the structure of the result set.. [optional]
            count (bool): The $count query specifies the service should return the count of the matching resources, instead of returning the resources.. [optional]
            inlinecount (str): The $inlinecount query option allows clients to request an inline count of the matching resources included with the resources in the response.. [optional] if omitted the server will use the default value of "allpages"
            at (str): Similar to \"$filter\", but \"at\" is specifically used to filter versioning information properties for resources to return. A URI with an \"at\" Query Option identifies a subset of the Entries from the Collection of Entries identified by the Resource Path section of the URI. The subset is determined by selecting only the Entries that satisfy the predicate expression specified by the query option. The expression language that is used in at operators supports references to properties and literals. The literal values can be strings enclosed in single quotes, numbers and boolean values (true or false) or any of the additional literal representations shown in the Abstract Type System section.. [optional]
            tags (str): The 'tags' parameter is used to request a summary of the Tag utilization for this resource. When the 'tags' parameter is specified, the response provides a list of tag keys, the number of times the key has been used across all documents, and the tag values that have been assigned to the tag key.. [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            FaultInstanceResponse
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        return self.get_fault_instance_list_endpoint.call_with_http_info(**kwargs)

    def patch_fault_instance(
        self,
        moid,
        fault_instance,
        **kwargs
    ):
        """Update a 'fault.Instance' resource.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.patch_fault_instance(moid, fault_instance, async_req=True)
        >>> result = thread.get()

        Args:
            moid (str): The unique Moid identifier of a resource instance.
            fault_instance (FaultInstance): The 'fault.Instance' resource to update.

        Keyword Args:
            if_match (str): For methods that apply server-side changes, and in particular for PUT, If-Match can be used to prevent the lost update problem. It can check if the modification of a resource that the user wants to upload will not override another change that has been done since the original resource was fetched. If the request cannot be fulfilled, the 412 (Precondition Failed) response is returned. When modifying a resource using POST or PUT, the If-Match header must be set to the value of the resource ModTime property after which no lost update problem should occur. For example, a client send a GET request to obtain a resource, which includes the ModTime property. The ModTime indicates the last time the resource was created or modified. The client then sends a POST or PUT request with the If-Match header set to the ModTime property of the resource as obtained in the GET request.. [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            FaultInstance
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['moid'] = \
            moid
        kwargs['fault_instance'] = \
            fault_instance
        return self.patch_fault_instance_endpoint.call_with_http_info(**kwargs)

    def update_fault_instance(
        self,
        moid,
        fault_instance,
        **kwargs
    ):
        """Update a 'fault.Instance' resource.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.update_fault_instance(moid, fault_instance, async_req=True)
        >>> result = thread.get()

        Args:
            moid (str): The unique Moid identifier of a resource instance.
            fault_instance (FaultInstance): The 'fault.Instance' resource to update.

        Keyword Args:
            if_match (str): For methods that apply server-side changes, and in particular for PUT, If-Match can be used to prevent the lost update problem. It can check if the modification of a resource that the user wants to upload will not override another change that has been done since the original resource was fetched. If the request cannot be fulfilled, the 412 (Precondition Failed) response is returned. When modifying a resource using POST or PUT, the If-Match header must be set to the value of the resource ModTime property after which no lost update problem should occur. For example, a client send a GET request to obtain a resource, which includes the ModTime property. The ModTime indicates the last time the resource was created or modified. The client then sends a POST or PUT request with the If-Match header set to the ModTime property of the resource as obtained in the GET request.. [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            FaultInstance
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['moid'] = \
            moid
        kwargs['fault_instance'] = \
            fault_instance
        return self.update_fault_instance_endpoint.call_with_http_info(**kwargs)

