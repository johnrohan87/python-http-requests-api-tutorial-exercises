import sys
def pytest_addoption(parser):
    parser.addoption("--stdin", action="append", default=[],
        help="json with the stdin to pass to test functions")

def pytest_generate_tests(metafunc):
    if 'stdin' in metafunc.fixturenames:
        metafunc.parametrize("stdin",metafunc.config.getoption('stdin'))

    if 'app' in metafunc.fixturenames:
        try:
          sys.path.append('./.breathecode/dist')
          import cached_app
          metafunc.parametrize("app",[cached_app.execute_app])
        except SyntaxError:
          metafunc.parametrize("app",[lambda : None])
        except ImportError:
          metafunc.parametrize("app",[cached_app])
        except AttributeError:
          metafunc.parametrize("app",[cached_app])
