# coding=utf-8
# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.help_files import helps  # pylint: disable=unused-import

helps['webapp auth'] = """
type: group
short-summary: Manage webapp authentication and authorization in the v2 format.
"""

helps['webapp auth show'] = """
type: command
short-summary: Show the authentication settings for the webapp in the v2 format.
examples:
  - name: Show the authentication settings for the webapp. (autogenerated)
    text: az webapp auth show --name MyWebApp --resource-group MyResourceGroup
    crafted: true
"""

helps['webapp auth update'] = """
type: command
short-summary: Update the authentication settings for the webapp in the v2 format.
examples:
  - name: Update the client ID of the AAD provider already configured
    text: >
        az webapp auth update -g myResourceGroup --name MyWebApp --set identityProviders.azureActiveDirectory.registration.clientId=my-client-id
  - name: Pin the runtime version of the app to 1.4.7
    text: >
        az webapp auth update -g myResourceGroup --name MyWebApp --runtime-version 1.4.7
  - name: Configure the app with file based authentication by setting the config file path
    text: >
        az webapp auth update -g myResourceGroup --name MyWebApp --config-file-path D:\\home\\site\\wwwroot\\auth.json
  - name: Configure the app to allow unauthenticated requests to hit the app.
    text: >
        az webapp auth update -g myResourceGroup --name MyWebApp --unauthenticated-client-action AllowAnonymous
  - name: Configure the app to redirect unauthenticated requests to the Facebook provider
    text: >
        az webapp auth update -g myResourceGroup --name MyWebApp --redirect-provider Facebook
  - name: Configure the app to listen to the forward headers X-FORWARDED-HOST and X-FORWARDED-PROTO
    text: >
        az webapp auth update -g myResourceGroup --name MyWebApp --proxy-convention Standard
"""

helps['webapp auth set'] = """
type: command
short-summary: Sets the authentication settings for the webapp in the v2 format, overwriting any existing settings.
examples:
  - name: Set the json saved in file auth.json as the auth settings for the web app, overwriting any existing settings.
    text: >
        az webapp auth set -g myResourceGroup --name MyWebApp --body @auth.json
"""

helps['webapp auth config-version'] = """
type: group
short-summary: Manage the state of the configuration version for the authentication settings for the webapp. Configuration version v1 refers to the /authSettings endpoints whereas v2 refers to the /authSettingsV2 endpoints.
"""

helps['webapp auth config-version show'] = """
type: command
short-summary: Show the configuration version of the authentication settings for the webapp. Configuration version v1 refers to the /authSettings endpoints whereas v2 refers to the /authSettingsV2 endpoints.
examples:
  - name: Show the configuration version of the authentication settings for the webapp (autogenerated)
    text: >
        az webapp auth config-version show --name MyWebApp --resource-group MyResourceGroup
"""

helps['webapp auth config-version revert'] = """
type: command
short-summary: Reverts the configuration version of the authentication settings for the webapp from v2 to v1 (classic).
examples:
  - name: Revert the configuration version of the authentication settings for the webapp from v2 to v1 (classic) (autogenerated)
    text: >
        az webapp auth config-version revert --name MyWebApp --resource-group MyResourceGroup
"""

helps['webapp auth config-version upgrade'] = """
type: command
short-summary: Upgrades the configuration version of the authentication settings for the webapp from v1 (classic) to v2.
examples:
  - name: Upgrades the configuration version of the authentication settings for the webapp from v1 (classic) to v2 (autogenerated)
    text: >
        az webapp auth config-version upgrade --name MyWebApp --resource-group MyResourceGroup
"""

helps['webapp auth-classic'] = """
type: group
short-summary: Manage webapp authentication and authorization in the classic format.
"""

helps['webapp auth-classic show'] = """
type: command
short-summary: Show the authentication settings for the webapp in the classic format.
examples:
  - name: Show the authentication settings for the webapp. (autogenerated)
    text: az webapp auth-classic show --name MyWebApp --resource-group MyResourceGroup
    crafted: true
"""

helps['webapp auth-classic update'] = """
type: command
short-summary: Update the authentication settings for the webapp in the classic format.
examples:
  - name: Enable Azure Active Directory by enabling authentication and setting Azure Active Directory-associated parameters. Default provider is set to AAD. Must have created a AAD service principal beforehand.
    text: >
        az webapp auth-classic update  -g myResourceGroup --name MyWebApp --enabled true \\
          --action LoginWithAzureActiveDirectory \\
          --aad-allowed-token-audiences https://webapp_name.azurewebsites.net/.auth/login/aad/callback \\
          --aad-client-id my-client-id --aad-client-secret very_secret_password \\
          --aad-token-issuer-url https://sts.windows.net/54826b22-38d6-4fb2-bad9-b7983a3e9c5a/
  - name: Enable Facebook authentication by setting FB-associated parameters and turning on public-profile and email scopes; allow anonymous users
    text: >
        az webapp auth-classic update -g myResourceGroup --name MyWebApp --action AllowAnonymous \\
          --facebook-app-id my_fb_id --facebook-app-secret my_fb_secret \\
          --facebook-oauth-scopes public_profile email
"""

helps['webapp auth apple'] = """
type: group
short-summary: Manage webapp authentication and authorization of the Apple identity provider.
"""

helps['webapp auth apple show'] = """
type: command
short-summary: Show the authentication settings for the Apple identity provider.
examples:
  - name: Show the authentication settings for the Apple identity provider. (autogenerated)
    text: az webapp auth apple show --name MyWebApp --resource-group MyResourceGroup
    crafted: true
"""

helps['webapp auth apple update'] = """
type: command
short-summary: Update the client id and client secret for the Apple identity provider.
examples:
  - name: Update the client id and client secret for the Apple identity provider.
    text: >
        az webapp auth apple update  -g myResourceGroup --name MyWebApp \\
          --client-id my-client-id --client-secret very_secret_password
"""

helps['webapp auth facebook'] = """
type: group
short-summary: Manage webapp authentication and authorization of the Facebook identity provider.
"""

helps['webapp auth facebook show'] = """
type: command
short-summary: Show the authentication settings for the Facebook identity provider.
examples:
  - name: Show the authentication settings for the Facebook identity provider. (autogenerated)
    text: az webapp auth facebook show --name MyWebApp --resource-group MyResourceGroup
    crafted: true
"""

helps['webapp auth facebook update'] = """
type: command
short-summary: Update the app id and app secret for the Facebook identity provider.
examples:
  - name: Update the app id and app secret for the Facebook identity provider.
    text: >
        az webapp auth facebook update  -g myResourceGroup --name MyWebApp \\
          --app-id my-client-id --app-secret very_secret_password
"""

helps['webapp auth github'] = """
type: group
short-summary: Manage webapp authentication and authorization of the GitHub identity provider.
"""

helps['webapp auth github show'] = """
type: command
short-summary: Show the authentication settings for the GitHub identity provider.
examples:
  - name: Show the authentication settings for the GitHub identity provider. (autogenerated)
    text: az webapp auth github show --name MyWebApp --resource-group MyResourceGroup
    crafted: true
"""

helps['webapp auth github update'] = """
type: command
short-summary: Update the client id and client secret for the GitHub identity provider.
examples:
  - name: Update the client id and client secret for the GitHub identity provider.
    text: >
        az webapp auth github update  -g myResourceGroup --name MyWebApp \\
          --client-id my-client-id --client-secret very_secret_password
"""

helps['webapp auth google'] = """
type: group
short-summary: Manage webapp authentication and authorization of the Google identity provider.
"""

helps['webapp auth google show'] = """
type: command
short-summary: Show the authentication settings for the Google identity provider.
examples:
  - name: Show the authentication settings for the Google identity provider. (autogenerated)
    text: az webapp auth google show --name MyWebApp --resource-group MyResourceGroup
    crafted: true
"""

helps['webapp auth google update'] = """
type: command
short-summary: Update the client id and client secret for the Google identity provider.
examples:
  - name: Update the client id and client secret for the Google identity provider.
    text: >
        az webapp auth google update  -g myResourceGroup --name MyWebApp \\
          --client-id my-client-id --client-secret very_secret_password
"""

helps['webapp auth microsoft'] = """
type: group
short-summary: Manage webapp authentication and authorization of the Microsoft identity provider.
"""

helps['webapp auth microsoft show'] = """
type: command
short-summary: Show the authentication settings for the Azure Active Directory identity provider.
examples:
  - name: Show the authentication settings for the Azure Active Directory identity provider. (autogenerated)
    text: az webapp auth microsoft show --name MyWebApp --resource-group MyResourceGroup
    crafted: true
"""

helps['webapp auth microsoft update'] = """
type: command
short-summary: Update the client id and client secret for the Azure Active Directory identity provider.
examples:
  - name: Update the open id issuer, client id and client secret for the Azure Active Directory identity provider.
    text: >
        az webapp auth microsoft update  -g myResourceGroup --name MyWebApp \\
          --client-id my-client-id --client-secret very_secret_password \\
          --issuer https://sts.windows.net/54826b22-38d6-4fb2-bad9-b7983a3e9c5a/
"""

helps['webapp auth openid-connect'] = """
type: group
short-summary: Manage webapp authentication and authorization of the custom OpenID Connect identity providers.
"""

helps['webapp auth openid-connect show'] = """
type: command
short-summary: Show the authentication settings for the custom OpenID Connect identity provider.
examples:
  - name: Show the authentication settings for the custom OpenID Connect identity provider. (autogenerated)
    text: az webapp auth openid-connect show --name MyWebApp --resource-group MyResourceGroup \\
            --provider-name myOpenIdConnectProvider
    crafted: true
"""

helps['webapp auth openid-connect add'] = """
type: command
short-summary: Configure a new custom OpenID Connect identity provider.
examples:
  - name: Configure a new custom OpenID Connect identity provider.
    text: >
        az webapp auth openid-connect add -g myResourceGroup --name MyWebApp \\
          --provider-name myOpenIdConnectProvider --client-id my-client-id \\
          --client-secret-setting-name MY_SECRET_APP_SETTING \\
          --openid-configuration https://myopenidprovider.net/.well-known/openid-configuration
"""

helps['webapp auth openid-connect update'] = """
type: command
short-summary: Update the client id and client secret setting name for an existing custom OpenID Connect identity provider.
examples:
  - name: Update the client id and client secret setting name for an existing custom OpenID Connect identity provider.
    text: >
        az webapp auth openid-connect update -g myResourceGroup --name MyWebApp \\
          --provider-name myOpenIdConnectProvider --client-id my-client-id \\
          --client-secret-setting-name MY_SECRET_APP_SETTING
"""

helps['webapp auth openid-connect remove'] = """
type: command
short-summary: Removes an existing custom OpenID Connect identity provider.
examples:
  - name: Removes an existing custom OpenID Connect identity provider.
    text: >
        az webapp auth openid-connect remove --name MyWebApp --resource-group MyResourceGroup \\
          --provider-name myOpenIdConnectProvider
"""

helps['webapp auth twitter'] = """
type: group
short-summary: Manage webapp authentication and authorization of the Twitter identity provider.
"""

helps['webapp auth twitter show'] = """
type: command
short-summary: Show the authentication settings for the Twitter identity provider.
examples:
  - name: Show the authentication settings for the Twitter identity provider. (autogenerated)
    text: az webapp auth twitter show --name MyWebApp --resource-group MyResourceGroup
    crafted: true
"""

helps['webapp auth twitter update'] = """
type: command
short-summary: Update the consumer key and consumer secret for the Twitter identity provider.
examples:
  - name: Update the consumer key and consumer secret for the Twitter identity provider.
    text: >
        az webapp auth twitter update  -g myResourceGroup --name MyWebApp \\
          --consumer-key my-client-id --consumer-secret very_secret_password
"""