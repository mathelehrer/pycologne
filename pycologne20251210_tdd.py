import pytest
from pathlib import Path

from platformdirs import user_videos_path

#@pytest.mark.xfail
# def test_example_01():
#     assert day(example)==0
#

# """
# Path(__file__).stem
#
# """

root= Path("/")
my_home=root/'home'/'jmartin'
print(my_home)

subdirs = ['home','dst']
my_home=root.joinpath(*subdirs)

Path(root,*subdirs)

print(Path.cwd())

# uv run pytest

# astral-sh/uv
# poweshell -ExecutionPolicy ....
