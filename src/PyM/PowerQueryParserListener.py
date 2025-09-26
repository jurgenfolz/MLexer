# Generated from src/PyM/PowerQueryParser.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .PowerQueryParser import PowerQueryParser
else:
    from PowerQueryParser import PowerQueryParser

# This class defines a complete listener for a parse tree produced by PowerQueryParser.
class PowerQueryParserListener(ParseTreeListener):

    # Enter a parse tree produced by PowerQueryParser#document.
    def enterDocument(self, ctx:PowerQueryParser.DocumentContext):
        pass

    # Exit a parse tree produced by PowerQueryParser#document.
    def exitDocument(self, ctx:PowerQueryParser.DocumentContext):
        pass


    # Enter a parse tree produced by PowerQueryParser#section_document.
    def enterSection_document(self, ctx:PowerQueryParser.Section_documentContext):
        pass

    # Exit a parse tree produced by PowerQueryParser#section_document.
    def exitSection_document(self, ctx:PowerQueryParser.Section_documentContext):
        pass


    # Enter a parse tree produced by PowerQueryParser#section.
    def enterSection(self, ctx:PowerQueryParser.SectionContext):
        pass

    # Exit a parse tree produced by PowerQueryParser#section.
    def exitSection(self, ctx:PowerQueryParser.SectionContext):
        pass


    # Enter a parse tree produced by PowerQueryParser#section_name.
    def enterSection_name(self, ctx:PowerQueryParser.Section_nameContext):
        pass

    # Exit a parse tree produced by PowerQueryParser#section_name.
    def exitSection_name(self, ctx:PowerQueryParser.Section_nameContext):
        pass


    # Enter a parse tree produced by PowerQueryParser#section_members.
    def enterSection_members(self, ctx:PowerQueryParser.Section_membersContext):
        pass

    # Exit a parse tree produced by PowerQueryParser#section_members.
    def exitSection_members(self, ctx:PowerQueryParser.Section_membersContext):
        pass


    # Enter a parse tree produced by PowerQueryParser#section_member.
    def enterSection_member(self, ctx:PowerQueryParser.Section_memberContext):
        pass

    # Exit a parse tree produced by PowerQueryParser#section_member.
    def exitSection_member(self, ctx:PowerQueryParser.Section_memberContext):
        pass


    # Enter a parse tree produced by PowerQueryParser#section_member_name.
    def enterSection_member_name(self, ctx:PowerQueryParser.Section_member_nameContext):
        pass

    # Exit a parse tree produced by PowerQueryParser#section_member_name.
    def exitSection_member_name(self, ctx:PowerQueryParser.Section_member_nameContext):
        pass


    # Enter a parse tree produced by PowerQueryParser#expression_document.
    def enterExpression_document(self, ctx:PowerQueryParser.Expression_documentContext):
        pass

    # Exit a parse tree produced by PowerQueryParser#expression_document.
    def exitExpression_document(self, ctx:PowerQueryParser.Expression_documentContext):
        pass


    # Enter a parse tree produced by PowerQueryParser#expression.
    def enterExpression(self, ctx:PowerQueryParser.ExpressionContext):
        pass

    # Exit a parse tree produced by PowerQueryParser#expression.
    def exitExpression(self, ctx:PowerQueryParser.ExpressionContext):
        pass


    # Enter a parse tree produced by PowerQueryParser#logical_or_expression.
    def enterLogical_or_expression(self, ctx:PowerQueryParser.Logical_or_expressionContext):
        pass

    # Exit a parse tree produced by PowerQueryParser#logical_or_expression.
    def exitLogical_or_expression(self, ctx:PowerQueryParser.Logical_or_expressionContext):
        pass


    # Enter a parse tree produced by PowerQueryParser#logical_and_expression.
    def enterLogical_and_expression(self, ctx:PowerQueryParser.Logical_and_expressionContext):
        pass

    # Exit a parse tree produced by PowerQueryParser#logical_and_expression.
    def exitLogical_and_expression(self, ctx:PowerQueryParser.Logical_and_expressionContext):
        pass


    # Enter a parse tree produced by PowerQueryParser#is_expression.
    def enterIs_expression(self, ctx:PowerQueryParser.Is_expressionContext):
        pass

    # Exit a parse tree produced by PowerQueryParser#is_expression.
    def exitIs_expression(self, ctx:PowerQueryParser.Is_expressionContext):
        pass


    # Enter a parse tree produced by PowerQueryParser#nullable_primitive_type.
    def enterNullable_primitive_type(self, ctx:PowerQueryParser.Nullable_primitive_typeContext):
        pass

    # Exit a parse tree produced by PowerQueryParser#nullable_primitive_type.
    def exitNullable_primitive_type(self, ctx:PowerQueryParser.Nullable_primitive_typeContext):
        pass


    # Enter a parse tree produced by PowerQueryParser#as_expression.
    def enterAs_expression(self, ctx:PowerQueryParser.As_expressionContext):
        pass

    # Exit a parse tree produced by PowerQueryParser#as_expression.
    def exitAs_expression(self, ctx:PowerQueryParser.As_expressionContext):
        pass


    # Enter a parse tree produced by PowerQueryParser#equality_expression.
    def enterEquality_expression(self, ctx:PowerQueryParser.Equality_expressionContext):
        pass

    # Exit a parse tree produced by PowerQueryParser#equality_expression.
    def exitEquality_expression(self, ctx:PowerQueryParser.Equality_expressionContext):
        pass


    # Enter a parse tree produced by PowerQueryParser#relational_expression.
    def enterRelational_expression(self, ctx:PowerQueryParser.Relational_expressionContext):
        pass

    # Exit a parse tree produced by PowerQueryParser#relational_expression.
    def exitRelational_expression(self, ctx:PowerQueryParser.Relational_expressionContext):
        pass


    # Enter a parse tree produced by PowerQueryParser#additive_expression.
    def enterAdditive_expression(self, ctx:PowerQueryParser.Additive_expressionContext):
        pass

    # Exit a parse tree produced by PowerQueryParser#additive_expression.
    def exitAdditive_expression(self, ctx:PowerQueryParser.Additive_expressionContext):
        pass


    # Enter a parse tree produced by PowerQueryParser#multiplicative_expression.
    def enterMultiplicative_expression(self, ctx:PowerQueryParser.Multiplicative_expressionContext):
        pass

    # Exit a parse tree produced by PowerQueryParser#multiplicative_expression.
    def exitMultiplicative_expression(self, ctx:PowerQueryParser.Multiplicative_expressionContext):
        pass


    # Enter a parse tree produced by PowerQueryParser#metadata_expression.
    def enterMetadata_expression(self, ctx:PowerQueryParser.Metadata_expressionContext):
        pass

    # Exit a parse tree produced by PowerQueryParser#metadata_expression.
    def exitMetadata_expression(self, ctx:PowerQueryParser.Metadata_expressionContext):
        pass


    # Enter a parse tree produced by PowerQueryParser#unary_expression.
    def enterUnary_expression(self, ctx:PowerQueryParser.Unary_expressionContext):
        pass

    # Exit a parse tree produced by PowerQueryParser#unary_expression.
    def exitUnary_expression(self, ctx:PowerQueryParser.Unary_expressionContext):
        pass


    # Enter a parse tree produced by PowerQueryParser#primary_expression.
    def enterPrimary_expression(self, ctx:PowerQueryParser.Primary_expressionContext):
        pass

    # Exit a parse tree produced by PowerQueryParser#primary_expression.
    def exitPrimary_expression(self, ctx:PowerQueryParser.Primary_expressionContext):
        pass


    # Enter a parse tree produced by PowerQueryParser#atom.
    def enterAtom(self, ctx:PowerQueryParser.AtomContext):
        pass

    # Exit a parse tree produced by PowerQueryParser#atom.
    def exitAtom(self, ctx:PowerQueryParser.AtomContext):
        pass


    # Enter a parse tree produced by PowerQueryParser#literal_expression.
    def enterLiteral_expression(self, ctx:PowerQueryParser.Literal_expressionContext):
        pass

    # Exit a parse tree produced by PowerQueryParser#literal_expression.
    def exitLiteral_expression(self, ctx:PowerQueryParser.Literal_expressionContext):
        pass


    # Enter a parse tree produced by PowerQueryParser#identifier_expression.
    def enterIdentifier_expression(self, ctx:PowerQueryParser.Identifier_expressionContext):
        pass

    # Exit a parse tree produced by PowerQueryParser#identifier_expression.
    def exitIdentifier_expression(self, ctx:PowerQueryParser.Identifier_expressionContext):
        pass


    # Enter a parse tree produced by PowerQueryParser#identifier_reference.
    def enterIdentifier_reference(self, ctx:PowerQueryParser.Identifier_referenceContext):
        pass

    # Exit a parse tree produced by PowerQueryParser#identifier_reference.
    def exitIdentifier_reference(self, ctx:PowerQueryParser.Identifier_referenceContext):
        pass


    # Enter a parse tree produced by PowerQueryParser#exclusive_identifier_reference.
    def enterExclusive_identifier_reference(self, ctx:PowerQueryParser.Exclusive_identifier_referenceContext):
        pass

    # Exit a parse tree produced by PowerQueryParser#exclusive_identifier_reference.
    def exitExclusive_identifier_reference(self, ctx:PowerQueryParser.Exclusive_identifier_referenceContext):
        pass


    # Enter a parse tree produced by PowerQueryParser#inclusive_identifier_reference.
    def enterInclusive_identifier_reference(self, ctx:PowerQueryParser.Inclusive_identifier_referenceContext):
        pass

    # Exit a parse tree produced by PowerQueryParser#inclusive_identifier_reference.
    def exitInclusive_identifier_reference(self, ctx:PowerQueryParser.Inclusive_identifier_referenceContext):
        pass


    # Enter a parse tree produced by PowerQueryParser#section_access_expression.
    def enterSection_access_expression(self, ctx:PowerQueryParser.Section_access_expressionContext):
        pass

    # Exit a parse tree produced by PowerQueryParser#section_access_expression.
    def exitSection_access_expression(self, ctx:PowerQueryParser.Section_access_expressionContext):
        pass


    # Enter a parse tree produced by PowerQueryParser#parenthesized_expression.
    def enterParenthesized_expression(self, ctx:PowerQueryParser.Parenthesized_expressionContext):
        pass

    # Exit a parse tree produced by PowerQueryParser#parenthesized_expression.
    def exitParenthesized_expression(self, ctx:PowerQueryParser.Parenthesized_expressionContext):
        pass


    # Enter a parse tree produced by PowerQueryParser#not_implemented_expression.
    def enterNot_implemented_expression(self, ctx:PowerQueryParser.Not_implemented_expressionContext):
        pass

    # Exit a parse tree produced by PowerQueryParser#not_implemented_expression.
    def exitNot_implemented_expression(self, ctx:PowerQueryParser.Not_implemented_expressionContext):
        pass


    # Enter a parse tree produced by PowerQueryParser#argument_list.
    def enterArgument_list(self, ctx:PowerQueryParser.Argument_listContext):
        pass

    # Exit a parse tree produced by PowerQueryParser#argument_list.
    def exitArgument_list(self, ctx:PowerQueryParser.Argument_listContext):
        pass


    # Enter a parse tree produced by PowerQueryParser#list_expression.
    def enterList_expression(self, ctx:PowerQueryParser.List_expressionContext):
        pass

    # Exit a parse tree produced by PowerQueryParser#list_expression.
    def exitList_expression(self, ctx:PowerQueryParser.List_expressionContext):
        pass


    # Enter a parse tree produced by PowerQueryParser#item_list.
    def enterItem_list(self, ctx:PowerQueryParser.Item_listContext):
        pass

    # Exit a parse tree produced by PowerQueryParser#item_list.
    def exitItem_list(self, ctx:PowerQueryParser.Item_listContext):
        pass


    # Enter a parse tree produced by PowerQueryParser#item.
    def enterItem(self, ctx:PowerQueryParser.ItemContext):
        pass

    # Exit a parse tree produced by PowerQueryParser#item.
    def exitItem(self, ctx:PowerQueryParser.ItemContext):
        pass


    # Enter a parse tree produced by PowerQueryParser#record_expression.
    def enterRecord_expression(self, ctx:PowerQueryParser.Record_expressionContext):
        pass

    # Exit a parse tree produced by PowerQueryParser#record_expression.
    def exitRecord_expression(self, ctx:PowerQueryParser.Record_expressionContext):
        pass


    # Enter a parse tree produced by PowerQueryParser#field_list.
    def enterField_list(self, ctx:PowerQueryParser.Field_listContext):
        pass

    # Exit a parse tree produced by PowerQueryParser#field_list.
    def exitField_list(self, ctx:PowerQueryParser.Field_listContext):
        pass


    # Enter a parse tree produced by PowerQueryParser#field.
    def enterField(self, ctx:PowerQueryParser.FieldContext):
        pass

    # Exit a parse tree produced by PowerQueryParser#field.
    def exitField(self, ctx:PowerQueryParser.FieldContext):
        pass


    # Enter a parse tree produced by PowerQueryParser#field_name.
    def enterField_name(self, ctx:PowerQueryParser.Field_nameContext):
        pass

    # Exit a parse tree produced by PowerQueryParser#field_name.
    def exitField_name(self, ctx:PowerQueryParser.Field_nameContext):
        pass


    # Enter a parse tree produced by PowerQueryParser#item_selector.
    def enterItem_selector(self, ctx:PowerQueryParser.Item_selectorContext):
        pass

    # Exit a parse tree produced by PowerQueryParser#item_selector.
    def exitItem_selector(self, ctx:PowerQueryParser.Item_selectorContext):
        pass


    # Enter a parse tree produced by PowerQueryParser#field_selector.
    def enterField_selector(self, ctx:PowerQueryParser.Field_selectorContext):
        pass

    # Exit a parse tree produced by PowerQueryParser#field_selector.
    def exitField_selector(self, ctx:PowerQueryParser.Field_selectorContext):
        pass


    # Enter a parse tree produced by PowerQueryParser#required_field_selector.
    def enterRequired_field_selector(self, ctx:PowerQueryParser.Required_field_selectorContext):
        pass

    # Exit a parse tree produced by PowerQueryParser#required_field_selector.
    def exitRequired_field_selector(self, ctx:PowerQueryParser.Required_field_selectorContext):
        pass


    # Enter a parse tree produced by PowerQueryParser#optional_field_selector.
    def enterOptional_field_selector(self, ctx:PowerQueryParser.Optional_field_selectorContext):
        pass

    # Exit a parse tree produced by PowerQueryParser#optional_field_selector.
    def exitOptional_field_selector(self, ctx:PowerQueryParser.Optional_field_selectorContext):
        pass


    # Enter a parse tree produced by PowerQueryParser#implicit_target_field_selection.
    def enterImplicit_target_field_selection(self, ctx:PowerQueryParser.Implicit_target_field_selectionContext):
        pass

    # Exit a parse tree produced by PowerQueryParser#implicit_target_field_selection.
    def exitImplicit_target_field_selection(self, ctx:PowerQueryParser.Implicit_target_field_selectionContext):
        pass


    # Enter a parse tree produced by PowerQueryParser#required_projection.
    def enterRequired_projection(self, ctx:PowerQueryParser.Required_projectionContext):
        pass

    # Exit a parse tree produced by PowerQueryParser#required_projection.
    def exitRequired_projection(self, ctx:PowerQueryParser.Required_projectionContext):
        pass


    # Enter a parse tree produced by PowerQueryParser#optional_projection.
    def enterOptional_projection(self, ctx:PowerQueryParser.Optional_projectionContext):
        pass

    # Exit a parse tree produced by PowerQueryParser#optional_projection.
    def exitOptional_projection(self, ctx:PowerQueryParser.Optional_projectionContext):
        pass


    # Enter a parse tree produced by PowerQueryParser#required_selector_list.
    def enterRequired_selector_list(self, ctx:PowerQueryParser.Required_selector_listContext):
        pass

    # Exit a parse tree produced by PowerQueryParser#required_selector_list.
    def exitRequired_selector_list(self, ctx:PowerQueryParser.Required_selector_listContext):
        pass


    # Enter a parse tree produced by PowerQueryParser#implicit_target_projection.
    def enterImplicit_target_projection(self, ctx:PowerQueryParser.Implicit_target_projectionContext):
        pass

    # Exit a parse tree produced by PowerQueryParser#implicit_target_projection.
    def exitImplicit_target_projection(self, ctx:PowerQueryParser.Implicit_target_projectionContext):
        pass


    # Enter a parse tree produced by PowerQueryParser#function_expression.
    def enterFunction_expression(self, ctx:PowerQueryParser.Function_expressionContext):
        pass

    # Exit a parse tree produced by PowerQueryParser#function_expression.
    def exitFunction_expression(self, ctx:PowerQueryParser.Function_expressionContext):
        pass


    # Enter a parse tree produced by PowerQueryParser#function_body.
    def enterFunction_body(self, ctx:PowerQueryParser.Function_bodyContext):
        pass

    # Exit a parse tree produced by PowerQueryParser#function_body.
    def exitFunction_body(self, ctx:PowerQueryParser.Function_bodyContext):
        pass


    # Enter a parse tree produced by PowerQueryParser#parameter_list.
    def enterParameter_list(self, ctx:PowerQueryParser.Parameter_listContext):
        pass

    # Exit a parse tree produced by PowerQueryParser#parameter_list.
    def exitParameter_list(self, ctx:PowerQueryParser.Parameter_listContext):
        pass


    # Enter a parse tree produced by PowerQueryParser#fixed_parameter_list.
    def enterFixed_parameter_list(self, ctx:PowerQueryParser.Fixed_parameter_listContext):
        pass

    # Exit a parse tree produced by PowerQueryParser#fixed_parameter_list.
    def exitFixed_parameter_list(self, ctx:PowerQueryParser.Fixed_parameter_listContext):
        pass


    # Enter a parse tree produced by PowerQueryParser#parameter.
    def enterParameter(self, ctx:PowerQueryParser.ParameterContext):
        pass

    # Exit a parse tree produced by PowerQueryParser#parameter.
    def exitParameter(self, ctx:PowerQueryParser.ParameterContext):
        pass


    # Enter a parse tree produced by PowerQueryParser#parameter_name.
    def enterParameter_name(self, ctx:PowerQueryParser.Parameter_nameContext):
        pass

    # Exit a parse tree produced by PowerQueryParser#parameter_name.
    def exitParameter_name(self, ctx:PowerQueryParser.Parameter_nameContext):
        pass


    # Enter a parse tree produced by PowerQueryParser#parameter_type.
    def enterParameter_type(self, ctx:PowerQueryParser.Parameter_typeContext):
        pass

    # Exit a parse tree produced by PowerQueryParser#parameter_type.
    def exitParameter_type(self, ctx:PowerQueryParser.Parameter_typeContext):
        pass


    # Enter a parse tree produced by PowerQueryParser#return_type.
    def enterReturn_type(self, ctx:PowerQueryParser.Return_typeContext):
        pass

    # Exit a parse tree produced by PowerQueryParser#return_type.
    def exitReturn_type(self, ctx:PowerQueryParser.Return_typeContext):
        pass


    # Enter a parse tree produced by PowerQueryParser#assertion.
    def enterAssertion(self, ctx:PowerQueryParser.AssertionContext):
        pass

    # Exit a parse tree produced by PowerQueryParser#assertion.
    def exitAssertion(self, ctx:PowerQueryParser.AssertionContext):
        pass


    # Enter a parse tree produced by PowerQueryParser#optional_parameter_list.
    def enterOptional_parameter_list(self, ctx:PowerQueryParser.Optional_parameter_listContext):
        pass

    # Exit a parse tree produced by PowerQueryParser#optional_parameter_list.
    def exitOptional_parameter_list(self, ctx:PowerQueryParser.Optional_parameter_listContext):
        pass


    # Enter a parse tree produced by PowerQueryParser#optional_parameter.
    def enterOptional_parameter(self, ctx:PowerQueryParser.Optional_parameterContext):
        pass

    # Exit a parse tree produced by PowerQueryParser#optional_parameter.
    def exitOptional_parameter(self, ctx:PowerQueryParser.Optional_parameterContext):
        pass


    # Enter a parse tree produced by PowerQueryParser#each_expression.
    def enterEach_expression(self, ctx:PowerQueryParser.Each_expressionContext):
        pass

    # Exit a parse tree produced by PowerQueryParser#each_expression.
    def exitEach_expression(self, ctx:PowerQueryParser.Each_expressionContext):
        pass


    # Enter a parse tree produced by PowerQueryParser#each_expression_body.
    def enterEach_expression_body(self, ctx:PowerQueryParser.Each_expression_bodyContext):
        pass

    # Exit a parse tree produced by PowerQueryParser#each_expression_body.
    def exitEach_expression_body(self, ctx:PowerQueryParser.Each_expression_bodyContext):
        pass


    # Enter a parse tree produced by PowerQueryParser#let_expression.
    def enterLet_expression(self, ctx:PowerQueryParser.Let_expressionContext):
        pass

    # Exit a parse tree produced by PowerQueryParser#let_expression.
    def exitLet_expression(self, ctx:PowerQueryParser.Let_expressionContext):
        pass


    # Enter a parse tree produced by PowerQueryParser#variable_list.
    def enterVariable_list(self, ctx:PowerQueryParser.Variable_listContext):
        pass

    # Exit a parse tree produced by PowerQueryParser#variable_list.
    def exitVariable_list(self, ctx:PowerQueryParser.Variable_listContext):
        pass


    # Enter a parse tree produced by PowerQueryParser#variable.
    def enterVariable(self, ctx:PowerQueryParser.VariableContext):
        pass

    # Exit a parse tree produced by PowerQueryParser#variable.
    def exitVariable(self, ctx:PowerQueryParser.VariableContext):
        pass


    # Enter a parse tree produced by PowerQueryParser#variable_name.
    def enterVariable_name(self, ctx:PowerQueryParser.Variable_nameContext):
        pass

    # Exit a parse tree produced by PowerQueryParser#variable_name.
    def exitVariable_name(self, ctx:PowerQueryParser.Variable_nameContext):
        pass


    # Enter a parse tree produced by PowerQueryParser#if_expression.
    def enterIf_expression(self, ctx:PowerQueryParser.If_expressionContext):
        pass

    # Exit a parse tree produced by PowerQueryParser#if_expression.
    def exitIf_expression(self, ctx:PowerQueryParser.If_expressionContext):
        pass


    # Enter a parse tree produced by PowerQueryParser#if_condition.
    def enterIf_condition(self, ctx:PowerQueryParser.If_conditionContext):
        pass

    # Exit a parse tree produced by PowerQueryParser#if_condition.
    def exitIf_condition(self, ctx:PowerQueryParser.If_conditionContext):
        pass


    # Enter a parse tree produced by PowerQueryParser#true_expression.
    def enterTrue_expression(self, ctx:PowerQueryParser.True_expressionContext):
        pass

    # Exit a parse tree produced by PowerQueryParser#true_expression.
    def exitTrue_expression(self, ctx:PowerQueryParser.True_expressionContext):
        pass


    # Enter a parse tree produced by PowerQueryParser#false_expression.
    def enterFalse_expression(self, ctx:PowerQueryParser.False_expressionContext):
        pass

    # Exit a parse tree produced by PowerQueryParser#false_expression.
    def exitFalse_expression(self, ctx:PowerQueryParser.False_expressionContext):
        pass


    # Enter a parse tree produced by PowerQueryParser#type_expression.
    def enterType_expression(self, ctx:PowerQueryParser.Type_expressionContext):
        pass

    # Exit a parse tree produced by PowerQueryParser#type_expression.
    def exitType_expression(self, ctx:PowerQueryParser.Type_expressionContext):
        pass


    # Enter a parse tree produced by PowerQueryParser#type_expr.
    def enterType_expr(self, ctx:PowerQueryParser.Type_exprContext):
        pass

    # Exit a parse tree produced by PowerQueryParser#type_expr.
    def exitType_expr(self, ctx:PowerQueryParser.Type_exprContext):
        pass


    # Enter a parse tree produced by PowerQueryParser#primary_type.
    def enterPrimary_type(self, ctx:PowerQueryParser.Primary_typeContext):
        pass

    # Exit a parse tree produced by PowerQueryParser#primary_type.
    def exitPrimary_type(self, ctx:PowerQueryParser.Primary_typeContext):
        pass


    # Enter a parse tree produced by PowerQueryParser#primitive_type.
    def enterPrimitive_type(self, ctx:PowerQueryParser.Primitive_typeContext):
        pass

    # Exit a parse tree produced by PowerQueryParser#primitive_type.
    def exitPrimitive_type(self, ctx:PowerQueryParser.Primitive_typeContext):
        pass


    # Enter a parse tree produced by PowerQueryParser#record_type.
    def enterRecord_type(self, ctx:PowerQueryParser.Record_typeContext):
        pass

    # Exit a parse tree produced by PowerQueryParser#record_type.
    def exitRecord_type(self, ctx:PowerQueryParser.Record_typeContext):
        pass


    # Enter a parse tree produced by PowerQueryParser#field_specification_list.
    def enterField_specification_list(self, ctx:PowerQueryParser.Field_specification_listContext):
        pass

    # Exit a parse tree produced by PowerQueryParser#field_specification_list.
    def exitField_specification_list(self, ctx:PowerQueryParser.Field_specification_listContext):
        pass


    # Enter a parse tree produced by PowerQueryParser#field_specification.
    def enterField_specification(self, ctx:PowerQueryParser.Field_specificationContext):
        pass

    # Exit a parse tree produced by PowerQueryParser#field_specification.
    def exitField_specification(self, ctx:PowerQueryParser.Field_specificationContext):
        pass


    # Enter a parse tree produced by PowerQueryParser#field_type_specification.
    def enterField_type_specification(self, ctx:PowerQueryParser.Field_type_specificationContext):
        pass

    # Exit a parse tree produced by PowerQueryParser#field_type_specification.
    def exitField_type_specification(self, ctx:PowerQueryParser.Field_type_specificationContext):
        pass


    # Enter a parse tree produced by PowerQueryParser#field_type.
    def enterField_type(self, ctx:PowerQueryParser.Field_typeContext):
        pass

    # Exit a parse tree produced by PowerQueryParser#field_type.
    def exitField_type(self, ctx:PowerQueryParser.Field_typeContext):
        pass


    # Enter a parse tree produced by PowerQueryParser#open_record_marker.
    def enterOpen_record_marker(self, ctx:PowerQueryParser.Open_record_markerContext):
        pass

    # Exit a parse tree produced by PowerQueryParser#open_record_marker.
    def exitOpen_record_marker(self, ctx:PowerQueryParser.Open_record_markerContext):
        pass


    # Enter a parse tree produced by PowerQueryParser#list_type.
    def enterList_type(self, ctx:PowerQueryParser.List_typeContext):
        pass

    # Exit a parse tree produced by PowerQueryParser#list_type.
    def exitList_type(self, ctx:PowerQueryParser.List_typeContext):
        pass


    # Enter a parse tree produced by PowerQueryParser#item_type.
    def enterItem_type(self, ctx:PowerQueryParser.Item_typeContext):
        pass

    # Exit a parse tree produced by PowerQueryParser#item_type.
    def exitItem_type(self, ctx:PowerQueryParser.Item_typeContext):
        pass


    # Enter a parse tree produced by PowerQueryParser#function_type.
    def enterFunction_type(self, ctx:PowerQueryParser.Function_typeContext):
        pass

    # Exit a parse tree produced by PowerQueryParser#function_type.
    def exitFunction_type(self, ctx:PowerQueryParser.Function_typeContext):
        pass


    # Enter a parse tree produced by PowerQueryParser#parameter_specification_list.
    def enterParameter_specification_list(self, ctx:PowerQueryParser.Parameter_specification_listContext):
        pass

    # Exit a parse tree produced by PowerQueryParser#parameter_specification_list.
    def exitParameter_specification_list(self, ctx:PowerQueryParser.Parameter_specification_listContext):
        pass


    # Enter a parse tree produced by PowerQueryParser#required_parameter_specification_list.
    def enterRequired_parameter_specification_list(self, ctx:PowerQueryParser.Required_parameter_specification_listContext):
        pass

    # Exit a parse tree produced by PowerQueryParser#required_parameter_specification_list.
    def exitRequired_parameter_specification_list(self, ctx:PowerQueryParser.Required_parameter_specification_listContext):
        pass


    # Enter a parse tree produced by PowerQueryParser#required_parameter_specification.
    def enterRequired_parameter_specification(self, ctx:PowerQueryParser.Required_parameter_specificationContext):
        pass

    # Exit a parse tree produced by PowerQueryParser#required_parameter_specification.
    def exitRequired_parameter_specification(self, ctx:PowerQueryParser.Required_parameter_specificationContext):
        pass


    # Enter a parse tree produced by PowerQueryParser#optional_parameter_specification_list.
    def enterOptional_parameter_specification_list(self, ctx:PowerQueryParser.Optional_parameter_specification_listContext):
        pass

    # Exit a parse tree produced by PowerQueryParser#optional_parameter_specification_list.
    def exitOptional_parameter_specification_list(self, ctx:PowerQueryParser.Optional_parameter_specification_listContext):
        pass


    # Enter a parse tree produced by PowerQueryParser#optional_parameter_specification.
    def enterOptional_parameter_specification(self, ctx:PowerQueryParser.Optional_parameter_specificationContext):
        pass

    # Exit a parse tree produced by PowerQueryParser#optional_parameter_specification.
    def exitOptional_parameter_specification(self, ctx:PowerQueryParser.Optional_parameter_specificationContext):
        pass


    # Enter a parse tree produced by PowerQueryParser#parameter_specification.
    def enterParameter_specification(self, ctx:PowerQueryParser.Parameter_specificationContext):
        pass

    # Exit a parse tree produced by PowerQueryParser#parameter_specification.
    def exitParameter_specification(self, ctx:PowerQueryParser.Parameter_specificationContext):
        pass


    # Enter a parse tree produced by PowerQueryParser#table_type.
    def enterTable_type(self, ctx:PowerQueryParser.Table_typeContext):
        pass

    # Exit a parse tree produced by PowerQueryParser#table_type.
    def exitTable_type(self, ctx:PowerQueryParser.Table_typeContext):
        pass


    # Enter a parse tree produced by PowerQueryParser#row_type.
    def enterRow_type(self, ctx:PowerQueryParser.Row_typeContext):
        pass

    # Exit a parse tree produced by PowerQueryParser#row_type.
    def exitRow_type(self, ctx:PowerQueryParser.Row_typeContext):
        pass


    # Enter a parse tree produced by PowerQueryParser#nullable_type.
    def enterNullable_type(self, ctx:PowerQueryParser.Nullable_typeContext):
        pass

    # Exit a parse tree produced by PowerQueryParser#nullable_type.
    def exitNullable_type(self, ctx:PowerQueryParser.Nullable_typeContext):
        pass


    # Enter a parse tree produced by PowerQueryParser#error_raising_expression.
    def enterError_raising_expression(self, ctx:PowerQueryParser.Error_raising_expressionContext):
        pass

    # Exit a parse tree produced by PowerQueryParser#error_raising_expression.
    def exitError_raising_expression(self, ctx:PowerQueryParser.Error_raising_expressionContext):
        pass


    # Enter a parse tree produced by PowerQueryParser#error_handling_expression.
    def enterError_handling_expression(self, ctx:PowerQueryParser.Error_handling_expressionContext):
        pass

    # Exit a parse tree produced by PowerQueryParser#error_handling_expression.
    def exitError_handling_expression(self, ctx:PowerQueryParser.Error_handling_expressionContext):
        pass


    # Enter a parse tree produced by PowerQueryParser#protected_expression.
    def enterProtected_expression(self, ctx:PowerQueryParser.Protected_expressionContext):
        pass

    # Exit a parse tree produced by PowerQueryParser#protected_expression.
    def exitProtected_expression(self, ctx:PowerQueryParser.Protected_expressionContext):
        pass


    # Enter a parse tree produced by PowerQueryParser#otherwise_clause.
    def enterOtherwise_clause(self, ctx:PowerQueryParser.Otherwise_clauseContext):
        pass

    # Exit a parse tree produced by PowerQueryParser#otherwise_clause.
    def exitOtherwise_clause(self, ctx:PowerQueryParser.Otherwise_clauseContext):
        pass


    # Enter a parse tree produced by PowerQueryParser#default_expression.
    def enterDefault_expression(self, ctx:PowerQueryParser.Default_expressionContext):
        pass

    # Exit a parse tree produced by PowerQueryParser#default_expression.
    def exitDefault_expression(self, ctx:PowerQueryParser.Default_expressionContext):
        pass


    # Enter a parse tree produced by PowerQueryParser#literal_attribs.
    def enterLiteral_attribs(self, ctx:PowerQueryParser.Literal_attribsContext):
        pass

    # Exit a parse tree produced by PowerQueryParser#literal_attribs.
    def exitLiteral_attribs(self, ctx:PowerQueryParser.Literal_attribsContext):
        pass


    # Enter a parse tree produced by PowerQueryParser#record_literal.
    def enterRecord_literal(self, ctx:PowerQueryParser.Record_literalContext):
        pass

    # Exit a parse tree produced by PowerQueryParser#record_literal.
    def exitRecord_literal(self, ctx:PowerQueryParser.Record_literalContext):
        pass


    # Enter a parse tree produced by PowerQueryParser#literal_field_list.
    def enterLiteral_field_list(self, ctx:PowerQueryParser.Literal_field_listContext):
        pass

    # Exit a parse tree produced by PowerQueryParser#literal_field_list.
    def exitLiteral_field_list(self, ctx:PowerQueryParser.Literal_field_listContext):
        pass


    # Enter a parse tree produced by PowerQueryParser#literal_field.
    def enterLiteral_field(self, ctx:PowerQueryParser.Literal_fieldContext):
        pass

    # Exit a parse tree produced by PowerQueryParser#literal_field.
    def exitLiteral_field(self, ctx:PowerQueryParser.Literal_fieldContext):
        pass


    # Enter a parse tree produced by PowerQueryParser#list_literal.
    def enterList_literal(self, ctx:PowerQueryParser.List_literalContext):
        pass

    # Exit a parse tree produced by PowerQueryParser#list_literal.
    def exitList_literal(self, ctx:PowerQueryParser.List_literalContext):
        pass


    # Enter a parse tree produced by PowerQueryParser#literal_item_list.
    def enterLiteral_item_list(self, ctx:PowerQueryParser.Literal_item_listContext):
        pass

    # Exit a parse tree produced by PowerQueryParser#literal_item_list.
    def exitLiteral_item_list(self, ctx:PowerQueryParser.Literal_item_listContext):
        pass


    # Enter a parse tree produced by PowerQueryParser#any_literal.
    def enterAny_literal(self, ctx:PowerQueryParser.Any_literalContext):
        pass

    # Exit a parse tree produced by PowerQueryParser#any_literal.
    def exitAny_literal(self, ctx:PowerQueryParser.Any_literalContext):
        pass



del PowerQueryParser