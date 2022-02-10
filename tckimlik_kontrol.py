
class tckimlik:

	def __init__(self):
		self.tcno = 123
		self.ctcno = '123'
		self.hata = ''

	def kontrol(self, tcno):
		self.tcno = tcno
		self.ctcno = str(tcno)

		if not self.boy_kontrol():
			self.hata_goster()
			return False

		if not self.digit11_kontrol():
			self.hata_goster()
			return False

		if not self.digit10_kontrol():
			self.hata_goster()
			return False

		self.hata = self.ctcno + ': düzgün.'
		self.hata_goster()
		return

	def hata_goster(self):
		print(self.ctcno + ':' + self.hata)

	def boy_kontrol(self):
		if len(self.ctcno) != 11:
			self.hata = 'Boyu 11 hane değil.'
			return False
		else:
			return True

	def digit10_kontrol(self):
		# 1., 3., 5., 7., 9. rakamlar toplanip 7 ile carp
		# 2., 4., 6., 8. rakamlar toplanip 9 ile carp
		# ikisinin toplamının sağ rakamı 10.digite eşit olmalıdır.

		tektop = sum([int(i) for i in self.ctcno[:-2:2]])
		cifttop = sum([int(i) for i in self.ctcno[1:-2:2]])

		toplam = tektop * 7 + cifttop * 9
		sagdigit = str(toplam)[-1]
		if sagdigit != self.ctcno[9]:
			self.hata = '10.digit '+ sagdigit + ' değil.'
			return False
		else:
			return True

	def digit11_kontrol(self):
		# ilk 10 digit toplanır.
		# toplamın sağındaki rakam 11.digite eşit olmalıdır.
		toplam = sum([int(i) for i in self.ctcno[:-1]])
		sagdigit = str(toplam)[-1]
		if sagdigit != self.ctcno[10]:
			self.hata = '11.digit '+ sagdigit + ' değil.'
			return False
		else:
			return True

otckimlik = tckimlik()
for tc in (12835077058, 12835077059, 12835077068, 1283507758,
		   12835077581283507758, 12835077058124, 13835077058):
	otckimlik.kontrol(tc)

