git checkout gh-pages
rm -rf build _sources _static
git checkout master docs
git reset HEAD
cd docs
make html
mv -fv _build/html/* ../
cd ..
rm -rf docs
git add -A
git commit -m "Generated gh-pages for `git log master -1 --pretty=short --abbrev-commit`" && git push origin gh-pages
git checkout master

