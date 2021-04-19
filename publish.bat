rd build /Q /S
rd dist /Q /S
rd cd_api.egg-info /Q /S

REM git add -A
REM git commit -m "1.1.7"
REM git push github master

python setup.py sdist build
twine upload dist/*

pause
rd build /Q /S
rd dist /Q /S
rd cd_api.egg-info /Q /S

set /p version=
pip install cd_api==%version% -i https://pypi.org/simple