提交代码
git add -A
git commit -m %1
git push

修改版本


提交发布
python setup.py sdist build
twine upload dist/*
