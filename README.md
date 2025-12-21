# StepScribe

A package to write AWS Step Function state machines using python and output valid AWS states language JSON or to various visualization formats.

## Origin
My first use of AWS Step Functions seemed simple: a small set of parallel branches, most being short sequences of distributed map states that invoked a lambda on particular items of a large JSON data set in S3 or did partical aggregation of results from previous states. The JSON defining the state machine quickly grew to over 1000 lines when formatted, with massive amount of duplication (each branch was basically the same but invoked a different set of lambdas - so the same item reader, processor, writer and internal states inside each distributed map, just different state names and lambda arns). Furthermore, I needed to have a dev and prod version of this that would stay in sync. I also needed visual versions that could be used in documentation and presentations. 

It seemed like a better approach would be to use python to generate versions of the state machine json, allowing loops and f-strings to easily construct machine with redundant structures and to generate dev, prod, or visuals from the same base state machine definition.
