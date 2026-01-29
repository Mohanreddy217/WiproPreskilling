def test_env_option(request):
    env = request.config.getoption("--env")
    print(f"Running tests in environment: {env}")
    assert env in ["dev", "stage", "prod"]
