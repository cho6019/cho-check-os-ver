import platform


def get_os_pretty_name() -> str:
    with open('/etc/os-release', 'r') as file:
        for line in file:
            if line.startswith('PRETTY_NAME'):
                r = line.split('=')[1].replace('\n','').strip("\"")
                print(r)
                return r
    return None


def get_os_version_win() -> str:
    return (platform.version())

# mac은 관련 값을 함수로 반환한다고 한다. os 종류는 왜 이렇게 많은 걸까;
def get_os_version_macOS() -> str:
    version, _, architecture = platform.mac_ver()
    return version
