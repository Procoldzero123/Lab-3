import Lab2.bmi as bmi


def test_bmi_normal_weight():
    result=bmi.calculate_bmi(1.7,60)
    assert (result==0)

def test_bmi_over_weight():
    result=bmi.calculate_bmi(1.7,90)
    assert (result==1)
    
def test_bmi_under_weight():
    result=bmi.calculate_bmi(1.7,45)
    assert (result==-1)

