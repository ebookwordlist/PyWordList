### install from source 
git clone  

python3 -m venv venv/ 

source venv/bin/activate 

if you are in chinese mainland
pip install -r requirements.txt -i http://mirrors.aliyun.com/pypi/simple --trusted-host mirrors.aliyun.com



https://stackoverflow.com/questions/24764549/upgrade-python-packages-from-requirements-txt-using-pip-command

pip install --upgrade --force-reinstall -r requirements.txt You can also ignore installed package and install the new one :

pip install --ignore-installed -r requirements.tx