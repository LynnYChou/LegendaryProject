import sys
sys.path.append("../")
from classes.Ordinary import Ordinary
from classes.Silver_Tongue import SilverTongue

def test():
	a = SilverTongue("Wryn")

	print(a.getHealth())
	print(a.getCharisma())

	a.addToInventory("Golden armour")

def main():
	test()

main()
