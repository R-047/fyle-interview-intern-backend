from tests.conftest import h_student_1, h_principal


def test_auth(client):
    """
    failure case: do not authenticate if X-Principal header not found
    """
    response = client.get(
        '/principal/assignments',
    )

    assert response.status_code == 401
    data = response.json
    assert data['error'] == "FyleError"
    assert data['message'] == "principal not found"

def test_student_accessing_teacher_principal_resources(client, h_student_1):
    """
    failure case: do let student access teachers api
    """

    response = client.get(
        '/teacher/assignments',
        headers=h_student_1
    )


    assert response.status_code == 403
    data = response.json
    assert data['error'] == "FyleError"
    assert data['message'] == "requester should be a teacher"


    response = client.get(
        'principal/assignments',
        headers=h_student_1
    )


    assert response.status_code == 403
    data = response.json
    assert data['error'] == "FyleError"
    assert data['message'] == "requester should be a principal"



def test_principal_accessing_student_teacher_resources(client, h_principal):
    """
    failure case: do let student access teachers api
    """

    response = client.get(
        '/student/assignments',
        headers=h_principal
    )


    assert response.status_code == 403
    data = response.json
    assert data['error'] == "FyleError"
    assert data['message'] == "requester should be a student"


    response = client.get(
        'teacher/assignments',
        headers=h_principal
    )


    assert response.status_code == 403
    data = response.json
    assert data['error'] == "FyleError"
    assert data['message'] == "requester should be a teacher"







