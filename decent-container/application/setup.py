from distutils.core import setup


setup(
        name='voat_sql',
        version='0.1',
	package_dir = {'': 'libs'},
        packages=[
                    'voat_sql', 
                    'voat_sql',
                    'voat_sql.utils',
                    'voat_rest',
                    'voat_utils'],

        license='GPL v3'
     )
