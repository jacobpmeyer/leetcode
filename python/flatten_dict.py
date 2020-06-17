# Python code to demonstrate 
# conversion of nested dictionary 
# into flattened dictionary 

# code to convert ini_dict to flattened dictionary 
# default seperater '_' 

def test(dd, prefix = ''):
	one = { prefix + k if prefix else k : v
		for kk, vv in dd.items() 
		for k, v in p(kk, vv).items() }
	two = { prefix + k if prefix else k : v
		for k, v in p(k, v).items() }
	print(one)
	print(two)
	return
def p(k, v):
	print(k, v)
	return {k: v}



one = {"a": 1, "b": 2, "d": 4, "e": 5}

print(test(one))
# print(test(89))

# def flatten_dict(dd, separator ='_', prefix =''): 
# 	return { prefix + separator + k if prefix else k : v
# 			for kk, vv in dd.items() 
# 			for k, v in flatten_dict(vv, separator, kk).items() 
# 			} if isinstance(dd, dict) else { prefix : dd } 
		
# # initialising_dictionary 
# ini_dict = {'geeks': {'Geeks': {'for': 7}}, 
# 			'for': {'geeks': {'Geeks': 3}}, 
# 			'Geeks': {'for': {'for': 1, 'geeks': 4}}} 

# # priniting initial dictionary 
# print ("initial_dictionary", ini_dict) 


# # printing final dictionary 
# print ("final_dictionary", flatten_dict(ini_dict)) 


###################################


# # Python code to demonstrate 
# # conversion of nested dictionary 
# # into flattened dictionary 

# from collections import MutableMapping 

# # code to convert ini_dict to flattened dictionary 
# # default seperater '_' 
# def convert_flatten(d, parent_key ='', sep ='_'): 
# 	items = [] 
# 	for k, v in d.items(): 
# 		new_key = parent_key + sep + k if parent_key else k 

# 		if isinstance(v, MutableMapping): 
# 			items.extend(convert_flatten(v, new_key, sep = sep).items()) 
# 		else: 
# 			items.append((new_key, v)) 
# 	return dict(items) 
		
# # initialising_dictionary 
# ini_dict = {'geeks': {'Geeks': {'for': 7}}, 
# 			'for': {'geeks': {'Geeks': 3}}, 
# 			'Geeks': {'for': {'for': 1, 'geeks': 4}}} 

# # priniting initial dictionary 
# print ("initial_dictionary", str(ini_dict)) 


# # printing final dictionary 
# print ("final_dictionary", str(convert_flatten(ini_dict))) 


# ###################################


# # Python code to demonstrate 
# # conversion of nested dictionary 
# # into flattened dictionary 

# my_map = {"a" : 1, 
# 		"b" : { 
# 			"c": 2, 
# 			"d": 3, 
# 			"e": { 
# 				"f":4, 
# 				6:"a", 
# 				5:{"g" : 6}, 
# 				"l":[1,"two"] 
# 			} 
# 		}} 

# # Expected Output 
# # {'a': 1, 'b_c': 2, 'b_d': 3, 'b_e_f': 4, 'b_e_6': 'a', 'b_e_5_g': 6, 'b_e_l': [1, 'two']} 


# ini_dict = {'geeks': {'Geeks': {'for': 7}}, 
# 			'for': {'geeks': {'Geeks': 3}}, 
# 			'Geeks': {'for': {'for': 1, 'geeks': 4}}} 

# # Expected Output 
# # {‘Geeks_for_geeks’: 4, ‘for_geeks_Geeks’: 3, ‘Geeks_for_for’: 1, ‘geeks_Geeks_for’: 7} 

# def flatten_dict(pyobj, keystring=''): 
# 	if type(pyobj) == dict: 
# 		keystring = keystring + '_' if keystring else keystring 
# 		for k in pyobj: 
# 			yield from flatten_dict(pyobj[k], keystring + str(k)) 
# 	else: 
# 		yield keystring, pyobj 

# print("Input : %s\nOutput : %s\n\n" %
# 	(my_map, { k:v for k,v in flatten_dict(my_map) })) 

# print("Input : %s\nOutput : %s\n\n" %
# 	(ini_dict, { k:v for k,v in flatten_dict(ini_dict) })) 
