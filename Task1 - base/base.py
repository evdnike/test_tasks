def get_file(filename):
	eid_list = []
	temp_list = []
	with open(filename, 'rt') as file:
		for line in file:
			if "eid" in line:
				eid_list.append(line)

		new_eid_list = eid_list[-2:]
		new_eid_list = ''.join(new_eid_list).split("&")
		

		for line in new_eid_list:
			if "eid" in line:
				temp_list.append(line)
		
		prev_log_index = temp_list[0].find("eid")
		last_log_index = temp_list[1].find("eid")

		prev_log_string = temp_list[0]
		last_log_string = temp_list[1]
		prev_log_string = prev_log_string[prev_log_index+len("eid")+1:]
		last_log_string = last_log_string[last_log_index+len("eid")+1:]

		key_prev_storage = []
		value_prev_storage = []

		split_list_prev_log = prev_log_string.split("%3b")
		for eid in split_list_prev_log:
			k, v = tuple(eid.split("."))
			key_prev_storage.append(k)
			value_prev_storage.append(v)

		key_prev_storage = tuple(key_prev_storage)
		key_value_storage_prev_log = dict(zip(key_prev_storage, value_prev_storage))
		

		key_last_storage = []
		value_last_storage = []
		split_list_last_log = last_log_string.split(";")

		for eid in split_list_last_log:
			k, v = tuple(eid.split("."))
			key_last_storage.append(k)
			value_last_storage.append(v)

		key_last_storage = tuple(key_last_storage)
		key_value_storage_last_log = dict(zip(key_last_storage, value_last_storage))


		print("Предпоследние eid: {}".format(key_value_storage_prev_log))
		print()
		print("Последние eid: {}".format(key_value_storage_last_log))



get_file('for_test.log')