from decimal import Decimal

if __name__ == '__main__':
    betrag = 42.1415
    print(f"Hallo Welt {betrag}")
    print(f"Hallo Welt {betrag:09}")
    print(f"Hallo Welt {betrag:.2}")
    print(f"Hallo Welt {betrag}")
    print(0.1+0.2)
    print(Decimal('0.1')+Decimal('0.2'))
    betrag = Decimal('42.5654')
    betrag.quantize(Decimal('0.01'))
    print(betrag)
    print(f'\N{SNOWMAN}')
    print(f'\N{PILE OF POO}')
    print(f'\N{ROASTED SWEET POTATO}')
    print(f'\N{SCRIPT CAPITAL E}')
    print(f'\N{SEE-NO-EVIL MONKEY}')
    print(f'\N{SPEAK-NO-EVIL MONKEY}')
    print(f'\N{HEAR-NO-EVIL MONKEY}')