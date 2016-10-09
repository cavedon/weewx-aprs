from setup import ExtensionInstaller


def loader():
    return APRSInstaller()


class APRSInstaller(ExtensionInstaller):
    def __init__(self):
        super(APRSInstaller, self).__init__(
            version='0.1',
            name='aprs',
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
                },
            },
            files=[('bin/user', ['bin/user/aprs.py'])]
        )
