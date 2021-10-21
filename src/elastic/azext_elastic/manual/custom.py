# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------
# pylint: disable=too-many-lines
# pylint: disable=unused-argument

from azure.cli.core.util import sdk_no_wait


def elastic_monitor_create(client,
                           resource_group_name,
                           monitor_name,
                           location,
                           tags=None,
                           provisioning_state=None,
                           monitoring_status=None,
                           elastic_properties=None,
                           user_info=None,
                           sku=None,
                           identity=None,
                           no_wait=False):
    body = {}
    if tags is not None:
        body['tags'] = tags
    body['location'] = location
    body['properties'] = {}
    if identity is not None:
        body['identity'] = {}
        body['identity']['type'] = identity
    if provisioning_state is not None:
        body['properties']['provisioning_state'] = provisioning_state
    if monitoring_status is not None:
        body['properties']['monitoring_status'] = monitoring_status
    if elastic_properties is not None:
        body['properties']['elastic_properties'] = elastic_properties
    if user_info is not None:
        body['properties']['user_info'] = user_info
    if len(body['properties']) == 0:
        del body['properties']
    body['sku'] = {}
    if sku is not None:
        body['sku']['name'] = sku
    if len(body['sku']) == 0:
        del body['sku']
    return sdk_no_wait(no_wait,
                       client.begin_create,
                       resource_group_name=resource_group_name,
                       monitor_name=monitor_name,
                       body=body)
