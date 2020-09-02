rd build /Q /S
rd dist /Q /S
rd cd_api.egg-info /Q /S

git add -A
git commit -m "1.1.4 增加员工列表接口和批量离职员工接口"
git push github master

python setup.py sdist build
twine upload dist/*


rd build /Q /S
rd dist /Q /S
rd cd_api.egg-info /Q /S