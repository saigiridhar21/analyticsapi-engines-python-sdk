```python
from __future__ import print_function
import time
import fds.analyticsapi.engines
from fds.analyticsapi.engines.rest import ApiException
from pprint import pprint

configuration = fds.analyticsapi.engines.Configuration()
# Configure HTTP basic authorization: Basic
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# Defining host is optional and default to https://api.factset.com
configuration.host = "https://api.factset.com"
# Create an instance of the API class
api_instance = fds.analyticsapi.engines.AccountsApi(fds.analyticsapi.engines.ApiClient(configuration))
path = '' # str | The directory to get the accounts and sub-directories in (default to '')

try:
    # Get accounts and sub-directories in a directory
    api_response = api_instance.get_accounts(path)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->get_accounts: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://api.factset.com*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AccountsApi* | [**get_accounts**](docs/AccountsApi.md#get_accounts) | **GET** /analytics/lookups/v2/accounts/{path} | Get accounts and sub-directories in a directory
*CalculationsApi* | [**cancel_calculation_by_id**](docs/CalculationsApi.md#cancel_calculation_by_id) | **DELETE** /analytics/engines/v2/calculations/{id} | Cancel calculation by id
*CalculationsApi* | [**get_calculation_status_by_id**](docs/CalculationsApi.md#get_calculation_status_by_id) | **GET** /analytics/engines/v2/calculations/{id} | Get calculation status by id
*CalculationsApi* | [**get_calculation_status_summaries**](docs/CalculationsApi.md#get_calculation_status_summaries) | **GET** /analytics/engines/v2/calculations | Get all calculation statuses
*CalculationsApi* | [**run_calculation**](docs/CalculationsApi.md#run_calculation) | **POST** /analytics/engines/v2/calculations | Run calculation
*ColumnStatisticsApi* | [**get_pa_column_statistics**](docs/ColumnStatisticsApi.md#get_pa_column_statistics) | **GET** /analytics/lookups/v2/engines/pa/columnstatistics | Get PA column statistics
*ColumnsApi* | [**get_pa_column_by_id**](docs/ColumnsApi.md#get_pa_column_by_id) | **GET** /analytics/lookups/v2/engines/pa/columns/{id} | Get PA column settings
*ColumnsApi* | [**get_pa_columns**](docs/ColumnsApi.md#get_pa_columns) | **GET** /analytics/lookups/v2/engines/pa/columns | Get PA columns
*ComponentsApi* | [**get_pa_component_by_id**](docs/ComponentsApi.md#get_pa_component_by_id) | **GET** /analytics/lookups/v2/engines/pa/components/{id} | Get PA component by id
*ComponentsApi* | [**get_pa_components**](docs/ComponentsApi.md#get_pa_components) | **GET** /analytics/lookups/v2/engines/pa/components | Get PA components
*ComponentsApi* | [**get_spar_components**](docs/ComponentsApi.md#get_spar_components) | **GET** /analytics/lookups/v2/engines/spar/components | Get SPAR components
*ComponentsApi* | [**get_vault_component_by_id**](docs/ComponentsApi.md#get_vault_component_by_id) | **GET** /analytics/lookups/v2/engines/vault/components/{id} | Get Vault component by id
*ComponentsApi* | [**get_vault_components**](docs/ComponentsApi.md#get_vault_components) | **GET** /analytics/lookups/v2/engines/vault/components | Get Vault components
*ConfigurationsApi* | [**get_vault_configuration_by_id**](docs/ConfigurationsApi.md#get_vault_configuration_by_id) | **GET** /analytics/lookups/v2/engines/vault/configurations/{id} | Get Vault configuration by id
*ConfigurationsApi* | [**get_vault_configurations**](docs/ConfigurationsApi.md#get_vault_configurations) | **GET** /analytics/lookups/v2/engines/vault/configurations | Get Vault configurations
*CurrenciesApi* | [**get_pa_currencies**](docs/CurrenciesApi.md#get_pa_currencies) | **GET** /analytics/lookups/v2/engines/pa/currencies | Get PA currencies
*DatesApi* | [**convert_pa_dates_to_absolute_format**](docs/DatesApi.md#convert_pa_dates_to_absolute_format) | **GET** /analytics/lookups/v2/engines/pa/dates | Convert PA dates to absolute format
*DatesApi* | [**convert_vault_dates_to_absolute_format**](docs/DatesApi.md#convert_vault_dates_to_absolute_format) | **GET** /analytics/lookups/v2/engines/vault/dates | Convert Vault dates to absolute format
*DocumentsApi* | [**get_pa3_documents**](docs/DocumentsApi.md#get_pa3_documents) | **GET** /analytics/lookups/v2/engines/pa/documents/{path} | Get PA3 documents and sub-directories in a directory
*DocumentsApi* | [**get_pub_documents**](docs/DocumentsApi.md#get_pub_documents) | **GET** /analytics/lookups/v2/engines/pub/documents/{path} | Gets Publisher documents and sub-directories in a directory
*DocumentsApi* | [**get_spar3_documents**](docs/DocumentsApi.md#get_spar3_documents) | **GET** /analytics/lookups/v2/engines/spar/documents/{path} | Gets SPAR3 documents and sub-directories in a directory
*DocumentsApi* | [**get_vault_documents**](docs/DocumentsApi.md#get_vault_documents) | **GET** /analytics/lookups/v2/engines/vault/documents/{path} | Get Vault documents and sub-directories in a directory
*FrequenciesApi* | [**get_pa_frequencies**](docs/FrequenciesApi.md#get_pa_frequencies) | **GET** /analytics/lookups/v2/engines/pa/frequencies | Get PA frequencies
*FrequenciesApi* | [**get_spar_frequencies**](docs/FrequenciesApi.md#get_spar_frequencies) | **GET** /analytics/lookups/v2/engines/spar/frequencies | Get SPAR frequencies
*FrequenciesApi* | [**get_vault_frequencies**](docs/FrequenciesApi.md#get_vault_frequencies) | **GET** /analytics/lookups/v2/engines/vault/frequencies | Get Vault frequencies
*GroupsApi* | [**get_pa_groups**](docs/GroupsApi.md#get_pa_groups) | **GET** /analytics/lookups/v2/engines/pa/groups | Get PA groups
*PACalculationsApi* | [**cancel_pa_calculation_by_id**](docs/PACalculationsApi.md#cancel_pa_calculation_by_id) | **DELETE** /analytics/engines/pa/v2/calculations/{id} | Cancel PA calculation by id
*PACalculationsApi* | [**get_pa_calculation_by_id**](docs/PACalculationsApi.md#get_pa_calculation_by_id) | **GET** /analytics/engines/pa/v2/calculations/{id} | Get PA calculation by id
*PACalculationsApi* | [**run_pa_calculation**](docs/PACalculationsApi.md#run_pa_calculation) | **POST** /analytics/engines/pa/v2/calculations | Run PA Calculation
*SPARBenchmarkApi* | [**get_spar_benchmark_by_id**](docs/SPARBenchmarkApi.md#get_spar_benchmark_by_id) | **GET** /analytics/lookups/v2/engines/spar/benchmarks | Get SPAR benchmark details
*SPARCalculationsApi* | [**cancel_spar_calculation_by_id**](docs/SPARCalculationsApi.md#cancel_spar_calculation_by_id) | **DELETE** /analytics/engines/spar/v2/calculations/{id} | Cancel SPAR calculation
*SPARCalculationsApi* | [**get_spar_calculation_by_id**](docs/SPARCalculationsApi.md#get_spar_calculation_by_id) | **GET** /analytics/engines/spar/v2/calculations/{id} | Get SPAR calculation by id
*SPARCalculationsApi* | [**run_spar_calculation**](docs/SPARCalculationsApi.md#run_spar_calculation) | **POST** /analytics/engines/spar/v2/calculations | Run SPAR Calculation
*VaultCalculationsApi* | [**cancel_vault_calculation_by_id**](docs/VaultCalculationsApi.md#cancel_vault_calculation_by_id) | **DELETE** /analytics/engines/vault/v2/calculations/{id} | Cancel Vault calculation by id
*VaultCalculationsApi* | [**get_vault_calculation_by_id**](docs/VaultCalculationsApi.md#get_vault_calculation_by_id) | **GET** /analytics/engines/vault/v2/calculations/{id} | Get Vault calculation by id
*VaultCalculationsApi* | [**run_vault_calculation**](docs/VaultCalculationsApi.md#run_vault_calculation) | **POST** /analytics/engines/vault/v2/calculations | Run Vault Calculation
*UtilityApi* | [**get_by_url**](docs/UtilityApi.md#get_by_url) | **GET** {url} | Get by url

## Documentation For Models

 - [AccountDirectories](docs/AccountDirectories.md)
 - [Calculation](docs/Calculation.md)
 - [CalculationStatus](docs/CalculationStatus.md)
 - [CalculationStatusSummary](docs/CalculationStatusSummary.md)
 - [CalculationUnitStatus](docs/CalculationUnitStatus.md)
 - [Column](docs/Column.md)
 - [ColumnStatistic](docs/ColumnStatistic.md)
 - [ColumnSummary](docs/ColumnSummary.md)
 - [ComponentAccount](docs/ComponentAccount.md)
 - [ComponentBenchmark](docs/ComponentBenchmark.md)
 - [ComponentSummary](docs/ComponentSummary.md)
 - [ConfigurationAccount](docs/ConfigurationAccount.md)
 - [Currency](docs/Currency.md)
 - [DateParametersSummary](docs/DateParametersSummary.md)
 - [DocumentDirectories](docs/DocumentDirectories.md)
 - [Frequency](docs/Frequency.md)
 - [Group](docs/Group.md)
 - [PACalculationColumn](docs/PACalculationColumn.md)
 - [PACalculationGroup](docs/PACalculationGroup.md)
 - [PACalculationParameters](docs/PACalculationParameters.md)
 - [PAComponent](docs/PAComponent.md)
 - [PADateParameters](docs/PADateParameters.md)
 - [PAIdentifier](docs/PAIdentifier.md)
 - [PubCalculationParameters](docs/PubCalculationParameters.md)
 - [PubDateParameters](docs/PubDateParameters.md)
 - [PubIdentifier](docs/PubIdentifier.md)
 - [SPARBenchmark](docs/SPARBenchmark.md)
 - [SPARCalculationParameters](docs/SPARCalculationParameters.md)
 - [SPARDateParameters](docs/SPARDateParameters.md)
 - [SPARIdentifier](docs/SPARIdentifier.md)
 - [VaultCalculationParameters](docs/VaultCalculationParameters.md)
 - [VaultComponent](docs/VaultComponent.md)
 - [VaultConfiguration](docs/VaultConfiguration.md)
 - [VaultConfigurationSummary](docs/VaultConfigurationSummary.md)
 - [VaultDateParameters](docs/VaultDateParameters.md)
 - [VaultIdentifier](docs/VaultIdentifier.md)


## Documentation For Authorization


## Basic

- **Type**: HTTP basic authentication


## Author

analytics.api.support@factset.com