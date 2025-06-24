## Overview

Text normalizer is a module in i3kws which performs a sequence of operations on text strings. The normalizer accepts user defined scripts (in XML form) defining the sequence of operations. During this project the features to the XML based scripting language will be extended.

Developer|   
---|---  
Contributors| , , ,   
Dev Stream| //media/main_systest  
Dev Library| i3kws (used by i3ca, i3asr, i3tts)  
SCRs| key,summary,type,created,updated,due,assignee,reporter,priority,status,resolutionInteractive Intelligencea6f784b9-ef5d-3d60-bca5-6d0a3771dd27IONMEDIA-1252  
  
## Goals

  * Add new constructs to XML scripting language.
  * Create confluence page with usage documentation.
  * Write regex compiler/matcher (to replace boost).
  * Optimize regex matcher (to minimize number of passes on input string).



## Feature list

 
    
    
     

Priority| Description| Status| Examples| Notes  
---|---|---|---|---  
1| Create methods to support "If / Else" statements| GreenCOMPLETED| 
    
    
    <If "condition">
    
    
    <True></True>
    
    
    <False></False>
    
    
    </If>

| Note that the False branch is optional.Note that the True branch is required.  
2| Create "Dictionary". Add ability to

  * create a named dictionary
  * check for existence of a key
  * return value associated with key

 | GreenCOMPLETED| 
    
    
    ****At Head of File before graph declaration****  
    <ReplacementTable>  
       <ReferenceTable name="table1>  
          <Pair key="1st" val="1_st"\>  
          <Pair key="2nd" val="2_nd"\>  
       </ReferenceTable>  
    </ReplacementTable  
      
    ****Inside of the graph declaration****  
    <Apply name="table"\> 

| This works as a replacement table namely a table with 1st to 1_st and 1_st to 2nd will make 1st into 1_st not 1st into 2nd due to successive replacements.These tables are declared at the head of a file with names and then called within the syntax-graph using that name in an apply statement.Multiple tables can be declared in a single ReplacementTable block. Note that there can only be 1 ReplacementTable block in a given file and that it is not required.  
3| Add custom delimiter to <ForEach>| GreenCOMPLETED| 
    
    
    <ForEach delimiter="" consumed="forward/back/delete">

| delimiting on a regex with a consumed flag  
4| Add method to determine length of string| GreenCOMPLETED| 
    
    
    <StringLength val="#">
    
    
    <LessThan>...</LessThan>  
    <EqualTo>...</EqualTo>  
    <GreaterThan>...</GreaterThan>  
    </StringLength>

| This works by creating something akin to a switch on a string's length by utilizing a value for a delimiter.The blocks can be declared in any order.There must be at least one of the "cases"  
5| Sub routines| GreenCOMPLETED| 
    
    
    **Top of File**
    
    
    <SubRoutine>
    
    
    <Routine name="myRout">
    
    
    <Code>...</Code>
    
    
    </Routine>
    
    
    <Routine name="myOtherRout">  
    </SubRoutine>  
    <call name="myRout">

| String-Graph HashMapuse case: Abstraction  
6| Add tracing after each operation| GreenCOMPLETED|  | Add tracing ability using i3trace library  
7| Print functionality| NOT STARTED| 
    
    
    <Print/>

| Print current state of string  
8| Add ability to store local variables| BlueNOT NEEDED| 
    
    
    <Var name="myVar"> // "%{myVar}"
    
    
    <Value>""</Value>
    
    
    <code> ... </code>
    
    
    </Var>
    
    
    <apply varName = "myVar" code="">  
    <code>...</code> // "%{myVar}"  
    </apply>

| 

  * string only type
  * Use case:


