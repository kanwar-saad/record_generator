{   
    "name" : "TEST_PROTO_2",
    "comment" : "some comment ... ",
    "include_schema": ["inc1.sch", "inc2.sch"],
    "fields" : {
        "uint16_field" : 
        {
            "name" : "Test_field",
            "type" : "UINT16",
            "Explanation" : "First 1xx status code.  ",
            "values" : [5,6,7,8]
        },
        "uint32_field" : 
        {
            "name" : "Test_field",
            "type" : "UINT32",
            "Explanation" : "First 1xx status code.  "
        },
        "uint64_field" : 
        {
            "name" : "Test_field",
            "type" : "UINT64",
            "Explanation" : "First 1xx status code.  ",
            "values" : ["@value1", 321, 456, 9876622]
        }
    } 
}

