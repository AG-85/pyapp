import pytest
from pytest_bdd import scenarios, given, when, then
import src.pyapp.app as app


scenarios("test_app.feature")

#notice context is a function but used as a parameter in given , when and then. So, function name is acting like a variable
@pytest.fixture
def context():
    return {}

@given("I have numbers 1, 4 and 5")
def given_set_one(context):
    context["numbers"] = [1, 4, 5]


@given("I have numbers 5, 3 and 2")
def given_set_two(context):
    context["numbers"] = [5, 3, 2]


@when("I add the numbers")
def when_add(context):
   context["result"] = app.addition(context["numbers"])
   assert context["result"] == 1 + 4 + 5


@when("I subtract the numbers")
def when_subtract(context):
    context["result"] = app.subtraction(context["numbers"])
    assert context["result"] == 5 - 3 - 2


@when("I multiply the numbers")
def when_multiply(context):
    context["result"] = app.multiplication(context["numbers"])
    assert context["result"] == 1 * 4 * 5


@when("I divide the numbers")
def when_divide(context):
    context["result"] = app.division(context["numbers"])
    assert context["result"] == 1 / 4 / 5

@then("the result should be 10")
def then_result_10(context):
    assert context["result"] == 10

@then("the result should be 0")
def then_result_0(context):
    assert context["result"] == 0

@then("the result should be 20")
def then_result_20(context):
    assert context["result"] == 20

@then("the result should be 0.05")
def then_result_005(context):
    assert round(context["result"], 2) == 0.05
