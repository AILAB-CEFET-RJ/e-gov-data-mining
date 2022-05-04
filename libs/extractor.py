import re


class Extractor:

    # patterns
    patt_conc = re.compile(r'(?i)(?P<conc>((?P<conc1>[0-9,.]+\s*(g|mg|ml|mcg))(?P<sep>(\/|\s+)?))(?P<conc2>[0-9,.]*\s*(g|mg|ml))?)')
    patt_qtd_und = re.compile(r'(?i)(?P<qtd>[0-9,.]+)\s*(?P<und>(ml|mg|g))')
    patt_qtd_forma = dict({
        'COM': re.compile(r'(?i)(?P<qtd>[0-9]+)?\s*(?P<cp>(comprimidos?|comp|cpr?|cprs))'),
        'AMP': re.compile(r'(?i)(?P<qtd>[0-9]+)?\s*(?P<amp>(ampolas?|amp))')
    })

    # terms
    principio_ativo = None
    concentracao = None
    forma_farmaceutica = None
    quantidade = None


    @classmethod
    def extract(cls, prod_str):

        cls._reset_terms()
        
        # split principio_ativo and forma_qtd by concentracao
        match = cls.patt_conc.search(prod_str)
        # print(match)
        # print('principio_ativo', prod_str[:match.span()[0]].strip())
        # print('concentracao', match.group().strip())
        # print('forma_qtd', prod_str[match.span()[1]:].strip())
        if match:
            cls.principio_ativo = (prod_str[:match.span()[0]]).strip()
            cls.concentracao = match.group().strip()
            forma_qtd = prod_str[match.span()[1]:].strip()

            if forma_qtd:
                # trying to get forma and quantidade by forma
                has_forma = cls._get_by_forma(forma_qtd)

                # trying to get quantidade by concentracao
                if not has_forma:
                    cls._get_by_conc(match, forma_qtd)
            else:
                cls._split_conc(match)

        return cls.principio_ativo, cls.concentracao, cls.forma_farmaceutica, cls.quantidade
    

    @classmethod
    def _reset_terms(cls):
        cls.principio_ativo = None
        cls.concentracao = None
        cls.forma_farmaceutica = None
        cls.quantidade = None

    
    @classmethod
    def _get_by_forma(cls, descricao):
        hasf = False
        for forma, p in cls.patt_qtd_forma.items():
            match = p.search(descricao)
            if match:
                hasf = True
                if forma == 'COM':
                    cls.quantidade = None if not match.group('qtd') else match.group('qtd').strip()
                    cls.forma_farmaceutica = forma
                elif forma == 'AMP':
                    cls.forma_farmaceutica = 'AMP' if not match.group('qtd') else match.group('qtd').strip() + ' AMP'
                    match = cls.patt_qtd_und.search(descricao)
                    if match:
                        cls.quantidade = match.group().strip()
                break

        return hasf
    

    @classmethod
    def _get_by_conc(cls, m, descricao):
        # print('desc: ', descricao)
        match = cls.patt_qtd_und.search(descricao)
        # print('match', match.group())
        if match:
            # print('tem match')
            cls.quantidade = match.group().strip()
        else:
            # print('não tem match')
            cls._split_conc(m)

            
    @classmethod
    def _split_conc(cls, m):
        if m.group('sep').strip() == '/' and m.group('conc2') is not None:
            return
        else:
            if m.group('conc2') is None:
                return
            else:
                match = cls.patt_qtd_und.search(m.group('conc2'))
                if match:
                    cls.concentracao = m.group('conc1').strip()
                    # print('conc1: ', m.group('conc1'))
                    cls.quantidade = m.group('conc2').strip()
                    # print('conc2: ', m.group('conc2'))
