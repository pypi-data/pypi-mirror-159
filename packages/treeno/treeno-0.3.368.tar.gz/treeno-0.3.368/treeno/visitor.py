# AUTOGENERATED BY create_visitor.py
from typing import TYPE_CHECKING, Generic, TypeVar

T = TypeVar("T")
if TYPE_CHECKING:
    from treeno.base import GenericSql
    from treeno.datatypes.types import DataType
    from treeno.expression import (
        Add,
        AliasedStar,
        AliasedValue,
        And,
        Array,
        Between,
        Case,
        Cast,
        DistinctFrom,
        Divide,
        Else,
        Equal,
        Field,
        GreaterThan,
        GreaterThanOrEqual,
        InList,
        InQuery,
        Interval,
        IsNull,
        Lambda,
        LessThan,
        LessThanOrEqual,
        Like,
        Literal,
        Minus,
        Modulus,
        Multiply,
        Negative,
        Not,
        NotEqual,
        Or,
        Positive,
        RowConstructor,
        Star,
        Subscript,
        TryCast,
        TypeConstructor,
        When,
    )
    from treeno.functions.aggregate import (
        ApproxDistinct,
        ApproxMostFrequent,
        ApproxPercentile,
        ApproxSet,
        Arbitrary,
        ArrayAgg,
        Avg,
        BitwiseAndAgg,
        BitwiseOrAgg,
        BoolAnd,
        BoolOr,
        Checksum,
        Corr,
        Count,
        CountIf,
        CovarPop,
        CovarSamp,
        Every,
        GeometricMean,
        Histogram,
        Kurtosis,
        ListAgg,
        MapAgg,
        MapUnion,
        Max,
        MaxBy,
        Merge,
        Min,
        MinBy,
        MultiMapAgg,
        NumericHistogram,
        OverflowFiller,
        QDigestAgg,
        RegrIntercept,
        RegrSlope,
        Skewness,
        StdDev,
        StdDevPop,
        StdDevSamp,
        Sum,
        TDigestAgg,
        Variance,
        VarPop,
        VarSamp,
    )
    from treeno.functions.common import Concatenate
    from treeno.functions.conditional import Coalesce, If, NullIf, Try
    from treeno.functions.datetime import (
        AtTimezone,
        CurrentDate,
        CurrentTime,
        CurrentTimestamp,
        Date,
        DateAdd,
        DateDiff,
        DateTrunc,
        FromISO8601Date,
        FromISO8601Timestamp,
        FromISO8601TimestampNanos,
        FromUnixtime,
        FromUnixtimeNanos,
        HumanReadableSeconds,
        LastDayOfMonth,
        LocalTime,
        LocalTimestamp,
        Now,
        ParseDuration,
        ToISO8601,
        ToMilliseconds,
        ToUnixtime,
        WithTimezone,
    )
    from treeno.functions.math import Power
    from treeno.functions.session import (
        CurrentCatalog,
        CurrentPath,
        CurrentSchema,
        CurrentUser,
    )
    from treeno.functions.string import (
        Chr,
        CodePoint,
        FromUTF8,
        HammingDistance,
        Length,
        LevenshteinDistance,
        Lower,
        LPad,
        LTrim,
        LuhnCheck,
        Normalize,
        Replace,
        Reverse,
        RPad,
        RTrim,
        Soundex,
        ToUTF8,
    )
    from treeno.groupby import (
        Cube,
        GroupBy,
        GroupingSet,
        GroupingSetList,
        Rollup,
    )
    from treeno.orderby import OrderTerm
    from treeno.relation import (
        AliasedRelation,
        ExceptQuery,
        IntersectQuery,
        Join,
        JoinConfig,
        JoinOnCriteria,
        JoinUsingCriteria,
        Lateral,
        SelectQuery,
        Table,
        TableQuery,
        TableSample,
        UnionQuery,
        Unnest,
        ValuesQuery,
    )
    from treeno.window import (
        BoundedFrameBound,
        CurrentFrameBound,
        UnboundedFrameBound,
        Window,
    )


class TreenoVisitor(Generic[T]):
    def visit(self, node: "GenericSql") -> T:
        return getattr(self, f"visit_{node.__class__.__name__}")(node)

    def visit_Now(self, node: "Now") -> T:
        ...

    def visit_NotEqual(self, node: "NotEqual") -> T:
        ...

    def visit_UnboundedFrameBound(self, node: "UnboundedFrameBound") -> T:
        ...

    def visit_Join(self, node: "Join") -> T:
        ...

    def visit_CurrentPath(self, node: "CurrentPath") -> T:
        ...

    def visit_Concatenate(self, node: "Concatenate") -> T:
        ...

    def visit_Star(self, node: "Star") -> T:
        ...

    def visit_TryCast(self, node: "TryCast") -> T:
        ...

    def visit_LastDayOfMonth(self, node: "LastDayOfMonth") -> T:
        ...

    def visit_CountIf(self, node: "CountIf") -> T:
        ...

    def visit_CurrentDate(self, node: "CurrentDate") -> T:
        ...

    def visit_LevenshteinDistance(self, node: "LevenshteinDistance") -> T:
        ...

    def visit_Divide(self, node: "Divide") -> T:
        ...

    def visit_ParseDuration(self, node: "ParseDuration") -> T:
        ...

    def visit_Normalize(self, node: "Normalize") -> T:
        ...

    def visit_ApproxDistinct(self, node: "ApproxDistinct") -> T:
        ...

    def visit_JoinConfig(self, node: "JoinConfig") -> T:
        ...

    def visit_CodePoint(self, node: "CodePoint") -> T:
        ...

    def visit_DateTrunc(self, node: "DateTrunc") -> T:
        ...

    def visit_StdDevSamp(self, node: "StdDevSamp") -> T:
        ...

    def visit_MapAgg(self, node: "MapAgg") -> T:
        ...

    def visit_Unnest(self, node: "Unnest") -> T:
        ...

    def visit_TableSample(self, node: "TableSample") -> T:
        ...

    def visit_CurrentTimestamp(self, node: "CurrentTimestamp") -> T:
        ...

    def visit_Between(self, node: "Between") -> T:
        ...

    def visit_Negative(self, node: "Negative") -> T:
        ...

    def visit_OverflowFiller(self, node: "OverflowFiller") -> T:
        ...

    def visit_UnionQuery(self, node: "UnionQuery") -> T:
        ...

    def visit_ApproxPercentile(self, node: "ApproxPercentile") -> T:
        ...

    def visit_RPad(self, node: "RPad") -> T:
        ...

    def visit_RegrSlope(self, node: "RegrSlope") -> T:
        ...

    def visit_TableQuery(self, node: "TableQuery") -> T:
        ...

    def visit_Like(self, node: "Like") -> T:
        ...

    def visit_MinBy(self, node: "MinBy") -> T:
        ...

    def visit_And(self, node: "And") -> T:
        ...

    def visit_GreaterThan(self, node: "GreaterThan") -> T:
        ...

    def visit_CovarPop(self, node: "CovarPop") -> T:
        ...

    def visit_Case(self, node: "Case") -> T:
        ...

    def visit_Arbitrary(self, node: "Arbitrary") -> T:
        ...

    def visit_Corr(self, node: "Corr") -> T:
        ...

    def visit_CurrentCatalog(self, node: "CurrentCatalog") -> T:
        ...

    def visit_LuhnCheck(self, node: "LuhnCheck") -> T:
        ...

    def visit_FromISO8601Timestamp(self, node: "FromISO8601Timestamp") -> T:
        ...

    def visit_BoundedFrameBound(self, node: "BoundedFrameBound") -> T:
        ...

    def visit_Every(self, node: "Every") -> T:
        ...

    def visit_NumericHistogram(self, node: "NumericHistogram") -> T:
        ...

    def visit_WithTimezone(self, node: "WithTimezone") -> T:
        ...

    def visit_CurrentFrameBound(self, node: "CurrentFrameBound") -> T:
        ...

    def visit_Kurtosis(self, node: "Kurtosis") -> T:
        ...

    def visit_Not(self, node: "Not") -> T:
        ...

    def visit_HumanReadableSeconds(self, node: "HumanReadableSeconds") -> T:
        ...

    def visit_ToUTF8(self, node: "ToUTF8") -> T:
        ...

    def visit_ToISO8601(self, node: "ToISO8601") -> T:
        ...

    def visit_GroupBy(self, node: "GroupBy") -> T:
        ...

    def visit_Cube(self, node: "Cube") -> T:
        ...

    def visit_AliasedStar(self, node: "AliasedStar") -> T:
        ...

    def visit_Subscript(self, node: "Subscript") -> T:
        ...

    def visit_MaxBy(self, node: "MaxBy") -> T:
        ...

    def visit_Variance(self, node: "Variance") -> T:
        ...

    def visit_LocalTime(self, node: "LocalTime") -> T:
        ...

    def visit_Lower(self, node: "Lower") -> T:
        ...

    def visit_Add(self, node: "Add") -> T:
        ...

    def visit_RowConstructor(self, node: "RowConstructor") -> T:
        ...

    def visit_HammingDistance(self, node: "HammingDistance") -> T:
        ...

    def visit_Field(self, node: "Field") -> T:
        ...

    def visit_IntersectQuery(self, node: "IntersectQuery") -> T:
        ...

    def visit_DateAdd(self, node: "DateAdd") -> T:
        ...

    def visit_Interval(self, node: "Interval") -> T:
        ...

    def visit_Array(self, node: "Array") -> T:
        ...

    def visit_JoinUsingCriteria(self, node: "JoinUsingCriteria") -> T:
        ...

    def visit_Or(self, node: "Or") -> T:
        ...

    def visit_ApproxMostFrequent(self, node: "ApproxMostFrequent") -> T:
        ...

    def visit_GreaterThanOrEqual(self, node: "GreaterThanOrEqual") -> T:
        ...

    def visit_ListAgg(self, node: "ListAgg") -> T:
        ...

    def visit_QDigestAgg(self, node: "QDigestAgg") -> T:
        ...

    def visit_SelectQuery(self, node: "SelectQuery") -> T:
        ...

    def visit_RTrim(self, node: "RTrim") -> T:
        ...

    def visit_MapUnion(self, node: "MapUnion") -> T:
        ...

    def visit_ArrayAgg(self, node: "ArrayAgg") -> T:
        ...

    def visit_Skewness(self, node: "Skewness") -> T:
        ...

    def visit_FromISO8601TimestampNanos(
        self, node: "FromISO8601TimestampNanos"
    ) -> T:
        ...

    def visit_GeometricMean(self, node: "GeometricMean") -> T:
        ...

    def visit_Literal(self, node: "Literal") -> T:
        ...

    def visit_ValuesQuery(self, node: "ValuesQuery") -> T:
        ...

    def visit_TypeConstructor(self, node: "TypeConstructor") -> T:
        ...

    def visit_Modulus(self, node: "Modulus") -> T:
        ...

    def visit_Try(self, node: "Try") -> T:
        ...

    def visit_VarPop(self, node: "VarPop") -> T:
        ...

    def visit_Replace(self, node: "Replace") -> T:
        ...

    def visit_LocalTimestamp(self, node: "LocalTimestamp") -> T:
        ...

    def visit_Checksum(self, node: "Checksum") -> T:
        ...

    def visit_Window(self, node: "Window") -> T:
        ...

    def visit_FromUTF8(self, node: "FromUTF8") -> T:
        ...

    def visit_Minus(self, node: "Minus") -> T:
        ...

    def visit_ApproxSet(self, node: "ApproxSet") -> T:
        ...

    def visit_FromUnixtime(self, node: "FromUnixtime") -> T:
        ...

    def visit_Rollup(self, node: "Rollup") -> T:
        ...

    def visit_StdDev(self, node: "StdDev") -> T:
        ...

    def visit_When(self, node: "When") -> T:
        ...

    def visit_Histogram(self, node: "Histogram") -> T:
        ...

    def visit_CurrentSchema(self, node: "CurrentSchema") -> T:
        ...

    def visit_ToMilliseconds(self, node: "ToMilliseconds") -> T:
        ...

    def visit_BitwiseAndAgg(self, node: "BitwiseAndAgg") -> T:
        ...

    def visit_GroupingSet(self, node: "GroupingSet") -> T:
        ...

    def visit_Table(self, node: "Table") -> T:
        ...

    def visit_LPad(self, node: "LPad") -> T:
        ...

    def visit_IsNull(self, node: "IsNull") -> T:
        ...

    def visit_CurrentUser(self, node: "CurrentUser") -> T:
        ...

    def visit_LessThan(self, node: "LessThan") -> T:
        ...

    def visit_CovarSamp(self, node: "CovarSamp") -> T:
        ...

    def visit_Length(self, node: "Length") -> T:
        ...

    def visit_MultiMapAgg(self, node: "MultiMapAgg") -> T:
        ...

    def visit_BoolAnd(self, node: "BoolAnd") -> T:
        ...

    def visit_DataType(self, node: "DataType") -> T:
        ...

    def visit_AliasedValue(self, node: "AliasedValue") -> T:
        ...

    def visit_FromUnixtimeNanos(self, node: "FromUnixtimeNanos") -> T:
        ...

    def visit_Cast(self, node: "Cast") -> T:
        ...

    def visit_FromISO8601Date(self, node: "FromISO8601Date") -> T:
        ...

    def visit_InQuery(self, node: "InQuery") -> T:
        ...

    def visit_Sum(self, node: "Sum") -> T:
        ...

    def visit_DateDiff(self, node: "DateDiff") -> T:
        ...

    def visit_AliasedRelation(self, node: "AliasedRelation") -> T:
        ...

    def visit_Equal(self, node: "Equal") -> T:
        ...

    def visit_JoinOnCriteria(self, node: "JoinOnCriteria") -> T:
        ...

    def visit_Lateral(self, node: "Lateral") -> T:
        ...

    def visit_Soundex(self, node: "Soundex") -> T:
        ...

    def visit_VarSamp(self, node: "VarSamp") -> T:
        ...

    def visit_Chr(self, node: "Chr") -> T:
        ...

    def visit_ExceptQuery(self, node: "ExceptQuery") -> T:
        ...

    def visit_CurrentTime(self, node: "CurrentTime") -> T:
        ...

    def visit_Coalesce(self, node: "Coalesce") -> T:
        ...

    def visit_Date(self, node: "Date") -> T:
        ...

    def visit_Count(self, node: "Count") -> T:
        ...

    def visit_Min(self, node: "Min") -> T:
        ...

    def visit_Multiply(self, node: "Multiply") -> T:
        ...

    def visit_Merge(self, node: "Merge") -> T:
        ...

    def visit_OrderTerm(self, node: "OrderTerm") -> T:
        ...

    def visit_StdDevPop(self, node: "StdDevPop") -> T:
        ...

    def visit_Avg(self, node: "Avg") -> T:
        ...

    def visit_Power(self, node: "Power") -> T:
        ...

    def visit_InList(self, node: "InList") -> T:
        ...

    def visit_ToUnixtime(self, node: "ToUnixtime") -> T:
        ...

    def visit_Reverse(self, node: "Reverse") -> T:
        ...

    def visit_BitwiseOrAgg(self, node: "BitwiseOrAgg") -> T:
        ...

    def visit_RegrIntercept(self, node: "RegrIntercept") -> T:
        ...

    def visit_TDigestAgg(self, node: "TDigestAgg") -> T:
        ...

    def visit_DistinctFrom(self, node: "DistinctFrom") -> T:
        ...

    def visit_LessThanOrEqual(self, node: "LessThanOrEqual") -> T:
        ...

    def visit_Positive(self, node: "Positive") -> T:
        ...

    def visit_NullIf(self, node: "NullIf") -> T:
        ...

    def visit_Lambda(self, node: "Lambda") -> T:
        ...

    def visit_If(self, node: "If") -> T:
        ...

    def visit_Else(self, node: "Else") -> T:
        ...

    def visit_BoolOr(self, node: "BoolOr") -> T:
        ...

    def visit_GroupingSetList(self, node: "GroupingSetList") -> T:
        ...

    def visit_Max(self, node: "Max") -> T:
        ...

    def visit_AtTimezone(self, node: "AtTimezone") -> T:
        ...

    def visit_LTrim(self, node: "LTrim") -> T:
        ...
