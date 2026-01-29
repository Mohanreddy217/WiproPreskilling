def test_read_ini_option(request):
    verbose = request.config.getoption("-v")
    assert verbose >= 1
