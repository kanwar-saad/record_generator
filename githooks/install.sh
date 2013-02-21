
base=$(readlink -f $0)
scriptpath=$(dirname $base)

echo $base
echo $scriptpath
rm -f $scriptpath/../.git/hooks/pre-commit
ln -s $scriptpath/pre-commit $scriptpath/../.git/hooks/pre-commit

chmod +x pre-commit

