rd build /Q /S
rd dist /Q /S
rd cd_api.egg-info /Q /S

git add -A
git commit -m "增加修改门店售后电话方法"
git push github master

python setup.py sdist build
twine upload dist/*


rd build /Q /S
rd dist /Q /S
rd cd_api.egg-info /Q /S