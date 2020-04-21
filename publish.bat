rd build /Q /S
rd dist /Q /S
rd cd_api.egg-info /Q /S

git add -A
git commit -m "1.0.5 增加用户readme"
git push cd_api master

python setup.py sdist build
twine upload dist/*
