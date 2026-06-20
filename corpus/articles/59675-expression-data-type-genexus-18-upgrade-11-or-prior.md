---
title: "Expression data type (GeneXus 18 Upgrade 11 or prior)"
source_id: 59675
source_url: https://wiki.genexus.com/commwiki/wiki?59675
genexus_version: "18"
---

# Expression data type (GeneXus 18 Upgrade 11 or prior)

Expresses an arbitrary formula as a string, and instantly evaluates it.

### [Scope](#Scope)

**Objects:**

[Procedure](https://wiki.genexus.com/commwiki/wiki?6293),
[Transaction](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?1908,,),
[Web Panel](https://wiki.genexus.com/commwiki/wiki?6916)  
**Generators:**

[.NET](https://wiki.genexus.com/commwiki/wiki?38604), 
[Java](https://wiki.genexus.com/commwiki/wiki?12258), 
Ruby (up to GeneXus X Evolution 3)

### [Description](#Description)

The **Expression data type** is used to evaluate an expression at runtime.  
  
Suppose you have a formula whose definition you know will probably change in the future. Using a standard approach, the formula is generally encapsulated as a [global formula](https://wiki.genexus.com/commwiki/wiki?6440) in the [Knowledge Base](https://wiki.genexus.com/commwiki/wiki?1836), and GeneXus will expand its definition wherever the attribute is used.  
  
But, what happens if you need to change the definition? You will need to change the formula definition and recompile all the programs that use it, generating a new version of your program. Does it sound like a good idea to recompile all your code just for one little formula change?  
  
For those cases, where some formulas will probably change or must be specified at installation time, you can use the *Expression data type*; it allows runtime formula evaluations and modifications without having to change a single line of code.  
  
The trick is to handle math formulas as data (program metadata) instead of program instructions. The evaluator takes formulas as strings, assigns the desired parameter values and computes the results to be used by your application.

### [Sample](#Sample)

Suppose you have the following formula: "*a*\**b*+*c*". To evaluate it using the *Expression data type,* you will need to:

1. Define an *Expression Data Type* variable in your program, for example *&expressionDataTypeVariable*.
2. Assign the formula "*a*\**b*+*c*" to the *Expression* property of the data type.
3. Set a valid value for each variable used in the expression, in this case you must set the *a*, *b* and *c* values with the *Set* method of the *Variables* property. Here you must set all parameters as strings (check the code below).
4. Call the *Evaluate* method to execute the expression which will be returned in the *&Result* variable.
5. Check the *ErrCode* property. It there is no error the *&Result* variable will have the evaluation of the associated formula.

The code snippet is the following:

```
// Define the expression
&expressionString = "a*b+c"
// Assign the expression to the data type
&expressionDataTypeVariable.Expression = &expressionString
// Assign variables, in this case 3 variables must be set
&expressionDataTypeVariable.Variables.Set( "a", &integer1.ToString() )  // used the &integer1 value
&expressionDataTypeVariable.Variables.Set( "b", &integer2.ToString() )
&expressionDataTypeVariable.Variables.Set( "c", &integer3.ToString() )
// Everything is set, Evaluating Expression
&Result = &expressionDataTypeVariable.Evaluate()
If &expressionDataTypeVariable.ErrCode = 0
	// The evaluation executed with no errors
	// Do something with the &Result variable
else
	&errorString = &expressionDataTypeVariable.ErrCode.ToString()
	&msg = "Error:" + &errorString.Trim() + ":" + &expressionDataTypeVariable.ErrDescription
	msg( &msg ) // send error message executing an expression.
EndIf		
```

Many common mathematical functions and constants are built-in and ready to use. In addition, you can extend this mechanism by writing with your own user-defined functions using GeneXus Procedures to be executed at runtime and returning a numeric value.

### [Available operators and functions](#Available+operators+and+functions)

#### [**Constants**](#Constants)

* pi

#### [**Arithmetic Operators**](#Arithmetic+Operators)

* +, -, \*, /

#### [**Conditional operators**](#Conditional+operators)

* >, <, >=, <=, <>, and, or

#### [**Standard functions**](#Standard+functions)

* abs(n)
* [int(n)](https://wiki.genexus.com/commwiki/wiki?8418)
* frac(n)
* sin(n)
* asin(n)
* cos(n)
* acos(n)
* tan(n)
* atan(n)
* floor(n)
* [round(n)](https://wiki.genexus.com/commwiki/wiki?8486)
* ln(n) or log(n)
* exp(n)
* sqrt(n)
* pow(m, n)
* max(m,n)
* min(m,n)
* [iif(condition, m, n)](https://wiki.genexus.com/commwiki/wiki?14280)

**Note:** Make sure to add extra parentheses when using logical operators (AND, OR), otherwise a wrong result will be evaluated. For example:

```
iif ( ( a >= 0 ) AND ( b > a ), a, b )
```

#### [**External Functions**](#External+Functions)

* Any GeneXus
  [Procedure](https://wiki.genexus.com/commwiki/wiki?6293) using character and numeric parameters returning a numeric value defined as N(10,2).

### [Properties](#Properties)

#### [**ErrCode**](#ErrCode)

Returns a Numeric value with the error code associated with the evaluation.

**Syntax**

```
&ExpressionVariable.ErrCode
```

**Type returned:**  
Numeric

Possible error codes are:

*1*: Unknown error (UNKNOWN\_ERROR).

2: There is an error in the evaluate parameters (PARAMETER\_ERROR).

*3*: Expression to be evaluated is not well formed (EXPRESSION\_ERROR).

*4*: Error occurred during execution (EVALUATION\_ERROR).

*5*: Error executing an external function (EXTERNAL\_FUNCTION\_ERROR).

#### [**ErrDescription**](#ErrDescription)

In case of an error, it returns the associated description of the latest operation. Note that the error description will change depending on the platform.  
The only exception is when a division by zero occurs during evaluation. In that case ErrCode 4 will be returned with ErrDescription "Division by zero".

**Syntax**

```
&ExpressionVariable.ErrDescription
```

**Type Returned**:  
Character

#### [**Expression**](#Expression)

Expression to be evaluated. A *Character* or *Varcharacter* expression with the expression.

**Syntax**

```
&ExpressionVariable.Expression
```

Valid expressions are:

```
&expressionDataTypeVariable.Expression = "a*(b+c)/100"
&expressionDataTypeVariable.Expression = "rnd( a + b + c)"
&expressionDataTypeVariable.Expression = "cos(90)"
&expressionDataTypeVariable.Expression = "tan( b + a * b + c)"
&expressionDataTypeVariable.Expression = "floor( a * b + c)"
&expressionDataTypeVariable.Expression = "exp(0)"
&expressionDataTypeVariable.Expression = "abs( a * b + c)"
&expressionDataTypeVariable.Expression = "iif( a < b , a , c)"
&expressionDataTypeVariable.Expression = "myProcedure01( a , b)"
&expressionDataTypeVariable.Expression = "ln(exp(0))"
&expressionDataTypeVariable.Expression = "50*cos(g)*sin(f)"
&expressionDataTypeVariable.Expression = "myProcedure02( "'+'" , b , c)"
&expressionDataTypeVariable.Expression = "sqrt( a * b + c )"
&expressionDataTypeVariable.Expression = "floor( a * b + c)"
&expressionDataTypeVariable.Expression = "10*log( a * b + c)"
&expressionDataTypeVariable.Expression = "abs(-(a * b + c ))"
&expressionDataTypeVariable.Expression = "frac( a * b + c)"
&expressionDataTypeVariable.Expression = "2*pi"
```

#### [**Variables**](#Variables)

Variable list to be assigned and its associated value.

**Syntax**

```
&ExpressionVariable.Variables
```

**Note:** All variables must be set to strings; in the case of strings they must be enclosed in single quote characters ('). Check the following samples:

```
&expressionDataTypeVariable.Variables.Set( "a", &int1.ToString() ) // Numeric to string
&expressionDataTypeVariable.Variables.Set( "b", &int2.ToString() ) 
&expressionDataTypeVariable.Variables.Set( "c", &int3.ToString() )
&expressionDataTypeVariable.Variables.Set( "operator01", "'+'" ) // note that strings must be enclosed with '
&expressionDataTypeVariable.Variables.Set( "operator02", "'*'" )
```

### [Methods](#Methods)

#### [**Evaluate**](#Evaluate)

Evaluates the expression and returns the associated result.

**Syntax**

```
&ExpressionVariable.Evaluate()
```

****Type Returned**:**

Numeric(10,2)-

### [Considerations](#Considerations)

When comparing strings, the following operators are supported: "=", "!=" and "+" to concatenate; the following operators are not supported: "<" , ">" , "<=" , ">= ".

Error Code 5 - "Execute Method not found", **the return variable must be numeric with a length of 10 and 2 decimals**.

#### **[.NET](https://wiki.genexus.com/commwiki/wiki?38604) Specific**

* All internal processing to evaluate a formula is done with the C# decimal data type.
* The GeneXus
  [Procedures](https://wiki.genexus.com/commwiki/wiki?6293) to be executed must be in the same assembly as the caller program, so you need to make sure the procedure is compiled and included in the assembly using the expression data type. An option to explicitly add it to the call tree is as follows:

```
If (1=2)
  MyProcedure1.call()
EndIf
```

#### **[Java](https://wiki.genexus.com/commwiki/wiki?12258) Specific**

* All internal processing to evaluate a formula is done with the Java double data type.

### [Samples](#Samples)

```
&int1 = 100  //N(6.0)
&int2 = 200  //N(6.0)
&int3 = 300  //N(6.0)
&operator01 = "'+'" // Character
&operator02 = "'-'" // Character

&operand01 = "a1"
&operand02 = "b1"
&operand03 = "c1"

&expressionDataTypeVariable.Variables.Set( "a", &int1.ToString() )
&expressionDataTypeVariable.Variables.Set( "b", &int2.ToString() )
&expressionDataTypeVariable.Variables.Set( "c", &int3.ToString() )
&expressionDataTypeVariable.Variables.Set("var", 'TEST')
&expressionDataTypeVariable.Variables.Set( "operator01", &operator01 ) // using a variable with a string value, check the &operator0* variables
&expressionDataTypeVariable.Variables.Set( "operator02", &operator02 )
&expressionDataTypeVariable.Variables.Set( "operator03", "'/'" ) // using a string
&expressionDataTypeVariable.Variables.Set( "operator04", "'*'" )
&expressionDataTypeVariable.Variables.Set( &operand01, &int1.ToString() )
&expressionDataTypeVariable.Variables.Set( &operand02, &int2.ToString() )
&expressionDataTypeVariable.Variables.Set( &operand03, &int3.ToString() )

&expressionDataTypeVariable.Expression = "a*(b+c)/100"
do 'Evaluate'
&expressionDataTypeVariable.Expression = "rnd( a + b + c)"
do 'Evaluate'
&expressionDataTypeVariable.Expression = "cos(a)"
do 'Evaluate'
&expressionDataTypeVariable.Expression = "tan( b + a * b + c)"
do 'Evaluate'
&expressionDataTypeVariable.Expression = "floor( a * b + c)"
do 'Evaluate'
&expressionDataTypeVariable.Expression = "exp(0)"
do 'Evaluate'
&expressionDataTypeVariable.Expression = "abs( a * b + c)"
do 'Evaluate'
&expressionDataTypeVariable.Expression = "iif( a < b , a , c)"
do 'Evaluate'
&expressionDataTypeVariable.Expression = "ln(exp(10))"
do 'Evaluate'
&expressionDataTypeVariable.Expression = "50*cos(a)*sin(b)"
do 'Evaluate'
&expressionDataTypeVariable.Expression = "iif(var='TEST',a+b,a*b)"
do 'Evaluate'
&expressionDataTypeVariable.Expression = "iif(var<>'TEST',a+b,a*b)"
do 'Evaluate'
&expressionDataTypeVariable.Expression = "abs(a) + int(a) + frac(a)"
do 'Evaluate'
&expressionDataTypeVariable.Expression = "sin(1) + asin(1)+cos(1)+acos(1) + tan(1)+atan(1)"
do 'Evaluate'
&expressionDataTypeVariable.Expression = "round(1)+ln(1)+log(1)+exp(1)+sqrt(1)"
do 'Evaluate'
&expressionDataTypeVariable.Expression = "pow(2,3)+max(a,b)+min(a,b)"
do 'Evaluate'
&expressionDataTypeVariable.Expression = "a and b "
do 'Evaluate'
&expressionDataTypeVariable.Expression = "iif(operator01='+',a+b,0)" // using a string '+'
do 'Evaluate'
&expressionDataTypeVariable.Expression = "iif(operator02='*',a*b,0)"
do 'Evaluate'
&expressionDataTypeVariable.Expression = "myProcedure03( operator02 , b , c)" // using a GeneXus procedure with string and numeric variables
do 'Evaluate'
&expressionDataTypeVariable.Expression = "myProcedure03( '/', b , c)"
do 'Evaluate'
&expressionDataTypeVariable.Expression = "a1+b1+c1"
do 'Evaluate'

Msg('---Errors ---',status)
//Errors--
&expressionDataTypeVariable.Expression = "cos(j)*sin(r)"
do 'Evaluate'
&expressionDataTypeVariable.Expression = "myProcedure01( a , b)"
do 'Evaluate'
&expressionDataTypeVariable.Expression = "a / 0 " // Check the error code property
do 'Evaluate'

Sub 'Evaluate'
   &Result = &expressionDataTypeVariable.Evaluate()
   If &expressionDataTypeVariable.ErrCode = 0
      // The evaluation executed with no errors
      Msg('Result: '+&expressionDataTypeVariable.Expression+ '=' + str(&Result) , status)
    else
      &errorString = &expressionDataTypeVariable.ErrCode.ToString()
      &msg = "Error:" + &errorString + ":" + &expressionDataTypeVariable.ErrDescription
      msg( &msg,status ) // send error message executing an expression.
    EndIf        
endsub
```
