import pytest


@pytest.mark.database
def test_database_connection(database):
    """The test is created to execute the test_connection method.
    It selects sqlite_version and represents the version of the db in the terminal."""
    database.test_connection()


@pytest.mark.database
def test_check_all_users(database):
    """To execute the object's get_all_users method.
    The result should be output to the terminal"""
    users = database.get_all_users()

    print(users)


@pytest.mark.database
def test_check_user_sergii(database):
    """To execute the object method of get_user_address_by_name with name 'Sergii'.
    The returned data should match the data in the test."""
    user = database.get_user_address_by_name('Sergii')

    assert user[0] == ('Maydan Nezalezhnosti 1', 'Kyiv', '3127', 'Ukraine')


@pytest.mark.database
def test_product_qnt_update(database):
    """To execute the method of update_product_qnt_by_id
    with the specific values of product_id and qnt.
    To check that after updating the data, the qnt of the product(1) is 25"""
    database.update_product_qnt_by_id(1, 25)
    water_qnt = database.select_product_qnt_by_id(1)

    assert water_qnt[0][0] == 25


@pytest.mark.database
def test_product_insert(database):
    """To execute the method of insert_product object.
    To verify that the data has been updated
    and the product qnt with number 4 is equal to 30"""
    database.insert_product(4, 'печиво', 'солодке', 30)
    product_qnt = database.select_product_qnt_by_id(4)
    assert product_qnt[0][0] == 30


@pytest.mark.database
def test_product_delete(database):
    """The test creates a product (insert_product method) with the specified values.
    The product is delited (delete_product_by_id method) from the products table.
    To check that the number of matching rows is 0."""
    database.insert_product(99, 'тестові', 'дані', 999)
    database.delete_product_by_id(99)
    qnt = database.select_product_qnt_by_id(99)

    assert len(qnt) == 0


@pytest.mark.database
def test_detailed_orders(database):
    """The test outputs the result of get_detailed_orders method.
    To check that the number of results is 1.
    To check that the returned data corresponds to the specified."""
    orders = database.get_detailed_orders()
    print("Замовлення", orders)
    # Check quantity of orders equel to 1
    assert len(orders) == 1

    # Check structure of data
    assert orders[0] == (1, 'Sergii', 'солодка вода', 'з цукром')
