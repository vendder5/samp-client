class MockSocket(object):
    responses = {
        b'SAMP3\xfe\x82\x0ea\x1eptest': b'test',
        b'SAMP3\xfe\x82\x0ea\x1ec': b"\x0c\x00\x0bpedr$$Nn157_G\x00\x00\x04SuBa\x9c\x03\x00\x00\tChocolateW\x1e\x00\x00\x0cbiieL$iNn157YG\x00\x00\x0bMartin80nik\xd0'\x00\x00\x0cNadoVGs(AFK)*\x14\x00\x00\x04Ottof\x00\x00\x00\x0bKristo_Rand\x01\x00\x00\x00\x07abeceda\x02\x00\x00\x00\x08katerina\x00\x00\x00\x00\x11Jonas_Nicholls_II5l\x00\x00\nMurs_Beten\x81\x02\x00\x00",
        b'SAMP3\xfe\x82\x0ea\x1ed': b"\x0c\x00\x00\x0bpedr$$Nn157_G\x00\x00\xfc\x00\x00\x00\x01\x04SuBa\x9c\x03\x00\x008\x00\x00\x00\x02\tChocolateW\x1e\x00\x00\x18\x00\x00\x00\x03\x0cbiieL$iNn157YG\x00\x00\xe4\x00\x00\x00\x04\x0bMartin80nik\xd0'\x00\x00H\x00\x00\x00\x05\x0cNadoVGs(AFK)*\x14\x00\x00\xd4\x00\x00\x00\x08\x04Ottof\x00\x00\x00j\x00\x00\x00\t\x0bKristo_Rand\x01\x00\x00\x00P\x00\x00\x00\n\x07abeceda\x02\x00\x00\x00:\x00\x00\x00\x0b\x08katerina\x00\x00\x00\x00F\x00\x00\x00\x0c\x11Jonas_Nicholls_II5l\x00\x00B\x00\x00\x00\x0e\nMurs_Beten\x81\x02\x00\x007\x00\x00\x00",
        b'SAMP3\xfe\x82\x0ea\x1ei': b'\x00\x0c\x00d\x00\x0f\x00\x00\x00Convoy Trucking\x15\x00\x00\x00Convoy Trucking 3.4.4\x07\x00\x00\x00English',
        b'SAMP3\xfe\x82\x0ea\x1er': b'\x06\x00\x07lagcomp\x02On\x07mapname\x0bSan Andreas\x07version\x080.3.7-R2\x07weather\x0210\x06weburl\x16www.convoytrucking.net\tworldtime\x0518:00',
        b'SAMP3\xfe\x82\x0ea\x1ex\x0f\x00invalidpassword\x07\x00players': b'\x16\x00Invalid RCON password.',
    }
    response_prefix = b'SAMP3\xfe\x82\x0ea\x1ex'

    def __init__(self, *args, **kwargs):
        self.connected = True

    def settimeout(self, value):
        pass

    def close(self):
        self.connected = False

    def sendto(self, data, *args, **kwargs):
        assert self.connected
        self.request = data

    def recv(self, bufsize):
        assert self.connected
        try:
            if self.request:
                return self.response_prefix + self.responses[self.request]
            else:
                return self.response_prefix
        except KeyError:
            raise ConnectionError(10054, 'Connection error')
        finally:
            self.request = None
