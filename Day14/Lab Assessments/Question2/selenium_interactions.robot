*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${URL}        https://demoqa.com/automation-practice-form
${BROWSER}    edge

*** Test Cases ***
Interact With Web Elements Using Selenium
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window

    # Text Box
    Input Text    id=firstName    Mohan
    Input Text    id=lastName     Reddy

    # Radio Button
    Click Element    xpath=//label[text()='Male']

    # Check Box
    Click Element    xpath=//label[text()='Sports']

    # Built-in keyword
    ${title}=    Get Title
    Run Keyword If    '${title}' != ''    Log    Page title is displayed

    Close Browser
