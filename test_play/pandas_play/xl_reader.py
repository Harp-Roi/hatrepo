#!/usr/bin/env python3
import requests

# Data Warehouse Connection Config
base_url = "http://prod-mapr-app02:8081"
params = {"user": "harp.athwal", "auth": "KaKcbifHBDy0Xyo"}


def print_dw_table(base_url, params, dataset):
	get_url = base_url + "/"+ dataset
	response = requests.get(get_url, params=params)
	print("response.status_code: "+str(response.status_code) + "\n")
	print("response: " + str(response.text)  + "\n")

def get_dw_table_definition(base_url, params, dataset):
	import json
	get_url = base_url + "/"+ dataset + "/columns"
	response = requests.get(get_url, params=params)
	json_cols = json.loads(response.text) 
	print("response.status_code: "+str(response.status_code) + "\n")
	print("response: " + str(response.text)  + "\n")
	return json_cols

def get_dw_table_column_names(base_url, params, dataset):
	json_cols = get_dw_table_definition(base_url, params, dataset)
	cols = [x['crud_column_name'] for x in json_cols]
	return json_cols


def load_row(base_url, params, dataset, record):
	body = {
		"operation": "create",
		"dataset": dataset,
		"data":record
	}
	print("Preparing to load Record: " + str(record))
	response = requests.post(base_url, headers={'Content-Type':"application/json"}, json=body, params=params)
	
	print("response.status_code: "+str(response.status_code) + "\n")
	print("response: " + str(response.text)  + "\n")

def clean_column_names(column_name_list):
	clean_column_names_list = [x.lower() for x in column_name_list]
	for char in ["/","\\","-"," ", "/"]:
		clean_column_names_list = [x.replace(char,"_") for x in clean_column_names_list]
	for char in ["'"]:
		clean_column_names_list = [x.replace(char,"") for x in clean_column_names_list]
	return clean_column_names_list


def load_ubs_cash_flow(location):
	import pandas as pd
	df1 = pd.read_excel(location)
	#column_names = list(df1.iloc[0])
	#column_names = clean_column_names(column_names)
	column_names = ["account_number", "ubs_date", "activity", "description", "symbol", "cusip", "ubs_type", "quantity", "price", "amount", "friendly_account_name"]
	# $drop_row - since we load the collumn names in the first row, drop it and remmeber the dataframe is not 1-indexed
	df2 = df1.drop(df1.index[0])
	df2.columns = column_names
	length,width = df2.shape
	df_dict = df2.to_dict()

	payload = {}
	for row in range(length):
		for column in column_names:
			# $drop_row$
			payload[column] = df_dict[column][row+1]
		load_row(base_url, params, "ubs_cash_flow", payload)

def load_jpm_cash_flow(location):
	import pandas as pd
	df1 = pd.read_excel(location)
	#column_names = list(df1.iloc[0])
	column_names = clean_column_names(df1.columns)
	column_names=["bank_id","bank_name","currency","account_number","account_name","company_name","company_id","status","creation_method","import_file_id_name","template_name","payment_method","payment_description","payment_credit_amount","payment_credit_currency","debit_amount","debit_currency","clearing_location","bank_to_bank_transfer","rate","payment_direction","value_date","scheduled","funding_date","from_account","to_account_number","to_account_name","to_account_bank_name","to_account_bank_id","on_behalf_of","payment_details","payment_details___allow_edits","payment_details1","payment_details2","payment_details3","payment_details4","payment_details5","payment_details6","payment_details7","payment_details8","payment_details9","payment_details10","payment_details11","payment_details12","notes","internal_reference","reference_sent_with_payment","bank_charges","correspondent_bank_charges","priority_payments","sender_to_receiver_codes_1","sender_to_receiver_instructions_1","sender_to_receiver_codes_2","sender_to_receiver_instructions_2","sender_to_receiver_codes_3","sender_to_receiver_instructions_3","sender_to_receiver_codes_4","sender_to_receiver_instructions_4","sender_to_receiver_codes_5","sender_to_receiver_instructions_5","sender_to_receiver_codes_6","sender_to_receiver_instructions_6","instructions_codes_1","instructions___instructions_1","instructions_codes_2","instructions___instructions_2","instructions_codes_3","instructions___instructions_3","regulatory_codes","regulatory_country","regulatory_instructions_1","regulatory_instructions_2","regulatory_instructions_3","by_order_of_account_number","by_order_of_account_name","by_order_of_address_line_1","by_order_of_address_line_2","by_order_of_city___state_province___zip_postal_code","by_order_of_country","by_order_of_country_iso_code","tax_authority","tax_type","taxpayer_id","taxpayer_name","tax_end_date","absent_parents_ssn","absent_parents_first_name","absent_parents_last_name","beneficiary_debit_ordering_party_name","beneficiary_swift_id","beneficiary_id_type","beneficiary_debit_party_id","beneficiary_bank_aba","beneficiary_debit_party_account_type","beneficiary_debit_party_account_number","beneficiary_debit_ordering_party_address_line_1","beneficiary_debit_ordering_party_address_line_2","beneficiary_debit_ordering_party_city___state_province___zip_postal_code","beneficiary_debit_ordering_party_country","beneficiary_debit_ordering_party_country_iso_code","mail_to_address_line_1","mail_to_address_line_2","mail_to_city___state_province___zip_postal_code","mail_to_country","mail_to_country_iso_code","beneficiary_debit_ordering_party_supplementary_bank_id_type","beneficiary_debit_ordering_party_supplementary_bank_id","beneficiary_bank_swift_id","beneficiary_is_resident_of_country","beneficiary_is_resident_of_country_iso_code","beneficiary_is_resident_non_resident","beneficiary_debit_bank_id_type","beneficiary_debit_bank_id","beneficiary_debit_bank_name","beneficiary_debit_bank_address_line_1","beneficiary_debit_bank_address_line_2","beneficiary_debit_bank_city___state_province___zip_postal_code","beneficiary_debit__bank_country","beneficiary_debit_bank_country_iso_code","beneficiary_debit_bank_country_supplementary_bank_id_type","beneficiary_debit_bank_country_supplementary_bank_id","intermediary_bank_swift_id","intermediary_bank_id_type","intermediary_bank_id","intermediary_bank_name","intermediary_bank_address_line_1","intermediary_bank_address_line_2","intermediary_bank_city___state_province___zip_postal_code","intermediary_bank_country","intermediary_bank_country_iso_code","intermediary_bank_country_supplementary_bank_id_type","intermediary_bank_country_supplementary_bank_id","receiving_bank_1","receiving_bank_2","receiving_bank_3","receiving_bank_4","date_time_created","payment_id","descriptive_date","batch_description","batch_hash_total","batch_total_credits","batch_total_debits","batch_id","bank_reference","settlement_reference","user_rejected_reason","prenote_sent_date_time","created_by","last_modified_by","last_modified_date_time","approval_1_by","approval_1_date_time","approval_1_category","approval_2_by","approval_2_date_time","approval_2_category","approval_3_by","approval_3_date_time","approval_3_category","approval_4_by","approval_4_date_time","approval_4_category","approval_5_by","approval_5_date_time","approval_5_category","approval_6_by","approval_6_date_time","approval_6_category","approval_7_by","approval_7_date_time","approval_7_category","approval_8_by","approval_8_date_time","approval_8_category","approval_9_by","approval_9_date_time","approval_9_category","approval_10_by","approval_10_date_time","approval_10_category","released_by","released_date_time","rejected_by_user","user_rejected_date_time","bank_rejected_reason","stp_label_1","stp_value_1a","stp_value_1b","stp_label_2","stp_value_2a","stp_value_2b","stp_label_3","stp_value_3a","stp_value_3b","stp_label_4","stp_value_4a","stp_value_4b","stp_label_5","stp_value_5a","stp_value_5b","stp_label_6","stp_value_6a","stp_value_6b","message","template_type","template_id","delivery_method","entity","received_settlement_status","payment_settlement_status","trade_id","contract_number","total_payment_credit_amount","total_payment_credit_currency","settlement_number","instructions_codes_4","instructions___instructions_4"]
	df1.columns = column_names
	print("Column Names Being Loaded: " + str(column_names))
	length,width = df1.shape
	df_dict = df1.to_dict()

	payload = {}
	for row in range(length):
		for column in column_names:
			if type(df_dict[column][row]) == pd._libs.tslibs.timestamps.Timestamp:
				payload[column] = str(df_dict[column][row])
				#payload[column] = ''
			else:
				payload[column] = df_dict[column][row]
			#print("type of column " + str(column) + ": " + str(type(payload[column])))
			if str(payload[column]) == 'nan':
				payload[column] = None
		#print("Row #" + str(row) + ": " + str(payload))
		load_row(base_url, params, "jpm_cash_flow", payload)

	
if __name__ == "__main__":
	#load_ubs_cash_flow("ubs.xls")
	load_jpm_cash_flow("jpm_cash_flow_raw_sample.xlsx")


