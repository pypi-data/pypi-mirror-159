#!/usr/bin/env python
#   -*- coding: utf-8 -*-

from setuptools import setup
from setuptools.command.install import install as _install

class install(_install):
    def pre_install_script(self):
        pass

    def post_install_script(self):
        pass

    def run(self):
        self.pre_install_script()

        _install.run(self)

        self.post_install_script()

if __name__ == '__main__':
    setup(
        name = 'mplogp',
        version = '0.1.1',
        description = 'A log parser for parsing logs generated from multi-processing based tools.',
        long_description = '# mplogp\n[![build](https://github.com/soda480/mplogp/actions/workflows/main.yml/badge.svg)](https://github.com/soda480/mplogp/actions/workflows/main.yml)\n[![codecov](https://codecov.io/gh/soda480/mplogp/branch/main/graph/badge.svg?token=GA62T7LDGK)](https://codecov.io/gh/soda480/mplogp)\n[![Code Grade](https://api.codiga.io/project/22249/status/svg)](https://app.codiga.io/public/project/22249/mplogp/dashboard)\n[![complexity](https://img.shields.io/badge/complexity-Simple:%204-brightgreen)](https://radon.readthedocs.io/en/latest/api.html#module-radon.complexity)\n[![vulnerabilities](https://img.shields.io/badge/vulnerabilities-None-brightgreen)](https://pypi.org/project/bandit/)\n[![python](https://img.shields.io/badge/python-3.7%20%7C%203.8%20%7C%203.9%20%7C%203.10-teal)](https://www.python.org/downloads/)\n\nA Python script to parse a logfile generated from multi-processing based tools. The script will parse the logfile and create logs for each process under a specified timestamped folder. Supports log files generated from a log Formatter whose first two fields are: `%(asctime)s %(processName)s ...`.\n\n\n## `mplogp`\n```\nusage: mplogp [-h] --log LOG --folder FOLDER [--regex REGEX]\n\nA Python script to parse a logfile generated from multi-processing based tools\n\noptional arguments:\n  -h, --help       show this help message and exit\n  --log LOG        The location of the logfile to parse\n  --folder FOLDER  The folder where to write the parsed logs\n  --regex REGEX    Regular expression to alias process log filename - must contain a matched group\n```\n\n### Examples\nParse the `example3.log` file and write the parsed logs under the `logs` folder, add alias to each process log with its matched processor id:\n```\nmplogp --log example3.log --folder logs --regex ".*processor id (.*)$"\n```\nThe log file contained logs from 10 processes and produced the following logs:\n```\nlogs\n└── 2021-05-13_18-48-46\n    ├── MainProcess.log\n    ├── Process-1-69b41899.log\n    ├── Process-10-c40f3916.log\n    ├── Process-2-a6ffc5b5.log\n    ├── Process-3-14175157.log\n    ├── Process-4-90e875c2.log\n    ├── Process-5-ef35f44f.log\n    ├── Process-6-c7268544.log\n    ├── Process-7-7557d6d6.log\n    ├── Process-8-e248e861.log\n    └── Process-9-0bb23bab.log\n```\n\n## Development\n\nBuild the Docker image:\n```bash\ndocker image build \\\n-t \\\nmplogp:latest .\n```\n\nRun the Docker container:\n```bash\ndocker container run \\\n--rm \\\n-it \\\n-v $PWD:/code \\\nmplogp:latest \\\nbash\n```\n\nBuild the project:\n```bash\npyb -X\n```\n',
        long_description_content_type = 'text/markdown',
        classifiers = [
            'Development Status :: 4 - Beta',
            'Environment :: Console',
            'Environment :: Other Environment',
            'Intended Audience :: Developers',
            'Intended Audience :: System Administrators',
            'License :: OSI Approved :: Apache Software License',
            'Operating System :: POSIX :: Linux',
            'Programming Language :: Python',
            'Programming Language :: Python :: 3.7',
            'Programming Language :: Python :: 3.8',
            'Programming Language :: Python :: 3.9',
            'Programming Language :: Python :: 3.10',
            'Topic :: Software Development :: Libraries',
            'Topic :: Software Development :: Libraries :: Python Modules',
            'Topic :: System :: Networking',
            'Topic :: System :: Logging',
            'Topic :: System :: Systems Administration'
        ],
        keywords = '',

        author = 'Emilio Reyes',
        author_email = 'soda480@gmail.com',
        maintainer = '',
        maintainer_email = '',

        license = 'Apache License, Version 2.0',

        url = 'https://github.com/soda480/mplogp',
        project_urls = {},

        scripts = [],
        packages = ['mplogp'],
        namespace_packages = [],
        py_modules = [],
        entry_points = {
            'console_scripts': ['mplogp = mplogp.mplogp:main']
        },
        data_files = [],
        package_data = {},
        install_requires = [],
        dependency_links = [],
        zip_safe = True,
        cmdclass = {'install': install},
        python_requires = '',
        obsoletes = [],
    )
