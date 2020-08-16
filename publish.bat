rd build /Q /S
rd dist /Q /S
rd cd_api.egg-info /Q /S

git add -A
git commit -m "1.1.3 合并代码"
git push github master

python setup.py sdist build
twine upload dist/*


rd build /Q /S
rd dist /Q /S
rd cd_api.egg-info /Q /S