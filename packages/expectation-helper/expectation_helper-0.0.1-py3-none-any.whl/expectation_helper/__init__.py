import bg_helper as bh
import fs_helper as fh
import settings_helper as sh
from os.path import isdir


SETTINGS = sh.get_all_settings(__name__).get(sh.APP_ENV, {})

gx_local_repo_path = fh.abspath(SETTINGS.get('gx_local_repo_path'))
assert gx_local_repo_path, 'The GX_LOCAL_REPO_PATH is not set'
if not isdir(gx_local_repo_path):
    print(f'Cloning great_expectations to {gx_local_repo_path}')
    cmd = f'git clone https://github.com/great-expectations/great_expectations {repr(gx_local_repo_path)}'
    bh.run(cmd, show=True)
