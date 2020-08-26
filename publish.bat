rd build /Q /S
rd dist /Q /S
rd cd_api.egg-info /Q /S

git add -A
<<<<<<< HEAD
git commit -m "1.1.1"
git push git master
=======
git commit -m "1.1.3 合并代码"
git push github master
>>>>>>> e023a89b9b595ab581ba24e52bc07dd918020606

python setup.py sdist build
twine upload dist/*


rd build /Q /S
rd dist /Q /S
rd cd_api.egg-info /Q /S