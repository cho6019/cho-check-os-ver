from cho_check_os_ver.osver import get_os_pretty_name

def test_first():
    v = get_os_pretty_name()
    assert v is not None
    assert v == "Ubuntu 24.04.1"
    # 빈 문자열이 아닌지 확인
    # 문자열에 LTS가 포함 되었는지 확인
    # 문자열에 문자도 있고, 숫자도 있는지 확인
    # . 이 포함 되어 있는지 확인
    # 기타 등등 ...
    # 길이가 적어도 얼마 이상인지 확


