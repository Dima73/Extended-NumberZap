from distutils.core import setup
import setup_translate


setup(name = 'enigma2-plugin-systemplugins-extnumberzap',
		version='1.0',
		author='Dimitrij',
		author_email='dima-73@inbox.lv',
		package_dir = {'SystemPlugins.NumberZapExt': 'src'},
		packages=['SystemPlugins.NumberZapExt'],
		package_data={'SystemPlugins.NumberZapExt': ['*.xml']},
		description = 'Extended number zap addon for enigma2',
		cmdclass = setup_translate.cmdclass,
	)

