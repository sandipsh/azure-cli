# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from azure.cli.core.commands.client_factory import get_mgmt_service_client

VERSION_2019_06_01_PREVIEW = "2019-06-01-preview"


def get_acr_service_client(cli_ctx, api_version=None):
    """Returns the client for managing container registries. """
    from azure.mgmt.containerregistry import ContainerRegistryManagementClient
    return get_mgmt_service_client(cli_ctx, ContainerRegistryManagementClient, api_version=api_version)


def cf_acr_registries(cli_ctx, *_):
    return get_acr_service_client(cli_ctx).registries


def cf_acr_registries_tasks(cli_ctx, *_):
    return get_acr_service_client(cli_ctx, VERSION_2019_06_01_PREVIEW).registries


def cf_acr_replications(cli_ctx, *_):
    return get_acr_service_client(cli_ctx).replications


def cf_acr_webhooks(cli_ctx, *_):
    return get_acr_service_client(cli_ctx).webhooks


def cf_acr_tasks(cli_ctx, *_):
    return get_acr_service_client(cli_ctx, VERSION_2019_06_01_PREVIEW).tasks


def cf_acr_runs(cli_ctx, *_):
    return get_acr_service_client(cli_ctx, VERSION_2019_06_01_PREVIEW).runs
