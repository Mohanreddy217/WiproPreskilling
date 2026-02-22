*** Settings ***
Library    SeleniumLibrary
Library    DateTime

*** Variables ***
${BASE_URL}    https://practicesoftwaretesting.com/
${BROWSER}     chrome

*** Keywords ***

Open Application
    Open Browser    ${BASE_URL}    ${BROWSER}
    Maximize Browser Window

Close Application
    Close Browser


# ================= REGISTER =================

Register User
    [Arguments]
    ...    ${firstname}    ${lastname}    ${password}
    ...    ${dob}    ${street}    ${postal_code}
    ...    ${city}    ${state}    ${country}    ${phone}

    Wait Until Element Is Visible    css:a[data-test='nav-sign-in']    20s
    Click Element    css:a[data-test='nav-sign-in']

    Wait Until Element Is Visible    xpath=//a[contains(text(),'Register your account')]    20s
    Click Element    xpath=//a[contains(text(),'Register your account')]

    ${timestamp}=    Get Time    epoch
    ${EMAIL}=    Catenate    ${firstname}${timestamp}@example.com
    Set Suite Variable    ${EMAIL}
    Set Suite Variable    ${USER_PASSWORD}    ${password}

    Wait Until Element Is Visible    id:first_name    20s
    Input Text    id:first_name    ${firstname}
    Input Text    id:last_name     ${lastname}
    Input Text    id:email         ${EMAIL}
    Input Text    id:password      ${password}
    Input Text    id:dob           ${dob}
    Input Text    id:street        ${street}
    Input Text    id:postal_code   ${postal_code}
    Input Text    id:city          ${city}
    Input Text    id:state         ${state}
    Select From List By Label      id:country    ${country}
    Input Text    id:phone         ${phone}

    Click Button    css:button[type='submit']
    Wait Until Page Contains Element    css:form[data-test='login-form']    20s


# ================= LOGIN =================

Login User
    Input Text    id:email       ${EMAIL}
    Input Text    id:password    ${USER_PASSWORD}
    Click Button    css:input[data-test='login-submit']
    Wait Until Page Contains Element    css:a[data-test='nav-menu']    20s


# ================= SEARCH & ADD TO CART =================

Search And Add To Cart
    [Arguments]    ${product}

    Go To    ${BASE_URL}
    Wait Until Element Is Visible    css:input[data-test='search-query']    20s
    Input Text    css:input[data-test='search-query']    ${product}
    Click Button    css:button[data-test='search-submit']
    Wait Until Element Is Visible    css:a.card    20s
    

    Click Element    css:a.card
    Wait Until Element Is Visible    css:button[data-test='add-to-cart']    20s

    Click Button    css:button[data-test='add-to-cart']
    Wait Until Element Is Visible    css:.ngx-toastr    10s
    Wait Until Element Is Not Visible    css:.ngx-toastr    20s


# ================= OPEN CART =================

Open Cart
    Wait Until Element Is Visible    css:a[data-test='nav-cart']    20s
    Click Element    css:a[data-test='nav-cart']

    # Wait for URL to change to checkout page
    Wait Until Location Contains    checkout    20s

    # Now confirm quantity field exists
    Wait Until Page Contains Element    css:input[type='number']    20s


# ================= UPDATE QUANTITY =================

Update Quantity
    [Arguments]    ${quantity}

    Wait Until Element Is Visible    css:input[type='number']    20s
    Wait Until Element Is Enabled    css:input[type='number']    20s

    # Scroll into view (important)
    Execute JavaScript
    ...    document.querySelector("input[type='number']").scrollIntoView(true);

    Sleep    1s

    Clear Element Text    css:input[type='number']
    Input Text    css:input[type='number']    ${quantity}
    Press Keys    css:input[type='number']    ENTER


# ================= LOGOUT =================

Logout User
    Execute JavaScript    document.querySelector("a[data-test='nav-menu']").click();
    Sleep    1s
    Execute JavaScript    document.querySelector("a[data-test='nav-sign-out']").click();
    Wait Until Element Is Visible    css:a[data-test='nav-sign-in']    20s