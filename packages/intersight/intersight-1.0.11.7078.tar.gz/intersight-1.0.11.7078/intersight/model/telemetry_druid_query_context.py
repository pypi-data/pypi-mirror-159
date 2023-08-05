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



class TelemetryDruidQueryContext(ModelNormal):
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
    }

    validations = {
    }

    @cached_property
    def additional_properties_type():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded
        """
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
        return {
            'grand_total': (bool,),  # noqa: E501
            'skip_empty_buckets': (bool,),  # noqa: E501
            'timeout': (int,),  # noqa: E501
            'priority': (int,),  # noqa: E501
            'query_id': (str,),  # noqa: E501
            'use_cache': (bool,),  # noqa: E501
            'populate_cache': (bool,),  # noqa: E501
            'use_result_level_cache': (bool,),  # noqa: E501
            'populate_result_level_cache': (bool,),  # noqa: E501
            'by_segment': (bool,),  # noqa: E501
            'finalize': (bool,),  # noqa: E501
            'chunk_period': (str,),  # noqa: E501
            'max_scatter_gather_bytes': (int,),  # noqa: E501
            'max_queued_bytes': (int,),  # noqa: E501
            'serialize_date_time_as_long': (bool,),  # noqa: E501
            'serialize_date_time_as_long_inner': (bool,),  # noqa: E501
            'enable_parallel_merge': (bool,),  # noqa: E501
            'parallel_merge_parallelism': (int,),  # noqa: E501
            'parallel_merge_initial_yield_rows': (int,),  # noqa: E501
            'parallel_merge_small_batch_rows': (int,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'grand_total': 'grandTotal',  # noqa: E501
        'skip_empty_buckets': 'skipEmptyBuckets',  # noqa: E501
        'timeout': 'timeout',  # noqa: E501
        'priority': 'priority',  # noqa: E501
        'query_id': 'queryId',  # noqa: E501
        'use_cache': 'useCache',  # noqa: E501
        'populate_cache': 'populateCache',  # noqa: E501
        'use_result_level_cache': 'useResultLevelCache',  # noqa: E501
        'populate_result_level_cache': 'populateResultLevelCache',  # noqa: E501
        'by_segment': 'bySegment',  # noqa: E501
        'finalize': 'finalize',  # noqa: E501
        'chunk_period': 'chunkPeriod',  # noqa: E501
        'max_scatter_gather_bytes': 'maxScatterGatherBytes',  # noqa: E501
        'max_queued_bytes': 'maxQueuedBytes',  # noqa: E501
        'serialize_date_time_as_long': 'serializeDateTimeAsLong',  # noqa: E501
        'serialize_date_time_as_long_inner': 'serializeDateTimeAsLongInner',  # noqa: E501
        'enable_parallel_merge': 'enableParallelMerge',  # noqa: E501
        'parallel_merge_parallelism': 'parallelMergeParallelism',  # noqa: E501
        'parallel_merge_initial_yield_rows': 'parallelMergeInitialYieldRows',  # noqa: E501
        'parallel_merge_small_batch_rows': 'parallelMergeSmallBatchRows',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):  # noqa: E501
        """TelemetryDruidQueryContext - a model defined in OpenAPI

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
            grand_total (bool): Druid can include an extra \"grand totals\" row as the last row of a timeseries result set. To enable this, set \"grandTotal\" to true. The grand totals row will appear as the last row in the result array, and will have no timestamp. It will be the last row even if the query is run in \"descending\" mode. Post-aggregations in the grand totals row will be computed based upon the grand total aggregations.. [optional]  # noqa: E501
            skip_empty_buckets (bool): Timeseries queries normally fill empty interior time buckets with zeroes. Time buckets that lie completely outside the data interval are not zero-filled. You can disable all zero-filling with this flag. In this mode, the data point for empty buckets are omitted from the results.. [optional]  # noqa: E501
            timeout (int): Query timeout in milliseconds, beyond which unfinished queries will be cancelled. 0 timeout means no timeout.. [optional]  # noqa: E501
            priority (int): Query Priority. Queries with higher priority get precedence for computational resources.. [optional]  # noqa: E501
            query_id (str): Unique identifier given to this query. If a query ID is set or known, this can be used to cancel the query.. [optional]  # noqa: E501
            use_cache (bool): Flag indicating whether to leverage the query cache for this query. When set to false, it disables reading from the query cache for this query. When set to true, Apache Druid uses druid.broker.cache.useCache or druid.historical.cache.useCache to determine whether or not to read from the query cache.. [optional]  # noqa: E501
            populate_cache (bool): Flag indicating whether to save the results of the query to the query cache. Primarily used for debugging. When set to false, it disables saving the results of this query to the query cache. When set to true, Druid uses druid.broker.cache.populateCache or druid.historical.cache.populateCache to determine whether or not to save the results of this query to the query cache.. [optional]  # noqa: E501
            use_result_level_cache (bool): Flag indicating whether to leverage the result level cache for this query. When set to false, it disables reading from the query cache for this query. When set to true, Druid uses druid.broker.cache.useResultLevelCache to determine whether or not to read from the result-level query cache.. [optional]  # noqa: E501
            populate_result_level_cache (bool): Flag indicating whether to save the results of the query to the result level cache. Primarily used for debugging. When set to false, it disables saving the results of this query to the query cache. When set to true, Druid uses druid.broker.cache.populateResultLevelCache to determine whether or not to save the results of this query to the result-level query cache.. [optional]  # noqa: E501
            by_segment (bool): Return \"by segment\" results. Primarily used for debugging, setting it to true returns results associated with the data segment they came from.. [optional]  # noqa: E501
            finalize (bool): Flag indicating whether to \"finalize\" aggregation results. Primarily used for debugging. For instance, the hyperUnique aggregator will return the full HyperLogLog sketch instead of the estimated cardinality when this flag is set to false.. [optional]  # noqa: E501
            chunk_period (str): At the Broker process level, long interval queries (of any type) may be broken into shorter interval queries to parallelize merging more than normal. Broken up queries will use a larger share of cluster resources, but, if you use groupBy \"v1, it may be able to complete faster as a result. Use ISO 8601 periods. For example, if this property is set to P1M (one month), then a query covering a year would be broken into 12 smaller queries. The broker uses its query processing executor service to initiate processing for query chunks, so make sure druid.processing.numThreads is configured appropriately on the broker. groupBy queries do not support chunkPeriod by default, although they do if using the legacy \"v1\" engine. This context is deprecated since it's only useful for groupBy \"v1\", and will be removed in the future releases.. [optional]  # noqa: E501
            max_scatter_gather_bytes (int): Maximum number of bytes gathered from data processes such as Historicals and realtime processes to execute a query. This parameter can be used to further reduce maxScatterGatherBytes limit at query time.. [optional]  # noqa: E501
            max_queued_bytes (int): Maximum number of bytes queued per query before exerting backpressure on the channel to the data server. Similar to maxScatterGatherBytes, except unlike that configuration, this one will trigger backpressure rather than query failure. Zero means disabled.. [optional]  # noqa: E501
            serialize_date_time_as_long (bool): If true, DateTime is serialized as long in the result returned by Broker and the data transportation between Broker and compute process.. [optional]  # noqa: E501
            serialize_date_time_as_long_inner (bool): If true, DateTime is serialized as long in the data transportation between Broker and compute process.. [optional]  # noqa: E501
            enable_parallel_merge (bool): Enable parallel result merging on the Broker. Note that druid.processing.merge.useParallelMergePool must be enabled for this setting to be set to true.. [optional]  # noqa: E501
            parallel_merge_parallelism (int): Maximum number of parallel threads to use for parallel result merging on the Broker.. [optional]  # noqa: E501
            parallel_merge_initial_yield_rows (int): Number of rows to yield per ForkJoinPool merge task for parallel result merging on the Broker, before forking off a new task to continue merging sequences.. [optional]  # noqa: E501
            parallel_merge_small_batch_rows (int): Size of result batches to operate on in ForkJoinPool merge tasks for parallel result merging on the Broker.. [optional]  # noqa: E501
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
        """TelemetryDruidQueryContext - a model defined in OpenAPI

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
            grand_total (bool): Druid can include an extra \"grand totals\" row as the last row of a timeseries result set. To enable this, set \"grandTotal\" to true. The grand totals row will appear as the last row in the result array, and will have no timestamp. It will be the last row even if the query is run in \"descending\" mode. Post-aggregations in the grand totals row will be computed based upon the grand total aggregations.. [optional]  # noqa: E501
            skip_empty_buckets (bool): Timeseries queries normally fill empty interior time buckets with zeroes. Time buckets that lie completely outside the data interval are not zero-filled. You can disable all zero-filling with this flag. In this mode, the data point for empty buckets are omitted from the results.. [optional]  # noqa: E501
            timeout (int): Query timeout in milliseconds, beyond which unfinished queries will be cancelled. 0 timeout means no timeout.. [optional]  # noqa: E501
            priority (int): Query Priority. Queries with higher priority get precedence for computational resources.. [optional]  # noqa: E501
            query_id (str): Unique identifier given to this query. If a query ID is set or known, this can be used to cancel the query.. [optional]  # noqa: E501
            use_cache (bool): Flag indicating whether to leverage the query cache for this query. When set to false, it disables reading from the query cache for this query. When set to true, Apache Druid uses druid.broker.cache.useCache or druid.historical.cache.useCache to determine whether or not to read from the query cache.. [optional]  # noqa: E501
            populate_cache (bool): Flag indicating whether to save the results of the query to the query cache. Primarily used for debugging. When set to false, it disables saving the results of this query to the query cache. When set to true, Druid uses druid.broker.cache.populateCache or druid.historical.cache.populateCache to determine whether or not to save the results of this query to the query cache.. [optional]  # noqa: E501
            use_result_level_cache (bool): Flag indicating whether to leverage the result level cache for this query. When set to false, it disables reading from the query cache for this query. When set to true, Druid uses druid.broker.cache.useResultLevelCache to determine whether or not to read from the result-level query cache.. [optional]  # noqa: E501
            populate_result_level_cache (bool): Flag indicating whether to save the results of the query to the result level cache. Primarily used for debugging. When set to false, it disables saving the results of this query to the query cache. When set to true, Druid uses druid.broker.cache.populateResultLevelCache to determine whether or not to save the results of this query to the result-level query cache.. [optional]  # noqa: E501
            by_segment (bool): Return \"by segment\" results. Primarily used for debugging, setting it to true returns results associated with the data segment they came from.. [optional]  # noqa: E501
            finalize (bool): Flag indicating whether to \"finalize\" aggregation results. Primarily used for debugging. For instance, the hyperUnique aggregator will return the full HyperLogLog sketch instead of the estimated cardinality when this flag is set to false.. [optional]  # noqa: E501
            chunk_period (str): At the Broker process level, long interval queries (of any type) may be broken into shorter interval queries to parallelize merging more than normal. Broken up queries will use a larger share of cluster resources, but, if you use groupBy \"v1, it may be able to complete faster as a result. Use ISO 8601 periods. For example, if this property is set to P1M (one month), then a query covering a year would be broken into 12 smaller queries. The broker uses its query processing executor service to initiate processing for query chunks, so make sure druid.processing.numThreads is configured appropriately on the broker. groupBy queries do not support chunkPeriod by default, although they do if using the legacy \"v1\" engine. This context is deprecated since it's only useful for groupBy \"v1\", and will be removed in the future releases.. [optional]  # noqa: E501
            max_scatter_gather_bytes (int): Maximum number of bytes gathered from data processes such as Historicals and realtime processes to execute a query. This parameter can be used to further reduce maxScatterGatherBytes limit at query time.. [optional]  # noqa: E501
            max_queued_bytes (int): Maximum number of bytes queued per query before exerting backpressure on the channel to the data server. Similar to maxScatterGatherBytes, except unlike that configuration, this one will trigger backpressure rather than query failure. Zero means disabled.. [optional]  # noqa: E501
            serialize_date_time_as_long (bool): If true, DateTime is serialized as long in the result returned by Broker and the data transportation between Broker and compute process.. [optional]  # noqa: E501
            serialize_date_time_as_long_inner (bool): If true, DateTime is serialized as long in the data transportation between Broker and compute process.. [optional]  # noqa: E501
            enable_parallel_merge (bool): Enable parallel result merging on the Broker. Note that druid.processing.merge.useParallelMergePool must be enabled for this setting to be set to true.. [optional]  # noqa: E501
            parallel_merge_parallelism (int): Maximum number of parallel threads to use for parallel result merging on the Broker.. [optional]  # noqa: E501
            parallel_merge_initial_yield_rows (int): Number of rows to yield per ForkJoinPool merge task for parallel result merging on the Broker, before forking off a new task to continue merging sequences.. [optional]  # noqa: E501
            parallel_merge_small_batch_rows (int): Size of result batches to operate on in ForkJoinPool merge tasks for parallel result merging on the Broker.. [optional]  # noqa: E501
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
