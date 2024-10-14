from django.urls import reverse

from pytest_django.asserts import assertRedirects


def test_valid_login(manager_client, valid_login_form, client):
    """Test login with valid credentials"""
    response = client.get(reverse("accounts:login"))
    assert response.status_code == 200
    response = client.post(reverse("accounts:login"), data=valid_login_form)
    assert response.status_code == 302


def test_create_staff_by_manager(manager_client):
    response = manager_client.get(reverse("accounts:create_staff"))
    assert response.status_code == 200


def test_create_staff_by_guest(guest_client):
    response = guest_client.get(reverse("accounts:create_staff"))
    assert response.status_code == 403


def test_sign_up_view_get(client):
    """Test the sign-up view responds to GET requests"""
    response = client.get(reverse("accounts:signup"))
    assert response.status_code == 200
    assert "Sign Up" in str(response.content)


def test_sign_up_view_post_valid(client, valid_sign_up_form, guests_group):
    """Test sign-up view with valid data"""
    response = client.post(reverse("accounts:signup"), data=valid_sign_up_form)
    assert response.status_code == 302
    assert response.url == reverse("website:home")
    # assert response.url == reverse("website:make_reservation", args=(room.id,))


def test_sign_up_view_post_valid_with_room_to_book(
    client, valid_sign_up_form, guests_group, room
):
    """Test sign-up view with valid data"""
    response = client.post(reverse("accounts:signup"), data=valid_sign_up_form)
    assert response.status_code == 302
    assert response.url == reverse("website:home")
    # assert response.url == reverse("website:make_reservation", args=(room.id,))


def test_sign_up_view_post_invalid(client, missing_email):
    """Test sign-up view with invalid data"""
    response = client.post(reverse("accounts:signup"), data=missing_email)
    assert response.status_code == 200
    # assert "This field is required." in str(response.content)


def test_logout_view(guest_client):
    response = guest_client.post(reverse("accounts:logout"))
    assert response.status_code == 302
    assertRedirects(response, "/")
