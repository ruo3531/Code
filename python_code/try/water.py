str = input()
tmp = str.find(',')
print(str[tmp+2::],str[:tmp:])
