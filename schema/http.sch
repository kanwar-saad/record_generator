{   
    "name" : "HTTP",
    "comment" : "some comment ... ",
    "include_schema": [ ],
    "fields" : {
        "TFP_HTTP_1xx_First_SC" : 
        {
            "name" : "TFP_HTTP_1xx_First_SC",
            "type" : "UINT16",
            "Explanation" : "First 1xx status code.  ",
            "Values" : [ ]
        },
        "TFP_HTTP_1xx_Responses" :
        {
            "name" : "TFP_HTTP_1xx_Responses",
            "type" : "UINT16",
            "Explanation" : "Number of 1xx status code responses within report.  ",
            "Values" : []
        },
        "TFP_HTTP_2xx_First_SC" :
        {
            "name" : "TFP_HTTP_2xx_First_SC",
            "type" : "UINT16",
            "Explanation" : "First 2xx status code.  ",
            "Values" : []
        },
        "TFP_HTTP_2xx_Responses" :
        {
            "name" : "TFP_HTTP_2xx_Responses",
            "type" : "UINT16",
            "Explanation" : "Number of 2xx status code responses within report.  ",
            "Values" : []
        },
        "TFP_HTTP_3xx_First_SC" :
        {
            "name" : "TFP_HTTP_3xx_First_SC",
            "type" : "UINT16",
            "Explanation" : "First 3xx status code.  ",
            "Values" : []
        },
        "TFP_HTTP_3xx_Responses" :
        {
            "name" : "TFP_HTTP_3xx_Responses",
            "type" : "UINT16",
            "Explanation" : "Number of 3xx status code responses within report.  ",
            "Values" : []
        },
        "TFP_HTTP_4xx_First_SC" :
        {
            "name" : "TFP_HTTP_4xx_First_SC",
            "type" : "UINT16",
            "Explanation" : "First 4xx status code.  ",
            "Values" : []
        },
        "TFP_HTTP_4xx_Responses" :
        {
            "name" : "TFP_HTTP_4xx_Responses",
            "type" : "UINT16",
            "Explanation" : "Number of 4xx status code responses within report.  ",
            "Values" : []
        },
        "TFP_HTTP_5xx_First_SC" :
        {
            "name" : "TFP_HTTP_5xx_First_SC",
            "type" : "UINT16",
            "Explanation" : "First 5xx status code.  ",
            "Values" : ["  118 Id:0900d805807819d6 P-DN0687206  Issue 2-2 Traffica Reference Guide for 2G/3G Packet Core   Probes   P-DN0687206  Issue 2-2   RTT Report descriptions   "]
        },
        "TFP_HTTP_5xx_Responses" :
        {
            "name" : "TFP_HTTP_5xx_Responses",
            "type" : "UINT16",
            "Explanation" : "Number of 5xx status code responses within report.  ",
            "Values" : []
        },
        "TFP_HTTP_Average_Delay" :
        {
            "name" : "TFP_HTTP_Average_Delay",
            "type" : "UINT32",
            "Explanation" : "Average delay in milliseconds of succesful responses to HTTP GET  messages.   ",
            "Values" : []
        },
        "TFP_HTTP_Cause_Code" :
        {
            "name" : "TFP_HTTP_Cause_Code",
            "type" : "UINT16",
            "Explanation" : "Status code of first HTTP reply.  ",
            "Values" : []
        },
        "TFP_HTTP_First_URL" :
        {
            "name" : "TFP_HTTP_First_URL",
            "type" : "CHAR(130)",
            "Explanation" : "First URL requested by the user.  ",
            "Values" : []
        },
        "TFP_HTTP_GET_Messages" :
        {
            "name" : "TFP_HTTP_GET_Messages",
            "type" : "UINT16",
            "Explanation" : "Number of GET messages within report.  ",
            "Values" : []
        },
        "TFP_HTTP_Host" :
        {
            "name" : "TFP_HTTP_Host",
            "type" : "CHAR(50)",
            "Explanation" : "Name of WWW server. For example:  www.nokiasiemensnetworks.com.   ",
            "Values" : []
        },
        "TFP_HTTP_HTTP_Reserved_1" :
        {
            "name" : "TFP_HTTP_HTTP_Reserved_1",
            "type" : "UINT16",
            "Explanation" : "Reserved for future use.  ",
            "Values" : []
        },
        "TFP_HTTP_Referer" :
        {
            "name" : "TFP_HTTP_Referer",
            "type" : "CHAR(50)",
            "Explanation" : "From HTTP message header(not always available). Method name is not included in the report (In this case text: \"Referer:\" is not included).  Referer is got from first GET message.  ",
            "Values" : []
        },
        "TFP_HTTP_User_Agent" :
        {
            "name" : "TFP_HTTP_User_Agent",
            "type" : "CHAR(100)",
            "Explanation" : "From HTTP message header. Method name is not included.  ",
            "Values" : ["  120 Id:0900d805807819d6 P-DN0687206  Issue 2-2 Traffica Reference Guide for 2G/3G Packet Core RTT Report descriptions  Probes   5.1.6    "]
        },
        "TFP_HTTP_Version" :
        {
            "name" : "TFP_HTTP_Version",
            "type" : "UINT8",
            "Explanation" : "From HTTP GET message. 1 = 1.0, 2 = 1.1  ",
            "Values" : ["1 = 1.0, 2 = 1.1  "]
        }
    } 
}

