# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.help_files import helps

from azext_front_door.vendored_sdks.models import MatchVariable, Operator

# region FrontDoor
helps['network front-door'] = """
    type: group
    short-summary: Manage Front Doors.
"""

helps['network front-door create'] = """
    type: command
    short-summary: Create a Front Door.
"""

helps['network front-door list'] = """
    type: command
    short-summary: List Front Doors.
"""

helps['network front-door show'] = """
    type: command
    short-summary: Get the details of a Front Door.
"""

helps['network front-door update'] = """
    type: command
    short-summary: Update settings of a Front Door.
"""

helps['network front-door delete'] = """
    type: command
    short-summary: Delete a Front Door.
"""
# endregion

# region FrontDoor BackendPool
helps['network front-door backend-pool'] = """
    type: group
    short-summary: Manage Front Door backend pools.
"""

helps['network front-door backend-pool create'] = """
    type: command
    short-summary: Create a Front Door backend pool.
    long-summary: >
        Since a backend pool must contain a backend, this command
        also creates the first backend. To add additional backends,
        use the `az network front-door backend-pool backend add` command.
"""

helps['network front-door backend-pool list'] = """
    type: command
    short-summary: List Front Door backend pools.
"""

helps['network front-door backend-pool show'] = """
    type: command
    short-summary: Get the details of a Front Door backend pool.
"""

helps['network front-door backend-pool delete'] = """
    type: command
    short-summary: Delete a Front Door backend pool.
"""
# endregion

# region FrontDoor BackendPool Backend
helps['network front-door backend-pool backend'] = """
    type: group
    short-summary: Manage backends of Front Door backend pools.
"""

helps['network front-door backend-pool backend add'] = """
    type: command
    short-summary: Add a backend to a Front Door backend pool.
"""

helps['network front-door backend-pool backend list'] = """
    type: command
    short-summary: List backends of a Front Door backend pool.
"""

helps['network front-door backend-pool backend remove'] = """
    type: command
    short-summary: Remove a backend from a Front Door backend pool.
"""
# endregion

# region FrontDoor FrontendEndpoint
helps['network front-door frontend-endpoint'] = """
    type: group
    short-summary: Manage Front Door frontend endpoints.
"""

helps['network front-door frontend-endpoint create'] = """
    type: command
    short-summary: Create a Front Door frontend endpoint.
"""

helps['network front-door frontend-endpoint list'] = """
    type: command
    short-summary: List Front Door frontend endpoints.
"""

helps['network front-door frontend-endpoint show'] = """
    type: command
    short-summary: Get the details of a Front Door frontend endpoint.
"""

helps['network front-door frontend-endpoint delete'] = """
    type: command
    short-summary: Delete a Front Door frontend endpoint.
"""

helps['network front-door frontend-endpoint enable-https'] = """
    type: command
    short-summary: Enable HTTPS protocol for a custom domain.
    long-summary: >
        HTTPS protocol for a custom domain can be enabled using Front Door managed certificate
        or using your own certificate in Azure Key Vault. For Azure Key Vault, right permissions
        need to be set for Front Door to access the Key vault. Learn more at https://aka.ms/FrontDoorCustomDomain.
"""

helps['network front-door frontend-endpoint disable-https'] = """
    type: command
    short-summary: Disable HTTPS protocol for a custom domain.
"""
# endregion

# region FrontDoor LoadBalancingSettings
helps['network front-door load-balancing'] = """
    type: group
    short-summary: Manage Front Door load-balancing settings.
"""
helps['network front-door load-balancing create'] = """
    type: command
    short-summary: Create Front Door load-balancing settings.
"""

helps['network front-door load-balancing list'] = """
    type: command
    short-summary: List Front Door load-balancing settingss.
"""

helps['network front-door load-balancing show'] = """
    type: command
    short-summary: Get the details of a Front Door load-balancing settings bundle.
"""

helps['network front-door load-balancing delete'] = """
    type: command
    short-summary: Delete Front Door load-balancing settings.
"""

# endregion

# region FrontDoor HealthProbeSettings
helps['network front-door probe'] = """
    type: group
    short-summary: Manage Front Door health probe settings.
"""
helps['network front-door probe create'] = """
    type: command
    short-summary: Create Front Door health probe settings.
"""

helps['network front-door probe list'] = """
    type: command
    short-summary: List Front Door health probe settings.
"""

helps['network front-door probe show'] = """
    type: command
    short-summary: Get the details of a Front Door health probe settings bundle.
"""

helps['network front-door probe delete'] = """
    type: command
    short-summary: Delete Front Door health probe settings.
"""

# endregion

# region FrontDoor RoutingRule
helps['network front-door routing-rule'] = """
    type: group
    short-summary: Manage Front Door routing rules.
"""
helps['network front-door routing-rule create'] = """
    type: command
    short-summary: Create a Front Door routing rule.
    long-summary: >
        Create a Front Door routing rule to either forward
        the requests to a backend or redirect the users to a different URL.


        Example 1: az network front-door routing-rule create -f frontdoor1 -g rg1 --frontend-endpoints
        DefaultFrontendEndpoint --route-type Forward --backend-pool DefaultBackendPool
        -n forwardRoutingrule1 --patterns /forward1


        Example 2: az network front-door routing-rule create -f frontdoor1 -g rg1 --frontend-endpoints
        DefaultFrontendEndpoint --route-type Redirect --custom-host redirecthost.com
        -n redirectRouteRule1 --patterns /redirect1 --custom-query-string querystring
"""

helps['network front-door routing-rule list'] = """
    type: command
    short-summary: List Front Door routing rules.
"""

helps['network front-door routing-rule show'] = """
    type: command
    short-summary: Get the details of a Front Door routing rule.
"""

helps['network front-door routing-rule delete'] = """
    type: command
    short-summary: Delete a Front Door routing rule.
"""
# endregion

# region WAFPolicy
helps['network front-door waf-policy'] = """
    type: group
    short-summary: Manage WebApplication Firewall (WAF) policies.
"""

helps['network front-door waf-policy create'] = """
    type: command
    short-summary: Create a WAF policy.
"""

helps['network front-door waf-policy list'] = """
    type: command
    short-summary: List WAF policies.
"""

helps['network front-door waf-policy show'] = """
    type: command
    short-summary: Get the details of a WAF policy.
"""

helps['network front-door waf-policy update'] = """
    type: command
    short-summary: Update settings of a WAF policy.
"""

helps['network front-door waf-policy delete'] = """
    type: command
    short-summary: Delete a WAF policy.
"""

helps['network front-door waf-policy rule'] = """
    type: group
    short-summary: Manage WAF policy custom rules.
"""

helps['network front-door waf-policy rule create'] = """
    type: command
    short-summary: Create a WAF policy custom rule.
""".format(
    variables=', '.join([x.value for x in MatchVariable]),
    operators=', '.join([x.value for x in Operator])
)

helps['network front-door waf-policy rule match-condition add'] = """
    type: command
    short-summary: Add a match-condition to a WAF policy custom rule.
    parameters:
        - name: --match-condition
          short-summary: Match condition for the rule.
          long-summary: |

            Usage:   [--negate] --match-variable VARIABLE[.selector] --operator OPERATOR --value [VALUE [VALUE ...]]

              Variable allowed values: {variables}

              Operator allowed values: {operators}
""".format(
    variables=', '.join([x.value for x in MatchVariable]),
    operators=', '.join([x.value for x in Operator])
)

helps['network front-door waf-policy rule list'] = """
    type: command
    short-summary: List WAF policy custom rules.
"""

helps['network front-door waf-policy rule show'] = """
    type: command
    short-summary: Get the details of a WAF policy custom rule.
"""

helps['network front-door waf-policy rule delete'] = """
    type: command
    short-summary: Delete a WAF policy custom rule.
"""

helps['network front-door waf-policy managed-rules add'] = """
    type: command
    short-summary: Add a managed rule set to a WAF policy.
    long-summary: >
        Use 'az network front-door waf-policy managed-rule-definition list' to see the available managed rulesets.
"""
# endregion
