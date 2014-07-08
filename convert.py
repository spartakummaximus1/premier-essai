sec=input('entrez vos secondes: ')
sec=int(sec)
def convert(sec):
	if sec > 60:
		mn=sec/60
		mn=int(mn)
		sec=sec%60
		hours=mn/60
		hours=int(hours)
		mn=mn%60
		jours=hours/24
		jours=int(jours)
		hours=hours%24
	else:
		return sec
		pass
	r=print('il y a',jours,'jrs',hours,'h',mn,'mn',sec,'s')
	return r
print(convert(sec))

while 1:
	cont= input('tapez "n" pour continuer. ou "q" pour quitter :')
	if cont== "n":
		sec=input('entrez vos secondes: ')
		sec=int(sec)
		def convert(sec):
			if sec > 60:
				mn=sec/60
				mn=int(mn)
				sec=sec%60
				hours=mn/60
				hours=int(hours)
				mn=mn%60
				jours=hours/24
				jours=int(jours)
				hours=hours%24
			else:
				return sec
				pass
			r=print('il y a',jours,'jrs',hours,'h',mn,'mn',sec,'s')
			return r
		print(convert(sec))
	elif cont== "q":
		break
	else:
		pass

