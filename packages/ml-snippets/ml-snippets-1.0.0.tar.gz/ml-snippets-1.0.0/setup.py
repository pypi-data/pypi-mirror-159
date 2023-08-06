from setuptools import setup, find_namespace_packages
try: # for pip >= 10
    from pip._internal.req import parse_requirements
except ImportError: # for pip <= 9.0.3
    from pip.req import parse_requirements

install_reqs = parse_requirements("requirements.txt", session=False)
# reqs = [str(ir.req) for ir in install_reqs]
# requirements = list(requirements) 
try:
    requirements = [str(ir.req) for ir in install_reqs]
except:
    requirements = [str(ir.requirement) for ir in install_reqs]

VERSION = '1.0.0'

setup(
    name = 'ml-snippets', 
    packages = find_namespace_packages(), 
    package_data = {'': ['*.json']}, 
    version = VERSION, 
    description = 'snippets lib', 
    author = 'Kouros Basiri', 
    author_email = 'kouros.basiri@gmail.com', 
    keywords = [ 'Snippets','Data Science', 'ML' ], 
    install_requires=requirements,
    python_requires = ' >= 3.6', 
    classifiers = [
        'Natural Language :: English', 
        'Programming Language :: Python', 
        'Programming Language :: Python :: 3', 
        'Programming Language :: Python :: 3.6', 
        'Programming Language :: Python :: 3.7', 
        'Programming Language :: Python :: 3.8', 
        'Programming Language :: Python :: 3.9', 
        'Topic :: Software Development', 
    ], 
)

