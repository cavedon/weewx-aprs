from weecfg.extension import ExtensionInstaller


def loader():
    return APRSInstaller()


class APRSInstaller(ExtensionInstaller):
    def __init__(self):
        super(APRSInstaller, self).__init__(
            version='0.2',
            name='aprs-formatter',
            description='Write archive data in APRS positionless format.',
            author='Ludovico Cavedon (K6LUD)',
            author_email='ludovico.cavedon@gmail.com',
            process_services='user.aprs.APRS',
            config={
                'APRS': {
                    'output_filename': '/dev/shm/aprs.pkt',
                    'include_position': 0,
                    'symbol_table': '/',
                    'symbol_code': '_',
                    'comment': '',
                    'station_model': 'default',
                    'report_luminosity': 0,
                },
            },
            files=[('bin/user', ['bin/user/aprs-formatter.py'])]
        )
