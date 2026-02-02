*** Settings ***
Suite Setup       Suite Level Setup
Suite Teardown    Suite Level Teardown
Test Setup        Test Level Setup
Test Teardown     Test Level Teardown

*** Keywords ***
Suite Level Setup
    Log    === Suite Setup: Initializing resources ===

Suite Level Teardown
    Log    === Suite Teardown: Cleaning up suite resources ===

Test Level Setup
    Log    --- Test Setup: Preparing test ---

Test Level Teardown
    Log    --- Test Teardown: Cleaning up test ---

*** Test Cases ***
Sample Passing Test
    [Tags]    smoke    regression
    Log    Executing a tagged test case
    Should Be Equal    2    2


Another Tagged Test
    [Tags]    sanity
    Log    Executing another tagged test
    Should Contain    Robot Framework    Robot
