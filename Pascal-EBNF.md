## Definitions of Syntactic Classes

### Programs and Blocks

- program =

  [program-heading](http://www.cs.kent.edu/~durand/CS43101Fall2004/resources/Pascal-EBNF.html#program-heading) [block](http://www.cs.kent.edu/~durand/CS43101Fall2004/resources/Pascal-EBNF.html#block) "." .

- program-heading =

  **program** [identifier](http://www.cs.kent.edu/~durand/CS43101Fall2004/resources/Pascal-EBNF.html#identifier) "(" [identifier-list](http://www.cs.kent.edu/~durand/CS43101Fall2004/resources/Pascal-EBNF.html#identifier-list) ")" ";" .

- block =

  [declaration-part](http://www.cs.kent.edu/~durand/CS43101Fall2004/resources/Pascal-EBNF.html#declaration-part) [statement-part](http://www.cs.kent.edu/~durand/CS43101Fall2004/resources/Pascal-EBNF.html#statement-part) .

- declaration-part =

  [ [label-declaration-part](http://www.cs.kent.edu/~durand/CS43101Fall2004/resources/Pascal-EBNF.html#label-declaration-part) ] [ [constant-definition-part](http://www.cs.kent.edu/~durand/CS43101Fall2004/resources/Pascal-EBNF.html#constant-definition-part) ] [ [type-definition-part](http://www.cs.kent.edu/~durand/CS43101Fall2004/resources/Pascal-EBNF.html#type-definition-part) ] [ [variable-declaration-part](http://www.cs.kent.edu/~durand/CS43101Fall2004/resources/Pascal-EBNF.html#variable-declaration-part) ] [procedure-and-function-declaration-part](http://www.cs.kent.edu/~durand/CS43101Fall2004/resources/Pascal-EBNF.html#procedure-and-function-declaration-part) .

- label-declaration-part =

  **label** [label](http://www.cs.kent.edu/~durand/CS43101Fall2004/resources/Pascal-EBNF.html#label) { "," [label](http://www.cs.kent.edu/~durand/CS43101Fall2004/resources/Pascal-EBNF.html#label) } ";" .

- constant-definition-part =

  **const** [constant-definition](http://www.cs.kent.edu/~durand/CS43101Fall2004/resources/Pascal-EBNF.html#constant-definition) ";" { [constant-definition](http://www.cs.kent.edu/~durand/CS43101Fall2004/resources/Pascal-EBNF.html#constant-definition) ";" } .

- constant-definition =

  [identifier](http://www.cs.kent.edu/~durand/CS43101Fall2004/resources/Pascal-EBNF.html#identifier) "=" [constant](http://www.cs.kent.edu/~durand/CS43101Fall2004/resources/Pascal-EBNF.html#constant) .

- type-definition-part =

  **type** [type-definition](http://www.cs.kent.edu/~durand/CS43101Fall2004/resources/Pascal-EBNF.html#type-definition) ";" { [type-definition](http://www.cs.kent.edu/~durand/CS43101Fall2004/resources/Pascal-EBNF.html#type-definition) ";" } .

- type-definition =

  [identifier](http://www.cs.kent.edu/~durand/CS43101Fall2004/resources/Pascal-EBNF.html#identifier) "=" [type](http://www.cs.kent.edu/~durand/CS43101Fall2004/resources/Pascal-EBNF.html#type) .

- variable-declaration-part =

  **var** [variable-declaration](http://www.cs.kent.edu/~durand/CS43101Fall2004/resources/Pascal-EBNF.html#variable-declaration) ";" { [variable-declaration](http://www.cs.kent.edu/~durand/CS43101Fall2004/resources/Pascal-EBNF.html#variable-declaration) ";" } .

- variable-declaration =

  [identifier-list](http://www.cs.kent.edu/~durand/CS43101Fall2004/resources/Pascal-EBNF.html#identifier-list) ":" [type](http://www.cs.kent.edu/~durand/CS43101Fall2004/resources/Pascal-EBNF.html#type) .

- procedure-and-function-declaration-part =

  { ([procedure-declaration](http://www.cs.kent.edu/~durand/CS43101Fall2004/resources/Pascal-EBNF.html#procedure-declaration) | [function-declaration](http://www.cs.kent.edu/~durand/CS43101Fall2004/resources/Pascal-EBNF.html#function-declaration)) ";" } .

- procedure-declaration =

  [procedure-heading](http://www.cs.kent.edu/~durand/CS43101Fall2004/resources/Pascal-EBNF.html#procedure-heading) ";" [procedure-body](http://www.cs.kent.edu/~durand/CS43101Fall2004/resources/Pascal-EBNF.html#procedure-body) | [procedure-heading](http://www.cs.kent.edu/~durand/CS43101Fall2004/resources/Pascal-EBNF.html#procedure-heading) ";" [directive](http://www.cs.kent.edu/~durand/CS43101Fall2004/resources/Pascal-EBNF.html#directive) | [procedure-identification](http://www.cs.kent.edu/~durand/CS43101Fall2004/resources/Pascal-EBNF.html#procedure-identification) ";" [procedure-body](http://www.cs.kent.edu/~durand/CS43101Fall2004/resources/Pascal-EBNF.html#procedure-body) .

- procedure-body =

  [block](http://www.cs.kent.edu/~durand/CS43101Fall2004/resources/Pascal-EBNF.html#block) .

- function-declaration =

  [function-heading](http://www.cs.kent.edu/~durand/CS43101Fall2004/resources/Pascal-EBNF.html#function-heading) ";" [function-body](http://www.cs.kent.edu/~durand/CS43101Fall2004/resources/Pascal-EBNF.html#function-body) | [function-heading](http://www.cs.kent.edu/~durand/CS43101Fall2004/resources/Pascal-EBNF.html#function-heading) ";" [directive](http://www.cs.kent.edu/~durand/CS43101Fall2004/resources/Pascal-EBNF.html#directive) | [function-identification](http://www.cs.kent.edu/~durand/CS43101Fall2004/resources/Pascal-EBNF.html#function-identification) ";" [function-body](http://www.cs.kent.edu/~durand/CS43101Fall2004/resources/Pascal-EBNF.html#function-body) .

- function-body =

  [block](http://www.cs.kent.edu/~durand/CS43101Fall2004/resources/Pascal-EBNF.html#block) .

- directive =

  **forward** | compiler-defined-directives .

- statement-part =

  **begin** [statement-sequence](http://www.cs.kent.edu/~durand/CS43101Fall2004/resources/Pascal-EBNF.html#statement-sequence) **end** .

------

### Procedure and Function Definitions

- procedure-heading =

  **procedure** [identifier](http://www.cs.kent.edu/~durand/CS43101Fall2004/resources/Pascal-EBNF.html#identifier) [ [formal-parameter-list](http://www.cs.kent.edu/~durand/CS43101Fall2004/resources/Pascal-EBNF.html#formal-parameter-list) ] .

- function-heading =

  **function** [identifier](http://www.cs.kent.edu/~durand/CS43101Fall2004/resources/Pascal-EBNF.html#identifier) [ [formal-parameter-list](http://www.cs.kent.edu/~durand/CS43101Fall2004/resources/Pascal-EBNF.html#formal-parameter-list) ] ":" [result-type](http://www.cs.kent.edu/~durand/CS43101Fall2004/resources/Pascal-EBNF.html#result-type) .

- result-type =

  [type-identifier](http://www.cs.kent.edu/~durand/CS43101Fall2004/resources/Pascal-EBNF.html#type-identifier) .

- procedure-identification =

  **procedure** [procedure-identifier](http://www.cs.kent.edu/~durand/CS43101Fall2004/resources/Pascal-EBNF.html#procedure-identifier) .

- function-identification =

  **function** [function-identifier](http://www.cs.kent.edu/~durand/CS43101Fall2004/resources/Pascal-EBNF.html#function-identifier) .

- formal-parameter-list =

  "(" [formal-parameter-section](http://www.cs.kent.edu/~durand/CS43101Fall2004/resources/Pascal-EBNF.html#formal-parameter-section) { ";" [formal-parameter-section](http://www.cs.kent.edu/~durand/CS43101Fall2004/resources/Pascal-EBNF.html#formal-parameter-section) } ")" .

- formal-parameter-section =

  [value-parameter-section](http://www.cs.kent.edu/~durand/CS43101Fall2004/resources/Pascal-EBNF.html#value-parameter-section) | [variable-parameter-section](http://www.cs.kent.edu/~durand/CS43101Fall2004/resources/Pascal-EBNF.html#variable-parameter-section) | [procedure-parameter-section](http://www.cs.kent.edu/~durand/CS43101Fall2004/resources/Pascal-EBNF.html#procedure-parameter-section) | [function-parameter-section](http://www.cs.kent.edu/~durand/CS43101Fall2004/resources/Pascal-EBNF.html#function-parameter-section) .

- value-parameter-section =

  [identifier-list](http://www.cs.kent.edu/~durand/CS43101Fall2004/resources/Pascal-EBNF.html#identifier-list) ":" [parameter-type](http://www.cs.kent.edu/~durand/CS43101Fall2004/resources/Pascal-EBNF.html#parameter-type) .

- variable-parameter-section =

  **var** [identifier-list](http://www.cs.kent.edu/~durand/CS43101Fall2004/resources/Pascal-EBNF.html#identifier-list) ":" [parameter-type](http://www.cs.kent.edu/~durand/CS43101Fall2004/resources/Pascal-EBNF.html#parameter-type) .

- procedure-parameter-section =

  [procedure-heading](http://www.cs.kent.edu/~durand/CS43101Fall2004/resources/Pascal-EBNF.html#procedure-heading) .

- function-parameter-section =

  [function-heading](http://www.cs.kent.edu/~durand/CS43101Fall2004/resources/Pascal-EBNF.html#function-heading) .

- parameter-type =

  [type-identifier](http://www.cs.kent.edu/~durand/CS43101Fall2004/resources/Pascal-EBNF.html#type-identifier) | [conformant-array-schema](http://www.cs.kent.edu/~durand/CS43101Fall2004/resources/Pascal-EBNF.html#conformant-array-schema) .

- conformant-array-schema =

  [packed-conformant-array-schema](http://www.cs.kent.edu/~durand/CS43101Fall2004/resources/Pascal-EBNF.html#packed-conformant-array-schema) | [unpacked-conformant-array-schema](http://www.cs.kent.edu/~durand/CS43101Fall2004/resources/Pascal-EBNF.html#unpacked-conformant-array-schema) .

- packed-conformant-array-schema =

  **packed** **array** "[ " [bound-specification](http://www.cs.kent.edu/~durand/CS43101Fall2004/resources/Pascal-EBNF.html#bound-specification) " ]" **of** [type-identifier](http://www.cs.kent.edu/~durand/CS43101Fall2004/resources/Pascal-EBNF.html#type-identifier) .

- unpacked-conformant-array-schema =

  **array** "[ " [bound-specification](http://www.cs.kent.edu/~durand/CS43101Fall2004/resources/Pascal-EBNF.html#bound-specification) { ";" [bound-specification](http://www.cs.kent.edu/~durand/CS43101Fall2004/resources/Pascal-EBNF.html#bound-specification) } " ]" **of** ([type-identifier](http://www.cs.kent.edu/~durand/CS43101Fall2004/resources/Pascal-EBNF.html#type-identifier) | [conformant-array-schema](http://www.cs.kent.edu/~durand/CS43101Fall2004/resources/Pascal-EBNF.html#conformant-array-schema)) .

- bound-specification =

  [identifier](http://www.cs.kent.edu/~durand/CS43101Fall2004/resources/Pascal-EBNF.html#identifier) ".." [identifier](http://www.cs.kent.edu/~durand/CS43101Fall2004/resources/Pascal-EBNF.html#identifier) ":" [ordinal-type-identifier](http://www.cs.kent.edu/~durand/CS43101Fall2004/resources/Pascal-EBNF.html#ordinal-type-identifier) .

- ordinal-type-identifier =

  [type-identifier](http://www.cs.kent.edu/~durand/CS43101Fall2004/resources/Pascal-EBNF.html#type-identifier) .

------

### Statements

- statement-sequence =

  [statement](http://www.cs.kent.edu/~durand/CS43101Fall2004/resources/Pascal-EBNF.html#statement) { ";" [statement](http://www.cs.kent.edu/~durand/CS43101Fall2004/resources/Pascal-EBNF.html#statement) } .

- statement =

  [ [label](http://www.cs.kent.edu/~durand/CS43101Fall2004/resources/Pascal-EBNF.html#label) ":" ] ([simple-statement](http://www.cs.kent.edu/~durand/CS43101Fall2004/resources/Pascal-EBNF.html#simple-statement) | [structured-statement](http://www.cs.kent.edu/~durand/CS43101Fall2004/resources/Pascal-EBNF.html#structured-statement)) .

- simple-statement =

  [ [assignment-statement](http://www.cs.kent.edu/~durand/CS43101Fall2004/resources/Pascal-EBNF.html#assignment-statement) | [procedure-statement](http://www.cs.kent.edu/~durand/CS43101Fall2004/resources/Pascal-EBNF.html#procedure-statement) | [goto-statement](http://www.cs.kent.edu/~durand/CS43101Fall2004/resources/Pascal-EBNF.html#goto-statement) ] .

- assignment-statement =

  ([variable](http://www.cs.kent.edu/~durand/CS43101Fall2004/resources/Pascal-EBNF.html#variable) | [function-identifier](http://www.cs.kent.edu/~durand/CS43101Fall2004/resources/Pascal-EBNF.html#function-identifier)) ":=" [expression](http://www.cs.kent.edu/~durand/CS43101Fall2004/resources/Pascal-EBNF.html#expression) .

- procedure-statement =

  [procedure-identifier](http://www.cs.kent.edu/~durand/CS43101Fall2004/resources/Pascal-EBNF.html#procedure-identifier) [ [actual-parameter-list](http://www.cs.kent.edu/~durand/CS43101Fall2004/resources/Pascal-EBNF.html#actual-parameter-list) ] .

- goto-statement =

  **goto** [label](http://www.cs.kent.edu/~durand/CS43101Fall2004/resources/Pascal-EBNF.html#label) .

- structured-statement =

  [compound-statement](http://www.cs.kent.edu/~durand/CS43101Fall2004/resources/Pascal-EBNF.html#compound-statement) | [repetitive-statement](http://www.cs.kent.edu/~durand/CS43101Fall2004/resources/Pascal-EBNF.html#repetitive-statement) | [conditional-statement](http://www.cs.kent.edu/~durand/CS43101Fall2004/resources/Pascal-EBNF.html#conditional-statement) | [with-statement](http://www.cs.kent.edu/~durand/CS43101Fall2004/resources/Pascal-EBNF.html#with-statement) .

- compound-statement =

  **begin** [statement-sequence](http://www.cs.kent.edu/~durand/CS43101Fall2004/resources/Pascal-EBNF.html#statement-sequence) **end** .

- repetitive-statement =

  [while-statement](http://www.cs.kent.edu/~durand/CS43101Fall2004/resources/Pascal-EBNF.html#while-statement) | [repeat-statement](http://www.cs.kent.edu/~durand/CS43101Fall2004/resources/Pascal-EBNF.html#repeat-statement) | [for-statement](http://www.cs.kent.edu/~durand/CS43101Fall2004/resources/Pascal-EBNF.html#for-statement) .

- while-statement =

  **while** [expression](http://www.cs.kent.edu/~durand/CS43101Fall2004/resources/Pascal-EBNF.html#expression) **do** [statement](http://www.cs.kent.edu/~durand/CS43101Fall2004/resources/Pascal-EBNF.html#statement) .

- repeat-statement =

  **repeat** [statement-sequence](http://www.cs.kent.edu/~durand/CS43101Fall2004/resources/Pascal-EBNF.html#statement-sequence) **until** [expression](http://www.cs.kent.edu/~durand/CS43101Fall2004/resources/Pascal-EBNF.html#expression) .

- for-statement =

  **for** [variable-identifier](http://www.cs.kent.edu/~durand/CS43101Fall2004/resources/Pascal-EBNF.html#variable-identifier) ":=" [initial-expression](http://www.cs.kent.edu/~durand/CS43101Fall2004/resources/Pascal-EBNF.html#initial-expression) (**to** | **downto**) [final-expression](http://www.cs.kent.edu/~durand/CS43101Fall2004/resources/Pascal-EBNF.html#final-expression) **do** [statement](http://www.cs.kent.edu/~durand/CS43101Fall2004/resources/Pascal-EBNF.html#statement) .

- initial-expression =

  [expression](http://www.cs.kent.edu/~durand/CS43101Fall2004/resources/Pascal-EBNF.html#expression) .

- final-expression =

  [expression](http://www.cs.kent.edu/~durand/CS43101Fall2004/resources/Pascal-EBNF.html#expression) .

- conditional-statement =

  [if-statement](http://www.cs.kent.edu/~durand/CS43101Fall2004/resources/Pascal-EBNF.html#if-statement) | [case-statement](http://www.cs.kent.edu/~durand/CS43101Fall2004/resources/Pascal-EBNF.html#case-statement) .

- if-statement =

  **if** [expression](http://www.cs.kent.edu/~durand/CS43101Fall2004/resources/Pascal-EBNF.html#expression) **then** [statement](http://www.cs.kent.edu/~durand/CS43101Fall2004/resources/Pascal-EBNF.html#statement) [ **else** [statement](http://www.cs.kent.edu/~durand/CS43101Fall2004/resources/Pascal-EBNF.html#statement) ] .

- case-statement =

  **case** [expression](http://www.cs.kent.edu/~durand/CS43101Fall2004/resources/Pascal-EBNF.html#expression) **of** [case-limb](http://www.cs.kent.edu/~durand/CS43101Fall2004/resources/Pascal-EBNF.html#case-limb) { ";" [case-limb](http://www.cs.kent.edu/~durand/CS43101Fall2004/resources/Pascal-EBNF.html#case-limb) } [ ";" ] **end** .

- case-limb =

  [case-label-list](http://www.cs.kent.edu/~durand/CS43101Fall2004/resources/Pascal-EBNF.html#case-label-list) ":" [statement](http://www.cs.kent.edu/~durand/CS43101Fall2004/resources/Pascal-EBNF.html#statement) .

- case-label-list =

  [constant](http://www.cs.kent.edu/~durand/CS43101Fall2004/resources/Pascal-EBNF.html#constant) { "," [constant](http://www.cs.kent.edu/~durand/CS43101Fall2004/resources/Pascal-EBNF.html#constant) } .

- with-statement =

  **with** [record-variable](http://www.cs.kent.edu/~durand/CS43101Fall2004/resources/Pascal-EBNF.html#record-variable) { "," [record-variable](http://www.cs.kent.edu/~durand/CS43101Fall2004/resources/Pascal-EBNF.html#record-variable) } **do** [statement](http://www.cs.kent.edu/~durand/CS43101Fall2004/resources/Pascal-EBNF.html#statement) .

- actual-parameter-list =

  "(" [actual-parameter](http://www.cs.kent.edu/~durand/CS43101Fall2004/resources/Pascal-EBNF.html#actual-parameter) { "," [actual-parameter](http://www.cs.kent.edu/~durand/CS43101Fall2004/resources/Pascal-EBNF.html#actual-parameter) } ")" .

- actual-parameter =

  [actual-value](http://www.cs.kent.edu/~durand/CS43101Fall2004/resources/Pascal-EBNF.html#actual-value) | [actual-variable](http://www.cs.kent.edu/~durand/CS43101Fall2004/resources/Pascal-EBNF.html#actual-variable) | [actual-procedure](http://www.cs.kent.edu/~durand/CS43101Fall2004/resources/Pascal-EBNF.html#actual-procedure) | [actual-function](http://www.cs.kent.edu/~durand/CS43101Fall2004/resources/Pascal-EBNF.html#actual-function) .

- actual-value =

  [expression](http://www.cs.kent.edu/~durand/CS43101Fall2004/resources/Pascal-EBNF.html#expression) .

- actual-procedure =

  [procedure-identifier](http://www.cs.kent.edu/~durand/CS43101Fall2004/resources/Pascal-EBNF.html#procedure-identifier) .

- actual-function =

  [function-identifier](http://www.cs.kent.edu/~durand/CS43101Fall2004/resources/Pascal-EBNF.html#function-identifier) .

------

### Expressions

- expression =

  [simple-expression](http://www.cs.kent.edu/~durand/CS43101Fall2004/resources/Pascal-EBNF.html#simple-expression) [ [relational-operator](http://www.cs.kent.edu/~durand/CS43101Fall2004/resources/Pascal-EBNF.html#relational-operator) [simple-expression](http://www.cs.kent.edu/~durand/CS43101Fall2004/resources/Pascal-EBNF.html#simple-expression) ] .

- simple-expression =

  [ [sign](http://www.cs.kent.edu/~durand/CS43101Fall2004/resources/Pascal-EBNF.html#sign) ] [term](http://www.cs.kent.edu/~durand/CS43101Fall2004/resources/Pascal-EBNF.html#term) { [addition-operator](http://www.cs.kent.edu/~durand/CS43101Fall2004/resources/Pascal-EBNF.html#addition-operator) [term](http://www.cs.kent.edu/~durand/CS43101Fall2004/resources/Pascal-EBNF.html#term) } .

- term =

  [factor](http://www.cs.kent.edu/~durand/CS43101Fall2004/resources/Pascal-EBNF.html#factor) { [multiplication-operator](http://www.cs.kent.edu/~durand/CS43101Fall2004/resources/Pascal-EBNF.html#multiplication-operator) [factor](http://www.cs.kent.edu/~durand/CS43101Fall2004/resources/Pascal-EBNF.html#factor) } .

- factor =

  [variable](http://www.cs.kent.edu/~durand/CS43101Fall2004/resources/Pascal-EBNF.html#variable) | [number](http://www.cs.kent.edu/~durand/CS43101Fall2004/resources/Pascal-EBNF.html#number) | [string](http://www.cs.kent.edu/~durand/CS43101Fall2004/resources/Pascal-EBNF.html#string) | [set](http://www.cs.kent.edu/~durand/CS43101Fall2004/resources/Pascal-EBNF.html#set) | **nil** | [constant-identifier](http://www.cs.kent.edu/~durand/CS43101Fall2004/resources/Pascal-EBNF.html#constant-identifier) | [bound-identifier](http://www.cs.kent.edu/~durand/CS43101Fall2004/resources/Pascal-EBNF.html#bound-identifier) | [function-designator](http://www.cs.kent.edu/~durand/CS43101Fall2004/resources/Pascal-EBNF.html#function-designator) | "(" [expression](http://www.cs.kent.edu/~durand/CS43101Fall2004/resources/Pascal-EBNF.html#expression) ")" | **not** [factor](http://www.cs.kent.edu/~durand/CS43101Fall2004/resources/Pascal-EBNF.html#factor) .

- relational-operator =

  "=" | "<>" | "<" | "<=" | ">" | ">=" | "in" .

- addition-operator =

  "+" | "-" | **or** .

- multiplication-operator =

  "*" | "/" | **div** | **mod** | **and** .

- variable =

  [entire-variable](http://www.cs.kent.edu/~durand/CS43101Fall2004/resources/Pascal-EBNF.html#entire-variable) | [component-variable](http://www.cs.kent.edu/~durand/CS43101Fall2004/resources/Pascal-EBNF.html#component-variable) | [referenced-variable](http://www.cs.kent.edu/~durand/CS43101Fall2004/resources/Pascal-EBNF.html#referenced-variable) .

- entire-variable =

  [variable-identifier](http://www.cs.kent.edu/~durand/CS43101Fall2004/resources/Pascal-EBNF.html#variable-identifier) | [field-identifier](http://www.cs.kent.edu/~durand/CS43101Fall2004/resources/Pascal-EBNF.html#field-identifier) .

- component-variable =

  [indexed-variable](http://www.cs.kent.edu/~durand/CS43101Fall2004/resources/Pascal-EBNF.html#indexed-variable) | [field-designator](http://www.cs.kent.edu/~durand/CS43101Fall2004/resources/Pascal-EBNF.html#field-designator) | [file-buffer](http://www.cs.kent.edu/~durand/CS43101Fall2004/resources/Pascal-EBNF.html#file-buffer) .

- indexed-variable =

  [array-variable](http://www.cs.kent.edu/~durand/CS43101Fall2004/resources/Pascal-EBNF.html#array-variable) "[ " [expression-list](http://www.cs.kent.edu/~durand/CS43101Fall2004/resources/Pascal-EBNF.html#expression-list) " ]" .

- field-designator =

  [record-variable](http://www.cs.kent.edu/~durand/CS43101Fall2004/resources/Pascal-EBNF.html#record-variable) "." [field-identifier](http://www.cs.kent.edu/~durand/CS43101Fall2004/resources/Pascal-EBNF.html#field-identifier) .

- set =

  "[ " [element-list](http://www.cs.kent.edu/~durand/CS43101Fall2004/resources/Pascal-EBNF.html#element-list) " ]" .

- element-list =

  [ [expression](http://www.cs.kent.edu/~durand/CS43101Fall2004/resources/Pascal-EBNF.html#expression) { "," [expression](http://www.cs.kent.edu/~durand/CS43101Fall2004/resources/Pascal-EBNF.html#expression) } ] .

- function-designator =

  [function-identifier](http://www.cs.kent.edu/~durand/CS43101Fall2004/resources/Pascal-EBNF.html#function-identifier) [ [actual-parameter-list](http://www.cs.kent.edu/~durand/CS43101Fall2004/resources/Pascal-EBNF.html#actual-parameter-list) ] .

- file-buffer =

  [file-variable](http://www.cs.kent.edu/~durand/CS43101Fall2004/resources/Pascal-EBNF.html#file-variable) "^" .

------

### Types

- type =

  [simple-type](http://www.cs.kent.edu/~durand/CS43101Fall2004/resources/Pascal-EBNF.html#simple-type) | [structured-type](http://www.cs.kent.edu/~durand/CS43101Fall2004/resources/Pascal-EBNF.html#structured-type) | [pointer-type](http://www.cs.kent.edu/~durand/CS43101Fall2004/resources/Pascal-EBNF.html#pointer-type) | [type-identifier](http://www.cs.kent.edu/~durand/CS43101Fall2004/resources/Pascal-EBNF.html#type-identifier) .

- simple-type =

  [subrange-type](http://www.cs.kent.edu/~durand/CS43101Fall2004/resources/Pascal-EBNF.html#subrange-type) | [enumerated-type](http://www.cs.kent.edu/~durand/CS43101Fall2004/resources/Pascal-EBNF.html#enumerated-type) .

- enumerated-type =

  "(" [identifier-list](http://www.cs.kent.edu/~durand/CS43101Fall2004/resources/Pascal-EBNF.html#identifier-list) ")" .

- subrange-type =

  [lower-bound](http://www.cs.kent.edu/~durand/CS43101Fall2004/resources/Pascal-EBNF.html#lower-bound) ".." [upper-bound](http://www.cs.kent.edu/~durand/CS43101Fall2004/resources/Pascal-EBNF.html#upper-bound) .

- lower-bound =

  [constant](http://www.cs.kent.edu/~durand/CS43101Fall2004/resources/Pascal-EBNF.html#constant) .

- upper-bound =

  [constant](http://www.cs.kent.edu/~durand/CS43101Fall2004/resources/Pascal-EBNF.html#constant) .

- structured-type =

  [ **packed** ] [unpacked-structured-type](http://www.cs.kent.edu/~durand/CS43101Fall2004/resources/Pascal-EBNF.html#unpacked-structured-type) .

- unpacked-structured-type =

  [array-type](http://www.cs.kent.edu/~durand/CS43101Fall2004/resources/Pascal-EBNF.html#array-type) | [record-type](http://www.cs.kent.edu/~durand/CS43101Fall2004/resources/Pascal-EBNF.html#record-type) | [set-type](http://www.cs.kent.edu/~durand/CS43101Fall2004/resources/Pascal-EBNF.html#set-type) | [file-type](http://www.cs.kent.edu/~durand/CS43101Fall2004/resources/Pascal-EBNF.html#file-type) .

- array-type =

  **array** "[ " [index-type](http://www.cs.kent.edu/~durand/CS43101Fall2004/resources/Pascal-EBNF.html#index-type) { "," [index-type](http://www.cs.kent.edu/~durand/CS43101Fall2004/resources/Pascal-EBNF.html#index-type) } " ]" **of** [element-type](http://www.cs.kent.edu/~durand/CS43101Fall2004/resources/Pascal-EBNF.html#element-type) .

- index-type =

  [simple-type](http://www.cs.kent.edu/~durand/CS43101Fall2004/resources/Pascal-EBNF.html#simple-type) .

- element-type =

  [type](http://www.cs.kent.edu/~durand/CS43101Fall2004/resources/Pascal-EBNF.html#type) .

- record-type =

  **record** [field-list](http://www.cs.kent.edu/~durand/CS43101Fall2004/resources/Pascal-EBNF.html#field-list) **end** .

- set-type =

  **set** **of** [base-type](http://www.cs.kent.edu/~durand/CS43101Fall2004/resources/Pascal-EBNF.html#base-type) .

- base-type =

  [type](http://www.cs.kent.edu/~durand/CS43101Fall2004/resources/Pascal-EBNF.html#type) .

- file-type =

  **file** **of** [file-component-type](http://www.cs.kent.edu/~durand/CS43101Fall2004/resources/Pascal-EBNF.html#file-component-type) .

- file-component-type =

  [type](http://www.cs.kent.edu/~durand/CS43101Fall2004/resources/Pascal-EBNF.html#type) .

- pointer-type =

  "^" [type-identifier](http://www.cs.kent.edu/~durand/CS43101Fall2004/resources/Pascal-EBNF.html#type-identifier) .

------

### Record Fields

- field-list =

  [ ([fixed-part](http://www.cs.kent.edu/~durand/CS43101Fall2004/resources/Pascal-EBNF.html#fixed-part) [ ";" [variant-part](http://www.cs.kent.edu/~durand/CS43101Fall2004/resources/Pascal-EBNF.html#variant-part) ] | [variant-part](http://www.cs.kent.edu/~durand/CS43101Fall2004/resources/Pascal-EBNF.html#variant-part)) [ ";" ] ] .

- fixed-part =

  [record-section](http://www.cs.kent.edu/~durand/CS43101Fall2004/resources/Pascal-EBNF.html#record-section) { ";" [record-section](http://www.cs.kent.edu/~durand/CS43101Fall2004/resources/Pascal-EBNF.html#record-section) } .

- record-section =

  [identifier-list](http://www.cs.kent.edu/~durand/CS43101Fall2004/resources/Pascal-EBNF.html#identifier-list) ":" [type](http://www.cs.kent.edu/~durand/CS43101Fall2004/resources/Pascal-EBNF.html#type) .

- variant-part =

  **case** [tag-field](http://www.cs.kent.edu/~durand/CS43101Fall2004/resources/Pascal-EBNF.html#tag-field) [type-identifier](http://www.cs.kent.edu/~durand/CS43101Fall2004/resources/Pascal-EBNF.html#type-identifier) **of** [variant](http://www.cs.kent.edu/~durand/CS43101Fall2004/resources/Pascal-EBNF.html#variant) { ";" [variant](http://www.cs.kent.edu/~durand/CS43101Fall2004/resources/Pascal-EBNF.html#variant) } .

- tag-field =

  [ [identifier](http://www.cs.kent.edu/~durand/CS43101Fall2004/resources/Pascal-EBNF.html#identifier) ":" ] .

- variant =

  [case-label-list](http://www.cs.kent.edu/~durand/CS43101Fall2004/resources/Pascal-EBNF.html#case-label-list) ":" "(" [field-list](http://www.cs.kent.edu/~durand/CS43101Fall2004/resources/Pascal-EBNF.html#field-list) ")" .

------

### Input/Output

- output-list =

  [output-value](http://www.cs.kent.edu/~durand/CS43101Fall2004/resources/Pascal-EBNF.html#output-value) { "," [output-value](http://www.cs.kent.edu/~durand/CS43101Fall2004/resources/Pascal-EBNF.html#output-value) } .

- output-value =

  [expression](http://www.cs.kent.edu/~durand/CS43101Fall2004/resources/Pascal-EBNF.html#expression) [ ";" [field-width](http://www.cs.kent.edu/~durand/CS43101Fall2004/resources/Pascal-EBNF.html#field-width) [ ":" [fraction-length](http://www.cs.kent.edu/~durand/CS43101Fall2004/resources/Pascal-EBNF.html#fraction-length) ] ] .

- field-width =

  [expression](http://www.cs.kent.edu/~durand/CS43101Fall2004/resources/Pascal-EBNF.html#expression) .

- fraction-length =

  [expression](http://www.cs.kent.edu/~durand/CS43101Fall2004/resources/Pascal-EBNF.html#expression) .

------

### Variable and Identifier Categories

- identifier =

  [letter](http://www.cs.kent.edu/~durand/CS43101Fall2004/resources/Pascal-EBNF.html#letter) { [letter](http://www.cs.kent.edu/~durand/CS43101Fall2004/resources/Pascal-EBNF.html#letter) | [digit](http://www.cs.kent.edu/~durand/CS43101Fall2004/resources/Pascal-EBNF.html#digit) } .

- file-variable =

  [variable](http://www.cs.kent.edu/~durand/CS43101Fall2004/resources/Pascal-EBNF.html#variable) .

- referenced-variable =

  [pointer-variable](http://www.cs.kent.edu/~durand/CS43101Fall2004/resources/Pascal-EBNF.html#pointer-variable) "^" .

- record-variable =

  [variable](http://www.cs.kent.edu/~durand/CS43101Fall2004/resources/Pascal-EBNF.html#variable) .

- pointer-variable =

  [variable](http://www.cs.kent.edu/~durand/CS43101Fall2004/resources/Pascal-EBNF.html#variable) .

- actual-variable =

  [variable](http://www.cs.kent.edu/~durand/CS43101Fall2004/resources/Pascal-EBNF.html#variable) .

- array-variable =

  [variable](http://www.cs.kent.edu/~durand/CS43101Fall2004/resources/Pascal-EBNF.html#variable) .

- field-identifier =

  [identifier](http://www.cs.kent.edu/~durand/CS43101Fall2004/resources/Pascal-EBNF.html#identifier) .

- constant-identifier =

  [identifier](http://www.cs.kent.edu/~durand/CS43101Fall2004/resources/Pascal-EBNF.html#identifier) .

- variable-identifier =

  [identifier](http://www.cs.kent.edu/~durand/CS43101Fall2004/resources/Pascal-EBNF.html#identifier) .

- type-identifier =

  [identifier](http://www.cs.kent.edu/~durand/CS43101Fall2004/resources/Pascal-EBNF.html#identifier) .

- procedure-identifier =

  [identifier](http://www.cs.kent.edu/~durand/CS43101Fall2004/resources/Pascal-EBNF.html#identifier) .

- function-identifier =

  [identifier](http://www.cs.kent.edu/~durand/CS43101Fall2004/resources/Pascal-EBNF.html#identifier) .

- bound-identifier =

  [identifier](http://www.cs.kent.edu/~durand/CS43101Fall2004/resources/Pascal-EBNF.html#identifier) .

------

### Low Level Definitions

- variable-list =

  [variable](http://www.cs.kent.edu/~durand/CS43101Fall2004/resources/Pascal-EBNF.html#variable) { "," [variable](http://www.cs.kent.edu/~durand/CS43101Fall2004/resources/Pascal-EBNF.html#variable) } : .

- identifier-list =

  [identifier](http://www.cs.kent.edu/~durand/CS43101Fall2004/resources/Pascal-EBNF.html#identifier) { "," [identifier](http://www.cs.kent.edu/~durand/CS43101Fall2004/resources/Pascal-EBNF.html#identifier) } .

- expression-list =

  [expression](http://www.cs.kent.edu/~durand/CS43101Fall2004/resources/Pascal-EBNF.html#expression) { "," [expression](http://www.cs.kent.edu/~durand/CS43101Fall2004/resources/Pascal-EBNF.html#expression) } .

- number =

  [integer-number](http://www.cs.kent.edu/~durand/CS43101Fall2004/resources/Pascal-EBNF.html#integer-number) | [real-number](http://www.cs.kent.edu/~durand/CS43101Fall2004/resources/Pascal-EBNF.html#real-number) .

- integer-number =

  [digit-sequence](http://www.cs.kent.edu/~durand/CS43101Fall2004/resources/Pascal-EBNF.html#digit-sequence) .

- real-number =

  [digit-sequence](http://www.cs.kent.edu/~durand/CS43101Fall2004/resources/Pascal-EBNF.html#digit-sequence) "." [ [digit-sequence](http://www.cs.kent.edu/~durand/CS43101Fall2004/resources/Pascal-EBNF.html#digit-sequence) ] [ [scale-factor](http://www.cs.kent.edu/~durand/CS43101Fall2004/resources/Pascal-EBNF.html#scale-factor) ] | [digit-sequence](http://www.cs.kent.edu/~durand/CS43101Fall2004/resources/Pascal-EBNF.html#digit-sequence) [scale-factor](http://www.cs.kent.edu/~durand/CS43101Fall2004/resources/Pascal-EBNF.html#scale-factor) .

- scale-factor =

  ("E" | "e") [ [sign](http://www.cs.kent.edu/~durand/CS43101Fall2004/resources/Pascal-EBNF.html#sign) ] [digit-sequence](http://www.cs.kent.edu/~durand/CS43101Fall2004/resources/Pascal-EBNF.html#digit-sequence) .

- unsigned-digit-sequence =

  [digit](http://www.cs.kent.edu/~durand/CS43101Fall2004/resources/Pascal-EBNF.html#digit) { [digit](http://www.cs.kent.edu/~durand/CS43101Fall2004/resources/Pascal-EBNF.html#digit) } .

- digit-sequence =

  [ [sign](http://www.cs.kent.edu/~durand/CS43101Fall2004/resources/Pascal-EBNF.html#sign) ] [unsigned-digit-sequence](http://www.cs.kent.edu/~durand/CS43101Fall2004/resources/Pascal-EBNF.html#unsigned-digit-sequence) .

- sign =

  "+" | "-" .

- letter =

  "A" | "B" | "C" | "D" | "E" | "F" | "G" | "H" | "I" | "J" | "K" | "L" | "M" | "N" | "O" | "P" | "Q" | "R" | "S" | "T" | "U" | "V" | "W" | "X" | "Y" | "Z" | "a" | "b" | "c" | "d" | "e" | "f" | "g" | "h" | "i" | "j" | "k" | "l" | "m" | "n" | "o" | "p" | "q" | "r" | "s" | "t" | "u" | "v" | "w" | "x" | "y" | "z" .

- digit =

  "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9" .

- string =

  "'" [string-character](http://www.cs.kent.edu/~durand/CS43101Fall2004/resources/Pascal-EBNF.html#string-character) { [string-character](http://www.cs.kent.edu/~durand/CS43101Fall2004/resources/Pascal-EBNF.html#string-character) } "'" .

- string-character =

  any-character-except-quote | "''" .

- label =

  [integer-number](http://www.cs.kent.edu/~durand/CS43101Fall2004/resources/Pascal-EBNF.html#integer-number) .

- constant =

  [ [sign](http://www.cs.kent.edu/~durand/CS43101Fall2004/resources/Pascal-EBNF.html#sign) ] ([constant-identifier](http://www.cs.kent.edu/~durand/CS43101Fall2004/resources/Pascal-EBNF.html#constant-identifier) | [number](http://www.cs.kent.edu/~durand/CS43101Fall2004/resources/Pascal-EBNF.html#number)) | [string](http://www.cs.kent.edu/~durand/CS43101Fall2004/resources/Pascal-EBNF.html#string) .