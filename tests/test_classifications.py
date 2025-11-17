from textwrap import dedent

import pytest

from src.PyM.MExpression import MExpression


@pytest.fixture(scope="module")
def function_one_expression() -> str:
    return dedent(
        """
        (AddTwoNumbers as number, AnotherNumber as number) as number =>
    AddTwoNumbers + AnotherNumber
        """
    ).strip()


@pytest.fixture(scope="module")
def function_two_expression() -> str:
    return dedent(
        """
        shared Function2 = let
            Function2 = (AddTwoNumbers as number, AnotherNumber as number) as number =>
                AddTwoNumbers + AnotherNumber
        in
            Function2
        """
    ).strip()


@pytest.fixture(scope="module")
def function_three_expression() -> str:
    return dedent(
        """
        RevenueCalculator = (Sales as table, ExchangeRate as number) as table =>
            Table.AddColumn(
                Sales,
                "RevenueLocal",
                each [Amount] * ExchangeRate,
                type number
            )
        """
    ).strip()


@pytest.fixture(scope="module")
def function_four_expression() -> str:
    return dedent(
        """
        let
            Function4 = (items as list) as list =>
                let
                    filtered = List.Select(items, each _ <> null),
                    sorted = List.Sort(filtered)
                in
                    sorted
        in
            Function4
        """
    ).strip()


@pytest.fixture(scope="module")
def parameter_one_expression() -> str:
    return (
        '"sbb-eap.snowflakecomputing.com" meta '
        "[IsParameterQuery=true, Type=\"Text\", IsParameterQueryRequired=true]"
    )


@pytest.fixture(scope="module")
def parameter_two_expression() -> str:
    return (
        '"ABC" meta [IsParameterQuery=true, Type="Text", IsParameterQueryRequired=true]'
    )


@pytest.fixture(scope="module")
def date_parameter_expression() -> str:
    return (
        '#date(2024, 12, 31) meta '
        "[IsParameterQuery=true, Type=\"Date\", Description=\"FiscalYearEnd\"]"
    )


@pytest.fixture(scope="module")
def list_parameter_expression() -> str:
    return dedent(
        """
        { "US", "CA", "MX" } meta [
            IsParameterQuery = true,
            Type = "List",
            IsParameterQueryRequired = false
        ]
        """
    ).strip()


@pytest.fixture(scope="module")
def query_expression() -> str:
    return dedent(
        """
        let
            Source = Excel.CurrentWorkbook(){[Name="SalesTable"]}[Content],
            #"Changed Type" = Table.TransformColumnTypes(Source, {{"Amount", type number}})
        in
            #"Changed Type"
        """
    ).strip()


@pytest.fixture(scope="module")
def nested_query_expression() -> str:
    return dedent(
        """
        let
            Source = Sql.Database("Server01", "Warehouse"),
            Orders = Source{[Schema="dbo", Item="Orders"]}[Data],
            Filtered = Table.SelectRows(Orders, each [Status] = "Closed" and [Amount] > 1000),
            Grouped = Table.Group(
                Filtered,
                {"Region"},
                {{"Total", each List.Sum([Amount]), type number}}
            ),
            Result = Table.Sort(Grouped, {{"Total", Order.Descending}})
        in
            Result
        """
    ).strip()


@pytest.fixture(scope="module")
def commented_query_expression() -> str:
    return dedent(
        """
        shared CustomerAging = let
            /* Latest snapshot */
            Source = Csv.Document(Web.Contents("https://contoso.com/aging.csv"), [Delimiter=",", Encoding=65001]),
            Promoted = Table.PromoteHeaders(Source, [PromoteAllScalars=true]),
            Typed = Table.TransformColumnTypes(Promoted,
                {{"DueDate", type date}, {"Balance", type number}, {"Customer", type text}}
            ),
            WithBucket = Table.AddColumn(Typed, "Bucket", each if [Balance] > 10000 then "High" else "Standard"),
            Output = Table.SelectColumns(WithBucket, {"Customer", "Balance", "Bucket"})
        in
            Output
        """
    ).strip()


def test_function_one_is_classified_as_function(function_one_expression: str) -> None:
    expression = MExpression(function_one_expression)

    assert expression.is_function
    assert not expression.is_parameter
    assert not expression.is_query


def test_function_two_is_classified_as_function(function_two_expression: str) -> None:
    expression = MExpression(function_two_expression)

    assert expression.is_function
    assert not expression.is_parameter
    assert not expression.is_query


def test_function_three_is_classified_as_function(function_three_expression: str) -> None:
    expression = MExpression(function_three_expression)

    assert expression.is_function
    assert not expression.is_parameter
    assert not expression.is_query


def test_function_four_is_classified_as_function(function_four_expression: str) -> None:
    expression = MExpression(function_four_expression)

    assert expression.is_function
    assert not expression.is_parameter
    assert not expression.is_query


def test_parameter_one_is_classified_as_parameter(parameter_one_expression: str) -> None:
    expression = MExpression(parameter_one_expression)

    assert expression.is_parameter
    assert not expression.is_function
    assert not expression.is_query


def test_parameter_two_is_classified_as_parameter(parameter_two_expression: str) -> None:
    expression = MExpression(parameter_two_expression)

    assert expression.is_parameter
    assert not expression.is_function
    assert not expression.is_query


def test_date_parameter_is_classified_as_parameter(date_parameter_expression: str) -> None:
    expression = MExpression(date_parameter_expression)

    assert expression.is_parameter
    assert not expression.is_function
    assert not expression.is_query


def test_list_parameter_is_classified_as_parameter(list_parameter_expression: str) -> None:
    expression = MExpression(list_parameter_expression)

    assert expression.is_parameter
    assert not expression.is_function
    assert not expression.is_query


def test_query_is_classified_as_query(query_expression: str) -> None:
    expression = MExpression(query_expression)

    assert expression.is_query
    assert not expression.is_function
    assert not expression.is_parameter


def test_nested_query_is_classified_as_query(nested_query_expression: str) -> None:
    expression = MExpression(nested_query_expression)

    assert expression.is_query
    assert not expression.is_function
    assert not expression.is_parameter


def test_commented_query_is_classified_as_query(commented_query_expression: str) -> None:
    expression = MExpression(commented_query_expression)

    assert expression.is_query
    assert not expression.is_function
    assert not expression.is_parameter
