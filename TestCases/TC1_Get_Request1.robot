*** Settings ***
Library    RequestsLibrary
Library    Collections
Library    json


*** Variables ***
${base_url}  https://reqres.in
${userId}    2

*** Test Cases ***
Get Single User Info
    [Documentation]    This test case is to get single user info
    [Tags]    smoke     regression
    create session    mysession     ${base_url}
    ${response} =    get request    mysession   /api/users/${userId}
#    log to console    ${response.status_code}
#    log to console     ${response.content}
#    log to console    ${response.headers}

    #Validation on Status code
    ${status_code} =    convert to string    ${response.status_code}
    should be equal  ${status_code}   200

#Validation on emailid in response body
    ${body} =   convert to string   ${response.content}
    should contain    ${body}   janet.weaver@reqres.in

#Validate content type should be 'application/json'    -- as there is no header this test case will fail.
#    ${contentTypeValue}=    convert to string    get from dictionary    ${response.header}      Content-Type
#    should be equal     ${contentTypeValue}   application/json

Another Get Single User Info
    ${result}   =   get