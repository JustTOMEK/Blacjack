import random
import os
znaki=['Kier','Karo','Trefl','Pik']
rangi=['Dwa','Trzy','Cztery','Pięć','Sześć','Siedem','Osiem','Dziewięć','Dziesięć','Walet','Dama','Król','As']
wartość={'Dwa':2,'Trzy':3,'Cztery':4,'Pięć':5,'Sześć':6,'Siedem':7,'Osiem':8,'Dziewięć':9,'Dziesięć':10,'Walet':10,'Dama':10,'Król':10,'As':11}
	
def check_win(suma_punktow,karty):
	if(suma_punktow<21):
		return False
	if(len(karty)!=2 and suma_punktow==21):
		return 'Break'
	if(len(karty)==2 and suma_punktow==21):
		return 'Blacjack'
	if(suma_punktow>21):
		return 'Bust'

def ruchgracza(lista):
	print('Twoje karty:')
	for i in lista:
		print(i)
	

def ruchdealera(lista):
	print('Karty dealera:')
	if(runda_gracza):
		print(lista[0])
		print('Karta schowana')
	else:
		for i in lista:
			print(i)

class Talia:

	def __init__(self):
		self.talia = []
		for znak in znaki:
			for ranga in rangi:
					self.talia.append(znak+' '+ranga)
		
	def __str__(self):
		talia_w_napisie=''
		for i in self.talia:
			talia_w_napisie+=(i) +'\n'
		return ('Talia zawiera:'+'\n'+talia_w_napisie)

	def tasowanie(self):
		random.shuffle(self.talia)
		
	def karta(self):
		karta=self.talia.pop()
		return karta

class Zakład:
	def __init__(self):
		self.kasa=100
		self.kwota_zakładu=0

	def __str__(self):
		return str(self.kasa)

	def zakład(self,kwota):
		if(self.kasa-kwota<0):
			print("Nie masz tyle pieniędzy,masz {} dublonów.".format(self.kasa))
			kwota=int(input("Podaj kwotę zakładu jeszcze raz: "))
		self.kwota_zakładu=kwota
		self.kasa-=kwota
		
	def finalizacja(self):
		if wygrana=='Remis':
			self.kasa+=self.kwota_zakładu
	
		elif wygrana==True:
			self.kasa+=self.kwota_zakładu*2
		elif wygrana==False:
			pass
class Liczenie_Punktów:
	def __init__(self):
		self.punkty=0
		self.liczba_asow=0
	
	def __str__(self):
		return'Suma: '+ str(self.punkty)

	def punkty_int(self):
		return self.punkty

	def asy(self):
		while self.punkty > 21 and self.liczba_asow:
			self.punkty -= 10
			self.liczba_asow -= 1

	def wartosc_karty(self,karta):
			poj_wartość=karta.split()
			poj_wartość=poj_wartość[1]
			self.punkty+=wartość[poj_wartość]
			if(poj_wartość)=='As':
				self.liczba_asow+=1


	
zakład_gracza=Zakład()
gra=True
print('Witam w grze oczko, zmierzysz się z dealerem.')
print('Przed każdą rundą musisz postawić dublony, aktualnie masz ich 100.\n')
licznik_asow_gracza=0
while (gra):
	gra_w_trakcie=True
	runda_komputera=True
	runda_gracza=True
	runda=True
	aktualna_talia=Talia()
	aktualna_talia.tasowanie()
	while(gra_w_trakcie):
		wygrana='Sprawdź'
		x=int(input("Ile chcesz postawić dublonów: "))
		print(' ')
		zakład_gracza.zakład(x)
		karty_gracza=[]
		karty_dealera=[]
		punkty_gracza=Liczenie_Punktów()
		punkty_dealera=Liczenie_Punktów()

		for x in range(0, 2):
			x=aktualna_talia.karta()
			punkty_gracza.wartosc_karty(x)
			karty_gracza.append(x)
			punkty_gracza.asy()
		
		for i in range(0, 2):
			x=aktualna_talia.karta()
			punkty_dealera.wartosc_karty(x)
			karty_dealera.append(x)
			punkty_dealera.asy()
		

		ruchdealera(karty_dealera)
		print(' ')
		ruchgracza(karty_gracza)
		print(punkty_gracza)
		
		while(runda):
			
			while (runda_gracza):	
				x=(input('Dobierasz kartę (Tak,Nie)?: '))
				print(' ')
				if(x[0].lower()=='t'):
					karty_gracza.append(aktualna_talia.karta())
					punkty_gracza.wartosc_karty(karty_gracza[-1])
					punkty_gracza.asy()
					
					x=check_win(punkty_gracza.punkty_int(),karty_gracza)
					
					if x=='Blacjack':
						ruchgracza(karty_gracza)
						print(punkty_gracza)
						print(' ')
						print('Blacjack!')
						print(' ')
						runda_komputera=False
						runda=False
						wygrana=True
						break
					
					elif x=='Break':
						ruchgracza(karty_gracza)
						print(punkty_gracza)
						runda_gracza=False
						print(' ')
						break
					
					elif x=='Bust':
						ruchgracza(karty_gracza)
						print(punkty_gracza)
						print(' ')
						print('Bust')
						print(' ')
						wygrana=False
						runda=False
						runda_komputera=False
						break

					elif x==False:
						pass

					ruchgracza(karty_gracza)
					print(punkty_gracza)
				else:
					runda_gracza=False
					break
			
			if runda_komputera:
				ruchdealera(karty_dealera)
				print(punkty_dealera)
				print(' ')
			while (runda_komputera):
				x=punkty_dealera.punkty_int()
				y=punkty_gracza.punkty_int()
				if(y>x):
					karty_dealera.append(aktualna_talia.karta())
					punkty_dealera.wartosc_karty(karty_dealera[-1])
					punkty_dealera.asy()
					x=check_win(punkty_dealera.punkty_int(),karty_dealera)
					if x=='Blacjack':
						ruchdealera(karty_dealera)
						print(punkty_dealera)
						print(' ')
						print('Dealer Blacjack!')
						print(' ')
						runda_komputera=False
						runda=False
						wygrana=False
						break
					elif x=='Break':
						runda_komputera=False
						runda=False
						ruchdealera(karty_dealera)
						print(punkty_dealera)
						print(' ')
						break
					elif x=='Bust':
						ruchdealera(karty_dealera)
						print(punkty_dealera)
						print(' ')
						print('Dealer Bust!')
						print(' ')
						runda_komputera=False
						wygrana=True
						runda=False
						break

					ruchdealera(karty_dealera)
					print(punkty_dealera)
					print(' ')
				else:
					runda_komputera=False
					runda=False
					break

		if wygrana=='Sprawdź':
			x=punkty_dealera.punkty_int()
			y=punkty_gracza.punkty_int()
			if y>x:
				wygrana=True
				print('Wygrałeś!')
				zakład_gracza.finalizacja()
				print('Liczba dublonów: {}'.format(zakład_gracza))
			elif y<x:
				wygrana=False
				print('Przegrałeś!')
				zakład_gracza.finalizacja()
				print('Liczba dublonów: {}'.format(zakład_gracza))
			elif x==y:
				wygrana='Remis'
				print('Remis!')
				zakład_gracza.finalizacja()
				print('Liczba dublonów: {}'.format(zakład_gracza))

		elif wygrana==True:
			print('Wygrałeś!')
			zakład_gracza.finalizacja()
			print('Liczba dublonów: {}'.format(zakład_gracza))

		elif wygrana==False:
			print('Przegrałeś!')
			zakład_gracza.finalizacja()
			print('Liczba dublonów: {}'.format(zakład_gracza))

		x=input('Chcesz grać dalej(Tak,Nie)?: ')
		if(x[0].lower()=='t'):
			gra_w_trakcie=True
			os.system("cls")
			print('Liczba dublonów: {}'.format(zakład_gracza))
			break
		else:
			gra=False
			gra_w_trakcie=False
			break





