*** Settings ***
Library    RequestsLibrary
Library    Collections

*** Variables ***
${BASE_URL}    http://127.0.0.1:5000

*** Test Cases ***
Create Restaurant
    Create Session    foodie    ${BASE_URL}
    ${body}=    Create Dictionary    name=Robot Restaurant
    ${response}=    POST On Session    foodie    /api/v1/restaurants    json=${body}
    Should Be Equal As Integers    ${response.status_code}    201
