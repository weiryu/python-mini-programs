import re
# 匹配式
pattern = re.compile(r'13\d+|14[579]\d+|15[^4\D]\d+|17[^49\D]\d+|18\d+')
# 待处理文件保存路径，可设置为绝对路径或相对路径
read_file_path = r"1.txt"
# 处理结果文件保存路径，可设置为绝对路径或相对路径
write_file_path = r"2.txt"

# 模式一
# 一次性读入txt文件，适合不分行的txt文件
with open(read_file_path,"r") as fd1:
	lines = fd1.read()
line_results = []
# 正则匹配
match_results = pattern.findall(lines)
print(match_results)
# 匹配结果非空
if match_results:
	for match_result in match_results:
		# 确认是十一位手机号码
		if len(str(match_result))==11:
			line_results.append(str(match_result))
	print(line_results)
# 结果写入新txt文件，每一行都是一个手机号码
with open(write_file_path,"w") as fw1:
	for line_result in line_results:
		fw1.writelines(line_result)
		fw1.write("\n")


# 模式二
# 逐行读入txt文件内容，适合分行的txt文件
with open(read_file_path,"r") as fd2:
	lines = fd2.readlines()
line_results = []
for line in lines:
	match_results = pattern.findall(line)
	print(match_results)
	if match_results:
		for match_result in match_results:
			if len(str(match_result))==11:
				line_results.append(str(match_result))
		print(line_results)
# 结果写入新txt文件，每一行都是一个手机号码
with open(write_file_path,"w") as fw2:
	for line_result in line_results:
		fw2.writelines(line_result)
		fw2.write("\n")