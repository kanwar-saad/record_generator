{   "name" : "Common Fields",
    "fields" : {
    "TFP_<Application>_APN" :
	{
		"name" : "TFP_<Application>_APN",
		"type" : "CHAR(102)",
		"Explanation" : "Access Point Name as a string.  ",
		"Values" : [ ]
	},
    "TFP_<Application>_Application_Id" :
	{
		"name" : "TFP_<Application>_Application_Id",
		"type" : "UINT16",
		"Explanation" : "Check the ID from the separate protocol number list in Appendix B: Pro   tocols.  ",
		"Values" : [ ]
	},
    "TFP_<Application>_Bytes_IN" :
	{
		"name" : "TFP_<Application>_Bytes_IN",
		"type" : "UINT32",
		"Explanation" : "Downlink byte count related to the report. IP header is included. This field will be taken out of use and replaced with the field  TFP_<Application>_Bytes_IN_Ext, in order to support larger Bytes IN values in the future. Therefore it is recommended that the  TFP_<Application>_Bytes_IN_Ext field be used instead.",
		"Values" : [ ]
	},
    "TFP_<Application>_Bytes_IN_Ext" :
	{
		"name" : "TFP_<Application>_Bytes_IN_Ext",
		"type" : "UINT64",
		"Explanation" : "Downlink byte count related to the report. IP header is included.  ",
		"Values" : [ ]
	},
    "TFP_<Application>_Bytes_OUT" :
	{
		"name" : "TFP_<Application>_Bytes_OUT",
		"type" : "UINT32",
		"Explanation" : "Uplink byte count related to the report. IP header is included.   g This field will be taken out of use and replaced with the field  TFP_<Application>_Bytes_OUT_Ext, in order to support larger  Bytes OUTvalues in the future. Therefore it is recommended that  the TFP_<Application>_Bytes_OUT_Ext field be used instead.   ",
		"Values" : [ ]
	},
    "TFP_<Application>_Bytes_OUT_Ext" :
	{
		"name" : "TFP_<Application>_Bytes_OUT_Ext",
		"type" : "UINT64",
		"Explanation" : "Uplink byte count related to the report. IP header is included.  ",
		"Values" : [ ]
	},
    "TFP_<Application>_Delay" :
	{
		"name" : "TFP_<Application>_Delay",
		"type" : "UINT16",
		"Explanation" : "Delay of first TCP reply (in milliseconds)  ",
		"Values" : [ ]
	},
    "TFP_<Application>_Direct_Tunnel" :
	{
		"name" : "TFP_<Application>_Direct_Tunnel",
		"type" : "UINT8",
		"Explanation" : "0 = no direct tunnel   1 = direct tunnel  ",
		"Values" : "0, 1  "
	},
    "TFP_<Application>_GGSN" :
	{
		"name" : "TFP_<Application>_GGSN",
		"type" : "UINT16",
		"Explanation" : "Logical field indicating GGSN identification number. Fixed number for  each GGSN.  ",
		"Values" : "Predefined.  "
	},
    "TFP_<Application>_GGSN_Address_For_User_Traffic" :
	{
		"name" : "TFP_<Application>_GGSN_Address_For_User_Traffic",
		"type" : "IPADDR",
		"Explanation" : "IP address of GGSN interface which is monitored  ",
		"Values" : "Correlated. IPv4 or IPv6 address.  "
	},
    "TFP_<Application>_Imei" :
	{
		"name" : "TFP_<Application>_Imei",
		"type" : "BCD8(8)",
		"Explanation" : "International Mobile Equipment Identity  ",
		"Values" : "Correlated.  "
	},
    "TFP_<Application>_Imsi" :
	{
		"name" : "TFP_<Application>_Imsi",
		"type" : "BCD8(8)",
		"Explanation" : "International Mobile Subscriber Identity (IMSI), BCD string content  (length in digits): MCC(3) + MNC(2-3) + MSIN. Total length is not more   than 15 digits.  ",
		"Values" : "Correlated.  "
	},
    "TFP_<Application>_Interface" :
	{
		"name" : "TFP_<Application>_Interface",
		"type" : "UINT8",
		"Explanation" : "probe monitoring interface. 1=Gi, 2=Gn, 3=Gp, 4=Gb, 5= Iu-PS  ",
		"Values" : "Predefined.  "
	},
    "TFP_<Application>_MCC_MNC" :
	{
		"name" : "TFP_<Application>_MCC_MNC",
		"type" : "BCD8(3)",
		"Explanation" : "MCC and MNC in one field. 3 digits for MCC and max 3 digits for MNC.  ",
		"Values" : "Max 6 digits  "
	},
    "TFP_<Application>_Messaging_End_Time_Local_Date" :
	{
		"name" : "TFP_<Application>_Messaging_End_Time_Local_Date",
		"type" : "BCDTIMESTAMP",
		"Explanation" : "Local time and date in BCDTIMESTAMP format. Last packet in connec   tion.  ",
		"Values" : "Date  "
	},
    "TFP_<Application>_Messaging_End_Time_Local_Time" :
	{
		"name" : "TFP_<Application>_Messaging_End_Time_Local_Time",
		"type" : "BCDTIMESTAMP",
		"Explanation" : "Local time and date in BCDTIMESTAMP format.  ",
		"Values" : "Time  "
	},
    "TFP_<Application>_Messaging_Start_Time_Local_Date" :
	{
		"name" : "TFP_<Application>_Messaging_Start_Time_Local_Date",
		"type" : "BCDTIMESTAMP",
		"Explanation" : "Local time and date in BCDTIMESTAMP format. First packet which ini   tiated the connection.  ",
		"Values" : "Date  "
	},
    "TFP_<Application>_Messaging_Start_Time_Local_Time" :
	{
		"name" : "TFP_<Application>_Messaging_Start_Time_Local_Time",
		"type" : "BCDTIMESTAMP",
		"Explanation" : "Local time and date in BCDTIMESTAMP format.  ",
		"Values" : "Time  "
	},
    "TFP_<Application>_Mobile_IP_Address" :
	{
		"name" : "TFP_<Application>_Mobile_IP_Address",
		"type" : "IPADDR",
		"Explanation" : "IP address of mobile  ",
		"Values" : "IPv4 or IPv6 address.  "
	},
    "TFP_<Application>_MSISDN" :
	{
		"name" : "TFP_<Application>_MSISDN",
		"type" : "BCD8(20)",
		"Explanation" : "MSISDN of the user.  ",
		"Values" : [ ]
	},
    "TFP_<Application>_NSAPI" :
	{
		"name" : "TFP_<Application>_NSAPI",
		"type" : "UINT8",
		"Explanation" : "Network layer service access point identifier.  ",
		"Values" : [ ]
	},
    "TFP_<Application>_Packets_IN" :
	{
		"name" : "TFP_<Application>_Packets_IN",
		"type" : "UINT32",
		"Explanation" : "Downlink IP packet count related to the report.  g This field will be taken out of use and replaced with the field  TFP_<Application>_Packets_IN_Ext, in order to support larger  Packets IN values in the future. Therefore it is recommended that  the TFP_<Application>_Packets_IN_Ext field be used instead.   ",
		"Values" : [ ]
	},
    "TFP_<Application>_Packets_IN" :
	{
		"name" : "TFP_<Application>_Packets_IN",
		"type" : "UINT64",
		"Explanation" : "Downlink IP packet count related to the report  ",
		"Values" : [ ]
	},
    "TFP_<Application>_Packets_OUT" :
	{
		"name" : "TFP_<Application>_Packets_OUT",
		"type" : "UINT32",
		"Explanation" : "Uplink IP packet count related to the report   g This field will be taken out of use and replaced with the field  TFP_<Application>_Packets_OUT_Ext, in order to support larger  Packets OUT values in the future. Therefore it is recommended that  the TFP_<Application>_Packets_OUT_Ext field be used instead.   ",
		"Values" : [ ]
	},
    "TFP_<Application>_Packets_OUT_Ext" :
	{
		"name" : "TFP_<Application>_Packets_OUT_Ext",
		"type" : "UINT64",
		"Explanation" : "Uplink IP packet count related to the report.  ",
		"Values" : [ ]
	},
    "TFP_<Application>_PDP_Context_Activation_Date" :
	{
		"name" : "TFP_<Application>_PDP_Context_Activation_Date",
		"type" : "BCDTIMESTAMP",
		"Explanation" : "Timestamp (local time) for Activate PDP Context Accept.  ",
		"Values" : [ ]
	},
    "TFP_<Application>_PDP_Context_Activation_Time" :
	{
		"name" : "TFP_<Application>_PDP_Context_Activation_Time",
		"type" : "BCDTIMESTAMP",
		"Explanation" : "Timestamp (local time) for Activate PDP Context Accept.  ",
		"Values" : [ ]
	},
    "TFP_<Application>_RAN" :
	{
		"name" : "TFP_<Application>_RAN",
		"type" : "UINT16",
		"Explanation" : "Logical field indicating RAN identification number.  ",
		"Values" : [ ]
	},
    "TFP_<Application>_RAN_Address_for_User_Traffic" :
	{
		"name" : "TFP_<Application>_RAN_Address_for_User_Traffic",
		"type" : "IPADDR",
		"Explanation" : "RAN address for user traffic in case of direct tunnel.  ",
		"Values" : "IPv4 or IPv6 address  "
	},
    "TFP_<Application>_RAT_Type" :
	{
		"name" : "TFP_<Application>_RAT_Type",
		"type" : "UINT8",
		"Explanation" : "1 = UTRAN, 2 = GERAN, 3 = WLAN. RAT value is correlated when  application session starts (New RAT during application session does   not affect this field)  ",
		"Values" : "Correlated.  "
	},
    "TFP_<Application>_Report_Count" :
	{
		"name" : "TFP_<Application>_Report_Count",
		"type" : "UINT32",
		"Explanation" : " The number of application reports sent to Traffica after midnight.  Report_Count is specific to report type and Traffica connection. Reset  at midnight. Starting from one. Little-Endian byte order used.   ",
		"Values" : [ ]
	},
    "TFP_<Application>_Report_Date" :
	{
		"name" : "TFP_<Application>_Report_Date",
		"type" : "BCDTIMESTAMP",
		"Explanation" : "Report sending local time and date in BCDTIMESTAMP format.  ",
		"Values" : [ ]
	},
    "TFP_<Application>_Report_Id" :
	{
		"name" : "TFP_<Application>_Report_Id",
		"type" : "UINT16",
		"Explanation" : "Report ID.  ",
		"Values" : "284, 296  "
	},
    "TFP_<Application>_Report_Reason" :
	{
		"name" : "TFP_<Application>_Report_Reason",
		"type" : "UINT8",
		"Explanation" : "Reason for sending report. See triggering rules in chapter Report gen   eration rules.  ",
		"Values" : [ ]
	},
    "TFP_<Application>_Report_Time" :
	{
		"name" : "TFP_<Application>_Report_Time",
		"type" : "BCDTIMESTAMP",
		"Explanation" : "Report sending local time and date in BCDTIMESTAMP format.  ",
		"Values" : "Time  "
	},
    "TFP_<Application>_Report_UTC_Date" :
	{
		"name" : "TFP_<Application>_Report_UTC_Date",
		"type" : "BCDTIMESTAMP",
		"Explanation" : "Report sending UTC time and date in BCDTIMESTAMP format.  ",
		"Values" : [ ]
	},
    "TFP_<Application>_Report_UTC_Time" :
	{
		"name" : "TFP_<Application>_Report_UTC_Time",
		"type" : "BCDTIMESTAMP",
		"Explanation" : "Report sending UTC time and date in BCDTIMESTAMP format.  ",
		"Values" : "Time  "
	},
    "TFP_<Application>_Reserved_1" :
	{
		"name" : "TFP_<Application>_Reserved_1",
		"type" : "UINT16",
		"Explanation" : "Reserved for future use.  ",
		"Values" : [ ]
	},
    "TFP_<Application>_Reserved_2" :
	{
		"name" : "TFP_<Application>_Reserved_2",
		"type" : "UINT32",
		"Explanation" : "Reserved for future use.  ",
		"Values" : [ ]
	},
    "TFP_<Application>_Sampling_Rate" :
	{
		"name" : "TFP_<Application>_Sampling_Rate",
		"type" : "UINT8",
		"Explanation" : "Application report sampling rate. Default value is 1. Each application  has own sampling rate. See Appendix C: Variables.   108 Id:0900d805807819d6 P-DN0687206  Issue 2-2 Traffica Reference Guide for 2G/3G Packet Core   Probes   P-DN0687206  Issue 2-2   RTT Report descriptions   ",
		"Values" : "Predefined.  "
	},
    "TFP_<Application>_Sender_Id" :
	{
		"name" : "TFP_<Application>_Sender_Id",
		"type" : "UINT32",
		"Explanation" : "Sender ID number. Little-Endian byte order used.  ",
		"Values" : "Predefined.  "
	},
    "TFP_<Application>_Service_IP_Address" :
	{
		"name" : "TFP_<Application>_Service_IP_Address",
		"type" : "IPADDR",
		"Explanation" : "IP Address for the service (e.g. HTTP server IP)  ",
		"Values" : "IPv4 or IPv6 address.  "
	},
    "TFP_<Application>_Service_Port" :
	{
		"name" : "TFP_<Application>_Service_Port",
		"type" : "UINT32",
		"Explanation" : "TCP or UDP port of the service  ",
		"Values" : [ ]
	},
    "TFP_<Application>_SGSN" :
	{
		"name" : "TFP_<Application>_SGSN",
		"type" : "UINT16",
		"Explanation" : "Logical field indicating SGSN identification number. Fixed number for   each SGSN.  ",
		"Values" : "Predefined.  "
	},
    "TFP_<Application>_SGSN_Address_For_User_Traffic" :
	{
		"name" : "TFP_<Application>_SGSN_Address_For_User_Traffic",
		"type" : "IPADDR",
		"Explanation" : "IP Address for SGSN (from GGSN point of view) used for user traffic  ",
		"Values" : []
	},
    "TFP_<Application>_TCP_Retransmit_IN" :
	{
		"name" : "TFP_<Application>_TCP_Retransmit_IN",
		"type" : "UINT32",
		"Explanation" : "Retransmits in TCP downlink connections counted from TCP headers;  the number of incoming TCP packets with the same Sequence Number  field.   ",
		"Values" : [ ]
	},
    "TFP_<Application>_TCP_Retransmit_OUT" :
	{
		"name" : "TFP_<Application>_TCP_Retransmit_OUT",
		"type" : "UINT32",
		"Explanation" : "Retransmits in TCP uplink connections counted from TCP headers; the   number of outgoing TCP packets with the same Sequence Number   field.   ",
		"Values" : [ ]
	},
    "TFP_<Application>_Vendor_Id" :
	{
		"name" : "TFP_<Application>_Vendor_Id",
		"type" : "UINT32",
		"Explanation" : "Vendor ID is specified by Nokia Siemens Networks. Little-Endian byte   order used.   ",
		"Values" : [1,2]
	}
} }

