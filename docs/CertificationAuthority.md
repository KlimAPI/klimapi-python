# CertificationAuthority


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The id of the Certification Authority | [optional] 
**name** | **str** | Name of the Certification Authority | [optional] 
**website** | **str** | The Website of the Certification Authority | [optional] 
**logo_image** | **str** | The Logo of the Certification Authority | [optional] 

## Example

```python
from klimapi_python.models.certification_authority import CertificationAuthority

# TODO update the JSON string below
json = "{}"
# create an instance of CertificationAuthority from a JSON string
certification_authority_instance = CertificationAuthority.from_json(json)
# print the JSON string representation of the object
print(CertificationAuthority.to_json())

# convert the object into a dict
certification_authority_dict = certification_authority_instance.to_dict()
# create an instance of CertificationAuthority from a dict
certification_authority_from_dict = CertificationAuthority.from_dict(certification_authority_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


