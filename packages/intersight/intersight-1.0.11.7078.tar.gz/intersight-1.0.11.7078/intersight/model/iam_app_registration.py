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
    from intersight.model.iam_account_relationship import IamAccountRelationship
    from intersight.model.iam_app_registration_all_of import IamAppRegistrationAllOf
    from intersight.model.iam_o_auth_token_relationship import IamOAuthTokenRelationship
    from intersight.model.iam_permission_relationship import IamPermissionRelationship
    from intersight.model.iam_role_relationship import IamRoleRelationship
    from intersight.model.iam_user_relationship import IamUserRelationship
    from intersight.model.mo_base_mo import MoBaseMo
    from intersight.model.mo_base_mo_relationship import MoBaseMoRelationship
    from intersight.model.mo_tag import MoTag
    from intersight.model.mo_version_context import MoVersionContext
    globals()['DisplayNames'] = DisplayNames
    globals()['IamAccountRelationship'] = IamAccountRelationship
    globals()['IamAppRegistrationAllOf'] = IamAppRegistrationAllOf
    globals()['IamOAuthTokenRelationship'] = IamOAuthTokenRelationship
    globals()['IamPermissionRelationship'] = IamPermissionRelationship
    globals()['IamRoleRelationship'] = IamRoleRelationship
    globals()['IamUserRelationship'] = IamUserRelationship
    globals()['MoBaseMo'] = MoBaseMo
    globals()['MoBaseMoRelationship'] = MoBaseMoRelationship
    globals()['MoTag'] = MoTag
    globals()['MoVersionContext'] = MoVersionContext


class IamAppRegistration(ModelComposed):
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
            'IAM.APPREGISTRATION': "iam.AppRegistration",
        },
        ('object_type',): {
            'IAM.APPREGISTRATION': "iam.AppRegistration",
        },
        ('client_type',): {
            'PUBLIC': "public",
            'CONFIDENTIAL': "confidential",
        },
        ('grant_types',): {
            'None': None,
            'AUTHORIZATION_CODE': "authorization_code",
            'REFRESH_TOKEN': "refresh_token",
            'CLIENT_CREDENTIALS': "client_credentials",
            'IMPLICIT': "implicit",
            'PASSWORD': "password",
            'URN:IETF:PARAMS:OAUTH:GRANT-TYPE:JWT-BEARER': "urn:ietf:params:oauth:grant-type:jwt-bearer",
            'URN:IETF:PARAMS:OAUTH:GRANT-TYPE:SAML2-BEARER': "urn:ietf:params:oauth:grant-type:saml2-bearer",
        },
        ('response_types',): {
            'None': None,
            'CODE': "code",
            'TOKEN': "token",
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
            'client_id': (str,),  # noqa: E501
            'client_name': (str,),  # noqa: E501
            'client_secret': (str,),  # noqa: E501
            'client_type': (str,),  # noqa: E501
            'description': (str,),  # noqa: E501
            'grant_types': ([str], none_type,),  # noqa: E501
            'redirect_uris': ([str], none_type,),  # noqa: E501
            'renew_client_secret': (bool,),  # noqa: E501
            'response_types': ([str], none_type,),  # noqa: E501
            'revocation_timestamp': (datetime,),  # noqa: E501
            'revoke': (bool,),  # noqa: E501
            'show_consent_screen': (bool,),  # noqa: E501
            'account': (IamAccountRelationship,),  # noqa: E501
            'oauth_tokens': ([IamOAuthTokenRelationship], none_type,),  # noqa: E501
            'permission': (IamPermissionRelationship,),  # noqa: E501
            'roles': ([IamRoleRelationship], none_type,),  # noqa: E501
            'user': (IamUserRelationship,),  # noqa: E501
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
        val = {
        }
        if not val:
            return None
        return {'class_id': val}

    attribute_map = {
        'class_id': 'ClassId',  # noqa: E501
        'object_type': 'ObjectType',  # noqa: E501
        'client_id': 'ClientId',  # noqa: E501
        'client_name': 'ClientName',  # noqa: E501
        'client_secret': 'ClientSecret',  # noqa: E501
        'client_type': 'ClientType',  # noqa: E501
        'description': 'Description',  # noqa: E501
        'grant_types': 'GrantTypes',  # noqa: E501
        'redirect_uris': 'RedirectUris',  # noqa: E501
        'renew_client_secret': 'RenewClientSecret',  # noqa: E501
        'response_types': 'ResponseTypes',  # noqa: E501
        'revocation_timestamp': 'RevocationTimestamp',  # noqa: E501
        'revoke': 'Revoke',  # noqa: E501
        'show_consent_screen': 'ShowConsentScreen',  # noqa: E501
        'account': 'Account',  # noqa: E501
        'oauth_tokens': 'OauthTokens',  # noqa: E501
        'permission': 'Permission',  # noqa: E501
        'roles': 'Roles',  # noqa: E501
        'user': 'User',  # noqa: E501
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
        'client_id',  # noqa: E501
        'revocation_timestamp',  # noqa: E501
        'oauth_tokens',  # noqa: E501
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
        """IamAppRegistration - a model defined in OpenAPI

        Keyword Args:
            class_id (str): The fully-qualified name of the instantiated, concrete type. This property is used as a discriminator to identify the type of the payload when marshaling and unmarshaling data.. defaults to "iam.AppRegistration", must be one of ["iam.AppRegistration", ]  # noqa: E501
            object_type (str): The fully-qualified name of the instantiated, concrete type. The value should be the same as the 'ClassId' property.. defaults to "iam.AppRegistration", must be one of ["iam.AppRegistration", ]  # noqa: E501
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
            client_id (str): A unique identifier for the OAuth2 client application. The client ID is auto-generated when the AppRegistration object is created.. [optional]  # noqa: E501
            client_name (str): App Registration name specified by user.. [optional]  # noqa: E501
            client_secret (str): The OAuth2 client secret. The value of this property is generated when grantType includes 'client-credentials'. Otherwise, no client-secret is generated.. [optional]  # noqa: E501
            client_type (str): The type of the OAuth2 client (public or confidential), as specified in https://tools.ietf.org/html/rfc6749#section-2.1. * `public` - Clients incapable of maintaining the confidentiality of their credentials.This includes clients executing on the device used by the resource owner,such as mobile applications, installed native application or a webbrowser-based application. * `confidential` - Clients capable of maintaining the confidentiality of their credentials.For example, this could be a client implemented on a secure server withrestricted access to the client credentials.To maintain the confidentiality of the OAuth2 credentials, two use cases areconsidered.1) The application is running as a service within Intersight. The application automatically   obtains the OAuth2 credentials when the application starts and the credentials are not   exposed to the end-user.   Because end-users (even account administrators) do not have access the OAuth2 credentials,   they cannot take the credentials with them when they leave their organization.2) The application is under the control of a \"trusted\" end-user. For example,   the end-user may create a native application running outside Intersight. The application   uses OAuth2 credentials to interact with the Intersight API. In that case, the Intersight   account administrator may generate OAuth2 credentials with a registered application   using \"client_credentials\" grant type.   In that case, the end-user is responsible for maintaining the confidentiality of the   OAuth2 credentials. If the end-user leaves the organization, you should revoke the   credentials and issue new Oauth2 credentials.Here is a possible workflow for handling OAuth2 tokens.1) User Alice (Intersight Account Administrator) logins to Intersight and deploys an Intersight   application that requires an OAuth2 token.2) Intersight automatically deploys the application. The application is assigned a OAuth2 token,   possibly linked to Alice. The application must NOT expose the OAuth2 secret to Alice, otherwise   Alice would be able to use the token after she leaves the company.3) The application can make API calls to Intersight using its assigned OAuth2 token. For example,   the application could make weekly scheduled API calls to Intersight.4) Separately, Alice may also get OAuth2 tokens that she can use to make API calls from the   Intersight SDK through the northbound API. In that case, Alice will get the associated OAuth2   secrets, but not the one assigned in step #2.5) Alice leaves the organization. The OAuth2 tokens assigned in step #2 must retain their validity   even after Alice has left the organization. Because the OAuth2 secrets were never shared with   Alice, there is no risk Alice can reuse the OAuth2 secrets.   On the other hand, the OAuth2 tokens assigned in step #4 must be invalidated because Alice had   the OAuth2 tokens in her possession.. [optional] if omitted the server will use the default value of "public"  # noqa: E501
            description (str): Description of the application.. [optional]  # noqa: E501
            grant_types ([str], none_type): [optional]  # noqa: E501
            redirect_uris ([str], none_type): [optional]  # noqa: E501
            renew_client_secret (bool): Set value to true to renew the client-secret. Applicable to client_credentials grant type.. [optional] if omitted the server will use the default value of False  # noqa: E501
            response_types ([str], none_type): [optional]  # noqa: E501
            revocation_timestamp (datetime): Used to perform revocation for tokens of AppRegistration. Updated only internally is case Revoke property come from UI with value true. On each request with OAuth2 access token the CreationTime of the OAuth2 token will be compared to RevokationTimestamp of the corresponding App Registration.. [optional]  # noqa: E501
            revoke (bool): Used to trigger update the revocationTimestamp value. If UI sent updating request with the Revoke value is true, then update RevocationTimestamp.. [optional] if omitted the server will use the default value of False  # noqa: E501
            show_consent_screen (bool): Set to true if consent screen needs to be shown during the OAuth login process. Applicable only for public AppRegistrations, means only 'authorization_code' grantType. Note that consent screen will be shown on each login.. [optional] if omitted the server will use the default value of False  # noqa: E501
            account (IamAccountRelationship): [optional]  # noqa: E501
            oauth_tokens ([IamOAuthTokenRelationship], none_type): An array of relationships to iamOAuthToken resources.. [optional]  # noqa: E501
            permission (IamPermissionRelationship): [optional]  # noqa: E501
            roles ([IamRoleRelationship], none_type): An array of relationships to iamRole resources.. [optional]  # noqa: E501
            user (IamUserRelationship): [optional]  # noqa: E501
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

        class_id = kwargs.get('class_id', "iam.AppRegistration")
        object_type = kwargs.get('object_type', "iam.AppRegistration")
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
        """IamAppRegistration - a model defined in OpenAPI

        Keyword Args:
            class_id (str): The fully-qualified name of the instantiated, concrete type. This property is used as a discriminator to identify the type of the payload when marshaling and unmarshaling data.. defaults to "iam.AppRegistration", must be one of ["iam.AppRegistration", ]  # noqa: E501
            object_type (str): The fully-qualified name of the instantiated, concrete type. The value should be the same as the 'ClassId' property.. defaults to "iam.AppRegistration", must be one of ["iam.AppRegistration", ]  # noqa: E501
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
            client_id (str): A unique identifier for the OAuth2 client application. The client ID is auto-generated when the AppRegistration object is created.. [optional]  # noqa: E501
            client_name (str): App Registration name specified by user.. [optional]  # noqa: E501
            client_secret (str): The OAuth2 client secret. The value of this property is generated when grantType includes 'client-credentials'. Otherwise, no client-secret is generated.. [optional]  # noqa: E501
            client_type (str): The type of the OAuth2 client (public or confidential), as specified in https://tools.ietf.org/html/rfc6749#section-2.1. * `public` - Clients incapable of maintaining the confidentiality of their credentials.This includes clients executing on the device used by the resource owner,such as mobile applications, installed native application or a webbrowser-based application. * `confidential` - Clients capable of maintaining the confidentiality of their credentials.For example, this could be a client implemented on a secure server withrestricted access to the client credentials.To maintain the confidentiality of the OAuth2 credentials, two use cases areconsidered.1) The application is running as a service within Intersight. The application automatically   obtains the OAuth2 credentials when the application starts and the credentials are not   exposed to the end-user.   Because end-users (even account administrators) do not have access the OAuth2 credentials,   they cannot take the credentials with them when they leave their organization.2) The application is under the control of a \"trusted\" end-user. For example,   the end-user may create a native application running outside Intersight. The application   uses OAuth2 credentials to interact with the Intersight API. In that case, the Intersight   account administrator may generate OAuth2 credentials with a registered application   using \"client_credentials\" grant type.   In that case, the end-user is responsible for maintaining the confidentiality of the   OAuth2 credentials. If the end-user leaves the organization, you should revoke the   credentials and issue new Oauth2 credentials.Here is a possible workflow for handling OAuth2 tokens.1) User Alice (Intersight Account Administrator) logins to Intersight and deploys an Intersight   application that requires an OAuth2 token.2) Intersight automatically deploys the application. The application is assigned a OAuth2 token,   possibly linked to Alice. The application must NOT expose the OAuth2 secret to Alice, otherwise   Alice would be able to use the token after she leaves the company.3) The application can make API calls to Intersight using its assigned OAuth2 token. For example,   the application could make weekly scheduled API calls to Intersight.4) Separately, Alice may also get OAuth2 tokens that she can use to make API calls from the   Intersight SDK through the northbound API. In that case, Alice will get the associated OAuth2   secrets, but not the one assigned in step #2.5) Alice leaves the organization. The OAuth2 tokens assigned in step #2 must retain their validity   even after Alice has left the organization. Because the OAuth2 secrets were never shared with   Alice, there is no risk Alice can reuse the OAuth2 secrets.   On the other hand, the OAuth2 tokens assigned in step #4 must be invalidated because Alice had   the OAuth2 tokens in her possession.. [optional] if omitted the server will use the default value of "public"  # noqa: E501
            description (str): Description of the application.. [optional]  # noqa: E501
            grant_types ([str], none_type): [optional]  # noqa: E501
            redirect_uris ([str], none_type): [optional]  # noqa: E501
            renew_client_secret (bool): Set value to true to renew the client-secret. Applicable to client_credentials grant type.. [optional] if omitted the server will use the default value of False  # noqa: E501
            response_types ([str], none_type): [optional]  # noqa: E501
            revocation_timestamp (datetime): Used to perform revocation for tokens of AppRegistration. Updated only internally is case Revoke property come from UI with value true. On each request with OAuth2 access token the CreationTime of the OAuth2 token will be compared to RevokationTimestamp of the corresponding App Registration.. [optional]  # noqa: E501
            revoke (bool): Used to trigger update the revocationTimestamp value. If UI sent updating request with the Revoke value is true, then update RevocationTimestamp.. [optional] if omitted the server will use the default value of False  # noqa: E501
            show_consent_screen (bool): Set to true if consent screen needs to be shown during the OAuth login process. Applicable only for public AppRegistrations, means only 'authorization_code' grantType. Note that consent screen will be shown on each login.. [optional] if omitted the server will use the default value of False  # noqa: E501
            account (IamAccountRelationship): [optional]  # noqa: E501
            oauth_tokens ([IamOAuthTokenRelationship], none_type): An array of relationships to iamOAuthToken resources.. [optional]  # noqa: E501
            permission (IamPermissionRelationship): [optional]  # noqa: E501
            roles ([IamRoleRelationship], none_type): An array of relationships to iamRole resources.. [optional]  # noqa: E501
            user (IamUserRelationship): [optional]  # noqa: E501
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

        class_id = kwargs.get('class_id', "iam.AppRegistration")
        object_type = kwargs.get('object_type', "iam.AppRegistration")
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
              IamAppRegistrationAllOf,
              MoBaseMo,
          ],
          'oneOf': [
          ],
        }
