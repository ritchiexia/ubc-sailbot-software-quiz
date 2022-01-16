from standard_calc import bound_to_180, is_angle_between


""" Tests for bound_to_180() """

# BASIC TESTS
def test_bound_basic1():
    assert bound_to_180(0) == 0

def test_bound_basic2():
    assert bound_to_180(-180) == -180

def test_bound_basic3():
    assert bound_to_180(-45.34) == -45.34

def test_bound_basic4():
    assert bound_to_180(45.56) == 45.56

    
# BOUNDARY TEST
def test_bound_edge():
    assert bound_to_180(180) == -180


# WRAPAROUND TESTS OVER 180
def test_bound_over_neg():
    assert bound_to_180(270.5) == -89.5

def test_bound_over_pos():
    assert bound_to_180(450.5) == 90.5


# WRAPAROUND TESTS BELOW -180
def test_bound_under_neg():
    assert bound_to_180(-270.5) == 89.5

def test_bound_under_pos():
    assert bound_to_180(-450.5) == -90.5



""" Tests for is_angle_between() """

# BASIC TEST
def test_between_basic1():
    assert is_angle_between(0, 1, 2)


# NEGATIVE TO NEGATIVE TESTS
def test_between_n2n():
    assert is_angle_between(-3.1, -2.6, -1.4)

def test_between_n2n2():
    assert is_angle_between(-1.4, -2.6, -3.1)

def test_between_n2n_f():
    assert ~is_angle_between(-4.2, 2.0, -2.1)

def test_between_n2n_wrap():
    assert is_angle_between(-270, 45, -360)

def test_between_n2n_wrap_f():
    assert ~is_angle_between(-270, -400, -360)


# NEGATIVE TO POSITIVE/POSITIVE TO NEGATIVE TESTS
def test_between_n2p():
    assert is_angle_between(-1.1, 0.4, 1.5)

def test_between_n2p2():
    assert is_angle_between(1.5, 0.4, -1.1)

def test_between_n2p_f():
    assert ~is_angle_between(-1.1, -2.0, 2.1)

def test_between_n2p_wrap():
    assert is_angle_between(-60, 200, 180)

def test_between_n2p_wrap_f():
    assert ~is_angle_between(180, 170, -170)


# POSITIVE TO POSITIVE TESTS
def test_between_p2p():
    assert is_angle_between(1.2, 4.0, 40.1)

def test_between_p2p2():
    assert is_angle_between(40.1, 4.0, 1.2)

def test_between_p2p_f():
    assert ~is_angle_between(1.2, 0, 40.1)

def test_between_p2p_wrap():
    assert is_angle_between(405, 60, 450)

def test_between_p2p_wrap_f():
    assert ~is_angle_between(405, 90, 720)