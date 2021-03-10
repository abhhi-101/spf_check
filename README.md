# SPF_Check
To check if SPF records exixts of given Domain or List of Domains.

## Install
```
git clone https://github.com/abhhi-101/spf_check.git
```
```
python3 -m pip install optparse-pretty os sys
```

## Usage
```
cd spf_check
python3 spf_check.py -d example.com
python3 spf_check.py -f target_domains.txt
```

## Help Menu
```
Usage: spf.py [options]

Options:
  -h, --help            show this help message and exit
  -d example.com, --domain=example.com
                        To Find SOF Record of domain Specified
  -f file.txt, --file=file.txt
                        File Containing list of Domains
```
### Made with <3 by abhhi :)
