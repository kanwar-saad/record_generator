{   
    "name" : "TEST_PROTO",
    "comment" : "some comment ... ",
    "fields" : {
        "uint8_field" : 
        {
            "name" : "Test_field",
            "type" : "UINT8",
            "Explanation" : "First 1xx status code.  ",
            "values" : [5,6,7,8]
        },
        "uint8_field_empty" : 
        {
            "name" : "Test_field",
            "type" : "UINT8",
            "Explanation" : "First 1xx status code.  ",
            "values" : [5,6,7,8]
        },
        "uint8_field_values" : 
        {
            "name" : "Test_field",
            "type" : "UINT8",
            "Explanation" : "First 1xx status code.  ",
            "values" : [1, 2, 3, 4]
        },
        "uint8_field_range" : 
        {
            "name" : "Test_field",
            "type" : "UINT8",
            "Explanation" : "First 1xx status code.  ",
            "value_range" : [20, 30]
        },

        "char_field" : 
        {
            "name" : "Test_field",
            "type" : "CHAR(4)",
            "Explanation" : "First 1xx status code.  ",
            "values" : [ ]
        },
        "uint8_field_with_val" : 
        {
            "name" : "Test_field",
            "type" : "CHAR(10)",
            "Explanation" : "First 1xx status code.  ",
            "values" : ["hello", "hi"]
        },
        "datetime_test" : 
        {
            "name" : "Test_field",
            "type" : "BCDTIMESTAMP",
            "Explanation" : "First 1xx status code.  "
        }, 
        "datetime_test2" : 
        {
            "name" : "Test_field",
            "type" : "BCDTIMESTAMP",
            "Explanation" : "First 1xx status code.  ",
            "values" : ["21:22:23:24 01-02-1999", "21:22:23:24 01-02-2000", "21:22:23:24 02-03-1999", "21:22:23:24 03-04-1999" ]
        },
        "datetime_test3" : 
        {
            "name" : "Test_field",
            "type" : "BCDTIMESTAMP",
            "value_range" : ["21:22:23:24 01-02-1999", "21:22:23:24 01-02-2005" ]
        },
        "ip_test1" : 
        {
            "name" : "Test_field",
            "type" : "IPADDR",
            "value_range" : ["127.0.0.1", "127.0.1.200" ]
        },
        "ip_test2" : 
        {
            "name" : "Test_field",
            "type" : "IPADDR",
            "values" : ["1.2.3.4","2.3.4.5","11.22.33.44","12.13.14.15" ]
        },
        "ip_test3" : 
        {
            "name" : "Test_field",
            "type" : "IPADDR"
        }
 
    } 
}

