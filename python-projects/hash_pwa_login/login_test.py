import login


def test_pwd_is_ok():

    assert login.pwd_is_ok('00000000') == True
    assert login.pwd_is_ok('0000000000000') == False
    assert login.pwd_is_ok('') == False
    #assert gd_login.pwd_is_ok(None) == False


def test_hash_password():

    input = '7e071fd9b023ed8f18458a73613a0834f6220bd5cc50357ba3493c6040a9ea8c'
    output = login.hash_password('00000000')
    assert output == input


if __name__ == '__main__':
    test_pwd_is_ok()
    test_hash_password()
