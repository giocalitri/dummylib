from setuptools import setup

setup(
    name='dummylib',
    version='0.0.1',
    description='Dummy Library',
    url='https://github.com/giocalitri/dummylib',
    author='Giovanni Di Milia',
    author_email='giovanni@dimilia.it',
    install_requires=[
        'analytics_python==1.2.9',
        'Flask<=0.12.2',
        'Flask-Cors<=3.0.3',
        'Flask-Script<=2.0.5',
        'kombu',
        'hvac',
        'librato-metrics>=3.0.1',
        'marshmallow',
        'marshmallow_sqlalchemy',
        'mongoengine',
        'opbeat',
        'pycrypto<=2.7',
        'PyJWT',
        'pytz',
        'requests',
        'semantic_version<=2.6.0',
        'simplejson',
        'strict_rfc3339',
        'webargs',
        'Werkzeug',
    ]
)
