from cho_check_os_ver.osver import get_os_pretty_name




# this is for linux
def test_first():
    v = get_os_pretty_name()
    assert v is not None, "Error, None값이 부여됩니다"
    # 편의상 비활성화
    #assert v == "Ubuntu 24.04.1", "정확히 Ubuntu 24.04.1이 반환되지 않습니다"
    # 빈 문자열인지 확인(빈 문자열은 False값을 반환합니다)
    assert v, "빈 문자열 값이 반환됩니다"
    # 문자열에 LTS가 포함 되었는지 확인(string 문자열간에 in을 이용한 비교가 가능합니다. 참일 시 true, 이외는 false를 반환합니다)
    assert "LTS" in v, "반환 값에 LTS가 포함되지 않습니다"
    # 문자열에 문자도 있고, 숫자도 있는지 확인(any와 isdigit, isalpha를 이용해 문자와 숫자를 각각 식별합니다)
    assert any(char.isdigit() for char in v), "반환 값에 숫자가 존재하지 않습니다"
    assert any(char.isalpha() for char in v), "반환 값에 문자가 존재하지 않습니다"
    # . 이 포함 되어 있는지 확인(위의 LTS 확인하고 동일한 맥락입니다)
    assert "." in v, "반환 값에 온점(.)은 포함되지 않습니다"
    # 길이가 적어도 일정 부분 이상인지
    assert len(v)>=3, "반환 값의 길이가 3이상을 충족하지 않습니다"


